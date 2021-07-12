from bs4 import BeautifulSoup
import requests

url=["https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=28489"] #,'https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=28489']
n=0
for i in range(1):
    page = requests.get(url[i])

    soup = BeautifulSoup(page.content, 'html.parser')
    Location=soup.find("span" , {'class':'ui-li-aside session_detail_location', 'style':'margin: 0px;padding: 0px;color:#666;font-size: 1.0em;'}).text
    Location = Location[0: -7:] 
    Abs_number=soup.find("div" , {'class':'sessionnumber'}).text
    Time=soup.find("div" , {'class':'session_detail_day text_bannercolor'}).text
    Date=soup.find("div" , {'class':'session_detail_day text_bannercolor','onclick':"DateTimeClicked('urn:eventpilot:all:agenda:filter:day=2019-07-15')"}).text
    Abstract_title=soup.find("li" , {'class':'session_detail_title_708','style':'padding:25px 0px 25px 0px;'}).text
    for Author in soup.find_all('h1', {"style":"margin-top:5px;margin-bottom:6px" }):
        print("author name-",Author.text)
        n=n+1
        
    Author_aff=soup.find("div",{"id":"session_detail_description","class":"detail_description"}).text     
    
    for Author_aff in soup.find_all("div",{"id":"session_detail_description","class":"detail_description" }):
        abc=Author_aff.text
    list=abc.split()    
    start = list.index("Block:")          
    list= list[start+n+1: :]
    last = list.index("ThemeDiagnosis")
    del list[last:]
    Category=soup.find("div",{"class":"filter_value bannercolor"}).text
    Sub_cat=soup.find("div",{"class":"filter","data-name":"categoryid"}).text
    Sub_cat = Sub_cat[6: :]     
    Abstract_txt=soup.find("div",{"class":"mediatextwrapper"}).text
    
    Sesssion_title=soup.find("div",{"class":"session_title list_cell_title","style":"opacity:.5;"}).text
   
    print("-------------------------------------")
    print(Location)
    print("-------------------------------------")
    print(Abs_number)
    print("-------------------------------------")
    print(Date)
    print("-------------------------------------")
    print(Time)    
    print("-------------------------------------")
    print(Abstract_title)
    print("-------------------------------------")
    print(*list)
    print("-------------------------------------")
    print("cat-",Category)
    print("-------------------------------------")
    print("sub cat-",Sub_cat)
    print("-------------------------------------")
    print("abs txt",Abstract_txt)
    print("-------------------------------------")
    print(Sesssion_title)
    print("-------------------------------------")
    print(url[i])
   