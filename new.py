import itertools
import multiprocessing
import csv
import time
import os
import json

class bruteforce:
    def __init__(self):
        self.is_custom = False
        self.dataset = self.json_reader('full_tabs', 'tab_full')
        self.length = self.json_reader("combination_length")
        self.total_combinations = len(self.dataset) ** self.length
        self.core_number = self.json_reader("core_number")
        self.part_number = self.json_reader("")

    def json_reader(self, key0='', key1='', file='params.json'):
        if len(key1) == 0 or key1 is None or key1 == '':
            with open(file, 'r') as file:
                json_content=json.load(file).get(key0)
                file.close()
                return json_content
        elif len(key1) != 0 or key1 is not None or key1 != '':
            with open(file,'r') as file :
                json_content=json.load(file).get(key0).get(key1)
                return json_content
        else: 
            print('Erreur lors de la lecture du fichier json')
            exit()
        
    def custom_params(self):
        self.is_custom = bool(input("Do you want to enter custom parameters ?"))
        if self.is_custom:
            self.custom_params_setter()
            
    def custom_params_setter(self):
        lower = input("Include lowercase characters (a-z)? (y/n): ").lower() == 'y'
        upper = input("Include uppercase characters (A-Z)? (y/n): ").lower() == 'y'
        numbers = input("Include numbers (0-9)? (y/n): ").lower() == 'y'
        special = input("Include special characters? (y/n): ").lower() == 'y'
        dataset = create_dataset(lower, upper, numbers, special)
        length = int(input("Enter the desired length of combinations: "))
        final_filename = input("Enter the final filename for the CSV (without .csv extension): ") + '.csv'
        total_combinations = len(dataset) ** length
        print(f"Total combinations to generate: {total_combinations}")
        num_processes = int(input(f"How many processes do you want to use? (1-{multiprocessing.cpu_count()}): "))

        
        
    def custom_dataset(lower, upper, numbers, special):
        dataset = ''
        if lower:
            dataset += 'abcdefghijklmnopqrstuvwxyz'
        if upper:
            dataset += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if numbers:
            dataset += '0123456789'
        if special:
            dataset += '!@#$%^&*()-_=+[]{}|;:",.<>?/`~'
        return dataset
    
    def combination_worker(task):
        (part_number, dataset, length, start_index, end_index, filename, lock) = task
        with open(f"{filename}_part_{part_number}.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            for combo in itertools.islice(itertools.product(dataset, repeat=length), start_index, end_index):
                writer.writerow([''.join(combo)])

    def concatenate_parts(filename, num_parts, lock):
        with open(filename, 'wb') as f_out:
            for i in range(num_parts):
                part_file = f"{filename}_part_{i}.csv"
                with lock:
                    with open(part_file, 'rb') as f_part:
                        f_out.write(f_part.read())
                os.remove(part_file)
            
            
            
            
            
            
            
            
            
            
            
            
            
    def test_values(self):
        print(self.dataset, self.length, self.total_combinations, self.core_number)
            
bruteforce().test_values()

            