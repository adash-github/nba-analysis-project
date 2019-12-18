# nba-analysis-project

### About:
Project to analyze NBA teams and players using Python. Using swar's https://github.com/swar/nba_api. This project aims to help NBA fans preview NBA games, looking at team stats, player stats, and model possible outcomes.

### Development Status:
Dec 18, 2019 - Added first files to create local pickles files of all current season (2019-2020) season games using the nba_team_data_gathering.py file. The nba_analysis_functions.py file allows user to call functions to output an NBA teams average points per game (ppg), quarterly ppg's, and standard deviations for each. 

### Goals:
1. Add game data to pickle files by date. This will save time without having to request all data up to current date, and instead add data by the date needed. Currently in progress. 
2. Begin Flask integration
  a. Create input/output options using pickle data.
  
3. Create a database structure to easily query data needed for display
  a. Begin transfering data to database, and create functions to auto add data by date, and not have to download all data.
  b. Create simple input/output display options for user.

