# Place code below to do the munging part of this assignment.

with open('data/GLB.Ts+dSST.txt', 'r') as file:
    data = file.readlines()

cleaned_data = []
collect_data = False

# Remove spaces
for line in data:
    line = line.strip()

# Test if a line starts with "Year" 
    if line.startswith("Year"):
        collect_data = True
        header = line  
        continue

# Append the line to cleaned_data
    if collect_data and line:
        values = line.split()

# Handle the missing data
        if values[0].isdigit():
            values = ['NaN' if v in ('***', '****') else v for v in values]

# Convert temperature to Fahrenheit
            for i in range(1, len(values) - 1):
                if values[i] != 'NaN':
                    values[i] = "{:.1f}".format(float(values[i]) * 0.018)
            cleaned_data.append(values)

new_filename = "data/clean_data.csv"

# Write the data into CSV file
with open(new_filename, "w") as csv_file:
    header_values = header.split()
    csv_file.write(header_values[0] + ",")
    csv_file.write(",".join(header_values[1:-1]) + ",")
    csv_file.write(header_values[-1] + "\n")

    for row in cleaned_data:
        csv_file.write(row[0] + ",")
        csv_file.write(",".join(row[1:-1]) + ",")
        csv_file.write(row[-1] + "\n")