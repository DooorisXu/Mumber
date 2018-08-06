import requests
import json
import csv
import xlrd

url = "https://www.thebluealliance.com/api/v3/"
TBAauthKey = "YbXeFRaoLQ8nnpXSlKM3unZokhN0VZWrSAcQF0uPQljRgI7wi4dgVB6fMGtQCDep"
headers = {"Accept":"application/json",
           "X-TBA-Auth-Key":TBAauthKey,}


year = "2018"
eventKey="ctwat"

response = requests.get(url + "event/"+year+eventKey+"/matches/simple", headers = headers)
data = response.json()
with open ("matchSchedule.csv",'w', encoding = "utf-8", newline = '') as csv_file:
    data_writer = csv.writer (csv_file, dialect = 'excel')
    data_writer.writerow(["MatchNumber", "Red1", "Red2", "Red3", "Blue1", "Blue2", "Blue3"])

    for item in data:
        if item["comp_level"] == "qm":
         data_writer.writerow([item["match_number"],
                              item["alliances"]["red"]["team_keys"][0][3:],
                              item["alliances"]["red"]["team_keys"][1][3:],
                              item["alliances"]["red"]["team_keys"][2][3:],
                              item["alliances"]["blue"]["team_keys"][0][3:],
                              item["alliances"]["blue"]["team_keys"][1][3:],
                              item["alliances"]["blue"]["team_keys"][2][3:],])