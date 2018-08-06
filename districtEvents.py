import json
import csv
import xlrd
import requests

url = "https://www.thebluealliance.com/api/v3/"
TBAauthKey = "YbXeFRaoLQ8nnpXSlKM3unZokhN0VZWrSAcQF0uPQljRgI7wi4dgVB6fMGtQCDep"
headers = {"Accept":"application/json","X-TBA-Auth-Key":TBAauthKey}

year = "2018"
districtKey = "ne"

response = requests.get (url + "district/"+ year + districtKey + "/events", headers = headers)
data = response.json()
'''
print (data)
'''
with open ("districtEvent.csv",'w', encoding = "utf-8", newline='') as csv_file:
    data_writer = csv.writer (csv_file, dialect = 'excel')
    data_writer.writerow(["eventKey", "week", "endDate", "town", "state", "address"])

    for item in data:
            data_writer.writerow([
                                  item["event_code"],
                                  int(item["week"]+1),
                                  item["end_date"],
                                  item["city"],
                                  item["state_prov"],
                                  item["address"],
                                   ])





