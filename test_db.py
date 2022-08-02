import mysql

#print(sys.version)


import datetime

date_time_str = '29-06-2018'
date_time_obj = datetime.datetime.strptime(date_time_str, '%d-%m-%Y')

print('Date:', date_time_obj.date())
print('Time:', date_time_obj.time())
print('Date-time:', date_time_obj)