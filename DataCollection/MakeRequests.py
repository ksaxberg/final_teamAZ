import os

# dataType = 'historical' #historical, rcp45, or rcp85
# lat = "32"
# lon = "-110"
#
# if dataType == 'rcp45' or 'rcp85':
#     baseRequest ="curl -o RAW_" + dataType + "_" + lat +"_" +lon+ ".csv 'http://climate-dev.nkn.uidaho.edu/Services/get-netcdf-data/?download-csv=True&" \
#                  "request_lat_lon=False&lat=" + lat + "&lon=" + lon + "&positive-east-longitude=True&data-path=http://thredds." \
#                  "northwestknowledge.net:8080/thredds/dodsC/agg_macav2metdata_tasmin_GFDL-ESM2M_r1i1p1_"+dataType +"_2006_2099_CONUS" \
#                  "_daily.nc&variable=air_temperature&variable-name=tasmin_GFDL-ESM2M_"+dataType+"&data-path=http://thredds." \
#                  "northwestknowledge.net:8080/thredds/dodsC/agg_macav2metdata_tasmax_GFDL-ESM2M_r1i1p1_"+dataType + "_2006_2099_" \
#                  "CONUS_daily.nc&variable=air_temperature&variable-name=tasmax_GFDL-ESM2M_" + dataType + "&data-path=http://thredds." \
#                  "northwestknowledge.net:8080/thredds/dodsC/agg_macav2metdata_rhsmin_GFDL-ESM2M_r1i1p1_"+ dataType + "_2006_2099_CONUS" \
#                  "_daily.nc&variable=relative_humidity&variable-name=rhsmin_GFDL-ESM2M_" + dataType +"&data-path=http://thredds." \
#                  "northwestknowledge.net:8080/thredds/dodsC/agg_macav2metdata_rhsmax_GFDL-ESM2M_r1i1p1_" + dataType + "_2006_2099_CONUS" \
#                  "_daily.nc&variable=relative_humidity&variable-name=rhsmax_GFDL-ESM2M_" + dataType + "&data-path=http://thredds" \
#                  ".northwestknowledge.net:8080/thredds/dodsC/agg_macav2metdata_pr_GFDL-ESM2M_r1i1p1_" + dataType +"_2006_2099_CONUS" \
#                  "_daily.nc&variable=precipitation&variable-name=pr_GFDL-ESM2M_" + dataType + "'"
#
# if dataType == 'historical':
#     baseRequest ="curl -o RAW_historical_" + lat +"_" +lon+ ".csv 'http://climate-dev.nkn.uidaho.edu/Services/get-netcdf-data/?download-csv=True&" \
#                  "request_lat_lon=False&lat=" + lat + "&lon=" + lon + "&positive-east-longitude=True&data-path=http://thredds." \
#                  "northwestknowledge.net:8080/thredds/dodsC/agg_macav2metdata_tasmin_GFDL-ESM2M_r1i1p1_historical_1950_2005_CONUS" \
#                  "_daily.nc&variable=air_temperature&variable-name=tasmin_GFDL-ESM2M_historical&data-path=http://thredds." \
#                  "northwestknowledge.net:8080/thredds/dodsC/agg_macav2metdata_tasmax_GFDL-ESM2M_r1i1p1_historical_1950_2005_" \
#                  "CONUS_daily.nc&variable=air_temperature&variable-name=tasmax_GFDL-ESM2M_historical&data-path=http://thredds." \
#                  "northwestknowledge.net:8080/thredds/dodsC/agg_macav2metdata_rhsmin_GFDL-ESM2M_r1i1p1_historical_1950_2005_CONUS" \
#                  "_daily.nc&variable=relative_humidity&variable-name=rhsmin_GFDL-ESM2M_historical&data-path=http://thredds." \
#                  "northwestknowledge.net:8080/thredds/dodsC/agg_macav2metdata_rhsmax_GFDL-ESM2M_r1i1p1_historical_1950_2005_CONUS" \
#                  "_daily.nc&variable=relative_humidity&variable-name=rhsmax_GFDL-ESM2M_historical&data-path=http://thredds" \
#                  ".northwestknowledge.net:8080/thredds/dodsC/agg_macav2metdata_pr_GFDL-ESM2M_r1i1p1_historical_1950_2005_CONUS" \
#                  "_daily.nc&variable=precipitation&variable-name=pr_GFDL-ESM2M_historical'"
#
# os.system(baseRequest)

lat = "31"
lon = "-110"

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