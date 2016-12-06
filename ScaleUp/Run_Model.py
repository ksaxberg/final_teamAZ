from MoLS import Run_Model
import sys
import logging

if __name__=="__main__":
    logging.debug('Running Model')
    f = sys.argv[1]
    Run_Model.model(os.getcwd(), f) 
    logging.debug('Model has finished running')
