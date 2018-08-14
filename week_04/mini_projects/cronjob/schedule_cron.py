from crontab import CronTab

my_cron = CronTab(user='martin')  # enter your own username here
# we need to include the full path to our python3 executable, as well as py file
# https://stackoverflow.com/a/44217854/5717580
# TODO: these paths WON'T WORK FOR YOU!!! gotta replace them with your own :)
job = my_cron.new(command='/usr/local/bin/python3 /Users/martin/Documents/codingnomads/curriculum/python_core/week_04/mini_projects/cronjob/time_ticker.py')
job.minutes.every(1)
my_cron.write()

for job in my_cron:
	print(job)

# if you are not getting what you expect, go to your terminal and
# check your `mail` to find out what's going on with cron!
