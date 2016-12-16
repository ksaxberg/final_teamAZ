#!/bin/bash
### This script downloads and sets up the MoLS folder

#git clone https://github.com/JocelineLega/MoLS.git

#Check if don't already have MoLS copy downloaded
if [ ! -d "MoLS" ]; then
	git clone https://github.com/JocelineLega/MoLS.git
    touch ./MoLS/__init__.py
    # Overwrite the Run_Model.py to call as a function
    printf "import MoLS\nimport matlab\n\ndef model(csvFolder, csvBeginningFileName):\n"> ./MoLS/Run_Model.py
    printf "\tMy_test=MoLS.initialize()\n\tMy_test.MoLS(csvFolder, csvBeginningFileName,nargout=0)\n" >> ./MoLS/Run_Model.py   
    printf "\tMy_test.terminate()\nif __name__==\"__main__\":\n\tMy_test=MoLS.initialize()\n" >> ./MoLS/Run_Model.py   
    printf "\tMy_test.MoLS('./Weather','Test_Data',nargout=0)\n\tMy_test.terminate()\n" >> ./MoLS/Run_Model.py   
fi

