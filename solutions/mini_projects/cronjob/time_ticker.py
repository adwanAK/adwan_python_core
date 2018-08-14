import os
from crontab import CronTab
import datetime

# getting the absolute path of the current file
abs_path = os.path.dirname(__file__)

# defining the absolute path for our new file object
with open (f'{abs_path}/dates.txt', 'a') as f:
	f.write(f'{datetime.datetime.now()}\n')
