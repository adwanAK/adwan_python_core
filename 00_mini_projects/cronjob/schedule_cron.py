#! usr/bin/python3

from crontab import CronTab

my_cron = CronTab(user='martin')

print('hei')
for job in my_cron:
	print(job)