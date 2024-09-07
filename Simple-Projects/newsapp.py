from newsapi import NewsApiClient
import pycountry

#init
key="your-api-key"
newsapi=NewsApiClient(api_key=key)

def countryavail():
    countries=list(pycountry.countries)
    countryposs=['ae', 'ar', 'at', 'au', 'be', 'bg', 'br', 'ca', 'ch', 'cn', 'co', 'cu', 'cz', 'de', 'eg', 'fr', 'gb', 'gr', 'hk', 'hu', 'id', 'ie', 'il', 'in', 'it', 'jp', 'kr', 'lt', 'lv', 'ma', 'mx', 'my', 'ng', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ro', 'rs', 'ru', 'sa', 'se', 'sg', 'si', 'sk', 'th', 'tr', 'tw', 'ua', 'us', 've', 'za']
    countrylist=[]
    for countryobj in countries:
        if countryobj.alpha_2.lower() in countryposs:
            countrylist.append(countryobj)
            print(countryobj.name, countryobj.flag)
            
    return countrylist        
	
def languageavail():
    languages=list(pycountry.languages)
    languageposs=['ar', 'de', 'en', 'es', 'fr', 'he', 'it', 'nl', 'no', 'pt', 'ru', 'sv', 'ud', 'zh']
    languagelist=[]
    for languageobj in languages:
        if hasattr(languageobj, 'alpha_2') and languageobj.alpha_2 in languageposs:
            languagelist.append(languageobj)
            print(languageobj.name)
            
    return languagelist    
    
def countryinput(countries):
	countryinput=input("Enter Country name: ").lower()
	for countryobj in countries:
		if countryobj.name.lower()==countryinput:
			return countryobj
	else:
		return None
	
def languageinput(languages):
	languageinput=input("Enter Language: ").lower()
	for languageobj in languages:
		if languageobj.name.lower()==languageinput:
			return languageobj
	else:
		return None
    
def categoryinput():
    categorylist=["Business", "Entertainment", "General", "Health", "Science", "Sports" "Technology"]
    print("Categories:")
    for category in categorylist:
        print(category)
    
    categoryname=input("Enter Category: ")
    if categoryname in categorylist:
        return categoryname
    else:
        return None    

languagelist=languageavail()
language=languageinput(languagelist)

countrylist=countryavail()
country=countryinput(countrylist)

categoryname="General"

def topheadlines(categoryname, language, country):
    #/top-headlines
    print("\nTop Headlines:\n")
    top_headlines = newsapi.get_top_headlines(
        category=categoryname.lower(),
        language=language.lower(),
        country=country.lower())
        
    return top_headlines["articles"]
        
# /v2/top-headlines/sources
sources = newsapi.get_sources()

def printheadlines(headlines):
    for i,headline in enumerate(top_headlines):
        print(f"{i+1}. {headline['title']}")
	
top_headlines=topheadlines(categoryname, language.alpha_2, country.alpha_2)
printheadlines(top_headlines)

def printnews(article):
    print(article['title'])
    print(f"by {article['author']}")
    source=article['source']['name']
    pubTime=article['publishedAt']
    print(f"{source} | {pubTime}")
    print(article['description'])
    print(article['content'])
    
    newsurl=article['url']
    print(f"Url: {newsurl}")
    imageurl=article['urlToImage']
    print(f"{imageurl}")
    
    
num=int(input("Enter Headline number to read full article: "))    
printnews(top_headlines[num-1])
