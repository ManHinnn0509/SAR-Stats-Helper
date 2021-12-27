# Don't change the order...
INFO_KEYS = ('遊戲名稱', '等級　　', '加入日期', 'STEAM64 ID', 'PLAYFAB   ID')
GAMEMODES = ('單人模式', '雙人模式', '團隊模式', 'S.A.W vs. 反抗軍', '神秘模式', "行雞走肉")

# DEFAULT_DATA_KEYS = ('勝場', '遊玩場數', '擊殺數', '死亡數', 'K/D', '勝率', 'Top', '最高擊殺數')
# HOWLOWEEN_DATA_KEYS = ('')

# Default template
LEADERBOARD_POSITIONS_TEMPLATE_FULL = {
   "Solo": {
      "Deaths": [0, 0],
      "Games": [0, 0],
      "Kills": [0, 0],
      "MeleeVictoriesSolo": [0, 0],
      "MostKills": [0, 0],
      "NoArmorVictoriesSolo": [0, 0],
      "PacifistVictoriesSolo": [0, 0],
      "Top5": [0, 0],
      "Wins": [0, 0]
   },
   "Duos": {
      "DeathsDuos": [0, 0],
      "GamesDuos": [0, 0],
      "KillsDuos": [0, 0],
      "MostKillsDuos": [0, 0],
      "Top3Duos": [0, 0],
      "WinsDuos": [0, 0]
   },
   "Squads": {
      "DeathsSquads": [0, 0],
      "GamesSquads": [0, 0],
      "KillsSquads": [0, 0],
      "MostKillsSquads": [0, 0],
      "Top2Squads": [0, 0],
      "WinsSquads": [0, 0]
   },
   "S.A.W. vs. Rebellion": {
      "DeathsCustom1": [0, 0],
      "FlagCaps": [0, 0],
      "GamesCustom1": [0, 0],
      "KillsCustom1": [0, 0],
      "MostKillsCustom1": [0, 0],
      "WinsCustom1": [0, 0]
   },
   "Mystery Mode": {
      "DeathsCustom2": [0, 0],
      "GamesCustom2": [0, 0],
      "KillsCustom2": [0, 0],
      "MostKillsCustom2": [0, 0],
      "Top2Custom2": [0, 0],
      "WinsCustom2": [0, 0]
   },
    "The Bwoking Dead": {
        'GamesCustom3': [0, 0],
        'KillsCustom3': [0, 0],
        'DeathsCustom3': [0, 0],
        'WinsCustom3': [0, 0],
        'MostKillsCustom3': [0, 0],
        'KillsCustom3Z': [0, 0],
        'DeathsCustom3Z': [0, 0],
        'MostKillsCustom3Z': [0, 0]
    },
   "Combat": {
      "BananaHits": [0, 0],
      "DamageDealt": [0, 0],
      "EnemyArmorBroken": [0, 0],
      "BananaHitsEnemyOnly": [0, 0],
      "Healing": [0, 0],
      "DestructiblesDestroyed": [0, 0],
      "SkunkBombDamageDealt": [0, 0]
   },
   "Kill Statistics": {
      "KillsAK": [0, 0],
      "KillsBow": [0, 0],
      "KillsCrossbow": [0, 0],
      "KillsDart": [0, 0],
      "KillsDeagle": [0, 0],
      "KillsDualPistol": [0, 0],
      "EmuKills": [0, 0],
      "GrenadeKills": [0, 0],
      "KillsHuntingRifle": [0, 0],
      "KillsJag7": [0, 0],
      "KillsM16": [0, 0],
      "KillsMagnum": [0, 0],
      "MeleeKills": [0, 0],
      "KillsMinigun": [0, 0],
      "KillsPistol": [0, 0],
      "KillsShotgun": [0, 0],
      "KillsSilencedPistol": [0, 0],
      "KillsSMG": [0, 0],
      "KillsSniper": [0, 0],
      "KillsThomas": [0, 0],
      "VehicleKills": [0, 0]
   },
   "Other": {
      "AccountLevelNew": [0, 0],
      "BananOfferings": [0, 0],
      "BeGalleryTarget": [0, 0],
      "BowHitsOneMatch": [0, 0],
      "CampfiresUsed": [0, 0],
      "ChestOpens": [0, 0],
      "CoconutsAte": [0, 0],
      "CrabDance": [0, 0],
      "DistanceTraveled": [0, 0],
      "DistanceTraveledIceW2": [0, 0],
      "AccountExpIntoCurrentLevelNew": [0, 0],
      "GalleryTargetsHit": [0, 0],
      "GalleryTargetsHitBow": [0, 0],
      "GrassCut": [0, 0],
      "HealthJuiceDrank": [0, 0],
      "MoleCrates": [0, 0],
      "MushroomsAte": [0, 0],
      "ParachuteSplats": [0, 0],
      "TimePlayedSeconds": [0, 0],
      "RatGG": [0, 0],
      "Scarecrows": [0, 0],
      "SuperJumpRolls": [0, 0],
      "TapeUsed": [0, 0],
      "ChickenWins": [0, 0],
      "TurkeyWins": [0, 0]
   },
   "Event": {
      "CandyCorn": [0, 0],
      "EggsAte": [0, 0],
      "FruitBaskets": [0, 0],
      "Presents": [0, 0]
   },
   "Milestones": {
      "StorytimeDonk": [0, 0],
      "DancingInTheRain": [0, 0],
      "NPCLab": [0, 0],
      "BarnRebelDoor": [0, 0],
      "NoDancing": [0, 0],
      "NpcSphynx": [0, 0]
   },
   "Super CRISPRmas 2019": {
      "UseCampfiresW1": [0, 0],
      "KillsHamsterWeek3": [0, 0],
      "HealthJuiceDrankWeek3": [0, 0],
      "KillsAsDeerWeek2": [0, 0],
      "KillsExplosionGrenadeWeek2": [0, 0],
      "MeleeKillsWeek2": [0, 0],
      "OpenMoleCratesW1": [0, 0],
      "KillsThomasGun": [0, 0]
   },
   "Legacy": {
      "AccountLevel": [0, 0],
      "AccountExpIntoCurrentLevel": [0, 0]
   }
}