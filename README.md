# Bike Theft in Chicago
For this project, I am to take data provided by the city of Chicago and produce some valuable information 

I am an avid biker, who recently had his bike seat stolen from him. I am going to look at cases of bike theft in the city of Chicago, and compare it to neighborhood data (socioeconomic information)

I will be looking at three specific questions:

1. Is there a relationship between the quantity of bike racks and bike theft per neighborhood? Are thieves likely to target areas with a greater quantity of bike racks (assumes that bike racks correlates with how many people are using bikes in neighborhood).
2. Is there a relationship between the income per capita and bike theft per neighborhood? Are wealthy neighborhoods or poorer neighborhoods affected by more theft?
3. Is there a relationship between income per capita and bike racks per neighborhood? Are wealthier neighborhoods more likely to have bike racks?

#### Method
All data is from the [Chicago Data Portal](https://data.cityofchicago.org/).
* [Census Data - Selected socioeconomic indicators in Chicago, 2008](https://data.cityofchicago.org/Health-Human-Services/Census-Data-Selected-socioeconomic-indicators-in-C/kn9c-c2s2)
* [Bike Racks in Chicago (2014)](https://data.cityofchicago.org/Transportation/Bike-Racks/cbyb-69xx)
* [Bike Related Crimes in Chicago (2014)](https://data.cityofchicago.org/Public-Safety/Crimes-2014/qnmj-8ku6)

I first started this project with the intent of of graphing the line of best fit for each correlation, and then determining the correlation coefficient. However, my inability to install numpy into Python, and the time constraints didn't allow me to do so, as such, I have decided to print out my results of totalling, and print averages. 

#### Results
I was ablt to find that the average bike racks per neighborhood is 113, and the Loop has the highest number of bike racks as well as an extremely high Per Capita Income of 65526. Bike theft occurs on average, 3 times per neighborhood, with West Town having the highest of 25 thefts. The Loop had 6, which is higher than average. West Town has 564 bike racks, and a high per Capita Income of 43198. The results are preliminary but the extreme example seem to show a correlation. Further study is needed to reach a conclusion. 