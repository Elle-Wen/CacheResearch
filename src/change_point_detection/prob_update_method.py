# assume one instance of uniform distrubution at the beginning, then update probability based on occurance 
# call with python3 ./src/change_point_detection/prob_update_method.py ./src/traces/ProbTest.atf [prefix length]
import csv 
import sys
from itertools import product, islice
import os 

atf_file = sys.argv[1]
prefix_length = int(sys.argv[2])

#create a linked list to store probabilities 
class Node:
    def __init__(self,item,count):        
        self.item = item
        self.count = count
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None
    def append(self,item): # append, set count = 1
        new_node = Node(item,1)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def display(self):
        current = self.head
        while current:
            print(current.item + ": "+ str(current.count), end=" -> ")
            current = current.next
        print("None")
    def incre_count(self,target):
        current = self.head
        while current:
            if current.item == target:
                current.count = current.count + 1 
                return
            current = current.next
        self.append(target)
    def calculate_prob(self, target): #return the prob of the target 
        #first calculate total count 
        total_count = 0
        spec_count = 0 
        uniform = True  
        current = self.head
        while current:
            total_count = total_count + current.count 
            if current.item == target:
                uniform = False 
                spec_count = current.count 
            current = current.next 
        if uniform:
            return (1/total_count) * (1/number_of_unique_items)
        else: 
            return (1/total_count) * (1/number_of_unique_items) + (spec_count/total_count) 


#first calculate the number of distinct items  
with open(atf_file, "r", encoding="utf-8") as source:
    unique_items = set()
    total_items = 0
    reader = csv.reader(source)
    for r in reader:
        if len(r) > 0:
            total_items += 1 
            first_column_value = r[0]
            unique_items.add(first_column_value)
    number_of_unique_items = len(unique_items)

#initialize linked lists 
count_dict = {}
prefix_combinations_list = list(product(unique_items, repeat = prefix_length)) # all possible prefix, cartesion product

for prefix in prefix_combinations_list:
    name = '_'.join(prefix)
    count_dict[name] = LinkedList()
    count_dict[name].append("uniform") # am exmple name would be '100_101'

#write probabilities 
prob_file_directory = "/home/yuheng/cache-sim/src/change_point_detection"
prob_file = 'prob_file.csv'
prob_file_path = os.path.join(prob_file_directory, prob_file)
with open(atf_file, "r", encoding="utf-8") as source:
    with open(prob_file_path, "a", encoding="utf-8") as output:
        writer = csv.writer(output)
        writer_rec = csv.writer
        #first write "None" to the first few unpredictable items 
        for k in range(prefix_length):
            writer.writerow(["None"]) ### add the trace in 
        reader = csv.reader(source)
        #convert csv to a list of lists 
        new_lists = [row[0] for row in reader] #['100','101','102',...]
        for i in range(total_items-prefix_length): #the start of a window
            #first find prefix 
            current_prefix = ''
            for j in range(i, i+prefix_length+1): #finding the prefix
                if j == i+prefix_length-1: #the last one prefix, no "_"
                    current_prefix = current_prefix + new_lists[j]
                elif j == i+prefix_length: #the item to be predicted
                    next_item = new_lists[j]
                else:
                    current_prefix = current_prefix + new_lists[j] + '_'
            spec_linked_list = count_dict[current_prefix] #finding the linked list of the prefix
            writer.writerow([next_item]+[spec_linked_list.calculate_prob(next_item)]+[prefix_length])
            spec_linked_list.incre_count(next_item)