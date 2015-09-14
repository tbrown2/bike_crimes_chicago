import csv
import sys
import operator
import CSV_classes

def Parse_Bike_Crimes():

    f = open('CSV_Data\Bike_Crimes_-_2014.csv')
    g = open('CSV_Data\Bike_Racks.csv')
    h = open('CSV_Data\Census_Data_-_Selected_socioeconomic_indicators_in_Chicago__2008___2012.csv')
    csv_br = csv.reader(g)
    csv_bc = csv.reader(f)
    csv_cd = csv.reader(h)

    neighborhoods = []

    for row in csv_cd:
        temp = CSV_classes.Neighborhood(row[0], row[1], 0, 0)
        neighborhoods.append(temp)
        print(temp.CommunityArea)


    f.close()
    g.close()
    h.close()

    return neighborhoods

Parse_Bike_Crimes()