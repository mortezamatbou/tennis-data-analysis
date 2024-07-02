import os
import pandas as pd 
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from sklearn import impute
from sklearn.preprocessing import LabelEncoder
from copy import copy

MatchEventInfo = pd.read_parquet('../Aggregation/MatchEventInfo.parquet')
MatchVotesInfo = pd.read_parquet('../Aggregation/MatchVotesInfo.parquet')
MatchTournamentInfo = pd.read_parquet('../Aggregation/MatchTournamentInfo.parquet')
MatchSeasonInfo = pd.read_parquet('../Aggregation/MatchSeasonInfo.parquet')
MatchVenueInfo = pd.read_parquet('../Aggregation/MatchVenueInfo.parquet')
MatchAwayTeamInfo = pd.read_parquet('../Aggregation/MatchAwayTeamInfo.parquet')
MatchAwayScoreInfo = pd.read_parquet('../Aggregation/MatchAwayScoreInfo.parquet')
MatchRoundInfo = pd.read_parquet('../Aggregation/MatchRoundInfo.parquet')
MatchHomeScoreInfo = pd.read_parquet('../Aggregation/MatchHomeScoreInfo.parquet')
MatchHomeTeamInfo = pd.read_parquet('../Aggregation/MatchHomeTeamInfo.parquet')
PowerInfo = pd.read_parquet('../Aggregation/PowerInfo.parquet')
GameInfo = pd.read_parquet('../Aggregation/GameInfo.parquet')
OddsInfo = pd.read_parquet('../Aggregation/OddsInfo.parquet')
TimeInfo = pd.read_parquet('../Aggregation/TimeInfo.parquet')
PeriodInfo = pd.read_parquet('../Aggregation/PeriodInfo.parquet')

data_frames = {
    'MatchEventInfo':MatchEventInfo,
    'MatchVotesInfo':MatchVotesInfo,
    'MatchTournamentInfo':MatchTournamentInfo,
    'MatchRoundInfo':MatchRoundInfo,
    'MatchSeasonInfo':MatchSeasonInfo,
    'MatchVenueInfo':MatchVenueInfo,
    'MatchAwayTeamInfo':MatchAwayTeamInfo,
    'MatchAwayScoreInfo':MatchAwayScoreInfo,
    'MatchHomeScoreInfo':MatchHomeScoreInfo,
    'MatchHomeTeamInfo':MatchHomeTeamInfo,
    'PowerInfo':PowerInfo,
    'GameInfo':GameInfo,
    'TimeInfo':TimeInfo,
    'PeriodInfo':PeriodInfo,
    'OddsInfo':OddsInfo
}

for key,value in data_frames.items():
    print(f'Shape Of {key} is: {value.shape}')


for key,value in data_frames.items():
    print(f'{key} Null Percentage')
    null_p = (value.isnull().sum() / value.shape[0]) * 100
    print(null_p)
    print('===' * 10)

def column_remover(df:pd.DataFrame) -> pd.DataFrame:
    """
    This function takes a dataframe and removes columns that are fully null.

    Parameters:
        df (DataFrame): The dataframe to be cleaned.
        
    Returns:
        DataFrame: A new dataframe without columns that have more than 90 percent null values.
    """
    # Identify columns which has more than 80 percent null values
    columns_to_remove = df.columns[df.isnull().mean(axis=0) == 1] 
    
    # Drop columns which are in columns_to_remove 
    new_df = df.drop(columns_to_remove, axis =1)
    
    return new_df        

