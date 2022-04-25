'''
Navigate to URL
scrape data
save table to CSV file
'''

import time
start_time = time.time()

from config import logging, endPopUp
from components import scrapeScholars, saveScholars
import traceback
from tkinter import Tk

try:
    # scrape data
    scholars = scrapeScholars()
    logging.info('total number of scholarships is' + str(len(scholars.keys())))
    #save data
    saveScholars(scholars)
    # get excution time
    execution_Time = time.time() - start_time
    logging.info("--- "+str(int(execution_Time/60))+" Minutes ---")
    # end notification popup
    root = Tk()
    app = endPopUp(root, len(scholars.keys()))
    root.mainloop()
except Exception as error:
    logging.error(traceback.format_exc())
    raise Exception(error)