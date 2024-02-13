import csv

# open/ read  CSV file
with open('clean_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # skip header row

    # group data by decade
    current_decade = 1880
    decade_data = []
    for row in csvreader:
        year = int(row[0])  # The year is the first column in the CSV
        if year < current_decade + 10:
            decade_data.append(row)
        else:
            # get the avg of the temperature anomalies for the decade
            total = 0
            count = 0
            for year_data in decade_data:
                # loop through monthly temperature anomalies
                for month_index in range(1, 13):
                    temp_anomaly = year_data[month_index]
                    if temp_anomaly != "NaN":
                        total += float(temp_anomaly)
                        count += 1
            avg_anomaly = total / count if count != 0 else "NaN"
            
            # output avg for the decade
            print(f"Average temperature anomaly for {current_decade} to {current_decade + 9}: {avg_anomaly:.2f}°F")
            
            # and the next decade
            current_decade += 10
            decade_data = [row]