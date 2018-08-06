import requests
import tbapy
import json
import csv

url = "https://www.thebluealliance.com/api/v3/"
TBAauthKey = "YbXeFRaoLQ8nnpXSlKM3unZokhN0VZWrSAcQF0uPQljRgI7wi4dgVB6fMGtQCDep"
headers = {"Accept":"application/json","X-TBA-Auth-Key":TBAauthKey}

#for future use, replace these variables with functions that look up the values from excel by cell name
year = "2018"
eventKey = "ctsct"

request1 = requests.get(url + "event/"+year+eventKey+"/teams/keys", headers = headers)
teams = request1.json()
teamKeys = []
for team in teams:
    teamKeys.append(team)

request2 = requests.get(url + "event/"+year+eventKey+"/district_points", headers=headers)
pointsData = request2.json()["points"]

with open ("districtPoints.csv",'w', encoding = "utf-8", newline = '') as csv_file:
    data_writer = csv.writer (csv_file, dialect = 'excel')
    data_writer.writerow(["teamNumber", "Qualification", "Alliance","Elimination", "Award", "Total"])

    for data in pointsData:
        data_writer.writerow([
            data[3:],
            pointsData[data]["qual_points"],
            pointsData[data]["alliance_points"],
            pointsData[data]["elim_points"],
            pointsData[data]["award_points"],
            pointsData[data]["total"]
        ])

