# Place code below to do the munging part of this assignment.

import csv

with open('data/clean_data.csv', 'r') as csvfile:
    data = csv.reader(csvfile)
    header = next(data) 

# Build a list to store the decade data
    decade_start = 1880
    decade_list = []

    for row in data:
        year = int(row[0])  
        if year < decade_start + 10:
            decade_list.append(row)
        else:
            total = 0
            count = 0

            for year_data in decade_list:
                for month in range(1, 13):
                    temperature = year_data[month]
                    if temperature != "NaN":
                        total += float(temperature)
                        count += 1
            avg_anomaly = total / count if count != 0 else "NaN"
            
            # Output the average temperature
            decade_start += 10
            decade_list = [row]
            print(f"{decade_start} to {decade_start + 9}: {avg_anomaly:.2f}°F")
