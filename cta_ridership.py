import requests
import json
from datetime import datetime

r = requests.get(
    "https://data.cityofchicago.org/resource/dv3z-wsyd.json?route=49"
)
ridership_list = r.json()

for i in ridership_list[1:]:
    i['date'] = datetime.strptime(str(i['date'][:10]), '%Y-%m-%d').date()

def rides_moving_avg(ridership_data,num_days):
    key_name = str(num_days) + 'd_moving_average'
    for i in ridership_data:
        position = ridership_data.index(i)
        if position < (num_days-1):
            ridership_data[position].update({key_name:0})
        else:
            rides_list = [int(i['rides']) for i in ridership_data[position-(num_days-1):position+1]]
            moving_avg = sum(rides_list)/len(rides_list)
            ridership_data[position].update({key_name:moving_avg})

rides_moving_avg(ridership_list,3)
