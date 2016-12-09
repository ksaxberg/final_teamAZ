def GetSingleColumnMonthlyAvg(columnName):

    columnIndex = None
    currentYearMonth = None
    pointsToAvg = []

    with open("MonthlyMosq.csv", "w") as writer:
        writer.write("Lat,Lon,Time,"+columnName+"\n")

        with open("/Users/danielkapellusch/Desktop/TESTrcp45Data.csv", "r") as reader:
            for line in enumerate(reader.readlines()):
                data = line[1].split(",")
                if (not columnIndex) or data[0] == "Lat":
                    columnIndex = data.index(columnName)
                    continue

                yearMonth = data[2][:-3]
                if yearMonth != currentYearMonth:
                    if (len(pointsToAvg) > 0):
                        writer.write("{0},{1},{2}-01,{3}\n".format(data[0], data[1], currentYearMonth,
                                                                   sum(map(float, pointsToAvg)) / len(pointsToAvg)))
                    pointsToAvg = []
                    currentYearMonth = yearMonth
                pointsToAvg.append(data[columnIndex])

            writer.write("{0},{1},{2}-01,{3}".format(data[0], data[1], currentYearMonth,
                                                     sum(map(float, pointsToAvg)) / len(pointsToAvg)))


GetSingleColumnMonthlyAvg("Abundance")
