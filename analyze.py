import csv

with open('data/clean_data.csv', 'r') as csvfile:
    data = csv.reader(csvfile)
    header = next(data) 

# Build a list to store the decade data
    decade = 1880
    decade_list = []

    for row in data:
        year = int(row[0])  
        if year < decade + 10:
            decade_list.append(row)
        else:
            total = 0
            count = 0

            for year_data in decade_list:
                for month in range(1, 13):
                    temp = year_data[month]
                    if temp != "NaN":
                        total += float(temp)
                        count += 1
            avg_anomaly = total / count if count != 0 else "NaN"
            
            # Output the average temperature
            print(f"{decade} to {decade + 9}: {avg_anomaly:.2f}°F")
            decade += 10
            decade_list = [row]