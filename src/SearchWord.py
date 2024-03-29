import re


class Node:

    def __init__(self, day, month, word):
        self.day = day
        self.month = month
        self.word = word

    def get_day(self):
        return self.day

    def get_month(self):
        return self.month
    
    def get_word(self):
        return self.word

class SearchWord:

    words = []
    words.append('Prova de Proficiência')
    words.append('Avaliação Global')
    words.append('Avaliação Área Técnica')
    words.append('Avaliação Global  - Fim 1ª Etapa')
    words.append('Conselho de Classe da 1ª Etapa')
    words.append('OBMEP 1ª fase')
    words.append('OBMEP')
    words.append('Conselho de Classe da 2ª Etapa')
    words.append('Conselho de Classe')
    words.append('Semana Nacional C&T')
    words.append('Mostra de Profissões/Feira de Ciências')
    words.append('Preparação para Recuperação')
    words.append('Recuperação')
    words.append('Exames Finais')
    words.append('Apresentações de TCC')
    words.append('Reunião de Pais/Responsáveis de alunos')
    words.append('Encontro de Pais e Mestres - Resultados 1º trim')
    words.append('Recuperação Final')
    words.append('Retorno das férias')
    words.append('Proficiência e Aproveitamento de Estudos')
    words.append('Data final para lançamentos notas de recuperação')
    words.append('Prova')
    
    nameFile = None #variable created to recieve the path of file

    day_months = [] #it is array of Nodes and Node has attributes as day and month


    def __init__(self):
        return None
    
    def set_nameFile(self, nameFile):
        self.nameFile =  nameFile
    
    def get_day_months(self):
        return self.day_months

    #this function get all information when calender likes this:
    #data - information
    #read data line by line
    #findLineByLine is function will read line by line each file.
    def findLineByLine(self):
        #open file
        try:
            file = open(self.nameFile,'r')
            if file.mode == 'r':
                lines = file.readlines() #i dont to take about stackoverflow because my scope is little
                file.close()

                for string in lines:
                    #here make the functin to look word into line
                    for word in self.words:
                        #for to each word in my list of words
                        match = re.search(word,string)
                        if (match):# if match we have try to get the month and day.
                            #print("String found at: " , match.start())
                            day_month_match = re.search(r'[0-3][0-9]\/[0-1][0-9]', string)
                            if (day_month_match):
                                day_month = day_month_match.group(0).split('/') #return for us day and month
                                #funtion here to split date
                                #the information retuned is 00/00
                                
                                day =  day_month[0] #the index 0 represent day
                                month = day_month[1] #and the index 1 represent month

                                self.day_months.append(Node(day,month,word))
                            else:
                                print('day and month havent found!')
                        #else:
                            #print("String not found!")
        except:
            print("something went wrongs")
    
    def numberMonth(self, month):
        months = {"Janeiro": "01","Fevereiro": "02","Março": "03","Abril": "04","Maio": "05",
            "Junho": "06","Julho": "07","Agosto": "08","Setembro": "09","Outubro": "10","Novembro": "11",
            "Dezembro": "12"} #this is a dictionary
        return months[month] #return to us the currently month in number

    def findBlockByBlock(self):
        months = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto",
        "Setembro","Outubro","Novembro","Dezembro"]
        current_month = "Janeiro" # default
        try: 
            file = open(self.nameFile,'r')
            if file.mode == 'r':
                lines = file.readlines() #i dont to take about stackoverflow because my scope is little
                file.close()
                for string in lines:
                    for month in months: #this for it is to verefy of month on line
                        match = re.search(month,string)# if we find the month we have to save it
                        if(match):
                            current_month = match.group(0)
                    
                    for month in months: #this for it is to verefy of month on line
                        match = re.search(str.upper(month),string)# if we find the month we have to save it
                        if(match):
                            current_month = match.group(0)
                            
                    for word in self.words:
                        match = re.search(word,string)
                        #print(word," ",string)
                        if(match):
                            #I need get the day
                            day_match = re.search(r'[0-3][0-9]', string) # return  to us a day if it exist
                            if(day_match):
                                day = day_match.group(0)
                                month = self.numberMonth(str.lower(current_month).capitalize())#month in number
                                self.day_months.append(Node(day,month,word))
                            
        except ValueError as valerr:
            print("Something went wrongs")
            Print("error is ", valerr) 

        return None
#this is a test function        
def test():
    #day and month
    #re = [/]
    strings = []
    strings.append("hey buddy today is 08/12")
    strings.append("hey buddy today is 08/11")
    strings.append("hey buddy today is 08/10")
    strings.append("hey buddy today is 08/09")
    strings.append("hey buddy today is 08/08")
    strings.append("hey buddy today is 08/07")
    strings.append("hey buddy today is 08/06")
    strings.append("hey buddy today is 08/05")
    strings.append("hey buddy today is 08/04")
    strings.append("hey buddy today is 08/03")
    strings.append("hey buddy today is 08/01")
    strings.append("hey buddy today is 08/02")
    strings.append("hey buddy today is 30/02")
    strings.append("hey buddy today is 31/02")
    strings.append("hey buddy today is 18/02")
    strings.append("hey buddy today is 28/02")
    #[0-0] [1-2]
    for strs in strings:
        #00 - 31
        match = re.search(r'[0-3][0-9]\/[0-1][0-9]',strs)
        if (match):
            print("String found at: " , match.start())
            print(match.group(0))
        else:
            print("String not found!")
    
    word = 'Recuperação'
    match = re.search(r'[0-3][0-9]\/[0-1][0-9]','20/09 ■ Notas Recuperação 2º trimestre')
    if(match):
        day_month = match.group(0).split('/')
        print(day_month[0])
        print(day_month[1])
#this is a test function
def month_test():
    months = {"Janeiro": "01","Fevereiro": "02","Março": "03","Abril": "04","Maio": "05",
        "Junho": "06","Julho": "07","Agosto": "08","Setembro": "09","Outubro": "10","Novembro": "11",
        "Dezembro": "12"} #this is a dictionary
    print(months["Janeiro"])


def main():
    #test()
    sWord = SearchWord()
    sWord.set_nameFile('ourobranco.txt')
    #sWord.findLineByLine()
    sWord.findBlockByBlock()
    for node in sWord.day_months:
        print(node.get_day()," ",node.get_month()," ", node.get_word())
    #month_test()
if __name__ == "__main__":
    main()
