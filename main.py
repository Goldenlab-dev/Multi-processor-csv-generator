import itertools
import multiprocessing
import csv
import time
import os
import json

class bruteforce:
    def __init__(self):
        self.core_number = self.json_reader('core_number')
        self.dataset = self.json_reader('full_tabs', 'tab_full')
        self.length = self.json_reader("combination_length")
        self.total_combinations = len(self.dataset) ** self.length
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

    def combination_worker(self, task):
        (part_number, charset, length, start_index, end_index, filename, lock) = task
        with open(f"{filename}_part_{part_number}.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            for combo in itertools.islice(itertools.product(charset, repeat=length), start_index, end_index):
                writer.writerow([''.join(combo)])


    def concatenate_parts(filename, num_parts, lock):
        with open(filename, 'wb') as f_out:
            for i in range(num_parts):
                part_file = f"{filename}_part_{i}.csv"
                with lock:
                    with open(part_file, 'rb') as f_part:
                        f_out.write(f_part.read())
                os.remove(part_file)


    def asker(self):
        
        self.length = int(input("Enter the desired length of combinations: "))
        final_filename = input("Enter the final filename for the CSV (without .csv extension): ") + '.csv'
        print(f"Total combinations to generate: {self.total_combinations}")
        num_processes = int(input(f"How many processes do you want to use? (1-{multiprocessing.cpu_count()}): "))
        start_time = time.time()
        print('/!\\ ASKER DONE /!\\')
        
        manager = multiprocessing.Manager()
        
        lock = manager.Lock()
        tasks = [(i, self.dataset, self.length, i * self.partition_size,
                (i + 1) * self.partition_size if i < num_processes - 1 else self.total_combinations, final_filename, lock) for i in
                range(num_processes)]

        # Create worker processes for combination generation
        with multiprocessing.Pool(processes=num_processes) as pool:
            pool.map(self.combination_worker, tasks)

        # Concatenate all the parts into the final CSV
        self.concatenate_parts(final_filename, num_processes, lock)

        end_time = time.time()
        print(f"CSV generation complete in {end_time - start_time:.2f} seconds.")

        # Verify final file integrity
        print("Verifying final file integrity...")
        generated_combinations = 0
        with open(final_filename, 'r') as f:
            for row in csv.reader(f):
                if len(row[0]) != self.length:
                    print(f"Error: Incorrect combination length found - {row}")
                generated_combinations += 1

        print(f"Total combinations expected: {self.total_combinations}, found: {generated_combinations}")
        if generated_combinations == self.total_combinations:
            print("All combinations generated successfully.")
        else:
            print("There was an error with the generated combinations.")

bruteforce().asker()