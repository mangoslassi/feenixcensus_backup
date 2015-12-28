#!/usr/bin/python

# feenixcensus_backup.py
# Create backups of FeenixCensus day by day.
# This is intended to preserve as many
#   ED character names as possible.

import requests
from calendar import monthrange

url = 'http://www.feenixcensus.com/?start_level=20&start_date=2015-09-01&end_date=2015-12-27&search=Search'
page = requests.get(url)
with open('20plus_last_three_months', 'w') as f:
    f.write(page.text)

