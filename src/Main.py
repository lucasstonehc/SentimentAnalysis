from SearchWord import SearchWord
from CalenderCrawler import *
from DataBase import *

def main():
    cCrawler = CalenderCrawler()
    cCrawler.set_all_links() 
    list_of_calenders_urls = cCrawler.urlsCalenders
    dBase = DataBase()

    sWord = SearchWord()
    for calender in list_of_calenders_urls:#this loop will looking for all files .txt into our folder
        sWord.set_nameFile(calender.name+'-'+calender.level+'.txt') 
        
        #here we must implements condition to choose  which method used 
        #sWord.findLineByLine()
        #sWord.findBlockByBlock()

        #after run the method, we need to get  day_months array
        #get_day_months()

   
    


if __name__=="__main__":
    main()