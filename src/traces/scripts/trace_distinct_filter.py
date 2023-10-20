# gievn a input file, output a file eliminating distinct items 
# run with python3 ./src/traces/scripts/trace_distinct_filter.py ./src/traces/Twitter_trace/cluster10.atf
import csv
import os
import sys

input_file_path = sys.argv[1]
with open(input_file_path, "r", encoding="utf-8") as source:
    reader1 = csv.reader(source)
    
    # Extract the parent directory from the input file path
    parent_directory = os.path.dirname(os.path.abspath(input_file_path))
    
    # Sets the output file name as .atf in the parent directory
    output_filename = os.path.splitext(os.path.basename(input_file_path))[0] + "_filtered.atf"
    output_file_path = os.path.join(parent_directory, output_filename)
    #first get a list of unqiue items 
    count_dict = {}
    unique_set = set()
    for r in reader1:
        if r[0] in unique_set:
            continue  # Skip items that have already been added
        if r[0] in count_dict:
            unique_set.discard(r[0])  # Remove item from set if it's no longer unique
        else:
            unique_set.add(r[0])
        count_dict[r[0]] = count_dict.get(r[0], 0) + 1
    print("unique_items_number:"+ str(len(unique_set)))
    with open(output_file_path, "w", newline="", encoding="utf-8") as result:
        writer = csv.writer(result)
        source.seek(0)
        reader2 = csv.reader(source)
        for r in reader2: 
            if r[0] in unique_set:
                writer.writerow(r) 