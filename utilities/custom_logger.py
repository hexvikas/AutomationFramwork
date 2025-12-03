import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        # 1. Log file ka naam aur path set karo
        log_path = os.path.join(os.getcwd(), "logs", "automation.log")
        
        # 2. Logging config set karo
        # format='%(asctime)s: %(levelname)s: %(message)s' -> Ye timestamp layega
        logging.basicConfig(filename=log_path,
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p',
                            force=True) # force=True purane handlers ko overwrite karta hai taaki duplicate logs na aayein
        
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger