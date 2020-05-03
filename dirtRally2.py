import requests

class dirtRankFinder():
    def __init__(self, name):
        self.session = requests.Session()
        self.nickname = name
        self.eventId = None
        self.challengeId = None

    def __eventChooser(self):
        response = self.session.get("https://dirtrally2.com/api/Challenge/Community")
        #Todo 200 if not raise exception
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
        self.challengeId = challenges["challenges"][challengeIndex]["id"]

        if(len(challenge["events"]) == 1):
            self.eventId = challenge["events"][0]["id"]
        else:
            #TODO megcsinálni, hogyne csak daily menjen
            print("Csak daily-re müködik a kód egyenlőre")
            raise NotImplementedError("To be implemented")

    def findRank(self):

        self.__eventChooser()

        if(self.eventId == None or self.challengeId == None):
            raise Exception("Nincs event kiválasztva")

        data =  {"challengeId":self.challengeId,
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
            "eventId":self.eventId
        }

        token = self.__getToken()

        headers = dict()
        headers["RaceNet.XSRFH"]=token

        leaderBoardResponse = self.session.post("https://dirtrally2.com/api/Leaderboard", json=data, headers = headers).json()

        rank = None
        page = 0
        for i in range(1,leaderBoardResponse["pageCount"] + 1):
            if(i != 1):
                data["page"] = i 
                leaderBoardResponse = self.session.post("https://dirtrally2.com/api/Leaderboard", json=data, headers = headers).json()
            
            for item in leaderBoardResponse["entries"]:
                if item["name"] == self.nickname:
                    rank = int(item["rank"])
                    page=i
                    break
            
            if(rank is not None):
                break

        if page != leaderBoardResponse['pageCount']:
            data["page"] = leaderBoardResponse["pageCount"]
            leaderBoardResponse = self.session.post("https://dirtrally2.com/api/Leaderboard", json=data, headers = headers).json()
        playerCount = str((leaderBoardResponse['pageCount']-1)*100+len(leaderBoardResponse['entries']))

        return (rank, playerCount)


    def __getToken(self):
        resp = self.session.get("https://dirtrally2.com/api/ClientStore/GetInitialState")
        return resp.json()["identity"]["token"]
    


if __name__ == "__main__":
    userName = "Fluffy"
    rankFinder = dirtRankFinder(userName)
    rank, playerCount = rankFinder.findRank()
    
    print(f"Elért eredmény: {rank}/{playerCount}")


