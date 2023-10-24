# convert cvs cambridge trace to atf 

import csv
import os
import sys
# call with python3 ./src/traces/scripts/cambridge_conversion.py ./src/traces/Camb_trace/sample

input_file_path = sys.argv[1]
with open(input_file_path, "r", encoding="utf-8") as source:
    
    reader = csv.reader(source)
    
    # Extract the parent directory from the input file path
    parent_directory = os.path.dirname(os.path.abspath(input_file_path))
    
    # Sets the output file name as .atf in the parent directory
    output_filename = os.path.splitext(os.path.basename(input_file_path))[0] + ".atf"
    output_file_path = os.path.join(parent_directory, output_filename)
    
    with open(output_file_path, "w", newline="", encoding="utf-8") as result:
        writer = csv.writer(result)
        for r in reader:
            item = r[4]
            time = r[0]
            IOType = r[3]
            size = r[5]
            writer.writerow((item,time,IOType,size,0))  # "#Address-anonymized key without name space", "Timestamp-timestamp", "IOType-operation", "Size-value size", "Cost"
