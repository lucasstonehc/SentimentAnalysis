# -*- Coding: UTF-8 -*-
#coding: utf-8
# encoding: utf-8

#Libraries we have need: requests

import os
import requests

class Linker():

    def __init__(self, name, level, link):
        self.name  = name
        self.level = level
        self.link = link
    
    def get_name(self):
        return self.name
    
    def get_level(self):
        return self.level
    
    def get_link(self):
        return self.link

#the class calender has been manipulete all elements and things that have connected with it
class CalenderCrawler():

    def __init__(self, driver):
        self.driver = driver
        self.urlsCalenders = []

    def set_all_links(self):
        self.urlsCalenders.append(
            Linker(
                name = 'ifmg-congonhas', 
                level = 'tecnico', 
                link = 'https://www.ifmg.edu.br/congonhas/ensino-1/Calendrio2019TcnicoIntegrado.pdf' 
            )
        )
        self.urlsCalenders.append(
            Linker(
                name = 'ifmg-governadorvaladares', 
                level = 'tecnico', 
                link = 'https://www.ifmg.edu.br/governadorvaladares/ensino/calendario-academico/calendario_academico_medio.pdf' 
            )
        )
        
        self.urlsCalenders.append(
            Linker(
                name = 'ifmg-conselheirolafaiete', 
                level = 'tecnico', 
                link = 'https://www.ifmg.edu.br/conselheirolafaiete/ensino-1/arquivos-ensino/calendario-academico-ifmg-cl-2019-ensino-medio-integrado-corrigido10jun.pdf' 
            )
        )
        self.urlsCalenders.append(
            Linker(
                name = 'ifmg-conselheirolafaiete', 
                level = 'tecnico', 
                link = 'https://www.ifmg.edu.br/congonhas/ensino-1/Calendrio2019TcnicoIntegrado.pdf' 
            )
        )
        self.urlsCalenders.append(
            Linker(
                name = 'ifmg-piumhi', 
                level = 'tecnico', 
                link = 'https://www.ifmg.edu.br/piumhi/ensino/docs/calendarios/Anexo_0220749_Calendario_2019_Cursos_Tecnicos_v.14dez.pdf' 
            )
        )
        self.urlsCalenders.append(
            Linker(
                name = 'ifmg-ourobranco', 
                level = 'tecnico', 
                link = 'https://www.ifmg.edu.br/ourobranco/nossos-cursos/copy_of_CalendrioIntegrado2019_1.pdf' 
            )
        )
        self.urlsCalenders.append(
            Linker(
                name = 'ifmg-ipatinga', 
                level = 'tecnico', 
                link = 'https://www.ifmg.edu.br/ipatinga/Calendrio2019CampusIpatingaIntegrado.pdf' 
            )
        )
        self.urlsCalenders.append(
            Linker(
                name = 'ifmg-ouropreto', 
                level = 'tecnico', 
                link = 'https://www.ifmg.edu.br/ouropreto/ensino/calendario-escolar/calendario-academico/calendarioacademico20191' 
            )
        )
        self.urlsCalenders.append(
            Linker(
                name = 'ifmg-itabirito', 
                level = 'tecnico', 
                link = '' 
            )
        )
        self.urlsCalenders.append(
            Linker(
                name = 'ifmg-ribeiraodasneves', 
                level = 'tecnico', 
                link = 'https://www.ifmg.edu.br/ribeiraodasneves/arquivos/ensino-arquivos/calendario-academico/calendario-tecnico-integrado-2019' 
            )
        )
        self.urlsCalenders.append(
            Linker(
                name = 'ifmg-pontenova', 
                level = 'tecnico', 
                link = 'https://www.ifmg.edu.br/pontenova/ensino-1/documentos-ensino/copy_of_Calendrio2019Integrado1.pdf' 
            )
        )
        self.urlsCalenders.append(
            Linker(
                name = 'ifmg-sabara', 
                level = 'tecnico', 
                link = 'https://www.ifmg.edu.br/sabara/ensino-pesquisa-e-extensao/registro-e-controle-academico/rca-documentos/Calendrio2019tcnicosite.pdf' 
            )
        )
        self.urlsCalenders.append(
            Linker(
                name = 'ifmg-formiga', 
                level = 'tecnico', 
                link = 'https://formiga.ifmg.edu.br/documents/2018/ConselhoAcademico/Resoluo-005-Conselho-acadmico---Aprovao-calendrio-acadmico-2019--Tcnico.pdf' 
            )
        )
        self.urlsCalenders.append(
            Linker(
                name = 'ifmg-saojoaoevangelista', 
                level = 'tecnico', 
                link = 'https://www.sje.ifmg.edu.br/portal/images/artigos/ensino/calendario_academico/2019/Calendario.2019_-DDE-CGEMT_v4.pdf' 
            )
        )
        self.urlsCalenders.append(
            Linker(
                name = 'ifmg-betim', 
                level = 'tecnico', 
                link = 'https://drive.google.com/file/d/1wM1ByncAcU8-_NbZT8gGCmZ2tSzGtTUE/view' 
            )
        )
        self.urlsCalenders.append(
            Linker(
                name = 'ifmg-arcos', 
                level = 'tecnico', 
                link = 'https://www.ifmg.edu.br/arcos/ensino-1/CalendarioAcademico2019.pdf' 
            )
        )
        self.urlsCalenders.append(
            Linker(
                name = 'ifmg-arcos', 
                level = 'tecnico', 
                link = '' 
            )
        )
        self.urlsCalenders.append(
            Linker(
                name = 'ifmg-arcos', 
                level = 'tecnico', 
                link = '' 
            )
        )
        self.urlsCalenders.append(
            Linker(
                name = 'ifmg-arcos', 
                level = 'tecnico', 
                link = '' 
            )
        )

    def salve_calender_on_folder(self, path):
        return None

    def calenderPDF_to_calenderTXT(self, listOLinks):
        #parameters 
        #pdf2txt.py -o example.txt -Y normal -t text calender.pdf
        for linker in listOLinks:
            try:
                myCmd = "pdftotext -layout -raw "+linker.name+"-"+linker.level+".pdf "+linker.name+"-"+linker.level+".txt"
                os.system(myCmd) #the system operation is going to execute the command into him terminal
            except:
                print('something went wrong!')

    def set_list_of_calenders(self, urlsCalenders):
        self.urlsCalenders = urlsCalenders
    
    def getCalender(self, listOLinks): #this function get calender from web, copy all contents into file web and save it into another file.

        for linker in listOLinks:
            fileName = linker.name+"-"+linker.level+".pdf"
            with open(fileName, "wb") as file:
                try:
                    response = requests.get(linker.link, verify=False) #right here we pass the link to method get of requests object
                    file.write(response.content) #save this file into current direct folder
                except:
                    print('something went wrong!')
                finally:
                    file.close()

def main():
    #the process is get calender into web and save it. after this we have must convert them in txt.
    calender = CalenderCrawler(driver=None)

    calender.set_all_links() #this function has all links where there are calenders files

    list_of_calenders_urls = calender.urlsCalenders

    calender.getCalender(list_of_calenders_urls) #This function will get calenders from web and save it

    calender.calenderPDF_to_calenderTXT(list_of_calenders_urls)#this function convert pdf file to text file.
   

if __name__ == "__main__":
    main()