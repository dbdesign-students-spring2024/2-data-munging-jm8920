import csv

def average(decade_data):
    total = sum(float(row[month]) for row in decade_data for month in range(1, 13) if row[month] != "NaN")
    count = sum(1 for row in decade_data for month in range(1, 13) if row[month] != "NaN")
    average_anomaly = total / count if count else "NaN"
    return average_anomaly

def process_temperature_data(filename):
    with open('data/clean_data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  

        decade_start = 1880
        decade = []

        for row in reader:
            year = int(row[0])
            if year < decade_start + 10:
                decade.append(row)
            else:
                # Calculate average 
                avg_anomaly = average(decade)
                print(f"{decade_start} to {decade_start + 9}: {avg_anomaly:.2f}°F" if avg_anomaly != "NaN" else "NaN")

                # Prepare for the next decade
                decade_start += 10
                decade = [row]

# Call the function with the path to the CSV file
process_temperature_data('data/clean_data.csv')
