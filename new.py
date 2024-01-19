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
        
    def asker(self):
        self.is_custom = bool(input("Do you want to enter custom parameters ?"))
        if not self.is_custom:
            pass          

            
            
            
            
            
            
            
            
            
            
            
            
            
    def test_values(self):
        print(self.dataset, self.length, self.total_combinations, self.core_number)
            
bruteforce().test_values()

            