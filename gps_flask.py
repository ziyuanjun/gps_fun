import serial as Ser
import time
import sys
from coordTransform_utils import *
import logging
logging.basicConfig(level=logging.DEBUG)


def startGPS(file_data, file_raw):
    ser = Ser.Serial('/dev/ttyUSB0', 4800, timeout=5)
    while 1:
        line = str(ser.readline())
        logging.info(line)
        splitline = line.split(',')

        if splitline[0] == '$GPGGA':
            file_raw.write(line)
            latitiude = splitline[2]
            latDirec = splitline[3]
            longitude = splitline[4]
            longDirec = splitline[5]
            # print(latitiude + "," + longitude, file=sys.stdout)
            logging.info(latitiude + "," + longitude)

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
    ISOTIMEFORMAT = '%Y-%m-%d_%X'
    date_time = time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
    filename1 = 'static/data_csv_' + date_time + '.csv'
    filename2 = 'gps_Data/data_raw_' + date_time + '.txt'
    file_data = open(filename1, 'w')
    file_data.write('loc\n')
    file_raw = open(filename2, 'w')

    startGPS(file_data, file_raw)
