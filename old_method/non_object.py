import itertools
from datetime import datetime
import os
import json        

now = datetime.now()
formatted_date = now.strftime('%Y' + '-' + '%m' + '-' + '%d' + '-' + '%H' + '-' + '%M' + '-' + '%S')


def json_reader(key0, key1 = '', file = 'option.json'):
    if len(key1) == 0 or key1 is None or key1 == '':
        with open('option.json','r') as file:
            json_content=json.load(file).get(key0)
            return json_content
    else:
        with open('option.json','r') as file :
            json_content=json.load(file).get(key0).get(key1)
            return json_content


pathTour = json_reader('path', 'pathTour')
pathPortable = json_reader('path', 'pathPortable')
pathNorah = json_reader('path', 'pathNorah')
path = pathTour
combination_length = json_reader(key0='combination_length')
tab_livebox = json_reader(key0='tab', key1='tab_livebox')
tab_2 = json_reader('tab', 'tab_2')
tab = tab_livebox
max_size = json_reader('max_size')*(1024e3)
url = json_reader('url') + '_'
file_extension = json_reader('file_extension')


def file_maker(path, url, formatted_date, file_extension):
    file = open(path + url + formatted_date + file_extension, 'w')
    return file


def file_verification_existence(path):
    if path == pathPortable and os.path.isdir(pathPortable) == True:
        file = file_maker(path, url, formatted_date, file_extension)
        return file
    elif path == pathPortable and os.path.isdir(pathPortable) == False:
        os.mkdir(path)
        file = file_maker(path, url, formatted_date, file_extension)
        return file
    elif path == pathTour and os.path.isdir(pathTour) == True:
        file = file_maker(path, url, formatted_date, file_extension)
        return file
    elif path == pathTour and os.path.isdir(pathTour) == False:
        os.mkdir(path)
        file = file_maker(path, url, formatted_date, file_extension)
        return file
    elif path == pathNorah and os.path.isdir(pathNorah) == True:
        file = file_maker(path, url, formatted_date, file_extension)
        return file
    elif path == pathNorah and os.path.isdir(pathNorah) == False:
        os.mkdir(path)
        file = file_maker(path, url, formatted_date, file_extension)
        return file


def dict_writer(tab):
    file = file_verification_existence(path)
    product = itertools.product(tab, repeat=combination_length)
    
    for valeurs in product:
        combination = ''.join(valeurs)
        file.write(combination + "\n")
    file.close()


dict_writer(tab)
