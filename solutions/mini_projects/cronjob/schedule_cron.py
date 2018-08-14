'''
Using `python-crontab`, create a CRON job that is basically a clock that
writes the date and time every minute to a file called `minutes.txt`.

Sample Output:

2018-08-14 10:09:00.572643
2018-08-14 10:10:00.572643

This exercise is focused on using crontab, therefore a script called
`time-ticker.py` is already provided. You need to correctly register a
CRON job programmatically from within this file, and make sure that the
output is what (and where!) you expect it.


HINTS:
We need to include the full path to our python3 executable, as well as
to the .py file: https://stackoverflow.com/a/44217854/5717580

If you are not getting what you expect, go to your terminal and
check your `mail` to find out what's going on with CRON.

'''

from crontab import CronTab

my_cron = CronTab(user='martin')  # enter your own username here
# TODO: these paths WON'T WORK FOR YOU!!! gotta replace them with your own :)
job = my_cron.new(command='/usr/local/bin/python3 /Users/martin/Documents/codingnomads/curriculum/python_core/week_04/mini_projects/cronjob/time_ticker.py')
job.minutes.every(1)
my_cron.write()

for job in my_cron:
	print(job)
