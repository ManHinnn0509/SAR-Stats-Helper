import calendar
import time
from datetime import datetime
from dateutil import tz

def convertTime(timeToConv, toZone='Asia/Taipei', returnString = False):
    """
        Converts UTC time to GMT+8 (Default) time.
    """
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz(toZone)

    # Splitted for debugging
    timeToConv = str(timeToConv)
    t = timeToConv.replace("T", " ")
    t = t.replace("Z", "")
    t = t.split(".")[0]

    utc = datetime.strptime(t, '%Y-%m-%d %H:%M:%S')

    utc = utc.replace(tzinfo=from_zone)
    central = utc.astimezone(to_zone)

    if (returnString):
        central = str(central)
    return central

def getDateTimeNow():
    """
        Format example: "2021-05-28 23:45:15"
    """
    now = str(datetime.now())
    now = now.split(".")[0]
    return now

def getTimestampNow():
    return calendar.timegm(time.gmtime())

def getTimestampDetailed():
    return datetime.datetime.now().timestamp()