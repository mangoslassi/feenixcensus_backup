#!/usr/bin/python

# feenixcensus_backup.py
# Create backups of FeenixCensus day by day.
# This is intended to preserve as many
#   ED character names as possible.

import requests
from calendar import monthrange

baseurl = 'http://www.feenixcensus.com/?'

year = 2015
for month in range(1, 13):
    days = monthrange(year, month)[1]
    while days > 1:
        if days - 7 >= 1:
            begin_day = days - 7
            end_day = days
            days -= 7
        else:
            begin_day = 1
            end_day = days
            days = 1
        searchQuery = 'start_level=60&start_date=' + str(year) + '-' + str(month) + '-' + str(begin_day) + '&end_date=' + str(year) + '-' + str(month) + '-' + str(end_day) + '&search=Search'
        page = requests.get(baseurl + searchQuery)
        with open(searchQuery + '.html', 'w') as f:
            f.write(page.text)

