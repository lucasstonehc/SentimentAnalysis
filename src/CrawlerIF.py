#get user by id and collect your attributes
#get twitter -> created_at, checked out weather
import tweepy 
import datetime
#Dados de conta
consumer_key ='5W7W6BSMHMsEtnLNNUJSo4jcs'
consumer_secret ='XJi5T7Ta5Co18Hbfgh1HvNubZ9pccx8y8q5uqUto5h8Sk9swo6'

access_key = '954784886157643778-buXhPhSb4eysyJVq01xTymPpzJBFO6a'
access_secret = 'yIFSSTBhzx1ZblAXa9ecrWKHuEtrZ2KJhur7Ddecf750G'

#Conexão com a API do Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

user = api.get_user(3048544857) # get name by id ok
#user = api.get_user(screen_name = 'fernandagperei3') # get id by name 
print(user.screen_name)
#we passed arrya of names 

#get twitter by location

twitters = []
#response = api.search(q='ifmg',)
for tweet in tweepy.Cursor(api.search,q="*",count=1000,geocode="19.8838,43.8534,105km").items(1000):
    twitters.append(tweet.user.id)
    print(tweet.user.id)


#AGE and GENDER -> name we have a problem - how can i solve them?
#AGE for year highschool or College
#Gender for boys or girls
#  

names = ['SilvaMyrla', 'duainerodrigues', 'VitoriaAnalian', 'dannicaastro', 'RaimundoAngelim', 'Igor_Maia_Costa', 'EdilbertoFarias', 'TiagoCaligula', 'emismendonca', 'bbarbosaraquel', 'vyctorius', 'nabiacraveiro','rebecafsilv', 'LourranySt', 'vina_prof', 'Viini28', 'pq_drilicius', 'galifreyana', 'MariliiaG']


tweets = api.user_timeline(id=user.id, count=10)

status = api.get_status(user.id)
#print(status)

#for name in names:
    #try:
        #user = api.get_user(screen_name = name)
        #print(user.id)
        #print(user.profile_location)
        #print(user.time_zone)
    #except tweepy.error.TweepError:
        #print("user not found")

   


#GET PROFILE LOCATION
    #user.profile_location
    #time_zone

#tweets = api.user_timeline(id=user.id, count=10) #get uo to 10 tweets of time line´s user

#GET LOCATION
#location = tweets[0].author.location  #get Location bring some emmotions
#print(location.encode())


def seasons_of_tweet(tweet):
    #get attr created_at from tweet object
    data = tweet.created_at # get when has cretead

    #strftime is a function from library´s datetime
    month = data.strftime(r"%b") #get month from data
    day = data.strftime(r"%d") # get day from data

    #SEASONS IN BRAZIL 
    #Summer > [December January February]
    #started: 21 December  Finished: 19 March

    #Autumn > [March April May]
    #started: 20 March  Finished: 19 June

    #Winter > [June July August]
    #started: 20 June Finished: 21 September

    #Spring > [September October November]
    #started: 22 September  Finished: 20 December

    if month == 'Dec' and day >= '21':
        print('summer')
    elif month == 'Jan':
        print('summer')
    elif month == 'Feb':
        print('summer')
    elif month == 'Mar' and day <= '19':
        print('summer')
    elif month == 'Mar' and day >= '20':
        print('Autumn')
    elif month == 'Apr':
        print('Autumn')
    elif month == 'May':
        print('Autumn')
    elif month == 'Jun' and day <= '19':
        print('Autumn')
    elif month == 'Jun' and day >= '20':
        print('Winter')
    elif month == 'Jul':
        print('Winter')
    elif month == 'Aug':
        print('Winter')
    elif month == 'Sep' and day <= '21':
        print('Winter')
    elif month == 'Sep' and day >= '22':
        print('Winter')
    elif month == 'Oct':
        print('Spring')
    elif month == 'Nov':
        print('Spring')
    elif month == 'Dec' and day <= '20':
        print('Spring')
    

seasons_of_tweet(tweet = tweets[0])


#SOME ACTIONS MAYBE I HAVE USED IN NEXT FUTURE 

#mounth = datetime.datetime.month(create_at)

#list_of_friends = api.friends_ids(1088398616)
#print(user.id)
#for friend_id in list_of_friends: #get all friends list
    #print(friend_id)
#Variável que irá armazenar todos os Tweets com a palavra escolhida na função search da API
#new_tweets = api.search(q,lang='pt',locale='brazil',rpp=100,count=200)


#agrupar calendarios - por datas semelhantes
#classificar os post ansiosos