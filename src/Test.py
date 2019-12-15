#Programa que coleta todos os twittes já realizados de acordo com uma palvra-chave.
#Os dados são colocados em uma planilha no formato xlsx.

#Adaptação dos códigos de Kaorw e Paulo:

#https://gist.github.com/Kaorw/7594044 
#'Grap multiple user's user_timeline from twitter API and save to Excel'

#https://paulovasconcellos.com.br/aprenda-a-fazer-um-analisador-de-sentimentos-do-twitter-em-python-3979454f2d0d
#'Aprenda a fazer um Analisador de Sentimentos do Twitter em Python'


#Biblioteca de escrita na planilha
import xlsxwriter

#Biblioteca de dados do Twitter
import tweepy 

#Dados de conta
consumer_key ='5W7W6BSMHMsEtnLNNUJSo4jcs'
consumer_secret ='XJi5T7Ta5Co18Hbfgh1HvNubZ9pccx8y8q5uqUto5h8Sk9swo6'

access_key = '954784886157643778-buXhPhSb4eysyJVq01xTymPpzJBFO6a'
access_secret = 'yIFSSTBhzx1ZblAXa9ecrWKHuEtrZ2KJhur7Ddecf750G'

#Funcao que coleta todos os tweets
def get_all_tweets(q):

	#Conexão com a API do Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True)

	#Lista para armazenar todos os tweets
    alltweets = []  
    

	#Variável que irá armazenar todos os Tweets com a palavra escolhida na função search da API
    new_tweets = api.search(q,lang='pt',locale='brazil',rpp=200,count=200)
	#A medida em que existirem novos twetts,a lista alltweets vai recebendo dados
    alltweets.extend(new_tweets)

	#Salvar o id do tweet mais antigo menos um
    oldest = alltweets[-1].id - 1

    #Continue pegando tweets até que não haja mais tweets para pegar
    while len(new_tweets) > 0:

        #Agora dentro do loop,iremos procurar a palvra-chave e acrescentar a variável max_id que evitará duplicatas
        new_tweets = api.search(q,lang='pt',locale='brazil',rpp=200,count=1500,max_id=oldest) 
		
        #Salva twittes mais recentes
        alltweets.extend(new_tweets)

        #Salva o id do tweet mais antigo menos um
        oldest = alltweets[-1].id - 1

    

    #Variável outtweets recebe uma matriz com diversos dados disponíveis na API para cada tweet
    outtweets = [[tweet.user.screen_name, tweet.created_at, tweet.coordinates, tweet.geo,tweet.source,tweet.text] for tweet in alltweets]
    #print(outtweets)
    return outtweets
def write_worksheet(q):

    #formating for excel
    format01 = workbook.add_format()
    format02 = workbook.add_format()
    format03 = workbook.add_format()
    format04 = workbook.add_format()
    format01.set_align('center')
    format01.set_align('vcenter')
    format02.set_align('center')
    format02.set_align('vcenter')
    format03.set_align('center')
    format03.set_align('vcenter')
    format03.set_bold()
    format04.set_align('vcenter')
    format04.set_text_wrap()

    out1 = []
    header = ["id","created_at","coordinates-x","coordinates-y","geolocation","source","text"]

    worksheet = workbook.add_worksheet(q)

    out1 = get_all_tweets(q)
    row = 0
    col = 0

    worksheet.set_column('A:A', 20)
    worksheet.set_column('B:B', 18)
    worksheet.set_column('C:C', 13)
    worksheet.set_column('D:D', 13)
    worksheet.set_column('E:E', 13)
    worksheet.set_column('F:F', 20)
    worksheet.set_column('G:G', 120)

    for h_item in header:
        worksheet.write(row, col, h_item, format03)
        col = col + 1

    row += 1
    col = 0

    for o_item in out1:
        write = []
        cord1 = 0
        cord2 = 0
        texto = ""
        write = [o_item[0], o_item[1], o_item[3],o_item[4], o_item[5]]
        #print(o_item[0])
        #print(o_item[1])
        #print(o_item[2])
        #print(o_item[3])
        #print(o_item[4])
        #print(o_item[5])
        '''
        0 return user to us
        1 return creat at to us
        2 return coordinates to us
        3 return geolocation to us
        4 return source to us 
        5 return text to us
        '''
        if o_item[2]: #if item[2] is filled then we get it!
            cord1 = str(o_item[2]['coordinates'][0])
            cord2 = str(o_item[2]['coordinates'][1])
        else:
            cord1 = ""
            cord2 = ""
        
        if write[2]:
            geolocation = str(write[2])
        else:
            geolocation = ""
            
        
        format01.set_num_format('yyyy/mm/dd hh:mm:ss')
        worksheet.write(row, 0, write[0], format02) #id
        worksheet.write(row, 1, write[1], format01) #creat at
        worksheet.write(row, 2, cord1, format02) #cood x
        worksheet.write(row, 3, cord2, format02) #cood y
        worksheet.write(row, 4, geolocation, format02) #geolocation
        worksheet.write(row, 5, write[3], format02) #source
        worksheet.write(row, 6, write[4], format04) #text
        row += 1
        col = 0


workbook = xlsxwriter.Workbook('ansiedade_crawler_IFs.xlsx')
write_worksheet('ifmg')         #ACRE
"""
write_worksheet('ifmgsabara')  
write_worksheet('ifal')         #ALAGOAS
write_worksheet('ifap')         #AMAPÁ
write_worksheet('ifam')         #AMAZONAS
write_worksheet('ifba')         #BAHIA
write_worksheet('ifbaiano')     #BAHIA
write_worksheet('ifce')         #CEARÁ
write_worksheet('ifb')          #DISTRITO FEDERAL
write_worksheet('ifes')         #ESPIRITO SANTO
write_worksheet('ifg')          #GOIÁS
write_worksheet('ifgoiano')     #GOIÁS
write_worksheet('ifmt')         #MATO GROSSO
write_worksheet('ifsuldeminas') #MINAS GERAIS
write_worksheet('ifmg')         #MINAS GERAIS
write_worksheet('ifnmg')        #MINAS GERAIS
#write_worksheet('ifsudeste')    #MINAS GERAIS
write_worksheet('iftm')         #MINAS GERAIS
write_worksheet('ifpa')         #PARÁ
write_worksheet('ifpb')         #PARAÍBA
write_worksheet('ifpr')         #PARANÁ
write_worksheet('ifpe')         #PERNAMBUCO
#write_worksheet('ifsertao')     #PERNAMBUCO
write_worksheet('ifpi')         #PIAUÍ
write_worksheet('ifrj')         #RIO DE JANEIRO
#write_worksheet('iff')          #RIO DE JANEIRO
write_worksheet('ifrn')         #RIO GRANDE DO NORTE
#write_worksheet('ifrsul')       #RIO GRANDE DO SUL
write_worksheet('ifrs')         #RIO GRANDE DO SUL
write_worksheet('iffarroupilha')#RIO GRANDE DO SUL
write_worksheet('ifro')         #RONDÔNIA
write_worksheet('ifrr')         #RORAIMA
write_worksheet('ifsp')         #SÃO PAULO
write_worksheet('ifsc')         #SANTACATARINA
write_worksheet('ifc')          #SANTACATARINA
write_worksheet('ifs')          #SERGIPE
write_worksheet('ifto')         #TOCANTINS
"""
workbook.close()



#ask nayane e cris, vcs estavam coletando quando vcs buscavam vinha os as coordenadas dos twiiters, pq me lembro que vcs falaram q tinha tirado esse dado do formulário.

