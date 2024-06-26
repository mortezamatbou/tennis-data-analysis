import os
from dotenv import load_dotenv, find_dotenv
import pandas as pd
import numpy as np
import mysql.connector


# find .env automagically by walking up directories until it's found
dotenv_path = find_dotenv()

# load up the entries as environment variables
load_dotenv(dotenv_path)

# Insert cleaned data to database
conn = mysql.connector.connect(
    host=os.environ.get("DB_HOST"),
    user=os.environ.get("DB_USERNAME"),
    password=os.environ.get("DB_PASSWORD"),
    database=os.environ.get("DB_DATABASE"),
    port=os.environ.get("DB_PORT")
)

db = conn.cursor()

"""
Table details:


01]
MatchEventInfo
    match_id,
    first_to_serve,
    home_team_seed,
    away_team_seed,
    custom_id,
    winner_code,
    default_period_count,
    start_datetime,
    match_slug,
    final_result_only

.
.
.

MatchTournamentInfo
    match_id,
    tournament_id,
    tournament_name,
    tournament_slug,
    tournament_unique_id,
    tournament_category_name,
    tournament_category_slug,
    user_count,
    ground_type,
    tennis_points,
    has_event_player_statistics,
    crowd_sourcing_enabled,
    has_performance_graph_feature,
    display_inverse_home_away_teams,
    priority
    competition_type
---------------------------------
MatchHomeScoreInfo
    match_id,
    current_score,
    display_score,
    period_1,
    period_2,
    period_3,
    period_4,
    period_5,
    period_1_tie_break,
    period_2_tie_break,
    period_3_tie_break,
    period_4_tie_break,
    period_5_tie_break,
    normal_time
---------------------------------
MatchHomeTeamInfo
    match_id,
    name,
    slug,
    gender,
    user_count,
    residence,
    birthplace,
    height,
    weight,
    plays,
    turned_pro,
    current_prize,
    total_prize,
    player_id,
    current_rank,
    name_code,
    country,
    full_name
---------------------------------
MatchAwayScoreInfo
    match_id,
    current_score,
    display_score,
    period_1,
    period_2,
    period_3,
    period_4,
    period_5,
    period_1_tie_break,
    period_2_tie_break,
    period_3_tie_break,
    period_4_tie_break,
    period_5_tie_break,
    normal_time
---------------------------------
MatchAwayTeamInfo
    match_id,
    name,
    slug,
    gender,
    user_count,
    residence,
    birthplace,
    height,
    weight,
    plays,
    turned_pro,
    current_prize,
    total_prize,
    player_id,
    current_rank,
    name_code,
    country,
    full_name
---------------------------------
MatchVenueInfo
    match_id,
    city,
    stadium,
    venue_id,
    country
---------------------------------
MatchSeasonInfo
    match_id,
    season_id,
    name,
    year
---------------------------------
MatchVotesInfo
    match_id,
    home_vote,
    away_vote
---------------------------------
MatchRoundInfo
    match_id,
    round_id,
    name,
    slug,
    cup_round_type
---------------------------------
MatchTimeInfo
    match_id,
    period_1,
    period_2,
    period_3,
    period_4,
    period_5,
    current_period_start_timestamp
---------------------------------
PeriodInfo
---------------------------------
GameInfo
    match_id,
    set_id,
    game_id,
    point_id,
    home_point,
    away_point,
    point_description,
    home_point_type,
    away_point_type,
    home_score
---------------------------------
OddsInfo
    match_id,
    market_id,
    market_name,
    is_live,
    suspended,
    initial_fractional_value,
    fractional_value,
    choice_name,
    choice_source_id,
    winnig,
    change
---------------------------------
PowerInfo
    match_id,
    set_num,
    game_num,
    value,
    break_occurred

"""
# give a dataframe, generate sql and execute


def df_to_table(table_name: str, df: pd.DataFrame):
    db.execute(f"TRUNCATE TABLE {table_name}")

    columns = ",".join(df.columns.to_list())
    holders = ",".join(["%s"] * df.columns.size)
    sql = f'INSERT INTO {table_name}({columns}) VALUES({holders})'
    for index, row in df.iterrows():
        values = tuple(row.values)
        try:
            db.execute(sql, values)
        except Exception as error:
            print(error)
            print(row)
            exit()

    conn.commit()


# ------- Find unique players from MatchAwayTeamInfo and MatchHomeTeamInfo ---------------------------------

