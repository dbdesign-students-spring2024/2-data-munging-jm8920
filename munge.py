# Place code below to do the munging part of this assignment.
original_data_file = 'data/GLB.Ts+dSST.txt'
munged_data_file = 'data/clean_data.csv'
heading_string = 'Year   Jan  Feb  Mar  Apr  May  Jun  Jul  Aug  Sep  Oct  Nov  Dec    J-D D-N    DJF  MAM  JJA  SON  Year'

# Read the data file 
f = open('data/GLB.Ts+dSST.txt','r')
data = f.readlines()

# Convert temperature anomalies to Farenheit
def convert_temp(celsius):
    fahrenheit = celsius * 9/5
    formatted_fahrenheit = f"{fahrenheit:.1f}"
    return formatted_fahrenheit

# Remove comment lines that start with ‘#’
cleaned_lines = [line for line in data if not line.startswith("#")]

# Remove all blank lines
cleaned_lines_no_empty = [line for line in data if line.strip()]

# Handle the missing data
def missing_data(value):
    return value if value != "***" else "NaN"

# Remove all but the first line of column headings.
lines_with_header = [data[0]]
for line in data[1:]:
    if line != heading_string:
        lines_with_header.append(line)

# Remove all lines with notes

# Convert to CSV format, using commas as a separator
csv_lines = []
for line in data:
    parts = line.strip().split()
    csv_line = ",".join(parts) + "\n"
    csv_lines.append(csv_line)

# Write the CSV data to a new file
munged_data_file = "data/clean_data.csv"
with open(munged_data_file, "w") as csv_file:
    csv_file.writelines(csv_lines)

