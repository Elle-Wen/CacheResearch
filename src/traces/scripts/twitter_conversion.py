import csv
import os
import sys
# convert csv to atf for twitter trace
# call with python3 ./src/traces/scripts/twitter_conversion.py ./src/traces/Twitter_trace/cluster10

input_file_path = sys.argv[1]
with open(input_file_path, "r", encoding="utf-8") as source:
    string_to_integer_map = {} #a map that keeps string to int mapping 
    next_int = 0 
    reader = csv.reader(source)
    
    # Extract the parent directory from the input file path
    parent_directory = os.path.dirname(os.path.abspath(input_file_path))
    
    # Sets the output file name as .atf in the parent directory
    output_filename = os.path.splitext(os.path.basename(input_file_path))[0] + ".atf"
    output_file_path = os.path.join(parent_directory, output_filename)
    
    with open(output_file_path, "w", newline="", encoding="utf-8") as result:
        writer = csv.writer(result)
        for r in reader:
            string_value = r[1]
            #convert string to numerical for parsing 
            if string_value in string_to_integer_map:
                # If the string is already in the map, use the existing integer value
                numerical_value = string_to_integer_map[string_value]
            else:
                # If not, assign a new integer value and store the mapping in the map
                string_to_integer_map[string_value] = next_int
                numerical_value = next_int
                next_int += 1
            #convert operation to read or write 
            operation = r[5]
            if operation == "add" or "set" or "replace" or "cas" or "append" or "prepend" or "delete" or "inc" or "decr":
                operation = "Write"
            if operation == "get" or "gets":
                operation = "Read"
            writer.writerow((numerical_value, r[0], operation, r[3], 1))  # "#Address-anonymized key without name space", "Timestamp-timestamp", "IOType-operation", "Size-value size", "Cost"
