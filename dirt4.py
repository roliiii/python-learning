import requests
from multiprocessing.pool import ThreadPool
from enum import Enum

class EventType(Enum):
    DiRT_DAILY_LIVE = "DiRT DAILY LIVE"
    OWNERS_CLUB = "THE OWNERS’ CLUB / DELTA DAILY"

class Dirt4RankUtil:
    def __init__(self, gamerMode: bool):
        self.gamerMode = gamerMode
        self.session = requests.Session() 
        self.session.put(r"https://www.dirt4game.com/api/profile/set-handling",{"isAltHandling":gamerMode})

    def __getUrl(self, eventId, page = 1):
        return f"https://www.dirt4game.com/api/leaderboard/event/{str(eventId)}/stage/1/page/{str(page)}?assists=0&controls=0&orderByTotal=true&pageSize=100&platform=0&players=0"
    
    def __getEventData(self, eventId, page = 1):
        data = self.session.get(self.__getUrl(eventId, page))
        return data.json()

    def __getEventId(self, eventType: EventType):
        data = self.session.get(f"https://www.dirt4game.com/api/event/summary/?altHandling={str(self.gamerMode)}")
        if data.status_code != 200:
            raise Exception(f"can't reach the server: {data.status_code}")
        respJson = data.json()
        actEventTypeData = [x for x in respJson["eventTypes"] if x["name"] == eventType.value]
        return actEventTypeData[0]["events"][0]["eventId"]

    def getRank(self, eventType: EventType, userName: str):
        eventId = self.__getEventId(eventType)
        parsedData = self.__getEventData(eventId)

        for i in range(1,parsedData["PageCount"] + 1):
            if(i != 1):
                parsedData = self.__getEventData(eventId, i)
            rank = "--"

            for item in parsedData["Entries"]:
                if item["Name"] == userName:
                    rank = str(item["Rank"])
                    break

            if i != parsedData['PageCount']:
                parsedData = self.__getEventData(eventId, parsedData['PageCount'])
            playerCount = str((parsedData['PageCount']-1)*100+len(parsedData['Entries']))
            
            return f"{rank}/{playerCount}"

if __name__ == "__main__":
    userName = "Fluffy"
    dirt = Dirt4RankUtil(False)
    
    pool = ThreadPool(processes=2)
    dailyResult = pool.apply_async(dirt.getRank, (EventType.DiRT_DAILY_LIVE,userName))
    ownersResult = pool.apply_async(dirt.getRank, (EventType.OWNERS_CLUB,userName))

    print(EventType.DiRT_DAILY_LIVE.value + ": " + dailyResult.get())
    print(EventType.OWNERS_CLUB.value + ": " + ownersResult.get())