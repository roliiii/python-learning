import requests
import json


url = r"""https://www.dirt4game.com/api/leaderboard/event/35675/stage/1/page/1?assists=0&controls=0&orderByTotal=true&pageSize=100&platform=0&players=0"""
data = requests.get(url, cookies={'ASP.NET_SessionId':'tein1ie5zj0kxcptu4rhyu2p'})
data = data.text

ranks = json.loads(data)

for item in ranks["Entries"]:
    if item["Name"] == "Fluffy":
        print("Rank: " + str(item["Rank"]) + "/" + str(len(ranks["Entries"])))
        break
