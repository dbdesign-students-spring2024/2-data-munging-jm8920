# Place code below to do the munging part of this assignment.
with open('data/GLB.Ts+dSST.txt', 'r') as file:
    raw_data = file.readlines()

cleaned_data = []
collect_data = False

# Process each line of raw data
for line in raw_data:
    # Remove whitespace
    line = line.strip()

    # if a line starts with "Year," it's the header, so start collecting data
    if line.startswith("Year"):
        collect_data = True
        header = line  # store the header for later use
        continue

    # Append the line to cleaned_data
    if collect_data and line:
        values = line.split()
        # check if the first box contains numeric data
        if values[0].isdigit():
            
        # Handle missing data by replacing them with 'NaN'
            values = ['NaN' if v in ('***', '****') else v for v in values]
            # convert temperature anomalies to Fahrenheit (excl. the "Year" columns)
            for i in range(1, len(values) - 1):
                if values[i] != 'NaN':
                    values[i] = "{:.1f}".format(float(values[i]) * 1.8 / 100)
            cleaned_data.append(values)

csv_filename = "clean_data.csv"

# open CSV file for writing
with open(csv_filename, "w") as csv_file:
    # write the header row with separate cells
    header_values = header.split()
    csv_file.write(header_values[0] + ",")
    csv_file.write(",".join(header_values[1:-1]) + ",")
    csv_file.write(header_values[-1] + "\n")

    # write cleaned data rows with separate cells
    for row in cleaned_data:
        csv_file.write(row[0] + ",")
        csv_file.write(",".join(row[1:-1]) + ",")
        csv_file.write(row[-1] + "\n")