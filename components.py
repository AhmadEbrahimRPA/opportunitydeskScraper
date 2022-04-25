from config import bs4, url, logging, requests
import glob
import os
import pandas as pd
from time import strftime





def getPageSource(in_URL):
    '''
    Navigate to desired URL then return page source
    '''
    logging.info('Navigate to desired '+in_URL)
    print('Navigate to desired '+in_URL)
    try:
        page = requests.get(in_URL)
    except:
        try:
            page = requests.get(in_URL)
        except:
            page = requests.get(in_URL)
    logging.info('navigated to URL')
    return page.content




    

def scrapeScholars():
    '''
    open URL, scrape the website, add data to the dictionary of needed data then go to next page and so on.
    '''
    logging.info('scraping scholarships...')
    sch = dict()
    pageNumber = 1
    while(True):
        prevNoOfScholars = len(list(sch.keys()))
        content = getPageSource(url+str(pageNumber))
        soup = bs4.BeautifulSoup(content,'html.parser')
        scholarships = soup.findAll("div", {"class": "blogposts-inner"})
        for scholarship in scholarships:
            name = (scholarship.find("a")).get('title')
            link = (scholarship.find("a")).get('href')
            deadline = (scholarship.find("div", {"class": "maga-excerpt clearfix"})).getText().strip().split(',')[0]
            postDate = (scholarship.find("span", {"class": "meta_date"})).getText().strip()
            sch.setdefault(name, [link, deadline, postDate])
        if len(list(sch.keys())) == prevNoOfScholars:
            break
        else:
            pageNumber += 1
    logging.info('scholarships scraped successfully')
    return sch



def writeRange(scholarships, excel_file_name=None):
    '''
    save data to excel file
    '''
    logging.info('write data to excel file')
    names = list(scholarships.keys())
    links = list(list(zip(*scholarships.values()))[0])
    deadline = list(list(zip(*scholarships.values()))[1])
    postDate = list(list(zip(*scholarships.values()))[2])
    scholarsExcel = pd.DataFrame({'Name':names,'Link':links, 'deadline':deadline, 'postDate':postDate})
    if not excel_file_name:
        excel_file_name = strftime("%a-%d-%m-%H-%M")+'.xlsx'
    scholarsExcel.to_excel(excel_file_name, index=False, encoding='utf-8')
    logging.info('data written to excel file')



def getNewScholars(oldNames, scholarships):
    '''
    compare two lists then save excel file with new data
    '''
    logging.info('get new scholarships')
    newScholars = dict()
    currentNames = list(scholarships.keys())
    newNames = [i for i in currentNames if i not in oldNames and i]
    if newNames:
        for name in newNames:
            if name.strip():
                newScholars.setdefault(name, scholarships[name])
    
        writeRange(newScholars, strftime("%a-%d-%m")+'new.xlsx')
        logging.info('new scholarships successfully got')


def getdeletedScholars(oldNames, oldScholars, currentNames):
    '''
    compare two lists then save excel file with deleted data
    '''
    logging.info('get deleted scholarships')
    deletedScholars = dict()
    delNames = [i for i in oldNames if i not in currentNames and i]
    if delNames:
        for name in delNames:
            if name.strip():
                deletedScholars.setdefault(name, oldScholars[name])
    
        writeRange(deletedScholars, strftime("%a-%d-%m")+'del.xlsx')
        logging.info('deleted scholarships successfully got')


def saveScholars(scholars):
    '''
    1.get last excel files and read name column from it
    2.get new scholarships
    3.get deleted scholarships
    4.get All scholarships
    '''
    # 1.get last excel files and read name column from it
    excelFiles = glob.glob('*.xlsx')
    if excelFiles:
        '''
        only in case there is an old file(not first run)
        '''
        oldScholars = dict()
        excelFiles.sort(key=lambda f: os.path.getctime(f)) # arrange them by last modified date (accending)
        recentExcel = excelFiles[len(excelFiles)-1] # last excel file
        lastData = pd.read_excel(recentExcel) # get last data from last excel shhet
        lastNames = list(lastData['Name']) # get name column

        #2.get new scholarships
        getNewScholars(lastNames, scholars)
        #3.get deleted scholarships
        lastLinks = list(lastData['Link'])
        lastdeadline = list(lastData['deadline'])
        lastpostDate = list(lastData['postDate'])
        # create dictionary of old values
        for name in range(len(lastNames)):
            oldScholars.setdefault(lastNames[name], [lastLinks[name], lastdeadline[name], lastpostDate[name]])
        newNames = list(scholars.keys())
        getdeletedScholars(lastNames, oldScholars, newNames)
        #4.get All scholarships
        writeRange(scholars)
    else:
        '''
        only in case there is no old file(first run)
        '''
        #4.get All scholarships
        writeRange(scholars)



