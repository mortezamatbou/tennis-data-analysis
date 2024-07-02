import pandas as pd
import numpy as np
import os
import zipfile
import shutil
import filecmp
from tennis_data_analysis.config import RAW_DATA_DIR, INTERIM_DATA_DIR, PROCESSED_DATA_DIR


INTERIM   = INTERIM_DATA_DIR / '02'
PROCESSED = PROCESSED_DATA_DIR / '02'


def extract_zip_files(main_zipfile, destination_folder):
    """
    Extracting Nested ZipFiles.

    Parameters:
    main_zipfile (str): The path to the main(root) zipfile.
    destination_folder (str): The path to where extracted files should be placed.
    
    """
    # Making a destination directory 
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Extract the main zip file
    with zipfile.ZipFile(main_zipfile, 'r') as main_zip:
        main_zip.extractall(destination_folder)

    # Creating a list of zipfiles inside the main one
    nested_zip_files = [os.path.join(destination_folder, filename) for filename in os.listdir(destination_folder) if filename.endswith('.zip')]

    for nested_zip in nested_zip_files:
        # Create a directory with the same name as the zip file
        nested_destination = os.path.join(destination_folder, os.path.splitext(os.path.basename(nested_zip))[0])
        os.makedirs(nested_destination, exist_ok=True)

        # Extract all the nested zipfiles
        with zipfile.ZipFile(nested_zip, 'r') as nested_zipfile:
            nested_zipfile.extractall(nested_destination)


def collect_files(source_root, destination_folder, target_subdir, target_filename_prefix):
    """
    Create directories based on the given schema and gather all data from the same category in each directory.
    Remove duplicates if found.

    Parameters:
    source_root (str): Directory that has all the 31 days data.
    destination_folder (str): Directory to collect the files from the same category into.
    target_subdir (str): The directory where we can find desired files.
    target_filename_prefix (str): Prefix of the files to collect.
    """
    
    # Make the destination directory if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Explore the directory structure
    for root, dirs, files in os.walk(source_root):
        # Check if the current directory is the target directory
        if os.path.basename(root) == target_subdir:
            # Copy the files to the destination folder
            for file in files:
                if file.startswith(target_filename_prefix):
                    source_file_path = os.path.join(root, file)
                    destination_file_path = os.path.join(destination_folder, file)
                    
                    # Check if the file already exists in the destination folder
                    if os.path.exists(destination_file_path):
                        os.remove(source_file_path)
                    else:
                        shutil.move(source_file_path, destination_file_path)
                        print(f"Copied {source_file_path} to {destination_file_path}")


def create_dataframe(folder_path):
    """
    Reads all Parqucoet files in a folder and concatenates them into a single DataFrame.

    Parameters:
    folder_path (str): The path to the folder containing the Parquet files.

    Returns:
    pd.DataFrame: A DataFrame containing the concatenated data from all Parquet files.
    """
    # List all Parquet files in the folder
    parquet_files = [f for f in os.listdir(folder_path) if f.endswith('.parquet')]
    
    # Read each Parquet file and concatenate into a single dataframe
    dataframes = [pd.read_parquet(os.path.join(folder_path, f)) for f in parquet_files]
    combined_dataframe = pd.concat(dataframes, ignore_index=True)
    
    return combined_dataframe

# away_team_score   = raw_match_parquet/away_team_score_12260075.parquet
# home_team_score   = raw_match_parquet/home_team_score_12260075.parquet
# away_team         = raw_match_parquet/away_team_12260075.parquet
# home_team         = raw_match_parquet/home_team_12260075.parquet
# event             = raw_match_parquet/event_12260075.parquet
# rond              = raw_match_parquet/round_12260075.parquet
# season            = raw_match_parquet/season_12260075.parquet
# time              = raw_match_parquet/time_12260075.parquet
# tournoment        = raw_match_parquet/tournament_12260075.parquet
# venue             = raw_match_parquet/venue_12260075.parquet

# pbp               = raw_point_by_point_parquet/pbp_12260075.parquet

# statistics        = raw_statistics_parquet/statistics_12260075.parquet



# Example usage -------------------------------------------------------------------------------------
#                                                                                                   -
# source_root               = RAW_DATA_DIR / "raw_data" # Directory that has all the 31 days data   -
# destination_folder        = RAW_DATA_DIR / "03/Venue" # Folder to collect the files into          -
# target_subdir             = "raw_match_parquet"       # Target subdirectory                       -
# target_filename_prefix    = "venue"                   # Prefix of the files to collect            -
# ---------------------------------------------------------------------------------------------------

