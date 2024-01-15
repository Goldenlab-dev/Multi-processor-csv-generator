import itertools
import threading
import time
from datetime import datetime
import os
import json


class bruteforce:
    
    def __init__(self):
        self.now = datetime.now()
        self.formatted_date = self.now.strftime('%Y' + '-' + '%m' + '-' + '%d' + '-' + '%H' + '-' + '%M' + '-' + '%S')
        self.combination_length = self.json_reader('combination_length')
        self.tab = self.json_reader(key0='tab', key1='tab_full')
        self.path = self.json_reader('path')
        self.max_size = self.json_reader('max_size')*(1024e3)
        self.url = self.json_reader('url') + '_'
        self.file_extension = self.json_reader('file_extension')
        self.file = self.verification_directory()
        self.json = self.json_reader()
        self.possibilities = len(self.tab)**self.combination_length
        self.iteration_limit = self.possibilities/4
        
    def iteration_setter(self):
        for i in range(self.iteration_limit):
            i += 1
            batch_limit = i*self.iteration_limit
            x=0
            while x<batch_limit:
                x+=1
                self.dict_writer()
            
        


    def json_reader(self, key0='', key1='', file='option.json'):
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


    def verification_directory(self):
        if os.path.isdir(self.path) == True:
            file = self.file_maker()
            return file
        elif os.path.isdir(self.path) == False:
            os.mkdir(self.path)
            file = self.file_maker()
            return file
        else:
            print('Le chemin n\'est pas valide')
            exit()


    def file_maker(self):
        return open(self.path + self.url + self.formatted_date + self.file_extension, 'w')


    def dict_writer(self, range) :
        product = itertools.product(self.tab, repeat=self.combination_length)
        for valeurs in product:
                combination = ''.join(valeurs)
                self.file.write(combination + "\n")
        self.file.close()


bruteforce().iteration_setter()