V1_DATA_RAW_DIR = os.path.abspath('./data/raw/01')

df_away = pd.read_parquet(V1_DATA_RAW_DIR + '/MatchAwayTeamInfo.parquet')
df_home = pd.read_parquet(V1_DATA_RAW_DIR + '/MatchHomeTeamInfo.parquet')

players = pd.concat([pd.Series(df_away['slug'].unique()), pd.Series(df_home['slug'].unique())], axis=0)

players = pd.Series(players.unique())
players.dropna(inplace=True)

unique_players = []

for slug in players:
    player = df_away[df_away['slug'] == slug]
    if player.size:
        unique_players.append(player.iloc[0])
        continue

    player = df_home[df_home['slug'] == slug]
    if player.size:
        unique_players.append(player.iloc[0])


df = pd.DataFrame(unique_players)


df = df.dropna(axis=1, how='all')
# drop match_id column
df = df.drop(columns=['match_id'], axis=1)
df.reset_index(inplace=True, drop=True)

# save dataframe to new parquet file

df['height'] = df['height'].fillna(df['height'].mean())
df['weight'] = df['weight'].fillna(df['weight'].mean())
df['current_prize'] = df['current_prize'].fillna(0)
df['total_prize'] = df['total_prize'].fillna(0)
df['current_rank'] = df['current_rank'].fillna(0)

df.to_parquet()
df = df[['name', 'slug', 'gender', 'height', 'weight', 'plays', 'turned_pro', 'current_prize', 'total_prize', 'player_id', 'current_rank', 'country', 'full_name']]

df_to_table('Players', df)


# --------- Add MatchEventInfo dataframe to MatchEventInfo table ----------------

df = pd.read_parquet(V1_DATA_RAW_DIR + '/MatchEventInfo.parquet')

df['home_team_seed'] = df['home_team_seed'].fillna(0)
df['away_team_seed'] = df['away_team_seed'].fillna(0)
df['winner_code'] = df['winner_code'].fillna(0)
df['first_to_serve'] = df['first_to_serve'].fillna(0).astype(int)
df['winner_code'] = df['winner_code'].fillna(0).astype(int)
df['final_result_only'] = df['final_result_only'].fillna("Undefined").map({np.True_: 1, np.False_: 0, "Undefined": -1})


df_to_table('MatchEventInfo', df)


# --------- Add GameInfo dataframe to GameInfo table ----------------

df = pd.read_parquet(V1_DATA_RAW_DIR + '/GameInfo.parquet')
df_to_table('GameInfo', df)

# --------- Add MatchHomeTeamInfo dataframe to MatchHomeTeamInfo table ----------------

df = pd.read_parquet(V1_DATA_RAW_DIR + '/MatchHomeTeamInfo.parquet')
df['gender'] = df['gender'].fillna('U')
df['turned_pro'] = df['turned_pro'].fillna(0)
df['plays'] = df['plays'].fillna('Undefined')
df['weight'] = df['weight'].fillna(df['weight'].mean())
df['height'] = df['height'].fillna(df['height'].mean())
df['residence'] = df['residence'].fillna("")
df['current_rank'] = df['current_rank'].fillna(0)
df['total_prize'] = df['total_prize'].fillna(0)
df['current_prize'] = df['current_prize'].fillna(0)

df_to_table('MatchHomeTeamInfo', df)

# --------- Add MatchAwayTeamInfo dataframe to MatchAwayTeamInfo table ----------------

df = pd.read_parquet(V1_DATA_RAW_DIR + '/MatchAwayTeamInfo.parquet')
df['gender'] = df['gender'].fillna('U')
df['turned_pro'] = df['turned_pro'].fillna(0)
df['plays'] = df['plays'].fillna('Undefined')
df['weight'] = df['weight'].fillna(df['weight'].mean())
df['height'] = df['height'].fillna(df['height'].mean())
df['residence'] = df['residence'].fillna("")
df['current_rank'] = df['current_rank'].fillna(0)
df['total_prize'] = df['total_prize'].fillna(0)
df['current_prize'] = df['current_prize'].fillna(0)

df_to_table('MatchAwayTeamInfo', df)

# --------- Add PowerInfo dataframe to PowerInfo table ----------------
df = pd.read_parquet(V1_DATA_RAW_DIR + '/PowerInfo.parquet')
df['break_occurred'] = df['break_occurred'].fillna('U').map({np.True_: 1, np.False_: 0, 'U': -1})

