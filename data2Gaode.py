from coordTransform_utils import *

filedata=file('gps_Data/data5.csv','r')
filedata1=file('gps_Data/data5-1.csv','w')
filedata1.write("loc\n")

for line in filedata.readlines()[1:]:
    strs=line.split(',')
    lon=float(strs[0][1:])
    lat=float(strs[1][:-2])
    print lon,lat
    lonlatGaoDe=wgs84_to_gcj02(lon,lat)
    filedata1.write("\""+str(lonlatGaoDe[0])+","+str(lonlatGaoDe[1])+"\"\n")



filedata1.close()
filedata.close()
