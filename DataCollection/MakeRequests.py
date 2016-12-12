"""This generates urls to download climate data from the specified lat/lon coordinate and curls the
data at the address."""

import os
import sys

arguments = sys.argv[1:]

if arguments[0] == '-h' or arguments[0] == '--h' or arguments[0] == '--help':
    print "MakeRequests.py takes two arguments:"
    print "(1) Latitude coordinate"
    print "(2) Longitude coordinate"
    sys.exit()

if len(arguments) != 2:
    print "Incorrect number of arguments"
    print "python MakeRequests.py -h for more information"
    sys.exit()

lat = arguments[0]
lon = arguments[1]

def check(type,csv, request,status):
    trys = status
    with open(csv,'r') as inputFile:
        first_line = inputFile.readline()
    if trys > 4:
        print 'Download failed too many times'
    if first_line != '#Variables:\n' and trys < 4:
        print first_line
        print 'DOWNLOAD FAILED. Re-executing download'
        os.system(request)
        trys += 1
        check(type,csv,request,trys)
    if first_line == '#Variables:\n':
        os.system("python DataProcessing.py RAW_"+type +"_" + lat + "_" + lon + ".csv "+type+"_" + lat + "_" + lon + ".csv")

#Get Future Data
dataTypes = ["rcp45","rcp85"]
for dataType in dataTypes:
    baseRequest ="curl -o RAW_" + dataType + "_" + lat +"_" +lon+ ".csv 'http://climate-dev.nkn.uidaho.edu/Services/get-netcdf-data/?download-csv=True&" \
                 "request_lat_lon=False&lat=" + lat + "&lon=" + lon + "&positive-east-longitude=True&data-path=http://thredds." \
                 "northwestknowledge.net:8080/thredds/dodsC/agg_macav2metdata_tasmin_GFDL-ESM2M_r1i1p1_"+dataType +"_2006_2099_CONUS" \
                 "_daily.nc&variable=air_temperature&variable-name=tasmin_GFDL-ESM2M_"+dataType+"&data-path=http://thredds." \
                 "northwestknowledge.net:8080/thredds/dodsC/agg_macav2metdata_tasmax_GFDL-ESM2M_r1i1p1_"+dataType + "_2006_2099_" \
                 "CONUS_daily.nc&variable=air_temperature&variable-name=tasmax_GFDL-ESM2M_" + dataType + "&data-path=http://thredds." \
                 "northwestknowledge.net:8080/thredds/dodsC/agg_macav2metdata_rhsmin_GFDL-ESM2M_r1i1p1_"+ dataType + "_2006_2099_CONUS" \
                 "_daily.nc&variable=relative_humidity&variable-name=rhsmin_GFDL-ESM2M_" + dataType +"&data-path=http://thredds." \
                 "northwestknowledge.net:8080/thredds/dodsC/agg_macav2metdata_rhsmax_GFDL-ESM2M_r1i1p1_" + dataType + "_2006_2099_CONUS" \
                 "_daily.nc&variable=relative_humidity&variable-name=rhsmax_GFDL-ESM2M_" + dataType + "&data-path=http://thredds" \
                 ".northwestknowledge.net:8080/thredds/dodsC/agg_macav2metdata_pr_GFDL-ESM2M_r1i1p1_" + dataType +"_2006_2099_CONUS" \
                 "_daily.nc&variable=precipitation&variable-name=pr_GFDL-ESM2M_" + dataType + "'"
    os.system(baseRequest)
    check(dataType,('RAW_'+dataType+'_'+lat+'_'+lon+'.csv'),baseRequest,1)

#Get Historical Data
Request ="curl -o RAW_historical_" + lat +"_" +lon+ ".csv 'http://climate-dev.nkn.uidaho.edu/Services/get-netcdf-data/?download-csv=True&" \
         "request_lat_lon=False&lat=" + lat + "&lon=" + lon + "&positive-east-longitude=True&data-path=http://thredds." \
         "northwestknowledge.net:8080/thredds/dodsC/agg_macav2metdata_tasmin_GFDL-ESM2M_r1i1p1_historical_1950_2005_CONUS" \
         "_daily.nc&variable=air_temperature&variable-name=tasmin_GFDL-ESM2M_historical&data-path=http://thredds." \
         "northwestknowledge.net:8080/thredds/dodsC/agg_macav2metdata_tasmax_GFDL-ESM2M_r1i1p1_historical_1950_2005_" \
         "CONUS_daily.nc&variable=air_temperature&variable-name=tasmax_GFDL-ESM2M_historical&data-path=http://thredds." \
         "northwestknowledge.net:8080/thredds/dodsC/agg_macav2metdata_rhsmin_GFDL-ESM2M_r1i1p1_historical_1950_2005_CONUS" \
         "_daily.nc&variable=relative_humidity&variable-name=rhsmin_GFDL-ESM2M_historical&data-path=http://thredds." \
         "northwestknowledge.net:8080/thredds/dodsC/agg_macav2metdata_rhsmax_GFDL-ESM2M_r1i1p1_historical_1950_2005_CONUS" \
         "_daily.nc&variable=relative_humidity&variable-name=rhsmax_GFDL-ESM2M_historical&data-path=http://thredds" \
         ".northwestknowledge.net:8080/thredds/dodsC/agg_macav2metdata_pr_GFDL-ESM2M_r1i1p1_historical_1950_2005_CONUS" \
         "_daily.nc&variable=precipitation&variable-name=pr_GFDL-ESM2M_historical'"
os.system(Request)
check('historical','RAW_historical_'+lat+'_'+lon+'.csv',Request,1)