def row_remover(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function takes a dataframe and removes rows that have 50 percent or more null values.

    Parameters:
        df (DataFrame): The dataframe to be cleaned.
        
    Returns:
        DataFrame: A new dataframe without rows that have 50 percent or more null values.
    """
    # Calculate the percentage of null values in each row
    null_percentages = df.isnull().mean(axis=1)

    # Identify rows that have 50 percent or more null values
    rows_to_drop = df.index[null_percentages >= 0.5]

    # Calculate the percentage of rows to drop relative to the entire dataframe
    percent_of_dropping_candidate = len(rows_to_drop) / df.shape[0]

    # Print the number of rows to drop for debugging
    print(f'Rows to drop: {len(rows_to_drop)}')
    print(percent_of_dropping_candidate)
    # Remove rows if the total number of rows to drop is less than 5 percent of data
    if percent_of_dropping_candidate < 0.05:
        print('True')
        new_df = df.drop(index=rows_to_drop)
        return new_df
    else:
        print('False')
        return df



def knn_filler(df:pd.DataFrame, k = 5) -> pd.DataFrame:
    """
    This function takes a dataframe and fills the null values using the KNN algorithm.

    Parameters:
        df (DataFrame): The dataframe to be cleaned.
        
    Returns:
        DataFrame: A new dataframe with its null values filled using the KNN algorithm.
    """

    # Prepare data to use Knn
    new_df = df.copy()
    for column in new_df.columns:
        if new_df[column].dtype == object or new_df[column].isnull().any():  # Check for object type or presence of NaNs
            le = LabelEncoder()
            new_df[column] = new_df[column].astype(str)  # Convert all values to string 
            new_df[column] = le.fit_transform(df[column])
        
    # Create Knn imputer
    knn_imputer = impute.KNNImputer(n_neighbors= k)
    new_df = pd.DataFrame(knn_imputer.fit_transform(new_df, ), columns=new_df.columns, index=new_df.index)
    return new_df.round(3)

# [markdown]
# Cleaning MatchEventInfo

# MatchEventInfo


# First To serve column has about 38 percent null value, 
# since there is no logic and it is a code so Mode is being used.
first_to_serve_mode = MatchEventInfo['first_to_serve'].mode()[0]
MatchEventInfo.fillna({'first_to_serve':first_to_serve_mode}, inplace=True)

# knn will be used to fill home_team_seed, away_team_seed and winner code
imputed_df = knn_filler(MatchEventInfo, k=10)
MatchEventInfo['home_team_seed'] = imputed_df['home_team_seed']
MatchEventInfo['away_team_seed'] = imputed_df['away_team_seed']
MatchEventInfo['winner_code'] = imputed_df['winner_code']

MatchEventInfo.isnull().sum()
# Now the Table is Clean

# [markdown]
# Cleaning MatchTournamentInfo

MatchTournamentInfo = column_remover(MatchTournamentInfo)
# MatchTournamentInfo


ground_tyep_mode = MatchTournamentInfo['ground_type'].mode()[0]
MatchTournamentInfo.fillna({'ground_type':ground_tyep_mode}, inplace=True)


imputed_df = knn_filler(MatchTournamentInfo,k=15)
MatchTournamentInfo['tennis_points'] = imputed_df['tennis_points']

MatchTournamentInfo.isnull().sum()
# Now the Table is Clean

# [markdown]
# Cleaning MatchRoundInfo

# MatchRoundInfo

MatchRoundInfo['cup_round_type'].unique()
MatchRoundInfo['name'].unique()

unique_values = MatchRoundInfo[['name', 'cup_round_type']].drop_duplicates()
# unique_values

cup_round= {'Final':1,'Round of 16	':8,'Quarterfinals':4,'Semifinals':2,
 'Round of 32':16,'Round of 64':32,'Round of 128':64,'Qualification round 2':128,
 'Qualification round 1':256 }

for name, value in cup_round.items():
    MatchRoundInfo.loc[MatchRoundInfo['cup_round_type'].isnull() &
                       MatchRoundInfo['name'].eq(name), 'cup_round_type'] = value

MatchRoundInfo.isnull().sum()
# Now the data is clean

# [markdown]
# Cleaning MatchAwayTeamInfo

# MatchAwayTeamInfo

MatchAwayTeamInfo.info()

genders = {'mrva-maxim':'M','werren-paul':'M','massard-loann':'M','tucakovic-suana':'F'}
for slug, sex in genders.items():
    MatchAwayTeamInfo.loc[(MatchAwayTeamInfo['gender'].isnull()) & 
                          (MatchAwayTeamInfo['slug'].eq(slug)),'gender'] = sex


MatchAwayTeamInfo.loc[MatchAwayTeamInfo['country'].isnull()]
MatchAwayTeamInfo.loc[MatchAwayTeamInfo['country'].isnull(),'country'] = "Australia"

# [markdown]
# Firts we try to check if there is a record in our dataframe which has the birth place of the player that is a missing value in another record.
# If the approach above fails, There is no way to fill residence and birthplace by other information in the dataframe, so we fill them with 'Unknown'.

null_birthplace_df = MatchAwayTeamInfo[MatchAwayTeamInfo['birthplace'].isnull()]
grouped_null_birthplace = null_birthplace_df.groupby('slug')
results = []
for slug, group in grouped_null_birthplace:
    original_group = MatchAwayTeamInfo[MatchAwayTeamInfo['slug'] == slug]
    has_non_null = original_group['birthplace'].notnull().any()
    results.append({
        'slug': slug,
        'null_birthplace_rows': len(group),
        'has_non_null_birthplace': has_non_null
    })


result_df = pd.DataFrame(results)
result_df.loc[result_df['has_non_null_birthplace'].eq(True)]



MatchAwayTeamInfo.loc[MatchAwayTeamInfo['slug'].eq('lobanov-aleksandr'),'birthplace'] = 'Sochi'

MatchAwayTeamInfo.fillna({'residence':'Unknown', 'birthplace':'Unknown'}, inplace=True)
MatchAwayTeamInfo

# We fill null values of highet and weight columns using trimmed_mean of those column
MatchAwayTeamInfo['height'].astype('float64')
MatchAwayTeamInfo['weight'].astype('float64')
trimmed_mean_height = stats.trim_mean(MatchAwayTeamInfo['height'].dropna(), proportiontocut=0.05)
trimmed_mean_weight = stats.trim_mean(MatchAwayTeamInfo['weight'].dropna(), proportiontocut=0.05)
MatchAwayTeamInfo.fillna({'height':trimmed_mean_height, 'weight':trimmed_mean_weight}, inplace=True)


# for choosing between right or left hand,
# first we calculate the percentage of right handed and left handed players
available_data = MatchAwayTeamInfo.loc[MatchAwayTeamInfo['plays'].notnull()].shape[0]
right_handed_per = len(MatchAwayTeamInfo.loc[MatchAwayTeamInfo['plays'].eq('right-handed')]) / available_data
left_handed_per = len(MatchAwayTeamInfo.loc[MatchAwayTeamInfo['plays'].eq('left-handed')]) / available_data

print(f'Percentage of right handed players: {right_handed_per}')
print(f'Percentage of left handed players: {left_handed_per}')

# to keep the distribution of the original data we fill around 88 percent of null data by right-handed,
# and 12 percent by left-handed
plays_null_indicies = MatchAwayTeamInfo[MatchAwayTeamInfo['plays'].isnull()].index
right_handed_filling = int(len(plays_null_indicies) * right_handed_per)

# random indicies from null values will be selected to fill by right-handed
select_right_indicies = np.random.choice(plays_null_indicies,right_handed_filling,replace=False)
MatchAwayTeamInfo.loc[select_right_indicies,'plays'] = 'right-handed'

# The rest will be filled by 'left-handed'
MatchAwayTeamInfo.fillna({'plays': 'left-handed'}, inplace=True)

# There is no relevant data which can help us to find the year when a player became pro,
# so the null values will be filled by 'Unknown'
MatchAwayTeamInfo.fillna({'turned_pro': 'Unknown'}, inplace=True)

# Median will be used to fill null values in current_prize and total_prize
MatchAwayTeamInfo['current_prize'] =  MatchAwayTeamInfo['current_prize'].astype('float64')
MatchAwayTeamInfo['total_prize'] = MatchAwayTeamInfo['total_prize'].astype('float64')

curren_prize_median = MatchAwayTeamInfo['current_prize'].median()
total_prize_median = MatchAwayTeamInfo['total_prize'].median()
MatchAwayTeamInfo.fillna({'current_prize':curren_prize_median,'total_prize':total_prize_median}, inplace=True)

# there is no information here that can help us to find Ranking, 
# so we replace null rankaning with -1 which indicate 'Not Ranked'
MatchAwayTeamInfo.fillna({'current_rank':-1}, inplace=True)

MatchAwayTeamInfo.isnull().sum()
# Now the data is clean

# [markdown]
# Cleaning MatchHomeTeamInfo

MatchHomeTeamInfo.isnull().sum()

MatchHomeTeamInfo.loc[MatchHomeTeamInfo['gender'].isnull(), 'slug'].unique()
genders = {
    'mrva-maxim':'M',
    'werren-paul':'M',
    'massard-loann':'M',
    'tucakovic-suana':'F',
    'cavallo-fernando':'M',
    'karahan-atakan':'M'
}


for slug, sex in genders.items():
    MatchHomeTeamInfo.loc[(MatchHomeTeamInfo['gender'].isnull()) & 
                          (MatchHomeTeamInfo['slug'].eq(slug)),'gender'] = sex

# [markdown]
# Firts we try to check if there is a record in our dataframe which has the birth place of the player that is a missing value in another record.
# If the approach above fails, There is no way to fill residence and birthplace by other information in the dataframe, so we fill them with 'Unknown'.

null_birthplace_df = MatchHomeTeamInfo[MatchHomeTeamInfo['birthplace'].isnull()]
grouped_null_birthplace = null_birthplace_df.groupby('slug')
results = []
for slug, group in grouped_null_birthplace:
    original_group = MatchHomeTeamInfo[MatchHomeTeamInfo['slug'] == slug]
    has_non_null = original_group['birthplace'].notnull().any()
    results.append({
        'slug': slug,
        'null_birthplace_rows': len(group),
        'has_non_null_birthplace': has_non_null
        
    })


result_df = pd.DataFrame(results)
result_df.loc[result_df['has_non_null_birthplace'].eq(True)]

for index, row in result_df.loc[result_df['has_non_null_birthplace']].iterrows():
    slug = row['slug']
    b_place = MatchHomeTeamInfo.loc[MatchHomeTeamInfo['slug'].eq(slug) & 
                                    MatchHomeTeamInfo['birthplace'].notnull(), 'birthplace'].unique()
    MatchHomeTeamInfo.loc[MatchHomeTeamInfo['slug'].eq(slug) & 
                          MatchHomeTeamInfo['birthplace'].isnull(), 'birthplace'] = b_place[0] if len(b_place) > 0 else None

MatchHomeTeamInfo.fillna({'residence':'Unknown', 'birthplace':'unknown'}, inplace=True)

# We fill null values of highet and weight columns using trimmed_mean of those column
MatchHomeTeamInfo['height'].astype('float64')
MatchHomeTeamInfo['weight'].astype('float64')
trimmed_mean_height = stats.trim_mean(MatchHomeTeamInfo['height'].dropna(), proportiontocut=0.05)
trimmed_mean_weight = stats.trim_mean(MatchHomeTeamInfo['weight'].dropna(), proportiontocut=0.05)
MatchHomeTeamInfo.fillna({'height':trimmed_mean_height, 'weight':trimmed_mean_weight}, inplace=True)


# for choosing between right or left hand,
# first we calculate the percentage of right handed and left handed players
available_data = MatchHomeTeamInfo.loc[MatchHomeTeamInfo['plays'].notnull()].shape[0]
right_handed_per = len(MatchHomeTeamInfo.loc[MatchHomeTeamInfo['plays'].eq('right-handed')]) / available_data
left_handed_per = len(MatchHomeTeamInfo.loc[MatchHomeTeamInfo['plays'].eq('left-handed')]) / available_data

print(f'Percentage of right handed players: {right_handed_per}')
print(f'Percentage of left handed players: {left_handed_per}')

# to keep the distribution of the original data we fill around 88 percent of null data by right-handed,
# and 12 percent by left-handed
plays_null_indicies = MatchHomeTeamInfo[MatchHomeTeamInfo['plays'].isnull()].index
right_handed_filling = int(len(plays_null_indicies) * right_handed_per)

# random indicies from null values will be selected to fill by right-handed
select_right_indicies = np.random.choice(plays_null_indicies,right_handed_filling,replace=False)
MatchHomeTeamInfo.loc[select_right_indicies,'plays'] = 'right-handed'

# The rest will be filled by 'left-handed'
MatchHomeTeamInfo.fillna({'plays':'left-handed'}, inplace=True)

# There is no relevant data which can help us to find the year when a player became pro,
# so the null values will be filled by 'Unknown'
MatchHomeTeamInfo.fillna({'turned_pro': 'Unknown'}, inplace=True)

# Median will be used to fill null values in current_prize and total_prize
MatchHomeTeamInfo['current_prize'].astype('float64')
MatchHomeTeamInfo['total_prize'].astype('float64')
curren_prize_median = MatchHomeTeamInfo['current_prize'].median()
total_prize_median = MatchHomeTeamInfo['total_prize'].median()
MatchHomeTeamInfo.fillna({'current_prize':curren_prize_median,'total_prize':total_prize_median}, inplace=True)

# there is no information here that can help us to find Ranking, 
# # so we replace null rankaning with -1 which indicate 'Not Ranked'
MatchHomeTeamInfo.fillna({'current_rank':-1}, inplace=True)

MatchHomeTeamInfo.isnull().sum()
# Now The data is Clean

# [markdown]
# Cleaning MatchAwayScoreInfo

MatchAwayScoreInfo.isnull().sum()

# There is columns called 'normal_time' which is 100 percent null, we drop this column.
MatchAwayScoreInfo.drop('normal_time', axis=1,inplace=True)

# We fill the null values from periods 3 to the end by -1, which by contract means 'Not Happened'
MatchAwayScoreInfo.fillna({
    'period_3':-1,
    'period_4':-1,
    'period_5':-1,
    'period_1_tie_break':-1,
    'period_2_tie_break':-1,
    'period_3_tie_break':-1,
    'period_4_tie_break':-1,
    'period_5_tie_break':-1
    }, inplace=True)



null_ind = MatchAwayScoreInfo.loc[MatchAwayScoreInfo['period_1'].isnull(),'match_id'].unique()

matched_rows = []

for ind in null_ind:
    matched_data = MatchAwayScoreInfo.loc[MatchAwayScoreInfo['match_id'].eq(ind)]
    if not matched_data['period_1'].isnull().all():  # Check if not all 'period_1' values are null
        matched_rows.append(matched_data)

# Concatenate the list into a new DataFrame
try:
    matched_df = pd.concat(matched_rows, ignore_index=True)
    matched_df
except:
    print('Noting to Concat')


                                    

MatchAwayScoreInfo.isnull().sum()

# [markdown]
# to calculate best option for these 4 columns: curren_score, display_score, period_1, period_2, 
# knn will be used

sub_data_set = MatchAwayScoreInfo[['current_score','display_score','period_1','period_2']]
sub_set_filled = knn_filler(sub_data_set)

# now we replace the columns in the main data frame with data in sub_set_filled
columns = ['current_score','display_score','period_1','period_2']
MatchAwayScoreInfo[columns] = sub_set_filled[columns]

MatchAwayScoreInfo.isnull().sum()

# [markdown]
# Cleaning MatchHomeScoreInfo

MatchHomeScoreInfo.isnull().sum()

# There is columns called 'normal_time' which is 100 percent null, we drop this column.
MatchHomeScoreInfo.drop('normal_time', axis=1,inplace=True)

# We fill the null values from periods 3 to the end by -1, which by contract means 'Not Happened'
MatchHomeScoreInfo.fillna({'period_3':-1, 'period_4':-1, 'period_5':-1,
                           'period_1_tie_break':-1,'period_2_tie_break':-1, 'period_3_tie_break':-1,
                          'period_4_tie_break':-1,'period_5_tie_break':-1 },inplace=True)



# [markdown]
# to calculate best option for these 4 columns: curren_score, display_score, period_1, period_2, 
# knn will be used

sub_data_set = MatchHomeScoreInfo[['current_score','display_score','period_1','period_2']]
sub_set_filled = knn_filler(sub_data_set)

# now we replace the columns in the main data frame with data in sub_set_filled
columns = ['current_score','display_score','period_1','period_2']
MatchHomeScoreInfo[columns] = sub_set_filled[columns]

MatchHomeScoreInfo.isnull().sum()

# [markdown]
# Cleaning TimeInfo

TimeInfo.isnull().sum()

# [markdown]
# there are around 3500 records that there is no information about their first and second periods. 
# It is to big to simply remove the rows so we fill these records using trimmed mean of each columns.

# first we need to calculate how many sets has been played 
match_id_null_time = TimeInfo.loc[TimeInfo['period_1'].isnull() | 
                                  TimeInfo['period_2'].isnull() ,'match_id']
periods = ['period_1', 'period_2', 'period_3', 'period_4', 'period_5']
played_periods = {}
for match_id in match_id_null_time:
    matched_data = MatchAwayScoreInfo.loc[MatchAwayScoreInfo['match_id'].eq(match_id)]
    periods_played = matched_data[periods].ne(-1).sum(axis=1).max()
    played_periods[match_id] = periods_played

mean_time_period1 = TimeInfo['period_1'].mean()
mean_time_period2 = TimeInfo['period_2'].mean()
mean_time_period3 = TimeInfo['period_3'].mean()
mean_time_period4 = TimeInfo['period_4'].mean()
mean_time_period5 = TimeInfo['period_5'].mean()
means = [mean_time_period1,mean_time_period2,mean_time_period3,
         mean_time_period4,mean_time_period5]

# means

# Now we update periods by trimmed mean that we calculated based on the number of periods that a match has.
periods = ['period_1', 'period_2', 'period_3', 'period_4', 'period_5']

for match_id in match_id_null_time:
    if match_id in played_periods:
        for i in range(played_periods[match_id]):
            if TimeInfo.loc[TimeInfo['match_id'].eq(match_id), periods[i]].isnull().all():
                TimeInfo.loc[TimeInfo['match_id'] == match_id, periods[i]] = means[i]
            else:
                continue
    else:
        continue


# There are afew games that went on to periods 3 - 5. -1 placed for periods that was not happened.
# now we check the scores if there is -1 for a period we update time by 0.
periods = ['period_3', 'period_4', 'period_5']


for match_id in TimeInfo['match_id']:
    for period in periods:
        score_value = MatchAwayScoreInfo.loc[MatchAwayScoreInfo['match_id'] == match_id, period].values[0]
        if score_value == -1:
            TimeInfo.loc[TimeInfo['match_id'] == match_id, period] = 0

        if pd.isna(TimeInfo.loc[TimeInfo['match_id'] == match_id, period]).values[0]:
            TimeInfo.loc[TimeInfo['match_id'] == match_id, period] = 0


# we use KNN to fill up the current_period_start_timestamp column
time_imputed = knn_filler(TimeInfo,k=10)
TimeInfo['current_period_start_timestamp'] = time_imputed['current_period_start_timestamp']

TimeInfo.isnull().sum()
# Now The data is clean

# [markdown]
# Cleaning PeriodInfo

PeriodInfo.isnull().sum()
PeriodInfo.loc[PeriodInfo['home_value'].eq(0),'home_total'].unique()
PeriodInfo.loc[PeriodInfo['away_value'].eq(0),'away_total'].unique()

# since there is no clear relatioship between home_value and home_total,
# and also between away_valu and away_total knn will be used to fill these two columns
period_imputed = knn_filler(PeriodInfo,k=20)
PeriodInfo[['home_total','away_total']] = period_imputed[['home_total','away_total']]
# Now The data is clean

# [markdown]
# Cleaning OddsInfo

OddsInfo.isnull().sum()
# OddsInfo.head()

# the relationship is not clear so knn will be used to fill up null values in winning columns.
odd_imputed = knn_filler(OddsInfo,k=20)
OddsInfo['winnig'] = odd_imputed['winnig']

OddsInfo.isnull().sum()
# Now the data is clean

MatchEventInfo.to_parquet('../Cleaned_data/MatchEventInfo.parquet')
MatchVotesInfo.to_parquet('../Cleaned_data/MatchVotesInfo.parquet')
MatchTournamentInfo.to_parquet('../Cleaned_data/MatchTournamentInfo.parquet')
MatchSeasonInfo.to_parquet('../Cleaned_data/MatchSeasonInfo.parquet')
MatchVenueInfo.to_parquet('../Cleaned_data/MatchVenueInfo.parquet')
MatchAwayTeamInfo.to_parquet('../Cleaned_data/MatchAwayTeamInfo.parquet')
MatchRoundInfo.to_parquet('../Cleaned_data/MatchRoundInfo.parquet')
MatchAwayScoreInfo.to_parquet('../Cleaned_data/MatchAwayScoreInfo.parquet')
MatchHomeScoreInfo.to_parquet('../Cleaned_data/MatchHomeScoreInfo.parquet')
MatchHomeTeamInfo.to_parquet('../Cleaned_data/MatchHomeTeamInfo.parquet')
PowerInfo.to_parquet('../Cleaned_data/PowerInfo.parquet')
GameInfo.to_parquet('../Cleaned_data/GameInfo.parquet')
OddsInfo.to_parquet('../Cleaned_data/OddsInfo.parquet')
TimeInfo.to_parquet('../Cleaned_data/TimeInfo.parquet')
PeriodInfo.to_parquet('../Cleaned_data/PeriodInfo.parquet')

# PeriodInfo

