# Place code below to do the analysis part of the assignment.

import csv

def analyze():
    file = open("data/clean_data.csv", "r")

    averages = []

    csv_reader = csv.DictReader(file)
    for line in csv_reader:
        averages.append(float(line["J-D"]))

    # taking the average
    result = 0
    counter = 0
    lower = 1880
    upper = 1889

    for i in range(0, len(averages)):
        if i % 10 ==  9 and i != 0:
            result += averages[i]
            final_averages = result / 10
            print(lower, " to ", upper, ": ", round(final_averages, 2), sep="")
            
            result = 0
            counter += 1
            upper += 10
            lower += 10
        
        elif i + 1 == len(averages):
            result += averages[i]
            final_averages = result / (i % 10 + 1)
            print(lower, " to ", (lower + (i % 10)), ": ",round(final_averages, 2), sep="")
        
        else:
            result += averages[i] 

analyze()
