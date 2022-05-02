#!/usr/bin/env python
# coding: utf-8

# In[733]:


def topic(url):
    import requests
    from bs4 import BeautifulSoup
    html_doc = requests.get(url)
    soup = BeautifulSoup(html_doc.text,'html.parser')
    return soup


# 1.Write a python program to display all the header tags from wikipedia.org.

# In[734]:


Wiki = topic('https://en.wikipedia.org/wiki/Main_Page')


# In[735]:


def Wikipedia(Wiki):
    h1,h2,h3 = [],[],[]
    for i in Wiki.find_all('h1'):
        h1.append((i.text).strip().replace('\xa0',''))
    for j in Wiki.find_all('h2'):
        h2.append((j.text).strip().replace('\xa0',''))
    for k in Wiki.find_all('h3'):
        h3.append((k.text).strip().replace('\xa0',''))
    
    Header_Tags = print('The header tags in Wikipedia are :\n h1: {} \n h2: {},\n h3: {}'.format(h1,h2,h3))
    return Header_Tags


# In[736]:


Wikipedia(Wiki)


# 2.Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release) and make data frame.

# In[738]:


IMDB1 = topic('https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc&ref_=adv_prv')
IMDB2 = topic('https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc&start=51&ref_=adv_nxt')


# In[739]:


def imdb(IMDB):
    name,rating,year_of_release = [],[],[]
    for i in IMDB.find_all('h3',class_='lister-item-header'):
        name.append(i.find('a').text)
    for j in IMDB.find_all('div',class_="inline-block ratings-imdb-rating"):
        rating.append((j.text).replace('\n',''))
    for k in IMDB.find_all('span',class_='lister-item-year text-muted unbold'):
        year_of_release.append((k.text).replace(')','').replace('(',''))
    
    import pandas as pd
    ind = list(range(1,50,1))
    
    df = pd.DataFrame(list(zip(name,rating,year_of_release)),columns=['Name of the movie','Rating','Year_of_release'])
    return df


# In[740]:


import pandas as pd
a,b = imdb(IMDB1),imdb(IMDB2)
MOVIE = pd.concat([a,b],axis=0)
MOVIE.index = [x for x in range(1, len(MOVIE.values)+1)]
MOVIE


# 3.Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. name, rating, year of release) and make data frame.

# In[741]:


Indian_IMDB = topic('https://www.imdb.com/india/top-rated-indian-movies/')


# In[744]:


def indian_imdb(ind_IMDB):
    name,rating,year_of_release = [],[],[]
    for i in Indian_IMDB.find_all('td','href',class_='titleColumn'):
        name.append((i).a.text)
    for j in Indian_IMDB.find_all('td',class_='ratingColumn imdbRating'):
        rating.append((j.text).strip())
    for k in Indian_IMDB.find_all('span',class_='secondaryInfo'):
        year_of_release.append((k.text))
    
    import pandas as pd
    ind = list(range(1,50,1))
    
    df = pd.DataFrame(list(zip(name,rating,year_of_release)),columns=['Name of the movie','Rating','Year_of_release'])
    df.index = [x for x in range(1, len(df.values)+1)]
    return df[0:100]


# In[745]:


indian_imdb(Indian_IMDB)


# 4.Write a python program to scrape product name, price and discounts from https://meesho.com/bags-ladies/pl/p7vbp .

# In[761]:


Meesho = topic('https://meesho.com/bags-ladies/pl/p7vbp')


# In[762]:


def bag(women):
    name,price,discounts = [],[],[]
    for i in Meesho.find_all('p',class_='Text__StyledText-sc-oo0kvp-0 bWSOET NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 cQhePS NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 cQhePS'):
        name.append((i).text)
    for j in Meesho.find_all('h5',class_='Text__StyledText-sc-oo0kvp-0 hiHdyy'):
        price.append((j).text)
    for k in  Meesho.find_all('span',class_='Text__StyledText-sc-oo0kvp-0 lnonyH'):
        discounts.append((k.text))
    
    import pandas as pd
    
    
    df = pd.DataFrame(list(zip(name,price,discounts)),columns=['Name of the Bag','Price','Discount'])
    df.index = [x for x in range(1, len(df.values)+1)]
    return df


