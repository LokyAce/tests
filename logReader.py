import sys, time, re
from datetime import datetime
from collections import Counter

LOG_FILE_NAME = 'd:/Work/Python/tests/logReader/access.log'
#TEST_LOG_STR = '103.131.71.47 - - [20/Nov/2024:00:13:54 +0000] "GET /robots.txt HTTP/1.1" 301 525 "-" "Mozilla/5.0 (compatible; coccocbot-image/1.0; +http://help.coccoc.com/searchengine)" '

def File2List(filename):
    with open(filename, 'r') as f:    
        return f.readlines()

def File2Str(filename):
    with open(filename, 'r') as f:
        return f.read()

print('Usage: 1-st param to specify a log file. \n')
fileLines = File2List(LOG_FILE_NAME)
#filestr = File2Str(LOG_FILE_NAME)
log_dict = {}
log_counts = Counter()

pattern = r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] (.*)' 
for logLine in fileLines:
    #print (logLine)
    match = re.match(pattern, logLine)    
    if match:
        ip, date_time, other = match.groups()
        #print (ip, '\n', date_time, '\n', other, '\n',)                #DEBUG
        #date_str = '20/Nov/2024:00:13:54 +0000'
        date_format = '%d/%b/%Y %H:%M:%S %z'
        datePattern = r'(\d{2}/[A-Za-z]{3}/\d{4}):(\d{2}:\d{2}:\d{2})'
        date_match = re.match(datePattern, date_time)
        if date_match:
            logRecDate, logRecTime = date_match.groups()
            #print (logRecDate, '\n', logRecTime, '\n')                  #DEBUG
            log_dict[logRecDate+'_'+logRecTime] = ip+other
            log_counts[logRecDate+'_'+logRecTime] += 1

#print('Dict: ', log_dict, '\n')
print ('Counter ', log_counts)