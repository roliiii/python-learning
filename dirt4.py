import requests
import json
from enum import Enum

class EventType(Enum):
    DiRT_DAILY_LIVE = "DiRT DAILY LIVE"
    OWNERS_CLUB = "THE OWNERS’ CLUB / DELTA DAILY"

class Dirt4RankUtil:
    def __init__(self, gamerMode: bool):
        self.session = requests.Session() 
        self.session.put(r"""https://www.dirt4game.com/api/profile/set-handling""",{"isAltHandling":gamerMode})

    def getUrl(self, eventId, page = 1):
        return r"""https://www.dirt4game.com/api/leaderboard/event/"""+str(eventId)+"""/stage/1/page/"""+str(page)+r"""?assists=0&controls=0&orderByTotal=true&pageSize=100&platform=0&players=0"""
    
    def getEventData(self, eventId, page = 1):
        data = self.session.get(self.getUrl(eventId, page))
        return data.json()

    def getEventId(self, eventType: EventType):
        data = self.session.get(r"""https://www.dirt4game.com/api/event/summary/?altHandling=false""")
        respJson = data.json()
        actEventTypeData = [x for x in respJson["eventTypes"] if x["name"] == eventType.value]

        return actEventTypeData[0]["events"][0]["eventId"]

    def getRank(self, eventType: EventType, userName: str):
        eventId = self.getEventId(eventType)
        parsedData = self.getEventData(eventId)

        for i in range(1,parsedData["PageCount"] + 1):
            if(i != 1):
                parsedData = getEventData(session, eventId, i)
            for item in parsedData["Entries"]:
                if item["Name"] == userName:
                    return("Rank: " + str(item["Rank"]) + "/" + str(len(parsedData["Entries"])))
            return None

if __name__ == "__main__":
    dirt = Dirt4RankUtil(False)
    print(dirt.getRank(EventType.OWNERS_CLUB,"Fluffy"))