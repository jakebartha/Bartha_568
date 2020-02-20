import csv
# get year out of code block
# make list of all years in data set
#Create 3 lists that I will use for calculations
year_list, month_list, value_list = [], [], []
with open("CO2.csv") as co2:
    csv_reader = csv.reader(co2, delimiter=',')
    line_count = 0
    headerline = co2.next()
    print headerline
    for row in csv_reader:
        year, month, day = row[0].split("-")
        if year not in year_list:
            year_list.append(year)
        if month not in month_list:
            month_list.append(month) # builds a month list
print year_list
print month_list
value_list.append(float(row[1])) # this stores my values in a list, you must make this a float or math will fail
line_count = line_count + 1 # how many datapoints in total.

print "Minimum = " + str(min(value_list))
print "Maximum = " + str(max(value_list))
print "Average = " + str(float(sum(value_list) / int(line_count)))
print "Average 2 = " + str(sum(value_list) / len(value_list))

# Annual Averages
year_value_dict = {}

for year in year_list:
    temp_year_list = []
    with open("CO2.csv") as co2:
        csv_reader = csv.reader(co2, delimiter=',')
        headerline = co2.next()  # I use this to skip the header line

        for row in csv_reader:
            year_co2, month_co2, day = row[0].split("-")  # Here I split my date string into queryable chunks
            if year_co2 == year:
                temp_year_list.append(float(row[1]))  # this stores my values in a list, you must make this a float or math will fail

    year_value_dict[year] = str(sum(temp_year_list) / len(temp_year_list))

print year_value_dict

# Seasonal Averages
# Spring (March, April, May),
# Summer (June, July, August),
# Autumn (September, October, November)
# Winter (December, January, February)

spring_season_list = []
summer_season_list = []
autumn_season_list = []
winter_season_list = []
with open("CO2.csv") as co2:
    csv_reader = csv.reader(co2, delimiter=',')
    headerline = co2.next()  # I use this to skip the header line

    for row in csv_reader:
        year_co2, month_co2, day = row[0].split("-")  # Here I split my date string into queryable chunks
        if month_co2 == '03' or month_co2 == '04' or month_co2 == '05':
            spring_season_list.append(float(row[1]))  # this stores my values in a list, you must make this a float or math will fail
        if month_co2 == '06' or month_co2 == '07' or month_co2 == '08':
            summer_season_list.append(float(row[1]))
        if month_co2 == '09' or month_co2 == '10' or month_co2 == '11':
            autumn_season_list.append(float(row[1]))
        if month_co2 == '12' or month_co2 == '01' or month_co2 == '02':
            winter_season_list.append(float(row[1]))

print "Spring = " + str(sum(spring_season_list) / len(spring_season_list))
print "Summer = " + str(sum(summer_season_list) / len(summer_season_list))
print "Autumn = " + str(sum(autumn_season_list) / len(autumn_season_list))
print "Winter = " + str(sum(winter_season_list) / len(winter_season_list))

# Bonus present plot graph of annual averages
import matplotlib.pylab as plt
lists = sorted(year_value_dict.items()) # sorted by key, return a list of tuples
x, y = zip(*lists) # unpack a list of pairs into two tuples
plt.plot(x, y)
plt.show()