import requests

nickname = "Fluffy"

session = requests.Session()
response = session.get("https://dirtrally2.com/api/Challenge/Community")
#Todo 200
communityJson = response.json()

#print and choice challange type
print("Challenges: ")
for i, element in enumerate(communityJson):
    print(f"{i}: {element['typeName']}")

print("Type the Id than press enter:")
challengeTypeIndex = int(input())

#print and choice challange date
print("Available days: ")
for i, element in enumerate(communityJson[challengeTypeIndex]["challengeGroups"]):
    print(f"{i}: {element['name']}")

print("Type the Id than press enter:")
challengeDateIndex = int(input())

challenges = communityJson[challengeTypeIndex]["challengeGroups"][challengeDateIndex]

#print and choice challange from available challenges that day
print("Available challenges: ")
for i, element in enumerate(challenges["challenges"]):
    print(f"{i}: {element['vehicleClass']}")

print("Type the Id than press enter:")
challengeIndex = int(input())

challenge = challenges["challenges"][challengeIndex]
challengeId = challenges["challenges"][challengeIndex]["id"]

eventId = None
if(len(challenge["events"]) == 1):
    eventId = challenge["events"][0]["id"]
else:
    #TODO megcsinálni, hogyne csak daily menjen
    print("Csak daily-re müködik a kód egyenlőre")
    quit()

data =  {"challengeId":challengeId,
    "selectedEventId":0,
    "stageId":0,
    "page":1,
    "pageSize":100,
    "orderByTotalTime": True,
    "platformFilter":"None",
    "playerFilter":"Everyone",
    "filterByAssists":"Unspecified",
    "filterByWheel":"Unspecified",
    "nationalityFilter":"None",
    "eventId":eventId
}


def getToken():
    resp = session.get("https://dirtrally2.com/api/ClientStore/GetInitialState")
    return resp.json()["identity"]["token"]
    
token = getToken()

headers = dict()
headers["RaceNet.XSRFH"]=token

leaderBoardResponse = session.post("https://dirtrally2.com/api/Leaderboard", json=data, headers = headers).json()

for i in range(1,leaderBoardResponse["pageCount"] + 1):
    if(i != 1):
        data["page"] = i 
        leaderBoardResponse = session.post("https://dirtrally2.com/api/Leaderboard", json=data, headers = headers).json()
    rank = "--"

    for item in leaderBoardResponse["entries"]:
        if item["name"] == nickname:
            rank = str(item["rank"])
            break

    if i != leaderBoardResponse['pageCount']:
        data["page"] = leaderBoardResponse["pageCount"]
        leaderBoardResponse = session.post("https://dirtrally2.com/api/Leaderboard", json=data, headers = headers).json()
    playerCount = str((leaderBoardResponse['pageCount']-1)*100+len(leaderBoardResponse['entries']))
    
    print(f"Versenyen elért eredményed: {rank}/{playerCount}")
    break