# In[765]:


bag(Meesho)


# 5) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
# a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
# b) Top 10 ODI Batsmen along with the records of their team and rating.
# c) Top 10 ODI bowlers along with the records of their team and rating.

# In[766]:


icc_mens_team = topic('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')


# In[769]:


def team(men):
    team, matches,rating = [],[],[]
    for i in icc_mens_team.find_all('span',class_='u-hide-phablet'):
        if i.text!='':
            team.append((i).text.strip())
        
    for j in icc_mens_team.find_all('td',{'class': ['table-body__cell u-center-text','rankings-block__banner--matches']}):
        matches.append((j).text)
    points = matches[0::2]
    
    for k in icc_mens_team.find_all('td',{'class': ['rankings-block__banner--rating u-text-right','table-body__cell u-text-right rating']}):
        rating.append((k).text.strip())
    
    
    import pandas as pd
    ind = list(range(1,50,1))
    
    df = pd.DataFrame(list(zip(team,points,rating)),columns=['Team','Points','Rating'])
    df.index = [x for x in range(1, len(df.values)+1)]
    return df[0:10]


# In[770]:


team(icc_mens_team)


# In[771]:


icc_mens_batsmen = topic('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting')


# In[772]:


def batsmen(men):
    player,team,rating = [],[],[]
    for i in icc_mens_batsmen.findAll(class_ = ['rankings-block__banner--name-large','table-body__cell rankings-table__name name']):
        player.append((i).text.strip())
        
    for j in icc_mens_batsmen.findAll(class_ = ['rankings-block__banner--nationality','table-body__logo-text']):
        team.append((j).text.strip())
    
    for k in icc_mens_batsmen.findAll(class_ = ['rankings-block__banner--rating','table-body__cell rating']):
        rating.append((k).text)
    
    
    import pandas as pd
    ind = list(range(1,50,1))
    
    df = pd.DataFrame(list(zip(player,team,rating)),columns=['Player','Team','Rating'])
    df.index = [x for x in range(1, len(df.values)+1)]
    return df[0:10]


# In[773]:


batsmen(icc_mens_batsmen)


# In[774]:


icc_mens_bowler = topic('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling')


# In[775]:


def bowler(men):
    player,team,rating = [],[],[]
    for i in icc_mens_bowler.findAll(class_ = ['rankings-block__banner--name-large','table-body__cell rankings-table__name name']):
        player.append((i).text.strip())
        
    for j in icc_mens_bowler.findAll(class_ = ['rankings-block__banner--nationality','table-body__logo-text']):
        team.append((j).text.strip())
    
    for k in icc_mens_bowler.findAll(class_ = ['rankings-block__banner--rating','table-body__cell rating']):
        rating.append((k).text.strip())
    
    
    import pandas as pd
    ind = list(range(1,50,1))
    
    df = pd.DataFrame(list(zip(player,team,rating)),columns=['Bowler','Team','Rating'])
    df.index = [x for x in range(1, len(df.values)+1)]
    return df[0:10]


# In[776]:


bowler(icc_mens_bowler)


# 6) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
# a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
# b) Top 10 women’s ODI Batting players along with the records of their team and rating.
# c) Top 10 women’s ODI all-rounder along with the records of their team and rating.

# In[777]:


icc_women_team = topic('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')


# In[778]:


def team(women):
    team, matches,rating = [],[],[]
    for i in icc_women_team.find_all('span',class_='u-hide-phablet'):
        if i.text!='':
            team.append((i).text.strip())
        
    for j in icc_women_team.find_all('td',{'class': ['rankings-block__banner--points','table-body__cell u-center-text']}):
        matches.append((j).text)
    points = matches[0::2]
    
    for k in icc_women_team.find_all('td',{'class': ['rankings-block__banner--rating u-text-right','table-body__cell u-center-text']}):
        rating.append((k).text.strip())
    
    
    import pandas as pd
    ind = list(range(1,50,1))
    
    df = pd.DataFrame(list(zip(team,points,rating)),columns=['Team','Points','Rating'])
    df.index = [x for x in range(1, len(df.values)+1)]
    return df[0:10]


