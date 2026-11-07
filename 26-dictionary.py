# dict 
# for  ex  i  have  a list   phone  number  
#and  i wnat  send  SMS    and  say  happy persion new year  
#but among  the  number  ,  there  are  also  french  numbers  
#As  result  ,  we  can fix  this  issus  with  the  help of  dictionaries  


# the  first  method(With out  dictionaries) 
# this  method  for  a  few  user  is  ok  but  when  we  have  a  lot  of  user  the  secend  method  is  good  
from  colorama import Fore,Style,init
import time  
init ()
mylist = ["ALI","FARHAD","JACK","LOCI"]
if  mylist[0] ==  "ALI" and  mylist[1] == "FARHAD" :  
    time.sleep(0.5) 
    print(Fore.GREEN+"Happy  new year")  
    
    
# The  secend  method (with dict) 
# dictionaries  has  two  items   first is  key  &  secend  is  value  
mydict = {"Key":"Value"}
print(Fore.BLUE+str(mydict))
print(type(mydict))
# when we  use  list  and  say  s.th[0] ==>>  print(s.th[0])  
# but  in  dict we  say  s.th["KEY"] ===>>  print for  me  value     
mydictionarie = {"CODA":"UODA"}
print(Fore.YELLOW+str(mydictionarie["CODA"]))
# New  ex  of  dict 
newdict =  {"1st groupe":["Ali","Amir","Ahmad"],"2nd groupe":("mona",)}
print(Fore.WHITE+str(newdict["1st groupe"]))
print(Fore.WHITE+str(newdict["2nd groupe"]))

# pro ex  
time.sleep(0.5)
info_name = input(Fore.RED+"[+]"+Fore.GREEN+"Enter your name :\n")
time.sleep(0.5)
info_phone= input (Fore.RED+"[+]"+Fore.GREEN+"Enter your mobail  phone :\n")
time.sleep(0.5)
info_job = input(Fore.RED+"[+]"+Fore.GREEN+"what  is  your  job  :\n")
time.sleep(0.5)
info_age = input(Fore.RED+"[+]"+Fore.GREEN+"How  old  are  you  :\n")
ex_dict =  {"1st DATA":"info_name","2nd DATA":"info_phone","3th DATA":"info_job","4th DATA":"info_age"}
if ex_dict ["1st DATA"] or ex_dict["2nd DATA"] or ex_dict["3th DATA"] or ex_dict["4th DATA"]:
    print(Fore.MAGENTA+"Hi")
if ex_dict["3th DATA"] == "Programmer" or "I don't have  job ": 
    print(Fore.MAGENTA+" we  can be good  frinds  to each other ")
    
    
# Acces items with in the dict (key, value,get,.....)   
# we  have  a  lot  of  method  for  print dict 
minidict = {"Uoda":994453}
print(minidict["Uoda"]) 
print(minidict.get("Uoda"))
# show  keys =====>>>>>>
print(Fore.CYAN+str(minidict.keys()))
# show value  ======>>>>
print(minidict.values())    
#can we  cansider  every data for the  key  (int,str,....)
#int &  float  &  bool 
# WE  CAN'T  USE  DICT  &  LIST  & SET  FOR  DATA  THE  KEY  
mydicter =  {
    1:"set"
    ,15.5:"Exam score"
    ,True:"PASS"
            }
print(Fore.WHITE+str(mydicter.get(1)))
print(Fore.WHITE+str(mydicter[15.5]))
print(Fore.WHITE+str(mydicter[True]))

##use  the  dict in the  real prj
# we  have  prj  that  name  is  strom breaker  
# this  prj  with  sending  link/link web sit  to  the  user  
# and the  end  hacking  her/him  user 
# as  resulat  we  use  dict for    send user informatio to  hacker/admin  
# python we say dictionarie    &  in   javascript  say  object
# strom brekear  ==== >>>  we  make  first  level  link with  java  
#  &  send  information  secend  level  with  PHP  
#  and  the  end  show  with  python  
# in  javascript  we  have  jeson.loads 
#  and  to  convert  javascrept  object  to  python  dictionaries 

# # # import  requests
# # # info =  {"Username":"admin",
# # #          "password":"admin",
# # #         "sub":""
# # #          }
# # # https =  requests.post("https://tryhackme.com/",data=info).content
# # # http =  requests.post("https://tryhackme.com/",data=info).text
# # # print(https)
# # # time.sleep(0.9)
###  print(http)



# import json
# myprj =  open("aa.json").read()
# data = json.loads(myprj)
# print(data.key())
# print(data.values())
 
## modify  &  add  items  in the  dictionry  
 
wwplc =  {"Username":"Coda","lastname":"Uoda"}
wwplc["Username"] = 'UBADE'

wwplc.update({"Username":"ZERO"})
wwplc.update({"Username1":"ZERO1"})
print(Fore.MAGENTA+str(wwplc))
 
    
    
# mini  prj 
#  for  ex  i want  right  malicius softeare(bad afzar)
#  as  resulat  if  i  send  user  and  user  install  my  malicius softeare(bad afzar)  
# send  me  a  massege  that  user  has  installed  this  on  thire phone  
#  and  the  end  send  me  the  user's  information  

