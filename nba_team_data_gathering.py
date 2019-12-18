import pandas as pd
import time

from nba_api.stats.endpoints import teamyearbyyearstats
from nba_api.stats.endpoints import teamgamelog
from nba_api.stats.endpoints import leaguedashteamstats
from nba_api.stats.endpoints import boxscoresummaryv2


'''
This portion of the code is to implant the current seasons team stats up to date [season = '2019-20']
We then want assign it to a data frame
'''
nbaTeamStats = leaguedashteamstats.LeagueDashTeamStats(season='2019-20')

df_teamStats = nbaTeamStats.get_data_frames()[0]
#print(df_teamStats) #Check if data frame is correctly filled

df_teamStats.to_pickle("/Users/anshumandash/nba_analysis_project/df_teamStats.pkl")


df_season_game_log = pd.DataFrame()

for i in range(0,len(df_teamStats),1):
#for i in range(0,2,1):
    #nbaTeamStatsDataFrame = df_teamStats.loc[[i],["TEAM_ID","TEAM_NAME","GP","PTS"]] These work right now
    #print(nbaTeamStatsDataFrame)

    nbaTeamID = df_teamStats.loc[i]['TEAM_ID']

    nbaSeasonGameLog = teamgamelog.TeamGameLog(season= "2019-20", team_id = nbaTeamID, season_type_all_star= "Regular Season")  

    df2=nbaSeasonGameLog.get_data_frames()[0]
    df_season_game_log = df_season_game_log.append(pd.DataFrame(df2))     #https://stackoverflow.com/questions/37009287/using-pandas-append-within-for-loop/37009377
       

df_season_game_log.to_pickle("/Users/anshumandash/nba_analysis_project/df_season_game_log.pkl")
#print(df_season_game_log) 

summaryBoxScoreDataFrame = pd.DataFrame()
filtered_df_season_game_log = df_season_game_log.drop_duplicates(subset=['Game_ID']).reset_index(drop=True)

##### This is to help populate the whole summary Box Score Data Frame with ALL Data ######

for i in range(0, len(filtered_df_season_game_log), 1):
#for i in range (0, 5, 1):   
    gameID = filtered_df_season_game_log.loc[i]['Game_ID']
    
    BoxScoreSummary = boxscoresummaryv2.BoxScoreSummaryV2(game_id = gameID)
    dfLocal = BoxScoreSummary.line_score.get_data_frame()
    summaryBoxScoreDataFrame = summaryBoxScoreDataFrame.append(pd.DataFrame(dfLocal))
    
    time.sleep(1)

summaryBoxScoreDataFrame.to_pickle("/Users/anshumandash/nba_analysis_project/boxScoreData.pkl")
print(summaryBoxScoreDataFrame)

########### END ############

##### To help populate summary data frame by date #####

'''Currently not working, In-Progress'''

# nbaTeamBoxScoreData = pd.read_pickle("/Users/anshumandash/nba_analysis_project/boxscoreData.pkl")

# for i in range(0, len(filtered_df_season_game_log),1):
#     gameID = filtered_df_season_game_log.loc[i]['Game_ID']
#     if filtered_df_season_game_log.loc[i]['GAME_DATE'] == "DEC 17, 2019":   #### Change Date to add games for that date
#         BoxScoreSummary = boxscoresummaryv2.BoxScoreSummaryV2(game_id = gameID)
#         dfLocal = BoxScoreSummary.line_score.get_data_frame()
#         nbaTeamBoxScoreData = nbaTeamBoxScoreData.append(pd.DataFrame(dfLocal))
#     else:
#         break


# nbaTeamBoxScoreData = nbaTeamBoxScoreData.drop_duplicates(subset=['GAME_ID' , 'TEAM_ABBREVIATION']).reset_index(drop=True)
# nbaTeamBoxScoreData.to_pickle("/Users/anshumandash/nba_analysis_project/boxScoreData.pkl")

########### END ###########

