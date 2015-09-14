__author__ = 'Tom'
class Bike_Crimes:
    def __init__(self, ID, Date, Arrest, CommunityArea, Location):
        self.ID = ID
        self.Date = Date
        self.Arrest = Arrest
        self.CommunityArea = CommunityArea
        self.Location = Location

class Bike_Racks:
    def __init__(self, RackID, CommunityArea, totinstall, Location):
        self.RackID = RackID
        self.CommunityArea = CommunityArea
        self.totinstall = totinstall
        self.location = Location

class Census_Data:
    def __init__(self, CommunityArea, CommunityAreaName, PerCapitaIncome, HardshipIndex):
        self.CommunityArea = CommunityArea
        self.CommunityAreaName = CommunityAreaName
        self.PerCapitaIncome = PerCapitaIncome
        self.HardshipIndex = HardshipIndex
