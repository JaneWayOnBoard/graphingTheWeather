from requests import get
import matplotlib.pyplot as plt
from dateutil import parser

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/2828199'

weather = get(url).json()

data = weather['items']


pages = 1

while 'next' in weather and pages < 9:
    url = weather['next']['$ref']
    print('Fetching {0}'.format(url))
    weather = get(url).json()
    data += weather['items']
    pages += 1
    
temperatures = [record['ambient_temp'] for record in data]
timestamps = [parser.parse(record['reading_timestamp']) for record in data]
print(temperatures)

plt.plot(timestamps, temperatures)
plt.ylabel('Temperature')
plt.xlabel('date and time')
plt.show()

