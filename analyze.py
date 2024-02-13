# Place code below to do the munging part of this assignment.

import csv

with open('data/clean_data.csv', 'r') as csvfile:
    data = csv.reader(csvfile)
    header = next(data) 

    decade_start = 1880
    decade_data = []

    for row in data:
        year = int(row[0])  
        if year < decade_start + 10:
            decade_data.append(row)
            
        else:
            total = 0
            count = 0
            for year_data in decade_data:
                for month in range(1, 13):
                    temp_anomaly = year_data[month]
                    if temp_anomaly != "NaN":
                        total += float(temp_anomaly)
                        count += 1
            avg_anomaly = total / count if count != 0 else "NaN"
            
            # Output
            print(f"{decade_start} to {decade_start + 9}: {avg_anomaly:.2f}°F")
            decade_start += 10
            decade_data = [row]