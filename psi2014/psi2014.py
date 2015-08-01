import pandas as pd
import time, datetime

df = pd.read_csv('20141027201710-PSI 2014.csv', header=0)

day_of_week = {0:"Sun", 1:"Mon", 2:"Tues", 3:"Wed", 4:"Thurs", 5:"Fri", 6:"Sat"}

time_of_day = {'night':range(0,5+1), 'morning':range(6,11+1), 
				'afternoon':range(12,18+1), 'evening':range(19,23+1)}

month_of_year = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 
				7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}


print "PSI 3hr,Datetime,DayOfWeek,Period,DayOfMonth,Month"

for idx, row in df.iterrows():
	psi, dts = row
	_psi_time, _, day_month_year = dts.strip().partition(' ')
	
	# Get time of day.
	psi_time =  datetime.datetime.strptime(_psi_time, '%I%p')
	psi_time_of_day = next(t for t in time_of_day 
							if psi_time.hour in time_of_day[t])
	
	# Get day of week.
	_date = time.strptime(day_month_year, "%d %b 20%y")  
	psi_date = datetime.datetime(_date.tm_year, _date.tm_mon, _date.tm_mday)
	psi_day = day_of_week[psi_date.weekday()]
	
	psi_month = month_of_year[psi_date.month]
	
	outrow = map(str, [psi,' '+ dts, psi_day, 
						psi_time_of_day, psi_date.day, psi_month])	
	print ",".join(outrow)
	
	
