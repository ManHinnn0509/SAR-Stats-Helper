import requests as req

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class SAR_Player:

    # E.g: Lv 10 -> Lv 11 Requires 1800 EXP
    EXP_NEEDED_TO_LEVEL_UP = {
        "0": 0,
        "1": 200,
        "2": 300,
        "3": 400,
        "4": 500,
        "5": 600,
        "6": 700,
        "7": 800,
        "8": 900,
        "9": 1000,
        "10": 1800,
        "11": 2000,
        "12": 2200,
        "13": 2400,
        "14": 2600,
        "15": 2800,
        "16": 3000,
        "17": 3200,
        "18": 3400,
        "19": 3600,
        "20": 3800,
        "21": 4000
    }

    def __init__(self, sessionTicket, playFabID):
        self.sessionTicket = sessionTicket
        self.playFabID = playFabID

        self.reqData = self.__getPlayerData()
        if (self.reqData == None):
            raise req.RequestException
        
        self.playerData = self.reqData["data"]
        self.accountInfo = self.reqData["data"]["InfoResultPayload"]["AccountInfo"]
        self.statData = self.reqData["data"]["InfoResultPayload"]["PlayerStatistics"]

        # Player statistics in key-value pair
        self.statDict = {}
        for s in self.statData:
            self.statDict[s["StatisticName"]] = s["Value"]
        
        # UTC Time
        self.accountCreateDateTime = str(self.accountInfo["Created"])
        self.accountCreateDate = self.accountCreateDateTime.split(" ")[0]

        self.currentLevel = 1 + int(self.statDict["AccountLevelNew"])
        self.currentEXP = int(self.statDict["AccountExpIntoCurrentLevelNew"])
        self.expNeededToLevelUp = self.EXP_NEEDED_TO_LEVEL_UP.get(str(self.currentLevel), 4200)

        self.nextLevel = 1 + self.currentLevel
        self.expToNextLevel = self.expNeededToLevelUp - self.currentEXP

    def success(self):
        return self.reqData != None

    def getSoloStat(self):
        keys = ["Wins", "Kills", "Deaths", "Games", "Top5", "Games", "MostKills"]
        return self.__formatStats(keys)
    
    def getDuosStat(self):
        keys = ["WinsDuos", "KillsDuos", "DeathsDuos", "GamesDuos", "Top3Duos", "GamesDuos", "MostKillsDuos"]
        return self.__formatStats(keys)
    
    def getSquadsStat(self):
        keys = ["WinsSquads", "KillsSquads", "DeathsSquads", "GamesSquads", "Top2Squads", "GamesSquads", "MostKillsSquads"]
        return self.__formatStats(keys)
        
    def getSAW_RebellionStat(self):
        keys = ["WinsCustom1", "KillsCustom1", "DeathsCustom1", "GamesCustom1", "N/A", "GamesCustom1", "MostKillsCustom1"]
        return self.__formatStats(keys)
    
    def getMysteryModeStat(self):
        keys = ["WinsCustom2", "KillsCustom2", "DeathsCustom2", "GamesCustom2", "Top2Custom2", "GamesCustom2", "MostKillsCustom2"]
        return self.__formatStats(keys)

    def getTotalKills(self):
        keys = [
            "Kills",
            "KillsDuos",
            "KillsSquads",
            "KillsCustom1",
            "KillsCustom2"
        ]

        return self.__calcTotalSum(keys)
    
    def getTotalDeaths(self):
        keys = [
            "Deaths",
            "DeathsDuos",
            "DeathsSquads",
            "DeathsCustom1",
            "DeathsCustom2"
        ]

    def __calcTotalSum(self, dataKeys: list) -> int:
        """
            Calculate total sum of a list of given keys
        """
        d = self.statDict
        count = 0
        for k in dataKeys:
            count += d.get(k, 0)
        
        return count

    def __formatStats(self, keys: list):
        """
            Calculate and format player stats with given keys
        """
        d = self.statDict
        perfectKD = "∞"

        wins = d.get(keys[0], "N/A")
        kills = d.get(keys[1], "N/A")
        deaths = d.get(keys[2], "N/A")      # Or 0 instead of N/A?

        # Calculate KD if possible
        try:
            kd = "%.2f" % (kills / deaths)
        except:
            kd = "N/A"

        # Calculate win rate
        try:
            winRate = "%.2f" % ((wins / d[keys[3]] * 100))
            winRate = str(winRate) + " %"
        except:
            winRate = "N/A"
        
        # Calculate top %
        try:
            top = "%.2f" % ((d[keys[4]] / d[keys[3]]) * 100)
            top = str(top) + " %"
        except:
            top = "N/A"
        
        gamesPlayed = d.get(keys[5], "N/A")
        mostKills = d.get(keys[6], "N/A")

        # These are the result calculated
        values = [wins, gamesPlayed, kills, deaths, kd, winRate, top, mostKills]
        
        # Merge the keys & values into dict()
        statNames = ['Wins', "Games played", "Kills", "Deaths", "K/D", "Win rate", "Top", "Most kills"]
        return dict(zip(statNames, values))

    def __getPlayerData(self):
        """
            Gets a player's info via GetPlayerCombinedInfo() \n
            See https://d36d.playfabapi.com/Client/GetPlayerCombinedInfo
        """

        url = "https://d36d.playfabapi.com/Client/GetPlayerCombinedInfo"

        h = {
            "X-Authorization": self.sessionTicket
        }

        b = {
            "InfoRequestParameters": {
                "GetPlayerProfile": True,
                "GetUserAccountInfo": True,
                "GetPlayerStatistics": True,
                "GetUserData": True
            },
            "PlayFabId": self.playFabID
        }

        r = req.post(url=url, headers=h, json=b, verify=False)

        if (r.status_code != 200):
            return None
        
        try:
            return r.json()
        except:
            return None