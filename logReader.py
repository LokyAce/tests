import sys, time, re, argparse
from datetime import datetime
from collections import Counter

#Parsing paramters, setting defaults
LOG_FILE_NAME = 'access.log'
GRANULARITY = 'min'
METHOD = 'RegExp'
log_dict = {}
log_counts = Counter()

parser = argparse.ArgumentParser(usage='%(prog)s logfile granularity method')
parser.add_argument('log_file', nargs='?', help='path to a file with logs', default=LOG_FILE_NAME)
parser.add_argument('granularity', nargs='?', help='Granularity of time to group log records. Valid values: sec, min or hour', default=GRANULARITY)
parser.add_argument('method', nargs='?', help='Method to use: RegExp or DateTimeObjects. Valid values: RegExp or DT ', default=METHOD)
args = parser.parse_args()
log_file_name = args.log_file
granularity = args.granularity
method = args.method

def File_to_List(filename):
    with open(filename, 'r') as f:    
        return f.readlines()

def File_to_Str(filename):
    with open(filename, 'r') as f:
        return f.read()

def ProcessLogRegExp (file_name, precision): #RegExp only method
    fileLines = File_to_List(file_name)
    #filestr = File_to_Str(file_name)
    pattern = r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] (.*)' 
    for logLine in fileLines:
        #print (logLine)
        match = re.match(pattern, logLine)    
        if match:
            ip, date_time, other = match.groups()
            #print (ip, '\n', date_time, '\n', other, '\n',)                    #DEBUG   
            if precision == 'sec':
                datePattern = r'(\d{2}/[A-Za-z]{3}/\d{4}):(\d{2}:\d{2}:\d{2})'
            if precision == 'min':
                datePattern = r'(\d{2}/[A-Za-z]{3}/\d{4}):(\d{2}:\d{2})'
            if precision == 'hour':
                datePattern = r'(\d{2}/[A-Za-z]{3}/\d{4}):(\d{2})'
            date_match = re.match(datePattern, date_time)
            if date_match:
                logRecDate, logRecTime = date_match.groups()
                #print (logRecDate, '\n', logRecTime, '\n')                     #DEBUG
                log_dict[logRecDate+'_'+logRecTime] = ip+other
                log_counts[logRecDate+'_'+logRecTime] += 1

        #print('Dict: ', log_dict, '\n')                                        #DEBUG
        #print ('Counter ', log_counts)                                         $DEBUG

def ProcessLogDateObject (file_name, precision): #DateObject method
    fileLines = File_to_List(file_name)
    #filestr = File_to_Str(file_name)
    pattern = r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] (.*)' 
    for logLine in fileLines:
        #print (logLine)
        match = re.match(pattern, logLine)    
        if match:
            ip, date_time, other = match.groups()
            #print (ip, '\n', date_time, '\n', other, '\n',)                    #DEBUG   
            date_format = '%d/%b/%Y:%H:%M:%S %z'
            #print ('date_time', date_time, '\n date_format ', date_format, )   #DEBUG
            date_obj = datetime.strptime(date_time, date_format)            
            if precision == 'sec':
                granulated_dateObj = date_obj
            if precision == 'min':
                granulated_dateObj = date_obj.replace(second=0)
            if precision == 'hour':
                granulated_dateObj = date_obj.replace(minute=0, second=0)
            #print('\n granulated_dateObj', granulated_dateObj, '\n')           #DEBUG
            log_dict[granulated_dateObj] = ip+other
            log_counts[granulated_dateObj] += 1

def main():
    #print('LogParser usage: \n    1-st param to specify a log file, \n    2-nd parameter: granularity. Valid values: sec/min/hour \n    3-rd parameter "RegExp" or "DT" to specify regexp method or DateTime objects. Default: regexp \n Example: logReader.py access.log min DT')

    if method == 'DT':
        print ('\n Using DateTimeObjects: \n')
        ProcessLogDateObject(log_file_name, granularity)
    else:
        print ('\n Using RegExp: \n')
        ProcessLogRegExp(log_file_name, granularity)
    #print('Dict: ', log_dict, '\n')                                             #DEBUG
    print ('Counter ', log_counts)    

if __name__ == "__main__":
    main()