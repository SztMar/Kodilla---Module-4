import logging
import sys

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")

def select_gender(gender):
    if gender == "M":
        logging.info("You are a man")
    elif gender == "W":
        logging.info("You are a woman")
    else:
        logging.info("Your gender is not difined as man or women")

if __name__ == "__main__":
    logging.debug("The program was called with this parameters %s" % sys.argv[1:])

    gender = str(sys.argv[1])
    select_gender(gender)