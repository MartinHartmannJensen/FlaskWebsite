from datetime import datetime, timedelta
import pytz

class UtcContainer:
    # UTC display
    utcOffset = 0
    utcCode = "code"
    currentTime = "time"
    # Dict containing the AdditionalZone class
    additionalZones = None
    def __init__(self, utc_offset):
        self.utcOffset = utc_offset
        time = datetime.now(pytz.timezone("UTC")) + timedelta(hours=utc_offset)
        self.currentTime = time.strftime("%H:%M")
        if utc_offset < 0:
            self.utcCode = "UTC" + str(utc_offset)
        else:
            self.utcCode = "UTC+" + str(utc_offset)

    def AddZoneDef(self, additionalZoneObj):
        additionalZoneObj.SetTime()
        if self.additionalZones is None:
            self.additionalZones = {additionalZoneObj.zoneId : additionalZoneObj}
            return
        self.additionalZones[additionalZoneObj.zoneId] = additionalZoneObj

class DistinctZone:
    zoneId = "zoneId"
    title = "zonetitle"
    fullTitle = "fullTitle"
    otherAbbreviations = []
    time = "time"

    def __init__(self, zoneId, title, fullTitle, otherAbbreviations):
        self.zoneId = zoneId
        self.title = title
        self.fullTitle = fullTitle
        self.otherAbbreviations = otherAbbreviations

    def SetTime(self):
        self.time = datetime.now(pytz.timezone(self.zoneId)).strftime("%H:%M")
        return self.time

    #"": DistinctZone("", "", "", [""]),
DefinedZones = {
    "MET": DistinctZone("MET", "CET", "Central European Time", ["MET", "CET", "CEST"]),
    "EET": DistinctZone("EET", "EET", "Eastern European Time", ["EET", "EEST"]),
    "WET": DistinctZone("WET", "WET", "Western European Time", ["WET", "WEST", "BST"]),
    "W-SU": DistinctZone("W-SU", "MSK", "Moscow Time", ["Moscow Time", "Minsk Time", "Further-eastern European Time", "Turkey Time"]),
    "America/Adak": DistinctZone("America/Adak", "HAT", "Hawaii-Aleutian Time", ["HAST", "HADT (Hawaii remains on UTC-10)"]),
    "US/Alaska": DistinctZone("US/Alaska", "AKT", "Alaska Time", ["AKST", "AKDT"]),
    "PST8PDT": DistinctZone("PST8PDT", "PT", "Pacific Time", ["PST", "PDT"]),
    "US/Mountain": DistinctZone("US/Mountain", "MT", "Mountain Time", ["MST", "MDT"]),
    "US/Central": DistinctZone("US/Central", "CT", "Central Time", ["CST", "CDT"]),
    "US/Eastern": DistinctZone("US/Eastern", "ET", "Eastern Time", ["EST", "EDT"]),
    "Canada/Atlantic": DistinctZone("Canada/Atlantic", "AT", "Atlantic Time", ["AST", "ADT"])
    }

def PrepareZoneContainers():
    timelist = []
    for i in range(-11, 12):
        timelist.append(UtcContainer(i))

    #timelist[0].AddZoneDef(DefinedZones[""]) #UTC-11
    timelist[1].AddZoneDef(DefinedZones["America/Adak"])
    timelist[2].AddZoneDef(DefinedZones["US/Alaska"]) #UTC-9
    timelist[3].AddZoneDef(DefinedZones["PST8PDT"])
    timelist[4].AddZoneDef(DefinedZones["US/Mountain"]) #UTC-7
    timelist[5].AddZoneDef(DefinedZones["US/Central"])
    timelist[6].AddZoneDef(DefinedZones["US/Eastern"]) #UTC-5
    timelist[7].AddZoneDef(DefinedZones["Canada/Atlantic"])
    #timelist[8].AddZoneDef(DefinedZones[""])
    #timelist[9].AddZoneDef(DefinedZones[""])
    #timelist[10].AddZoneDef(DefinedZones[""]) 
    timelist[11].AddZoneDef(DefinedZones["WET"]) #UTC
    timelist[12].AddZoneDef(DefinedZones["MET"])
    timelist[13].AddZoneDef(DefinedZones["EET"]) #UTC+2
    timelist[14].AddZoneDef(DefinedZones["W-SU"])
    #timelist[15].AddZoneDef(DefinedZones[""]) #UTC+4
    #timelist[16].AddZoneDef(DefinedZones[""])
    #timelist[17].AddZoneDef(DefinedZones[""]) #UTC+6
    #timelist[18].AddZoneDef(DefinedZones[""])
    #timelist[19].AddZoneDef(DefinedZones[""]) #UTC+8
    #timelist[20].AddZoneDef(DefinedZones[""])
    #timelist[21].AddZoneDef(DefinedZones[""]) #UTC+10
    #timelist[22].AddZoneDef(DefinedZones[""]) 

    return timelist