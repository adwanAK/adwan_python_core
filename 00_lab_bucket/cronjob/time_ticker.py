from crontab import CronTab
import datetime

with open ('dates.txt', 'a') as f:
	f.write(f'{datetime.datetime.now()}\n')