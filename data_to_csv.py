# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 11:55:20 2023
@author: Pavel

"""
import pandas as pd
import os
def data_to_csv(path, new_fie_name, binary = True):  # path - путь к txt файлу,
                                                     # new_file_name - путь и название нового файла csv
                                                     # binary - небходимость изменения sentiment в бинарное состояние
    data = []
    paths = os.listdir(path)
    for filename in paths:
        if binary == True:
            mark = 1 if path[-3::]=='pos' else 0
        else:
            mark = filename[filename.find('_')+1:filename.find('.')+1]
        try:
            with open(path +'\\'+ filename, 'r') as file:
                text = file.read().replace('\n', '')
                data.append([text, mark])
        except: pass
    df = pd.DataFrame(columns=['Review', 'Sentiment'], data=data)
    df.to_csv(new_fie_name + '.csv', index= False)