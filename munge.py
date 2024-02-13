# Import necessary library for CSV writing
import csv

def read_file_lines(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def filter_and_transform_data(data_lines):

    processed_lines = []
    start_processing = False
    for line in data_lines:
        line = line.strip()
        if line.startswith("Year"):
            start_processing = True
            header_line = line
            continue
        if start_processing and line:
            values = line.split()
            values = ['NaN' if v == '***' or v == '****' else v for v in values]
            values = [f"{float(v) * 0.018 :.1f}" if v.isdigit() else v for v in values]
            processed_lines.append(values)
    return header_line, processed_lines

def write_to_csv_file(header, cleaned_data, output_file_path):
    """Writes the cleaned data into a CSV file with the given header."""
    with open(output_file_path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header.split())
        writer.writerows(cleaned_data)

# Original code logic with function calls
data = read_file_lines('data/GLB.Ts+dSST.txt')
header, cleaned_data = filter_and_transform_data(data)
new_filename = "data/clean_data.csv"
write_to_csv_file(header, cleaned_data, new_filename)
