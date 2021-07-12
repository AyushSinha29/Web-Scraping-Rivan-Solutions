from bs4 import BeautifulSoup
import requests
import csv
import random


url=["https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=28489",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=31198",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=31540",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=33318",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=34059",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=30578",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=34245",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=27848",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=28120",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=28122",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=28456",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=28496",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=28546",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=29235",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=29236",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=29273",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=29552",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=29553",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=29576",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=30105",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=30288",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=30501",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=30541",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=30764",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=30965",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=31067",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=31074",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=31098",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=31103",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=31135",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=31403",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=31426",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=31524",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=31607",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=31630",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=31837",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=31962",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=32163",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=32431",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=32530",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=32622",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=32722",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=32757",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=33185",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=33263",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=33408",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=33495",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=33860",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=33920",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=34048",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=34228",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=34349",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=34442",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=31797",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=32906",
"https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=33799"]

j=len(url)
n=0


csvFile = open('test05.csv', 'w+')
for i in range(j):
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
        
    
    Category=soup.find("div",{"class":"filter_value bannercolor"}).text
    Sub_cat=soup.find("div",{"class":"filter","data-name":"categoryid"}).text
    Sub_cat = Sub_cat[6: :]     
    Abstract_txt=soup.find("div",{"class":"mediatextwrapper"}).text
    Session_title=soup.find("div",{"class":"session_title list_cell_title","style":"opacity:.5;"}).text
   
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
    #print(*list)
    #print("-------------------------------------")
    print(Category)
    print("-------------------------------------")
    print(Sub_cat)
    print("-------------------------------------")
    print(Abstract_txt)
    print("-------------------------------------")
    print(Session_title)
    print("-------------------------------------")
    print(url[i])
    print("-------------------------------------")
    
    writer = csv.writer(csvFile)
    writer.writerow(('Author', 'Location', 'Abs_number','Date','Time','Abstract_title','Category','Sub_cat','Abstract_txt','Session_title','url'))
    for i in range(j):
        writer.writerow((Author.text.encode('utf-8'), Location.encode('utf-8'), Abs_number.encode('utf-8'),Date.encode('utf-8'),Time.encode('utf-8'),Abstract_title.encode('utf-8'),Category.encode('utf-8'),Sub_cat.encode('utf-8'),Abstract_txt.encode('utf-8'),Session_title.encode('utf-8'),url[i].encode('utf-8')))

csvFile.close()