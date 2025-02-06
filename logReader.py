# use data object instead regexp
# use param to determine min-hour-days
import sys, time, re
from datetime import datetime
from collections import Counter

#Parsing paramters
LOG_FILE_NAME = 'access.log'
if sys.argv[1]:
    log_file_name = sys.argv[1]
else:
    log_file_name = LOG_FILE_NAME
if sys.argv[2]:
    granularity = sys.argv[2]
else:
    granularity = 'sec'
log_dict = {}
log_counts = Counter()



def File_to_List(filename):
    with open(filename, 'r') as f:    
        return f.readlines()

def File_to_Str(filename):
    with open(filename, 'r') as f:
        return f.read()

print('LogParser usage: \n  1-st param to specify a log file, \n  2-nd parameter: granularity. Valid values: sec/min/hour \n Example: logReader.py access.log sec')

fileLines = File_to_List(log_file_name)
#filestr = File2Str(log_file_name)

pattern = r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] (.*)' 
for logLine in fileLines:
    #print (logLine)
    match = re.match(pattern, logLine)    
    if match:
        ip, date_time, other = match.groups()
        #print (ip, '\n', date_time, '\n', other, '\n',)                #DEBUG   
        date_format = '%d/%b/%Y %H:%M:%S %z'
        datePattern = r'(\d{2}/[A-Za-z]{3}/\d{4}):(\d{2}:\d{2}:\d{2})'
        date_match = re.match(datePattern, date_time)
        if date_match:
            logRecDate, logRecTime = date_match.groups()
            #print (logRecDate, '\n', logRecTime, '\n')                  #DEBUG
            log_dict[logRecDate+'_'+logRecTime] = ip+other
            log_counts[logRecDate+'_'+logRecTime] += 1

#print('Dict: ', log_dict, '\n')                                         #DEBUG
print ('Counter ', log_counts)