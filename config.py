import requests, bs4
from datetime import datetime
import logging

from tkinter import ttk

url = 'http://opportunitydesk.org/category/fellowships-and-scholarships/page/'

# establish logging system
logging.basicConfig(filename= "logs\\"+datetime.now().strftime('%Y-%m-%d')+".txt", level=logging.INFO, format=' %(asctime)s - %(levelname)s- %(message)s')

# Pop up configration
class endPopUp:
    def __init__(self, master, NoOfScholars):
        master.title('weMakeScholars')
        self.label = ttk.Label(master, text ="number of scraped shcolarships = "+str(NoOfScholars),width=50).pack()
        ttk.Button(master, text = 'OK',command = master.destroy).pack()


