__author__ = 'Tom'
class Neighborhood:
    def __init__(self, CommunityArea, CommunityAreaName, total_install, PerCapitaIncome, totalCrimes):
        self.CommunityArea = CommunityArea
        self.CommunityAreaName = CommunityAreaName
        self.total_install = total_install
        self.PerCapitaIncome = PerCapitaIncome
        self.totalCrimes = totalCrimes
    def set_total_install(self, new_total):
        self.total_install += new_total
    def set_total_crimes(self, totalcrime):
        self.totalCrimes += totalcrime