# In[779]:


team(icc_women_team)


# In[780]:


icc_women_batswomen = topic('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting')


# In[781]:


def batswomen(women):
    player,team,rating = [],[],[]
    for i in icc_women_batswomen.findAll(class_ = ['rankings-block__banner--name-large','table-body__cell rankings-table__name name']):
        player.append((i).text.strip())
        
    for j in icc_women_batswomen.findAll(class_ = ['rankings-block__banner--nationality','table-body__logo-text']):
        team.append((j).text.strip())
    
    for k in icc_women_batswomen.findAll(class_ = ['rankings-block__banner--rating','table-body__cell rating']):
        rating.append((k).text)
    
    
    import pandas as pd
    ind = list(range(1,50,1))
    
    df = pd.DataFrame(list(zip(player,team,rating)),columns=['Player','Team','Rating'])
    df.index = [x for x in range(1, len(df.values)+1)]
    return df[0:10]


# In[782]:


batswomen(icc_women_batswomen)


# In[783]:


icc_women_bowler = topic('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/bowling')


# In[784]:


def bowler(women):
    player,team,rating = [],[],[]
    for i in icc_women_bowler.findAll(class_ = ['rankings-block__banner--name-large','table-body__cell rankings-table__name name']):
        player.append((i).text.strip())
        
    for j in icc_women_bowler.findAll(class_ = ['rankings-block__banner--nationality','table-body__logo-text']):
        team.append((j).text.strip())
    
    for k in icc_women_bowler.findAll(class_ = ['rankings-block__banner--rating','table-body__cell rating']):
        rating.append((k).text.strip())
    
    
    import pandas as pd
    ind = list(range(1,50,1))
    
    df = pd.DataFrame(list(zip(player,team,rating)),columns=['Bowler','Team','Rating'])
    df.index = [x for x in range(1, len(df.values)+1)]
    return df[0:10]


# In[785]:


bowler(icc_women_bowler)


# 7.Write a python program to scrape details of all the posts from coreyms.com. Scrape the heading, date, content
# and the code for the video from the link for the youtube video from the post.

# In[786]:


from bs4 import BeautifulSoup
import requests

page = 1
while page != 18:
    url = f"https://coreyms.com/page/{page}"
    print(url)
    page = page + 1

    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')

    for i in soup.find_all('article'):
        Heading = i.h2.a.text
        print('\033[1m'+Heading+'\033[0m')

        Description = i.find('div', class_='entry-content').p.text
        print(Description)

        try:
            Total_youtube_link = i.find('iframe', class_='youtube-player')['src']

            Youtube_id = Total_youtube_link.split('/')[4]
            Video_id = Youtube_id.split('?')[0]

            Youtube_Page_ID = f'https://youtube.com/watch?v={Video_id}'
        except Exception as e:
            Youtube_Page_ID = None

        print(Youtube_Page_ID)

        print()


# 8.Write a python program to scrape house details from mentioned URL. It should include house title, location, area, EMI and price from https://www.nobroker.in/ .Enter three localities which are Indira Nagar, Jayanagar, Rajaji Nagar

# In[816]:


