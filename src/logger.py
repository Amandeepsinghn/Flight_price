import logging 
import os 
from datetime import datetime



logs_file=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path=os.path.join(os.getcwd(),'artifact',logs_file)

os.makedirs(logs_path,exist_ok=True)

logs_path_file=os.path.join(logs_path,logs_file)




logging.basicConfig(
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    filename=logs_path_file
)



    
if __name__=="__main__":
    try:
        d=1/0
            
    except Exception as e:
        raise Custom_Exception(e,sys)