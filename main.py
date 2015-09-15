import csv
import sys
import operator
import CSV_classes

def Parse_Bike_Crimes():
    #opening and assigning each CSV file to their own variable
    f = open('CSV_Data\Bike_Crimes_-_2014.csv')
    g = open('CSV_Data\Bike_Racks.csv')
    h = open('CSV_Data\Census_Data_-_Selected_socioeconomic_indicators_in_Chicago__2008___2012.csv')
    csv_br = csv.reader(g)
    csv_bc = csv.reader(f)
    csv_cd = csv.reader(h)

    #will hold each neighborhood and their subsequent attributes for data comparison
    neighborhoods = []
    #need a variable to act as a switch
    i = 0
    #looping through the first csv file to acquire the community area number, name, and the per capita income
    for row in csv_cd:
        if i>0:
            temp = CSV_classes.Neighborhood(row[0], row[1], 0, row[4], 0)
            neighborhoods.append(temp)
        else:
            i=1

    #looping through the bike rack file to count the number of available installed bike racks per neighborhood
    for row in csv_br:
        if i==0:
            neighborhoods[int(row[1])-1].set_total_install(int(row[3]))
        i = 0

    #looping through the bike crimes to count how many occurences of bike theft occurred
    for row in csv_bc:
        if i>0:
            neighborhoods[int(row[3])-1].set_total_crimes(1)
        else:
            i = 1

    #closing all the files
    f.close()
    g.close()
    h.close()

    return neighborhoods

def print_crime_average(neighborhoods):
    sum = 0
    n = len(neighborhoods)-1
    highest = 0
    highest_n = ""
    for x in range(0, len(neighborhoods)-1):
        print (str(neighborhoods[x].CommunityAreaName) + ": " + str(neighborhoods[x].totalCrimes) + "\n\tPer Capita Income of: " + str(neighborhoods[x].PerCapitaIncome))
        sum += neighborhoods[x].totalCrimes
        if neighborhoods[x].totalCrimes>highest:
            highest = neighborhoods[x].totalCrimes
            highest_n = neighborhoods[x].CommunityAreaName


    average = float(sum) / float(n)
    print ("Average Bike Theft Per Neighborhood: " + str(average))
    print ("Community with the highest theft: " + highest_n + " with " + str(highest) + " in 2014.")

def bike_racks_per(neighborhoods):
    sum = 0
    n = len(neighborhoods)-1
    highest = 0
    highest_n = ""
    for x in range(0, len(neighborhoods)-1):
        print (str(neighborhoods[x].CommunityAreaName) + ": " + str(neighborhoods[x].total_install) + "\n\tPer Capita Income of: " + str(neighborhoods[x].PerCapitaIncome))
        sum += neighborhoods[x].total_install
        if neighborhoods[x].total_install>highest:
            highest = neighborhoods[x].total_install
            highest_n = neighborhoods[x].CommunityAreaName


    average = float(sum) / float(n)
    print ("Average Bike Racks Per Neighborhood: " + str(average))
    print ("Community with the highest number of bike racks: " + highest_n + " with " + str(highest) + " .")

def Main():
    print ("This is a program that explores some information about bike theft")
    neighborhoods = Parse_Bike_Crimes()

    print("Crimes against Per Capita Income per Neighborhood\n----------------------------------------------------\n")
    print_crime_average(neighborhoods)
    print ("\nBike Racks against Per Capita Income per Neighborhood\n-------------------------------------------------------\n")
    bike_racks_per(neighborhoods)
    print ("\nThat concludes this program.")

Main()