Nobroker = topic('https://www.nobroker.in/property/sale/bangalore/multiple?searchParam=W3sibGF0IjoxMi45NzgzNjkyLCJsb24iOjc3LjY0MDgzNTYsInBsYWNlSWQiOiJDaElKa1FOM0dLUVdyanNSTmhCUUpyaEdEN1UiLCJwbGFjZU5hbWUiOiJJbmRpcmFuYWdhciIsInNob3dNYXAiOmZhbHNlfSx7ImxhdCI6MTIuOTMwNzczNSwibG9uIjo3Ny41ODM4MzAyLCJwbGFjZUlkIjoiQ2hJSjJkZGxaNWdWcmpzUmgxQk9BYWYtb3JzIiwicGxhY2VOYW1lIjoiSmF5YW5hZ2FyIiwic2hvd01hcCI6ZmFsc2V9LHsibGF0IjoxMi45OTgxNzMyLCJsb24iOjc3LjU1MzA0NDU5OTk5OTk5LCJwbGFjZUlkIjoiQ2hJSnhmVzREUE05cmpzUktzTlRHLTVwX1FRIiwicGxhY2VOYW1lIjoiUmFqYWppbmFnYXIiLCJzaG93TWFwIjpmYWxzZX1d&radius=2.0&city=bangalore&locality[0]=Indiranagar,&locality[1]=Jayanagar,&locality[2]=Rajajinagar')


# In[817]:


def house(new):
    Name = []
    for i in Nobroker.find_all('span',class_='overflow-hidden overflow-ellipsis whitespace-nowrap max-w-80pe po:max-w-full'):
        Name.append((i.text))
    Ren = []
    for i in Nobroker.find_all('div',class_='font-semi-bold heading-6'):
        Ren.append((i).text)
    Price = [x.replace('â\x82¹', '') for x in Ren]
    Cost_of_House = Price[2::3]
    EMI = Price[1::3]
    Area = Price[0::3]
    Locality = []
    for i in Nobroker.find_all('div',class_='mt-0.5p overflow-hidden overflow-ellipsis whitespace-nowrap max-w-70 text-gray-light leading-4 po:mb-0 po:max-w-95'):
        Locality.append((i.text))
    Address = [x.replace('Â\xa0', '') for x in Locality]
    import pandas as pd


    df = pd.DataFrame(list(zip(Name,Cost_of_House,EMI,Area,Locality)),columns=['Name','Cost_of_House','EMI','Area','Locality'])
    df.index = [x for x in range(1, len(df.values)+1)]
    return(df)


# In[818]:


house(Nobroker)


# 9.Write a python program to scrape mentioned details from dineout.co.in :
# i) Restaurant name
# ii) Cuisine
# iii) Location
# iv) Ratings
# v) Image URL

# In[787]:


Food = topic('https://www.dineout.co.in/delhi-restaurants/buffet-special')


# In[788]:


def Dineout(Night):    
    name,Cuisine,Price,Dish = [],[],[],[]
    for i in Food.find_all('div',class_='restnt-info cursor'):
        name.append(i.find('a').text)
    import re

    for j in Food.find_all('span',class_='double-line-ellipsis'):
        Cuisine.append(j.text.split('|'))

    for i in range(13):
        Price.append(Cuisine[i][0])

    for i in range(13):
        Dish.append(Cuisine[i][1])


    import pandas as pd
    ind = list(range(1,50,1))

    df = pd.DataFrame(list(zip(name,Dish,Price)),columns=['Name of the Restaurant','Dish','Price'])
    df.index = [x for x in range(1, len(df.values)+1)]
    return df


# In[789]:


Dineout(Food)


# 10.Write a python program to scrape first 10 product details which include product name , price , Image URL from https://www.bewakoof.com/women-tshirts?ga_q=tshirts .

# In[813]:


Bewakoof = topic('https://www.bewakoof.com/women-printed-t-shirts')


# In[814]:


def women(ladies):    
    Shirt = Bewakoof.find_all('div',class_='plp-product-card')
    Original_Price,Dress = [],[]

    for i in Shirt:
        Original_Price.append(i)
    Price = []
    for j in range(10):
        Price.append((Original_Price[j].b.text))

    for i in Bewakoof.find_all('h3'):
        Dress.append(i.text)
    url = []
    for i in range(10):
        url.append(Shirt[i].find('img',alt=True)['src'])
    import pandas as pd


    df = pd.DataFrame(list(zip(Dress,Price,url)),columns=['Dress','Price','URL'])
    df.index = [x for x in range(1, len(df.values)+1)]
    return(df)


# In[819]:


women(Bewakoof)


# In[ ]:




