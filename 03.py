from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

url=["https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=31198"]

#["https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=28489"] #,'https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=28489']
n=0

#csvfile = open('abc.csv', 'w')
#writer = csv.writer(file)
#fieldnames=['Author', 'Location', 'Abs_number','Date','Time','Abstract_title','Category','Sub_cat','Abstract_txt','Session_title','url']
 

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
   # print(*list)
    print("-------------------------------------")
    print(Category)
    print("-------------------------------------")
    print(Sub_cat)
    print("-------------------------------------")
    print(Abstract_txt)
    print("-------------------------------------")
    print(Session_title)
    print("-------------------------------------")
    print(url[i])
    
  #  df=pd.DataFrame[ {'Author':Author, 'Location':Location,'Abs_number':Abs_number, 'Date':Date, 'Time':Time, 'Abstract_title':Abstract_title,  'Category':Category, 'Sub_cat':Sub_cat, 'Abstract_txt':Abstract_txt,'Session_title':Session_title,   'url':url[i] }   ] 

    #writer = csv.DictWriter(csvfile, fieldnames=['Author', 'Location', 'Abs_number','Date','Time','Abstract_title','Category','Sub_cat','Abstract_txt','Session_title','url'], 
     #                   extrasaction='ignore', delimiter = ';')

   # with open('abc.csv', 'w',encoding='UTF8',newline='') as f:
    #    writer=csv.DictWriter(f, fieldnames=fieldnames)
     #   writer.writeheader()
      #  writer.writerows(rows)



    #writer.writerow([Author.encode('utf-8'), Location.encode('utf-8'), Abs_number.encode('utf-8'),Date.encode('utf-8'),Time.encode('utf-8'),Abstract_title.encode('utf-8'),Category.encode('utf-8'),Abstract_txt.encode('utf-8'),Session_title.encode('utf-8'),url[i].encode('utf-8')])

   




 #   df.to_csv('products.csv', index=False, encoding='utf-8')

# write title row

 

#writer.writerow([Author.encode('utf-8'), Location.encode('utf-8'), Abs_number.encode('utf-8'),Date.encode('utf-8'),Time.encode('utf-8'),Abstract_title.encode('utf-8'),Category.encode('utf-8'),Abstract_txt.encode('utf-8'),Session_title.encode('utf-8'),url[i].encode('utf-8')])
 
#file.close()