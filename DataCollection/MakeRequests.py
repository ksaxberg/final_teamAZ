"""This generates urls to download climate data from the specified lat/lon coordinate and curls the
data at the address."""

import os
import sys

arguments = sys.argv[1:]

if arguments[0] == '-h' or arguments[0] == '--h' or arguments[0] == '--help':
    print "MakeRequests.py arguments:"
    print "(1) Latitude coordinate"
    print "(2) Longitude coordinate"
    print "(3) Model (default = GFDL-ESM2M)"
    sys.exit()

if len(arguments) != 2:
    if len(arguments) == 3:
        model = arguments[2]
    else:
        print "Incorrect number of arguments"
        print "python MakeRequests.py -h for more information"
        sys.exit()
if len(arguments) == 2:
    lat = arguments[0]
    lon = arguments[1]
    model = "GFDL-ESM2M"

#Checks to make sure what was downloaded was the climate CSV
def check(type,csv, request,status=1):
    trys = status
    with open(csv,'r') as inputFile:
        first_line = inputFile.readline()
    if trys > 4:
        print 'Download failed too many times'
        return None
    elif first_line != '#Variables:\r\n' and trys < 4:
        print 'DOWNLOAD FAILED. Re-executing download'
        os.system(request)
        trys += 1
        check(type,csv,request,trys)
    else:
        os.system("python DataProcessing.py RAW_"+type +"_" + lat + "_" + lon + ".csv "+type+"_" + lat + "_" + lon + ".csv")



#Get Future Data
dataTypes = ["rcp45","rcp85"]
for dataType in dataTypes:
    baseRequest ="curl -o RAW_" + dataType + "_" + lat +"_" +lon+ ".csv 'http://climate-dev.nkn.uidaho.edu/Services/get-netcdf-data/?download-csv=True&" \
                 "request_lat_lon=False&lat=" + lat + "&lon=" + lon + "&positive-east-longitude=True&data-path=http://thredds." \
                 "northwestknowledge.net:8080/thredds/dodsC/agg_macav2metdata_tasmin_"+model+"_r1i1p1_"+dataType +"_2006_2099_CONUS" \
                 "_daily.nc&variable=air_temperature&variable-name=tasmin_"+model+"_"+dataType+"&data-path=http://thredds." \
                 "northwestknowledge.net:8080/thredds/dodsC/agg_macav2metdata_tasmax_"+model+"_r1i1p1_"+dataType + "_2006_2099_" \
                 "CONUS_daily.nc&variable=air_temperature&variable-name=tasmax_"+model+"_" + dataType + "&data-path=http://thredds." \
                 "northwestknowledge.net:8080/thredds/dodsC/agg_macav2metdata_rhsmin_"+model+"_r1i1p1_"+ dataType + "_2006_2099_CONUS" \
                 "_daily.nc&variable=relative_humidity&variable-name=rhsmin_"+model+"_" + dataType +"&data-path=http://thredds." \
                 "northwestknowledge.net:8080/thredds/dodsC/agg_macav2metdata_rhsmax_"+model+"_r1i1p1_" + dataType + "_2006_2099_CONUS" \
                 "_daily.nc&variable=relative_humidity&variable-name=rhsmax_"+model+"_" + dataType + "&data-path=http://thredds" \
                 ".northwestknowledge.net:8080/thredds/dodsC/agg_macav2metdata_pr_"+model+"_r1i1p1_" + dataType +"_2006_2099_CONUS" \
                 "_daily.nc&variable=precipitation&variable-name=pr_"+model+"_" + dataType + "'"
    os.system(baseRequest)
    check(dataType,('RAW_'+dataType+'_'+lat+'_'+lon+'.csv'),baseRequest)

#Get Historical Data
Request ="curl -o RAW_historical_" + lat +"_" +lon+ ".csv 'http://climate-dev.nkn.uidaho.edu/Services/get-netcdf-data/?download-csv=True&" \
         "request_lat_lon=False&lat=" + lat + "&lon=" + lon + "&positive-east-longitude=True&data-path=http://thredds." \
         "northwestknowledge.net:8080/thredds/dodsC/agg_macav2metdata_tasmin_"+model+"_r1i1p1_historical_1950_2005_CONUS" \
         "_daily.nc&variable=air_temperature&variable-name=tasmin_"+model+"_historical&data-path=http://thredds." \
         "northwestknowledge.net:8080/thredds/dodsC/agg_macav2metdata_tasmax_"+model+"_r1i1p1_historical_1950_2005_" \
         "CONUS_daily.nc&variable=air_temperature&variable-name=tasmax_"+model+"_historical&data-path=http://thredds." \
         "northwestknowledge.net:8080/thredds/dodsC/agg_macav2metdata_rhsmin_"+model+"_r1i1p1_historical_1950_2005_CONUS" \
         "_daily.nc&variable=relative_humidity&variable-name=rhsmin_"+model+"_historical&data-path=http://thredds." \
         "northwestknowledge.net:8080/thredds/dodsC/agg_macav2metdata_rhsmax_"+model+"_r1i1p1_historical_1950_2005_CONUS" \
         "_daily.nc&variable=relative_humidity&variable-name=rhsmax_"+model+"_historical&data-path=http://thredds" \
         ".northwestknowledge.net:8080/thredds/dodsC/agg_macav2metdata_pr_"+model+"_r1i1p1_historical_1950_2005_CONUS" \
         "_daily.nc&variable=precipitation&variable-name=pr_"+model+"_historical'"
os.system(Request)
check('historical','RAW_historical_'+lat+'_'+lon+'.csv',Request)