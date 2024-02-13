# Place code below to do the munging part of this assignment.

with open('data/GLB.Ts+dSST.txt', 'r') as file:
    data = file.readlines()

cleaned_data = []
is_data_section = False

# Remove all the spaces
for line in data:
    line = line.strip()

# Remove all lines with notes
    if line.startswith("Year"):
        is_data_section = True
        header = line  
        continue
    if is_data_section and line:
        values = line.split()

# Handle the missing data
        if values[0].isdigit():
            for index, value in enumerate(values):
                if value in ('***', '****'):
                    values[index] = 'nan'
            
# Convert temperature to Fahrenheit
            for i in range(1, len(values) - 1):
                if values[i] != 'nan':
                    values[i] = "{:.1f}".format(float(values[i]) * 0.018)
            cleaned_data.append(values)

new_filename = "data/clean_data.csv"

# Write the data into the CSV file
with open(new_filename, "w") as csv_file:
    header_values = header.split()
    csv_file.write(",".join(header_values) + "\n")

    for row in cleaned_data:
        csv_file.write(",".join(row) + "\n")