import sqlite3
import re
import requests
from math import pi
from itertools import chain
from collections import namedtuple
from bokeh.io import show, output_notebook
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, FuncTickFormatter, FixedTicker, ColumnDataSource
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict
from pandas import DataFrame
from collections import Counter
from operator import itemgetter



token = ''
header = headers = {'Authorization': f'Bearer {token}','Content-type': 'application/json'}


steam_hours = requests.get('https://query.data.world/s/5cOVc-nvDK4DkUJ2MFZuAqCcAqTJrN', 
                             headers=headers)
raw_data = steam_hours.text

steam_list = raw_data.split('\r\n')
print("Steam List")
print(steam_list)
steam_list[2]

game_hours = [r.split('|')[-1] for r in steam_list[1:]]
game_name = [r.split('|')[0] for r in steam_list[1:]]

print("game hours")
print(game_hours)

print("game name")
print(game_name)

game_hours_edit = [i.replace('"', '') for i in game_hours]

print("Game edited hours")
print(game_hours_edit)


def remove_comma(s):
    return s[1:]

def remove_comma_name(s):
    return s[:-1]

game_hours_edit = [remove_comma(s) for s in game_hours_edit]
game_hours = game_hours_edit

game_name_edit = [remove_comma_name(s) for s in game_name]
game_name = game_name_edit

games_dict = OrderedDict(zip(game_name, game_hours))
print(games_dict)

#key, value = ('asd', 1)

print('\n')
for key, value in games_dict.items():
    print('\n')
    print(key, value)
print('\n')

scrubbed = [re.sub(r'[^\x00-\x7F]+',' ', game_hours) for game_hours in game_hours]
#print(f"Game Name: {game_name}\n Hours Played: {scrubbed}")

conn = sqlite3.connect('steam_hours.db')
cur = conn.cursor() 
cur.execute('''drop table IF EXISTS name_game''')
cur.execute('''CREATE TABLE IF NOT EXISTS name_game (game_name TEXT, game_hours TEXT)''')

for key, value in games_dict.items():
    #print(game_name)
    #print(game_hours)
    cur.execute('INSERT OR REPLACE INTO name_game VALUES (?, ?)', (key, value,))
    conn.commit()

name_results = cur.execute('SELECT game_name FROM name_game LIMIT 10;').fetchall()
hours_results = cur.execute('SELECT game_hours FROM name_game LIMIT 10;').fetchall()

list_int = hours_results

names_flat = [item for sublist in name_results for item in sublist]
hours_flat = [item for sublist in hours_results for item in sublist]

list_int = np.array(hours_flat)
list_int = [item.replace(",", "") for item in list_int]
list_int = list(map(int, list_int))

print("LIST INT PRINTOUT")
print(list_int)

from collections import OrderedDict

final_dict = OrderedDict(zip(list_int, names_flat))

print("final dict")
print(final_dict)

print("FOR LOOP")
print('\n')
for key, value in final_dict.items():
    print('\n')
    print(key, value)
print('\n')



def make_autopct(values):
    def my_autopct(pct):
        total = sum(final_dict.keys())
        val = int(round(pct*total/100.0))
        return '{p:.01f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct
    
cols= ['r','y','g','b','c','#FB00FF','m','#FFA8A8','#9FFFA6', '#D7FFF7']
plt.pie(final_dict.keys(), labels=final_dict.values(), colors=cols, autopct=make_autopct(final_dict.keys),  pctdistance=.5, labeldistance=1)
plt.title('TOP 10 STEAM GAMES BY HOURS PLAYED ' '\n' 'Piechart displayed based on overall percentage' '\n' 'Rounded with Autopct to equal 100%' '\n' 'Data accurate as of 2/12/2018')
plt.xticks(rotation=15, fontsize=5)
plt.legend()
plt.show()
