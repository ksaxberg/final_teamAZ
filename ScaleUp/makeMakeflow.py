import sys
import os

arg = sys.argv[1]

files = os.listdir(arg)

with open("Makeflow.makeflow", "w") as f:
    run = ""
    for line in files:
        if (line.endswith(".csv")): 
            run = "{0}.out->weather.csv: {0}->weather.csv Get_MoLS.sh Run_Model.py\n".format(line.strip()) 
            run += "    bash ./Get_MoLS.sh ; python Run_Model.py weather.csv\n\n".format(line.strip())
            f.write(run)
