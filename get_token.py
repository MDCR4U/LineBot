import csv
import requests

def get_token(url ,wstoken):
    wurl = url + "token.csv"
    response = requests.get(wurl)
    if response.status_code != 200:
        return "Error: Cannot fetch data from the server."

    content = response.content.decode('utf-8')
    csv_reader = csv.reader(content.splitlines(), delimiter=',')

    header = next(csv_reader)
    if header != ["code", "description"]:
        return "Error: Invalid CSV header."

    for row in csv_reader:
        code, description = row
        if code == wstoken:
            print("get token return " + description)
            return description

    return "NF"

# 使用範例
#wstoken = "a001_1"
#print(get_token(wstoken))