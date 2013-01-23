#!/usr/bin/env python

import os
from datetime import datetime


LOG_PATH = '/data/log/nova'
LOG_CPU = 'nova-compute'
LOG_NET = 'nova-network'
THRESHOLD = 50 
LOG_FORMAT = '%(nr)s. leak: %(leak_time)s |report: %(report_time)s |last: %(last_time)s' 

print 'Threadhold: %s' % THRESHOLD
print 'Path: %s' % LOG_PATH
print '---'

logfiles = [f for f in os.listdir(LOG_PATH) 
            if f.find(LOG_CPU) != -1 or f.find(LOG_NET) != -1]

for log in logfiles:
    with open(os.path.join(LOG_PATH, log)) as log:
        print '--'
        print 'File: %s' % log.name

        last_time = datetime.now()

        for nr, line in enumerate(log.readlines()):
            nr = nr + 1
            if line.find('Report state.') != -1:
                report_time = datetime.strptime(line[:19], '%Y-%m-%d %H:%M:%S')
                leak_time = (report_time - last_time).total_seconds()
                if (last_time and leak_time > THRESHOLD):
                    print LOG_FORMAT % locals()
                last_time = report_time
