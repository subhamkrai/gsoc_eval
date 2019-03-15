import glob, os   #for getting file name
import pytz       
from datetime import datetime

a=[]

#getting file name and keeping the h5 file in same folder
for pdf_file in glob.glob(os.path.join( '*.h5')):
    a=pdf_file
    

#getting 18 digit number
a=a[:18]
print("18 digit number which is the UNIX time in nanoseconnds:",a)
a=int(a)
secs = a / 1e9

#converting in utc time format
dt = datetime.utcfromtimestamp(secs)
s=dt.strftime('%Y-%m-%d %H:%M:%S.%f')
print("DateTime in UTC            ",s)


#converting cern localtime zone
dt=s
utc_time = datetime.strptime(dt,"%Y-%m-%d %H:%M:%S.%f")
cern_localtz = pytz.timezone('Etc/GMT-1')

cern_time=pytz.utc.localize(utc_time, is_dst=None).astimezone(cern_localtz)
print("DateTime in CERN local time",cern_time)
