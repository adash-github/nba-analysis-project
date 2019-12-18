import pandas as pd
import pickle


# We need to load our files and assign them to variables to work some basic calculations
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_pickle.html  This is a helpful link to understand a part of the process

nbaTeamUnPickled = pd.read_pickle("/Users/anshumandash/nba_analysis_project/df_teamStats.pkl")
#print(nbaTeamUnPickled)

nbaTeamGameLogsUnPickled = pd.read_pickle("/Users/anshumandash/nba_analysis_project/df_season_game_log.pkl")
#print(nbaTeamGameLogsUnPickled)

nbaTeamBoxScoreData = pd.read_pickle("/Users/anshumandash/nba_analysis_project/boxScoreData.pkl")

#Find average points scored by each team

nbaTeamLength = len(nbaTeamUnPickled)
nbaTeamSummaryData = {}

######## Useful Functions for Team Analysis ###########

nbaTeamAbbrv = nbaTeamBoxScoreData.filter(['TEAM_ABBREVIATION']).drop_duplicates(subset = ['TEAM_ABBREVIATION']).reset_index(drop=True)

def nba_team_avg_ppg(team_abbrv):

    TeamPPGAvg = (nbaTeamBoxScoreData.loc[nbaTeamBoxScoreData['TEAM_ABBREVIATION'] == team_abbrv, 'PTS'].mean()) #/ (nbaTeamBoxScoreData.loc[nbaTeamBoxScoreData['TEAM_ABBREVIATION'] == team_abbrv, 'TEAM_ABBREVIATION'].count())
    
    TeamPPGAvgStd = (nbaTeamBoxScoreData.loc[nbaTeamBoxScoreData['TEAM_ABBREVIATION'] == team_abbrv, 'PTS'].std())

    print(TeamPPGAvg)
    print(TeamPPGAvgStd)

def nba_team_Q1_avg(team_abbrv):

    Q1boxscore = (nbaTeamBoxScoreData.loc[nbaTeamBoxScoreData['TEAM_ABBREVIATION'] == team_abbrv, 'PTS_QTR1'].mean()) #/ (nbaTeamBoxScoreData.loc[nbaTeamBoxScoreData['TEAM_ABBREVIATION'] == team_abbrv, 'TEAM_ABBREVIATION'].count())
    
    Q1boxscoreStd = (nbaTeamBoxScoreData.loc[nbaTeamBoxScoreData['TEAM_ABBREVIATION'] == team_abbrv, 'PTS_QTR1'].std())

    print(Q1boxscore)
    print(Q1boxscoreStd)

def nba_team_Q2_avg(team_abbrv):

    Q2boxscore = (nbaTeamBoxScoreData.loc[nbaTeamBoxScoreData['TEAM_ABBREVIATION'] == team_abbrv, 'PTS_QTR2'].mean()) #/ (nbaTeamBoxScoreData.loc[nbaTeamBoxScoreData['TEAM_ABBREVIATION'] == team_abbrv, 'TEAM_ABBREVIATION'].count())
    
    Q2boxscoreStd = (nbaTeamBoxScoreData.loc[nbaTeamBoxScoreData['TEAM_ABBREVIATION'] == team_abbrv, 'PTS_QTR2'].std())

    print(Q2boxscore)
    print(Q2boxscoreStd)

def nba_team_Q3_avg(team_abbrv):

    Q3boxscore = (nbaTeamBoxScoreData.loc[nbaTeamBoxScoreData['TEAM_ABBREVIATION'] == team_abbrv, 'PTS_QTR3'].mean()) #/ (nbaTeamBoxScoreData.loc[nbaTeamBoxScoreData['TEAM_ABBREVIATION'] == team_abbrv, 'TEAM_ABBREVIATION'].count())
    
    Q3boxscoreStd = (nbaTeamBoxScoreData.loc[nbaTeamBoxScoreData['TEAM_ABBREVIATION'] == team_abbrv, 'PTS_QTR3'].std())

    print(Q3boxscore)
    print(Q3boxscoreStd)

def nba_team_Q4_avg(team_abbrv):

    Q4boxscore = (nbaTeamBoxScoreData.loc[nbaTeamBoxScoreData['TEAM_ABBREVIATION'] == team_abbrv, 'PTS_QTR4'].mean()) #/ (nbaTeamBoxScoreData.loc[nbaTeamBoxScoreData['TEAM_ABBREVIATION'] == team_abbrv, 'TEAM_ABBREVIATION'].count())
    
    Q4boxscoreStd = (nbaTeamBoxScoreData.loc[nbaTeamBoxScoreData['TEAM_ABBREVIATION'] == team_abbrv, 'PTS_QTR4'].std())

    print(Q4boxscore)
    print(Q4boxscoreStd)

########## End ##########
nba_team_avg_ppg(input())
