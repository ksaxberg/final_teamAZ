"""Takes the full set of data and takes monthly averages of desired variable (default = abundance)"""

import sys

args = sys.argv[1:]

inputPath = args[0]   #EXAMPLE: rcp45_Arizona.csv
outputPath = args[1]  #EXAMPLE: MonthlyTemp.csv
if len(args) == 2:
    variable = 'Abundance\n'
elif len(args) == 3:
    variable = args[2]

def GetSingleColumnMonthlyAvg(columnName):

    columnIndex = None
    currentYearMonth = None
    pointsToAvg = []

    with open(outputPath, "w") as writer:
        writer.write("Lat,Lon,Time,"+columnName)

        with open(inputPath, "r") as reader:
            for line in enumerate(reader.readlines()):
                data = line[1].split(",")
                if (not columnIndex) or data[0] == "Lat":
                    columnIndex = data.index(columnName)
                    continue

                time = data[2].split('-')
                if int(time[1]) < 10:
                    mon = '0'+time[1]
                if int(time[1]) >= 10:
                    mon = time[1]
                yearMonth = time[0] + '-'+mon
                if yearMonth != currentYearMonth:
                    if (len(pointsToAvg) > 0):
                        writer.write("{0},{1},{2}-01,{3}\n".format(data[0], data[1], currentYearMonth,
                                                                   sum(map(float, pointsToAvg)) / len(pointsToAvg)))
                    pointsToAvg = []
                    currentYearMonth = yearMonth
                pointsToAvg.append(data[columnIndex])

            writer.write("{0},{1},{2}-01,{3}".format(data[0], data[1], currentYearMonth,
                                                     sum(map(float, pointsToAvg)) / len(pointsToAvg)))


GetSingleColumnMonthlyAvg(variable)
