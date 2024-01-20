import itertools
import multiprocessing
import csv
import time
import os
import json

class bruteforce:
    def __init__(self):
        self.is_custom = False
        self.final_filename = self.json_reader('final_filename')
        self.dataset = self.json_reader('full_tabs', 'tab_full')
        self.length = self.json_reader('combination_length')
        self.total_combinations = len(self.dataset) ** self.length
        self.core_number = self.json_reader('core_number')
        self.partition_size = self.total_combinations // self.core_number

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
            
    def custom_params_setter(self):
        self.dataset_lower = input("Include lowercase characters (a-z)? (y/n): ").lower() == 'y'
        self.dataset_upper = input("Include uppercase characters (A-Z)? (y/n): ").lower() == 'y'
        self.dataset_numbers = input("Include numbers (0-9)? (y/n): ").lower() == 'y'
        self.dataset_special = input("Include special characters? (y/n): ").lower() == 'y'
        dataset = self.create_custom_dataset(self.dataset_lower, self.dataset_upper, self.dataset_numbers, self.dataset_special)
        self.dataset_length = int(input("Enter the desired length of combinations: "))
        self.final_filename = input("Enter the final filename for the CSV (without .csv extension): ") + '.csv'
        self.total_combinations = len(dataset) ** self.dataset_length
        print(f"Total combinations to generate: {self.total_combinations}")
        self.core_number = int(input(f"How many CPU cores do you want to use? (1-{multiprocessing.cpu_count()}): "))

    def create_custom_dataset(self):
        dataset = ''
        if self.dataset_lower:
            dataset += 'abcdefghijklmnopqrstuvwxyz'
        if self.dataset_upper:
            dataset += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if self.dataset_numbers:
            dataset += '0123456789'
        if self.dataset_special:
            dataset += '!@#$%^&*()-_=+[]\{\}|;:",.<>?/`~'
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
                
    def multiprocessing_starter(self):
        
        start_time = time.time()
        
        manager = multiprocessing.Manager()
        lock = manager.Lock()
        tasks = [(i, self.dataset, self.length, i * self.partition_size,
                (i + 1) * self.partition_size if i < self.core_number - 1 else self.total_combinations, self.final_filename, lock) for i in
                range(self.core_number)]
        
        with multiprocessing.Pool(processes=self.core_number) as pool:
            pool.map(self.combination_worker(), tasks)
        
        self.concatenate_parts(self.final_filename, self.core_number, lock)
            
        end_time = time.time()
        print(f"CSV generation complete in {end_time - start_time:.2f} seconds.")
        
        print("Verifying final file integrity...")
        generated_combinations = 0
        with open(self.final_filename, 'r') as f:
            for row in csv.reader(f):
                if len(row[0]) != self.length:
                    print(f"Error: Incorrect combination length found - {row}")
                generated_combinations += 1
                
        print(f"Total combinations expected: {self.total_combinations}, found: {generated_combinations}")
        if generated_combinations == self.total_combinations:
            print("All combinations generated successfully.")
        else:
            print("There was an error with the generated combinations.")

        
    def is_custom_params(self):
        self.is_custom = bool(input("Do you want to enter custom parameters ? (y/n): ").lower()) == 'y'
        if self.is_custom:
            self.custom_params_setter()
        else: 
            self.combination_worker()
            
bruteforce().is_custom_params()
