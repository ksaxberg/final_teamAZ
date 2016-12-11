"""mergeCSVs.py takes the csv outputs from DataProcessing and
concatenates the historical and future data into a single CSV for each lat/lon point"""

import os
import sys

args = sys.argv[1:]
scenario = args[0]
errors = "erros.txt"
if args[0] == '-h':
    print 'mergeCSVS.py takes one argument:'
    print 'SCENARIO (rcp45 or rcp85)'
    print 'Go to the directory with all of the csvs that were downloaded and execute'
    sys.exit()


def combine_data(scen):
    with open('filteredFloridaCoords.csv','r') as coords:
        lines = coords.readlines()
    coordinates = []
    for line in lines:
        if line != lines[0]:
            coordinates.append(line.split(','))

    if os.path.exists('historical/') == False:
        os.system('mkdir historical')
        os.system('mv *historical* historical/')

    os.system('mkdir ' + scen)
    os.system('mv *' + scen + '* ' + scen + '/')
    os.system('mkdir ' + scen +'DataFlorida')
    with open(errors,'w') as e:
        for coor in coordinates:
            lat = coor[0]
            lon = str(float(coor[1]))
            histInFile = 'historical/historical'+'_'+lat+'_'+lon+'.csv'
            futInFile = scen +"/" + scen +'_'+lat+'_'+lon+'.csv'
            outfile = scen + 'DataFlorida/' + scen + '_'+lat+'_'+lon+'.csv'
            try:
                with open(outfile,'w') as output:
                    with open(histInFile,'r') as histIn:
                        histData = histIn.readlines()
                    for histd in histData:
                        output.write(histd)
                    with open(futInFile,'r') as futIn:
                        futData = futIn.readlines()
                    for futd in futData:
                        if futd != futData[0]:
                            output.write(futd)
            except Exception as exp:
                e.write(str(exp)+"\n")

answer = raw_input('Are you in the directory with all of your CSVs (historical, rcp45, and rcp85)? y or n?')
if answer == 'y' or answer == 'Y':
    combine_data(scenario)
else:
    print 'Go to directory with all CSVs and re-execute'
    print 'mergeCSVs.py -h for more information'
    sys.exit()