'''When each file is executed the data related to file is logged in the a new log file'''
import logging
import os
from datetime import datetime


'''Setting format of log file'''

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" 


'''Crete a logger path such that each logger file is created in under src folder'''

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)  


''' Create new logger files in same folder where old logger files are present'''

os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)


'''Setting up configurayion format for logger data'''

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s ",
    level=logging.INFO,
    
)

""""
'''To check whether logger is working properly or not   '''

if __name__=='__main__':
    logging.info("Logging has started")

"""