import  platform  
import  requests
import  time
import  getpass
osname =  platform.uname()[0]
#  if  the  user  change  ip  or  use  VPN   
# we can  find  real  location  of  time  desktop  or  phone  
#  real  time  for  ex  iran 
# time_zone = time.tzname
# print(Fore.LIGHTBLUE_EX+str(time_zone))
# #  if  you  want  see  your  ip  
# #  serch  api.ipify.org(https://api64.ipify.org?format=json'
# #"ip":"2a01:5ec0:e804:1482:e9ea:d500:ab9a:d135")
# ## ip =  requests.get('https://api.ipify.org').text
# # #print(f"Your  public ip  is  : {ip}")



#get  your  city 
# with dict   
# import  whereismyip
# location = whereismyip.whereismyip()
# print(location)
# info = whereismyip.whereismyip_dict()
# print(info.get('city'))
# print(info.get('region'))
# print(info.get('country'))


#get Exact location 
from  ipspot import  get_public_ipv4 , IPv4API
data_ip = get_public_ipv4(api=IPv4API.IP_API_COM,geo=True,timeout=10)
if data_ip['status']:
    info = data_ip['data']
    print(f"city:{info.get('city')}")
    print(f"region:{info.get('region')}")
 

    print(f"city:{info.get('latitude')},{info.get('longitude')}")
    # when  your  internt  not  connect  ======>>>>> is  else  : 
else :  
    print("NOT AT ALL  ")    

   

#   Delet  items with  in the  dict
mytrs =  {"Iran":"Persion","opnion":"culture"}
mytrs.pop("opnion")
print(Fore.RED+str(mytrs))
mytrs.popitem
print(Fore.RED+str(mytrs))
mytrs.popitem
mytrs.popitem

print(Fore.RED+str(mytrs))
# method  clear  is  clear  any  items  in  your  dict  
mytrs.clear()
print(Fore.RED+str(mytrs))



#  we  have  del  like  delet  
# a = {"amin":"amiri"}
# #  when  we  say  del is   a  like  delet  a so  if  you  print  a  say  not  found  
# del a

# print(a)

b =  {"AAAA":"BBBBB","CCCCC":"DDDDDD"}
del b["AAAA"]
print (b)

# better proces sing  on  dict
mykey =  {"ali":"amin",2027:"the  End  of  any  WAR "}
# if  you  want   just  print  value  we use itmes() method   
for   method1  in mykey.values():
    time.sleep(0.5)
    print(Fore.BLUE+str("[+]")+Fore.GREEN+str("First method :")+Fore.YELLOW+str(method1))
#  if  you  want just  print   key we use itmes() method 
time.sleep(0.5)
for  method2 in mykey:
    print(Fore.BLUE+str("[+]")+Fore.GREEN+str("second method :")+Fore.YELLOW+str(method2))    

# if  you  want  print  value  &  key we use itmes() method   
time.sleep(0.5) 
for method3 in mykey.items():
    print(Fore.BLUE+str("[+]")+Fore.GREEN+str("third method :")+Fore.YELLOW+str(method3))
    
#if  we  want  print  value  &  key  in  one  line  
time.sleep(0.5) 
for key, value in  mykey.items():
    print (f"{key}:{value}",end=" | ")
print()    
# so  we  can use  str  methods  for  change  some  things 
time.sleep(0.5)
import platform
dictname =  platform.system().title().replace("Windows","correct operating system").upper()
print(Fore.MAGENTA+str(dictname))
# asdict  ======>>>  we  can  make  dict  
listname =  platform.uname()
dictnames =list( listname._asdict().items())[0]
print(dictnames) 
#  copy  dict
#  WHEN  YOU wanna  make  new  dict  of  old  dict  
#  but  you  dont  want  chang  old  dict  when you add  a  new  kays  on  new dict  
#  we  can  use  copy  dict
Ndict = {1:"First",2:"Second"} 
Mdict = Ndict.copy()
Mdict.update({"3":"Third"})
print(Ndict)
print(Mdict)
# option  IP    information  
# we  have  websit  is  ipapi.co
# we  can  chech  User ip  for   collecting information  
import  ipapi
#  for  use method  location  we  must    use  of  STR
# BUT    out  put  is  DICT  
# data  =  ipapi.location("Your  ip ")
# print(type(data))




##work  with  nested dict  
import platform
import requests

hs_name = platform.uname()[0]
hs_ver = platform.uname()[2]
architecutre = platform.uname()[4]


hs_ip = requests.get("https://api.ipify.org").text


response = requests.get(f"http://ip-api.com/json/{hs_ip}")
ip_info = response.json()

ip_city = ip_info['city']
ip_country = ip_info['country']

datahs = {
    # we have 2 keys and it keys have 2 values that dict 
    "hs_info": {
        "hs_name": hs_name,
        "hs_version": hs_ver,
        "architecutr": architecutre
    },
    
    "ip-info": {
        "ip": hs_ip,
        "city": ip_city,
        "country": ip_country
    },
    "names":[
            "coda",'uoda',
        ]
    
}


print(datahs['hs_info'])
print(datahs["ip-info"])
print(datahs["ip-info"]['ip'])
print(datahs)
print(datahs["names"][0])
# better  undrestanding of  nested dict 
