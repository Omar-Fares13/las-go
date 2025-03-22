import requests

API_KEY = "RGAPI-06f315ff-f2ad-4419-9f26-72cefe7ddab6"
SUMMONER_NAME = "kaztr"
TAGLINE = "2372"  # e.g., "EUW1"

url = f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{SUMMONER_NAME}/{TAGLINE}"

headers = {"X-Riot-Token": API_KEY}

response = requests.get(url, headers=headers)
print(response.json())  # This will return the player's PUUID


import requests

API_KEY = "YOUR_API_KEY"
PUUID = "abcdefgh-1234-5678-ijklmnop"

url = f"https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{PUUID}"
headers = {"X-Riot-Token": API_KEY}

response = requests.get(url, headers=headers)
print(response.json())  # Player's level, summoner ID, etc.
