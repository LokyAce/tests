import re
import argparse
from datetime import datetime
from datetime import date
from collections import Counter

#Parsing parameters, setting defaults
LOG_FILE_NAME = 'access.log'
GRANULARITY = 'min'
METHOD = 'RegExp'
log_dict = {}
log_counts = Counter()
data = []

parser = argparse.ArgumentParser(usage='%(prog)s logfile granularity method')
parser.add_argument('log_file', nargs='?', help='path to a file with logs', default=LOG_FILE_NAME)
parser.add_argument('granularity', nargs='?', help='Granularity of time to group log records. Valid values: sec, min or hour', default=GRANULARITY)
parser.add_argument('method', nargs='?', help='Method to use: RegExp or DateTimeObjects. Valid values: RegExp or DT ', default=METHOD)
args = parser.parse_args()
log_file_name = args.log_file
granularity = args.granularity
method = args.method

def file_to_list(filename):
    with open(filename, 'r') as f:    
        return f.readlines()

def file_to_str(filename):
    with open(filename, 'r') as f:
        return f.read()

def process_log_regexp (file_name, precision): #RegExp only method
    file_lines = file_to_list(file_name)
    #filestr = file_to_str(file_name)
    pattern = r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] (.*)' 
    for logLine in file_lines:
        #print (logLine)
        match = re.match(pattern, logLine)    
        if match:
            ip, date_time, other = match.groups()
            #print (ip, '\n', date_time, '\n', other, '\n',)                    #DEBUG   
            date_pattern = ''
            if precision == 'sec':
                date_pattern = r'(\d{2}/[A-Za-z]{3}/\d{4}):(\d{2}:\d{2}:\d{2})'
            if precision == 'min':
                date_pattern = r'(\d{2}/[A-Za-z]{3}/\d{4}):(\d{2}:\d{2})'
            if precision == 'hour':
                date_pattern = r'(\d{2}/[A-Za-z]{3}/\d{4}):(\d{2})'
            date_match = re.match(date_pattern, date_time)
            if date_match:
                log_rec_date, log_rec_time = date_match.groups()
                #print (log_rec_date, '\n', log_rec_time, '\n')                     #DEBUG
                log_dict[log_rec_date+'_'+log_rec_time] = ip+other
                log_counts[log_rec_date+'_'+log_rec_time] += 1

        #print('Dict: ', log_dict, '\n')                                        #DEBUG
        #print ('Counter ', log_counts)                                         $DEBUG

def process_log_dateobject (file_name, precision): #DateObject method
    granulated_dateobj = date.today()
    file_lines = file_to_list(file_name)
    #filestr = file_to_str(file_name)
    pattern = r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] (.*)' 
    for log_line in file_lines:
        #print (logLine)
        match = re.match(pattern, log_line)
        if match:
            ip, date_time, other = match.groups()
            #print (ip, '\n', date_time, '\n', other, '\n',)                    #DEBUG   
            date_format = '%d/%b/%Y:%H:%M:%S %z'
            #print ('date_time', date_time, '\n date_format ', date_format, )   #DEBUG
            date_obj = datetime.strptime(date_time, date_format)            
            if precision == 'sec':
                granulated_dateobj = date_obj
            if precision == 'min':
                granulated_dateobj = date_obj.replace(second=0)
            if precision == 'hour':
                granulated_dateobj = date_obj.replace(minute=0, second=0)
            #print('\n granulated_dateObj', granulated_dateObj, '\n')           #DEBUG
            log_dict[granulated_dateobj] = ip+other
            log_counts[granulated_dateobj] += 1

def main():
    #print('LogParser usage: \n    1-st param to specify a log file, \n    2-nd parameter: granularity. Valid values: sec/min/hour \n    3-rd parameter "RegExp" or "DT" to specify regexp method or DateTime objects. Default: regexp \n Example: logReader.py access.log min DT')

    if method == 'DT':
        print ('\n Using DateTimeObjects: \n')
        process_log_dateobject(log_file_name, granularity)
    if method == 'RegExp':
        print ('\n Using RegExp: \n')
        process_log_regexp(log_file_name, granularity)
    #print('Dict: ', log_dict, '\n')                                             #DEBUG
    print ('Counter ', log_counts)    

if __name__ == "__main__":
    main()