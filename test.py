import requests
import csv
import xlrd
import config

TBAauthKey = config.TBAauthKey
url = "https://www.thebluealliance.com/api/v3/"
headers = {"Accept": "application/json", "X-TBA-Auth-Key": TBAauthKey}
mumber = xlrd.open_workbook('C:\\2018cthar\\2018ctharMumber.xlsm')
specs = mumber.sheet_by_name('pythonSpecs')

start = int((specs.cell(3,2)).value)
print(start)

stop = int((specs.cell(4,2)).value)
print(stop)

# get the eventKey value from Mumber
eventKey = str((specs.cell(2, 2)).value)
print(eventKey)

'''
eventKey = "2018ctwat"
'''
# get all match keys
request1 = requests.get(url + "event/" + eventKey + "/matches/keys", headers=headers)
allMatchKeys = request1.json()

for match in allMatchKeys:
    matchKey = match

    if matchKey[10:12] == "qm" :
        matchNum = int(float(matchKey[12:]))

        if matchNum > start and matchNum <= stop:
            request2 = requests.get(url + "match/" + matchKey, headers=headers)
            data = request2.json()
            with open("C:\\2018cthar\\" + eventKey + "MatchDetails.csv", 'a', encoding="utf-8", newline='') as csvFile:
                dataWriter = csv.writer(csvFile, dialect='excel')
                if (matchNum == 1):
                    dataWriter.writerow([
                        "matchNumber", "matchKey",
                        "blue1", "blue2", "blue3", "red1", "red2", "red3",
                        "blueScore", "redScore",
                        "post_result_time", "predicted_time",
                        "blueAdjustPoints", "blueAutoOwnership", "blueAutoPts", "blueAutoRanking",
                        "blueAutoBot1", "blueAutoBot2", "blueAutoBot3",
                        "blueAutoRunPoints", "blueAutoScaleOwnershipSec", "blueAutoSwitchAtZero",
                        "blueAutoSwitchOwnershipSpec",
                        "blueEndGamePoints",
                        "blueEndGameBot1", "blueEndGameBot2", "blueEndGameBot3",
                        "blueEndGameRP",
                        "blueFoulCount", "blueFoulPts",
                        "blueRP", "tbaGameData", "blueTechFoulCount",
                        # TO stands for Tele-Op
                        "blueTOownership", "blueTOpts", "blueScaleBoost", "blueScaleForce",
                        "blueTOscaleOwnershipSec", "blueTOswitchBoost", "blueTOswitchForce",
                        "blueTOswitchOwnershipSec",
                        "blueBoostPlayed", "blueBoostTotal", "blueForcePlayed", "blueForceTotal",
                        "blueLevitatePlayed", "blueLevitateTotal", "blueVaultPts",

                        "redAdjustPoints", "redAutoOwnership", "redAutoPts", "redAutoRanking",
                        "redAutoBot1", "redAutoBot2", "redAutoBot3",
                        "redAutoRunPoints", "redAutoScaleOwnershipSec", "redAutoSwitchAtZero",
                        "redAutoSwitchOwnershipSpec",
                        "redEndGamePoints",
                        "redEndGameBot1", "redEndGameBot2", "redEndGameBot3",
                        "redEndGameRP",
                        "redFoulCount", "redFoulPts",
                        "redRP", "tbaGameData", "redTechFoulCount",
                        # TO stands for Tele-Op
                        "redTOownership", "redTOpts", "redScaleBoost", "redScaleForce",
                        "redTOscaleOwnershipSec", "redTOswitchBoost", "redTOswitchForce",
                        "redTOswitchOwnershipSec",
                        "redBoostPlayed", "redBoostTotal", "redForcePlayed", "redForceTotal",
                        "redLevitatePlayed", "redLevitateTotal", "redVaultPts"
                    ])

                dataWriter.writerow([
                    data["match_number"],
                    data["key"],
                    data["alliances"]["blue"]["team_keys"][0][3:],
                    data["alliances"]["blue"]["team_keys"][1][3:],
                    data["alliances"]["blue"]["team_keys"][2][3:],
                    data["alliances"]["red"]["team_keys"][0][3:],
                    data["alliances"]["red"]["team_keys"][1][3:],
                    data["alliances"]["red"]["team_keys"][2][3:],
                    data["alliances"]["blue"]["score"],
                    data["alliances"]["red"]["score"],
                    data["post_result_time"],
                    data["predicted_time"],
                    data["score_breakdown"]["blue"]["adjustPoints"],
                    data["score_breakdown"]["blue"]["autoOwnershipPoints"],
                    data["score_breakdown"]["blue"]["autoPoints"],
                    data["score_breakdown"]["blue"]["autoQuestRankingPoint"],
                    data["score_breakdown"]["blue"]["autoRobot1"],
                    data["score_breakdown"]["blue"]["autoRobot2"],
                    data["score_breakdown"]["blue"]["autoRobot3"],
                    data["score_breakdown"]["blue"]["autoRunPoints"],
                    data["score_breakdown"]["blue"]["autoScaleOwnershipSec"],
                    data["score_breakdown"]["blue"]["autoSwitchAtZero"],
                    data["score_breakdown"]["blue"]["autoSwitchOwnershipSec"],
                    data["score_breakdown"]["blue"]["endgamePoints"],
                    data["score_breakdown"]["blue"]["endgameRobot1"],
                    data["score_breakdown"]["blue"]["endgameRobot2"],
                    data["score_breakdown"]["blue"]["endgameRobot3"],
                    data["score_breakdown"]["blue"]["faceTheBossRankingPoint"],
                    data["score_breakdown"]["blue"]["foulCount"],
                    data["score_breakdown"]["blue"]["foulPoints"],
                    data["score_breakdown"]["blue"]["rp"],
                    data["score_breakdown"]["blue"]["tba_gameData"],
                    data["score_breakdown"]["blue"]["techFoulCount"],
                    data["score_breakdown"]["blue"]["teleopOwnershipPoints"],
                    data["score_breakdown"]["blue"]["teleopPoints"],
                    data["score_breakdown"]["blue"]["teleopScaleBoostSec"],
                    data["score_breakdown"]["blue"]["teleopScaleForceSec"],
                    data["score_breakdown"]["blue"]["teleopScaleOwnershipSec"],
                    data["score_breakdown"]["blue"]["teleopSwitchBoostSec"],
                    data["score_breakdown"]["blue"]["teleopSwitchForceSec"],
                    data["score_breakdown"]["blue"]["teleopSwitchOwnershipSec"],
                    data["score_breakdown"]["blue"]["vaultBoostPlayed"],
                    data["score_breakdown"]["blue"]["vaultBoostTotal"],
                    data["score_breakdown"]["blue"]["vaultForcePlayed"],
                    data["score_breakdown"]["blue"]["vaultForceTotal"],
                    data["score_breakdown"]["blue"]["vaultLevitatePlayed"],
                    data["score_breakdown"]["blue"]["vaultLevitateTotal"],
                    data["score_breakdown"]["blue"]["vaultPoints"],

                    data["score_breakdown"]["red"]["adjustPoints"],
                    data["score_breakdown"]["red"]["autoOwnershipPoints"],
                    data["score_breakdown"]["red"]["autoPoints"],
                    data["score_breakdown"]["red"]["autoQuestRankingPoint"],
                    data["score_breakdown"]["red"]["autoRobot1"],
                    data["score_breakdown"]["red"]["autoRobot2"],
                    data["score_breakdown"]["red"]["autoRobot3"],
                    data["score_breakdown"]["red"]["autoRunPoints"],
                    data["score_breakdown"]["red"]["autoScaleOwnershipSec"],
                    data["score_breakdown"]["red"]["autoSwitchAtZero"],
                    data["score_breakdown"]["red"]["autoSwitchOwnershipSec"],
                    data["score_breakdown"]["red"]["endgamePoints"],
                    data["score_breakdown"]["red"]["endgameRobot1"],
                    data["score_breakdown"]["red"]["endgameRobot2"],
                    data["score_breakdown"]["red"]["endgameRobot3"],
                    data["score_breakdown"]["red"]["faceTheBossRankingPoint"],
                    data["score_breakdown"]["red"]["foulCount"],
                    data["score_breakdown"]["red"]["foulPoints"],
                    data["score_breakdown"]["red"]["rp"],
                    data["score_breakdown"]["red"]["tba_gameData"],
                    data["score_breakdown"]["red"]["techFoulCount"],
                    data["score_breakdown"]["red"]["teleopOwnershipPoints"],
                    data["score_breakdown"]["red"]["teleopPoints"],
                    data["score_breakdown"]["red"]["teleopScaleBoostSec"],
                    data["score_breakdown"]["red"]["teleopScaleForceSec"],
                    data["score_breakdown"]["red"]["teleopScaleOwnershipSec"],
                    data["score_breakdown"]["red"]["teleopSwitchBoostSec"],
                    data["score_breakdown"]["red"]["teleopSwitchForceSec"],
                    data["score_breakdown"]["red"]["teleopSwitchOwnershipSec"],
                    data["score_breakdown"]["red"]["vaultBoostPlayed"],
                    data["score_breakdown"]["red"]["vaultBoostTotal"],
                    data["score_breakdown"]["red"]["vaultForcePlayed"],
                    data["score_breakdown"]["red"]["vaultForceTotal"],
                    data["score_breakdown"]["red"]["vaultLevitatePlayed"],
                    data["score_breakdown"]["red"]["vaultLevitateTotal"],
                    data["score_breakdown"]["red"]["vaultPoints"],
                ])


            print(matchNum)
            print(data)

