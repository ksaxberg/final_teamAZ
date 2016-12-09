import os

files = os.listdir(os.getcwd())

with open("Makeflow.makeflow", "w") as f:
    run = ""
    for line in files:
        if (line.endswith(".csv")): 
            run = "{0}.out->weather1.csv: {0}->weather.csv Get_MoLS.sh Run_Model.py\n".format(line.strip()) 
            run += "    bash ./Get_MoLS.sh ; python Run_Model.py weather; cp weather.csv weather1.csv\n\n".format(line.strip())
            f.write(run)
