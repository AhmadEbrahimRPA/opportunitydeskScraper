# from config import *

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# from selenium import webdriver

# highlight
# def highlight(element):
#     """Highlights a Selenium webdriver element"""
#     driver = element._parent

#     def apply_style(s):
#         driver.execute_script("arguments[0].setAttribute('style', arguments[1])", element, s)

#     orignal_style = element.get_attribute('style')
#     apply_style("border: 4px solid red")
#     if (element.get_attribute("style") != None):
#         sleep(5)
#     apply_style(orignal_style)


# navigate to url
# driver.get(url)
# scroll down and click view more
# while True:
#     try:
#         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID,'load-more')))
#         element = driver.find_element_by_id('load-more')
#         print('element found')
#         driver.execute_script("arguments[0].scrollIntoView();", element)
#         print('scrolled to element')
#         element.click()
#         print('element clicked')
#     except:
#         print('no view more')
#         break
# res = requests.get(driver.page_source)
# playFile = open('wemakescholars.txt', 'wb')
# playFile.write(driver.page_source)
# noStarchSoup = bs4.BeautifulSoup(res.text, features="html.parser")


# x = dict(a=1, b=2)
# y = dict(a=2, b=2, c=3)
# new_items = {k: y[k] for k in y if k not in x}

# from tkinter import *
# from time import sleep



# def print_result():
#     print('Hi')
#     for i in range(100):
#         print(i)
#         sleep(5)

# root = Tk()
# close= Button(root, text="Close script", command=exit)
# close.pack()
# prints = Button(root, text="prints", command=print_result)
# prints.pack()

# root.mainloop()
# def getScholarsNumbers():
#     '''
#     go to URL of scholars sorted by dateposted then get total number of scholars
#     '''
#     logging.info('getting No. of scholarships...')
#     content = getPageSource('https://www.wemakescholars.com/scholarship/search?sort=dateposted')
#     soup = bs4.BeautifulSoup(content,'html.parser')
#     NoOfScholars = int((((soup.find("p", {"class": "records-found-num"})).getText()).split())[0])
#     print(NoOfScholars)
#     logging.info('No. of scholarships is'+str(NoOfScholars))
#     return NoOfScholars


# # open chrome in background
# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('disable-gpu')
# options.add_argument('--disable-notifications')
# options.add_argument("--window-size=1920,1080")
# driver = webdriver.Chrome(chrome_options= options)


from tkinter import Tk

root = Tk()