df_to_table('PowerInfo', df)


# --------- Add MatchTimeInfo dataframe to MatchTimeInfo table ----------------
df = pd.read_parquet(V1_DATA_RAW_DIR + '/TimeInfo.parquet')

df['period_1'] = df['period_1'].fillna(0)
df['period_2'] = df['period_2'].fillna(0)
df['period_3'] = df['period_3'].fillna(0)
df['period_4'] = df['period_4'].fillna(0)
df['period_5'] = df['period_5'].fillna(0)
df['current_period_start_timestamp'] = df['current_period_start_timestamp'].fillna(0)

df_to_table('MatchTimeInfo', df)

# --------- Add OddsInfo dataframe to OddsInfo table ----------------

# df = pd.read_parquet(V1_DATA_RAW_DIR + '/OddsInfo.parquet')
# df_to_table('OddsInfo', df)

# --------- Add MatchVenueInfo dataframe to MatchVenueInfo table ----------------

df = pd.read_parquet(V1_DATA_RAW_DIR + '/MatchVenueInfo.parquet')
df_to_table('MatchVenueInfo', df)

# --------- Add MatchSeasonInfo dataframe to MatchSeasonInfo table ----------------

df = pd.read_parquet(V1_DATA_RAW_DIR + '/MatchSeasonInfo.parquet')
df_to_table('MatchSeasonInfo', df)

# --------- Add MatchVotesInfo dataframe to MatchVotesInfo table ----------------

df = pd.read_parquet(V1_DATA_RAW_DIR + '/MatchVotesInfo.parquet')
df['match_id'] = df['match_id'].astype(int)
df['away_vote'] = df['away_vote'].astype(int)
df['home_vote'] = df['home_vote'].astype(int)
df_to_table('MatchVotesInfo', df)

# --------- Add MatchRoundInfo dataframe to MatchRoundInfo table ----------------
df = pd.read_parquet(V1_DATA_RAW_DIR + '/MatchRoundInfo.parquet')
df['cup_round_type'] = df['cup_round_type'].fillna(0)

df_to_table('MatchRoundInfo', df)

# --------- Add MatchTournamentInfo dataframe to MatchTournamentInfo table ----------------
df = pd.read_parquet(V1_DATA_RAW_DIR + '/MatchTournamentInfo.parquet')

df['tournament_unique_id'] = df['tournament_unique_id'].fillna(0)
df['ground_type'] = df['ground_type'].fillna('Undefined')
df['tennis_points'] = df['tennis_points'].fillna(df['tennis_points'].mean())


df = df[['match_id', 'tournament_id', 'tournament_name', 'tournament_slug', 'tournament_category_name', 'tournament_category_slug', 'user_count', 'ground_type', 'tennis_points', 'priority', 'competition_type']]
df_to_table('MatchTournamentInfo', df)

# --------- Add MatchHomeScoreInfo dataframe to MatchHomeScoreInfo table ----------------
df = pd.read_parquet(V1_DATA_RAW_DIR + '/MatchHomeScoreInfo.parquet')

df['period_1'] = df['period_1'].fillna(-1)
df['period_2'] = df['period_2'].fillna(-1)
df['period_3'] = df['period_3'].fillna(-1)
df['period_4'] = df['period_4'].fillna(-1)
df['period_5'] = df['period_5'].fillna(-1)
df['current_score'] = df['current_score'].fillna(-1)
df['display_score'] = df['display_score'].fillna(-1)

df = df[['match_id', 'current_score', 'display_score', 'period_1', 'period_2', 'period_3', 'period_4', 'period_5']]
df_to_table('MatchHomeScoreInfo', df)

# --------- Add MatchAwayScoreInfo dataframe to MatchAwayScoreInfo table ----------------
df = pd.read_parquet(V1_DATA_RAW_DIR + '/MatchAwayScoreInfo.parquet')

df['period_1'] = df['period_1'].fillna(-1)
df['period_2'] = df['period_2'].fillna(-1)
df['period_3'] = df['period_3'].fillna(-1)
df['period_4'] = df['period_4'].fillna(-1)
df['period_5'] = df['period_5'].fillna(-1)
df['current_score'] = df['current_score'].fillna(-1)
df['display_score'] = df['display_score'].fillna(-1)

df = df[['match_id', 'current_score', 'display_score', 'period_1', 'period_2', 'period_3', 'period_4', 'period_5']]
df_to_table('MatchAwayScoreInfo', df)
