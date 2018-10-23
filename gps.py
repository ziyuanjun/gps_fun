import serial as Ser
import time
from coordTransform_utils import *
ISOTIMEFORMAT='%Y-%m-%d_%X'
ser=Ser.Serial('/dev/ttyUSB0',4800,timeout=5)
date_time=time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )
filename1='gps_data/data_csv_'+date_time+'.csv'
filename2='gps_data/data_raw_'+date_time+'.txt'
file_data=file(filename1,'w')
file_data.write('loc\n')
file_raw=file(filename2,'w')

while 1:
    line=ser.readline()
    splitline=line.split(',')

    if splitline[0]=='$GPGGA':
        file_raw.write(line)
        latitiude=splitline[2]
        latDirec=splitline[3]
        longitude=splitline[4]
        longDirec=splitline[5]
        #print line
        print latDirec+": "+latitiude+"  "+longDirec+": "+longitude
        #print


        #
        try:
            latdata=float(latitiude)
            longdata=float(longitude)
            long_deg=longdata//100
            lat_deg=latdata//100
            longall=long_deg+(longdata-long_deg*100)/60.0
            latall=lat_deg+(latdata-lat_deg*100)/60.0
            lng_lat_GaoDe=wgs84_to_gcj02(longall,latall)#WGS84->GAODE
            #print lng_lat_GaoDe
            data=str(lng_lat_GaoDe[0])+","+str(lng_lat_GaoDe[1])
            file_data.write("\""+data+"\"\n")
        except:
            continue
            

