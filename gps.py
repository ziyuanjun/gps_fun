import serial as Ser
import time
from coordTransform_utils import *
ISOTIMEFORMAT = '%Y-%m-%d_%X'
ser = Ser.Serial('/dev/ttyUSB0', 4800, timeout=5)
date_time = time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
filename1 = 'static/data_csv_' + date_time + '.csv'
filename2 = 'gps_Data/data_raw_' + date_time + '.txt'
file_data = open(filename1, 'w')
file_data.write('loc\n')
file_raw = open(filename2, 'w')


def startGPS(filename1=filename1, filename2=filename2):
    while 1:
        line = str(ser.readline())
        splitline = line.split(',')

        if splitline[0] == 'b\'$GPGGA':
            file_raw.write(line)
            latitiude = splitline[2]
            latDirec = splitline[3]
            longitude = splitline[4]
            longDirec = splitline[5]
            print(latitiude + "," + longitude)

            # parse longitude and latitiude, transform to GaoDe map
            try:
                latdata = float(latitiude)
                longdata = float(longitude)
                long_deg = longdata // 100
                lat_deg = latdata // 100
                longall = long_deg + (longdata - long_deg * 100) / 60.0
                latall = lat_deg + (latdata - lat_deg * 100) / 60.0
                lng_lat_GaoDe = wgs84_to_gcj02(longall, latall)  # WGS84->GAODE
                data = str(lng_lat_GaoDe[0]) + "," + str(lng_lat_GaoDe[1])
                file_data.write("\"" + data + "\"\n")
                file_data.flush()
            except:
                continue

if __name__ == "__main__":
    startGPS()
