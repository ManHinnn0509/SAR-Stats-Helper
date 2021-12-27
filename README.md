# SAR-Stats-Helper <a href='#'><img src='./img/icon/dr_beagle_head.ico' align="right" height="138.5" /></a>

Player stats checker, rank monitor for Super Animal Royale

## Running this program

If you want to run them individually, you can do `python stats_checker.py` or `python rank_monitor.py`

Or, if you want a main window what spawns multuple stats checker / rank monitor. You can do `python menu_window.py` or just start the `run.bat` file

## Requirements

See [requirements.txt](requirements.txt)

## PlayFab session ticket

This project uses endpoint [LoginWithPlayFab](https://docs.microsoft.com/en-us/rest/api/playfab/client/authentication/login-with-playfab?view=playfab-rest) to generate session ticket

In this case, PlayFab **Username** and **Password** is required (Stored in `.env` file)

You can check out the function in [here](https://github.com/ManHinnn0509/SAR-Stats-Helper/blob/main/sar/__init__.py#L11) for more details

## .env file

.env file is being used in this project for storing secrets

Template:

```
# Steam
STEAM_API_KEY=YOUR_STEAM_WEB_API_KEY_HERE

# PlayFab
PLAYFAB_AC=YOUR_PLAYFAB_USERNAME_HERE
PLAYFAB_PW=YOUR_PLAYFAB_PASSWORD_HERE
```

## Demo (images)

* [Menu window](#menu-window)
* [Stats Checker](#stats-checker)
* [Rank Monitor](#rank-monitor)

### Menu window

* Multiple Stats Checker / Rank Monitor supported

![menu_window](./img/demo/menu_window.png)

### Stats Checker

![stats_checker](./img/demo/stats_checker.png)
![stats_checker_result](./img/demo/stats_checker_result.png)

### Rank Monitor

* What to show is totally customizable (The more to show, the longer it takes to refresh)
* Refresh time is customizable (Should not be shorter than 30s)

![rank_monitor](img/demo/rank_monitor.png)
![rank_monitor_result](img/demo/rank_monitor_result.png)