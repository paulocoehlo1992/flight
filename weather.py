import requests
from dateutil.rrule import *
from dateutil.parser import *

# Variables
daySt = "20160101" # state date
dayEnd = "20161231" # end date
outPath = '/Users/vishal hp/Documents/WeatherData' # output path
station = 'VIDD' # weather station ID
api = 'a413b1af50168c24' # developer API key

# Create list of dates between start and end
days = list(rrule(DAILY, dtstart=parse(daySt), until=parse(dayEnd)))

# Create daily url, fetch json file, write to disk
for day in days:
	r = requests.get('http://api.wunderground.com/api/' + api + '/history_' + day.strftime("%Y%m%d") + '/q/' + station + '.json')
	with open(outPath + station + '_' + day.strftime("%Y%m%d") + '.json', 'w') as outfile:
		outfile.write(r.content)