_files = [
    {
        'source_root': INTERIM,
        'destination_folder': INTERIM / "AwayTeamScore",
        'target_subdir': "raw_match_parquet",
        'target_filename_prefix': "away_team_score",
        'result_parquet_name': 'MatchAwayScoreInfo'
    },
    {
        'source_root': INTERIM / 'raw_data',
        'destination_folder': INTERIM / "HomeTeamScore",
        'target_subdir': "raw_match_parquet",
        'target_filename_prefix': "home_team_score",
        'result_parquet_name': 'MatchHomeScoreInfo'
    },
    {
        'source_root': INTERIM,
        'destination_folder': INTERIM / "AwayTeam",
        'target_subdir': "raw_match_parquet",
        'target_filename_prefix': "away_team",
        'result_parquet_name': 'MatchAwayTeamInfo'
    },
    {
        'source_root': INTERIM,
        'destination_folder': INTERIM / "HomeTeam",
        'target_subdir': "raw_match_parquet",
        'target_filename_prefix': "home_team",
        'result_parquet_name': 'MatchHomeTeamInfo'
    },
    {
        'source_root': INTERIM,
        'destination_folder': INTERIM / "Event",
        'target_subdir': "raw_match_parquet",
        'target_filename_prefix': "event",
        'result_parquet_name': 'MatchEventInfo'
    },
    {
        'source_root': INTERIM,
        'destination_folder': INTERIM / "Round",
        'target_subdir': "raw_match_parquet",
        'target_filename_prefix': "round",
        'result_parquet_name': 'MatchRoundInfo'
    },
    {
        'source_root': INTERIM,
        'destination_folder': INTERIM / "Season",
        'target_subdir': "raw_match_parquet",
        'target_filename_prefix': "season",
        'result_parquet_name': 'MatchSeasonInfo'
    },
    {
        'source_root': INTERIM,
        'destination_folder': INTERIM / "Time",
        'target_subdir': "raw_match_parquet",
        'target_filename_prefix': "time",
        'result_parquet_name': 'TimeInfo'
    },
    {
        'source_root': INTERIM,
        'destination_folder': INTERIM / "Tournament",
        'target_subdir': "raw_match_parquet",
        'target_filename_prefix': "tournament",
        'result_parquet_name': 'MatchTournamentInfo'
    },
    {
        'source_root': INTERIM,
        'destination_folder': INTERIM / "Venue",
        'target_subdir': "raw_match_parquet",
        'target_filename_prefix': "venue",
        'result_parquet_name': 'MatchVenueInfo'
    },
    {
        'source_root': INTERIM,
        'destination_folder': INTERIM / "Pbp",
        'target_subdir': "raw_point_by_point_parquet",
        'target_filename_prefix': "pbp",
        'result_parquet_name': 'MatchAwayScoreInfo'
    },
    {
        'source_root': INTERIM,
        'destination_folder': INTERIM / "Statistics",
        'target_subdir': "raw_statistics_parquet",
        'target_filename_prefix': "statistics",
        'result_parquet_name': 'PeriodInfo'
    },
]

# Votes Power Odds

# Extract zip files
extract_zip_files(RAW_DATA_DIR / '202405.zip', INTERIM / 'raw_data')


for f in _files:
    collect_files(f['source_root'], f['destination_folder'], f['target_subdir'], f['target_filename_prefix'])
    # df = create_dataframe(INTERIM / 'HomeTeamScore')
    # df.to_parquet(PROCESSED / 'MatchHomeScoreInfo.parquet')


# Integrate parquet files from different days to dataframes
# Save integrated parquets file to /data/processed/02

MatchHomeScoreInfo = create_dataframe(INTERIM / 'HomeTeamScore')
MatchHomeScoreInfo.to_parquet(PROCESSED / 'MatchHomeScoreInfo.parquet')

MatchAwayScoreInfo = create_dataframe(INTERIM / 'AwayTeamScore')
MatchAwayScoreInfo.to_parquet(PROCESSED / 'MatchAwayScoreInfo.parquet')

MatchHomeTeamInfo = create_dataframe(INTERIM / 'HomeTeam')
MatchHomeTeamInfo.to_parquet(PROCESSED / 'MatchHomeTeamInfo.parquet')

MatchAwayTeamInfo = create_dataframe(INTERIM / 'AwayTeam')
MatchAwayTeamInfo.to_parquet(PROCESSED / 'MatchAwayTeamInfo.parquet')

MatchEventInfo = create_dataframe(INTERIM / 'Event')
MatchEventInfo.to_parquet(PROCESSED / 'MatchEventInfo.parquet')

MatchRoundInfo = create_dataframe(INTERIM / 'Round')
MatchRoundInfo.to_parquet(PROCESSED / 'MatchRoundInfo.parquet')

MatchSeasonInfo = create_dataframe(INTERIM / 'Season')
MatchSeasonInfo.to_parquet(PROCESSED / 'MatchSeasonInfo.parquet')

TimeInfo = create_dataframe(INTERIM / 'Time')
TimeInfo.to_parquet(PROCESSED / 'TimeInfo.parquet')

MatchTournamentInfo = create_dataframe(INTERIM / 'Tournament')
MatchTournamentInfo.to_parquet(PROCESSED / 'MatchTournamentInfo.parquet')

MatchVenueInfo = create_dataframe(INTERIM / 'Venue')
MatchVenueInfo.to_parquet(PROCESSED / 'MatchVenueInfo.parquet')

PeriodInfo = create_dataframe(INTERIM / 'Statistics')
PeriodInfo.to_parquet(PROCESSED / 'PeriodInfo.parquet')


GameInfo = create_dataframe(INTERIM / 'GameInfo')
GameInfo.to_parquet(PROCESSED / 'GameInfo.parquet')

MatchVotesInfo = create_dataframe(INTERIM / 'Votes')
MatchVotesInfo.to_parquet(PROCESSED / 'MatchVotesInfo.parquet')

PowerInfo = create_dataframe(INTERIM / 'Power')
PowerInfo.to_parquet(PROCESSED / 'PowerInfo.parquet')

OddsInfo = create_dataframe(INTERIM / 'Odds')
OddsInfo.to_parquet(PROCESSED / 'OddsInfo.parquet')

