# The First  Idea  
#about Rings  

# For  EX    
#  We  have  a  lot  of  
# customer phone  numbers  
#  and  we wanna send  SMS  
# adout  the autumn discount 
list1 =  {'093600','0922','12122'}

# if  you  want  use  Timer ====>> 
#  you  can  use the  while 

#  FOR  ======>>>
#  We  have  a  list  with  10 items  
#  and  we  wanna print  these  items
from  colorama import Fore,Style,init
import time  
init ()
list1 =  {'093600','0922','12122','0981234','090876','098711111','10239323','555111','77771112','1212133124355768','576073456'}  
print(len(list1)) 

for  i  in  list1:  
    print(Fore.CYAN+str(i))
    time.sleep(0.5)
    
mytext =  "Coda"
for i in mytext :
       print(Fore.MAGENTA+str(i))
       time.sleep(0.5)
       
       
# We  can  use   best    in  circels  
# for  ex  if  we  wanna  send SMS   bombs,
# we  use  loops,  but  we need  to  be  able  to  put  conditions  inside  the  loops 
# so  that  if an  SMS   wasn't  sent  to  a  cartain  number  and we  got  blacklisted  
#  it  tells  us  "i  couldn't send  to  this  number "


##USE  IF  in the  FOR    loop  

for i  in  list1:
    if i ==  '093600':
       print(Fore.WHITE+"True:"+str(i))
       time.sleep(0.5)
       
       
# in  the  loop  above  ,  the  condition gets checked 
# but  the  loop  isn't  finished  yet  
# there  are  still  other  items (len) left  
# since  we  didn't  use  break  
# the  program  goes  back  to  yhe  top  of  the  loop and  checks 
#  the  next  item  
#THIS  KEEPS  happening  until the  last  item  
       
   
#**  if  we  print i  ,  the loop  ends .
for i  in  list1:
    if i ==  '093600':
       print(Fore.WHITE+"True:"+str(i))
       time.sleep(0.5)
    print(Fore.CYAN+str(i))    
   
# **  if  we  want to  end the  loop without using   print (i) =====>>>>>
for i  in  list1:
    if i ==  '093600':
       print(Fore.WHITE+"True:"+str(i))
       time.sleep(0.5)
       break         
       
       
##solve  a  face  to  face     challenge in the  for  loop  for  beginners
#  **  if  insted  of  print(i) we  use  print(list1) here's what happens?????======>>>
#** it  prints  the  values  inside  the  list  over  and  over  again  .
#for  i  in  list1:
    # print(list1)      
    
    
    
## The  best  way  to  use  loops  ====>> we can use range
#*NUM  PRINS  NUMBER  FOR  EACH  ITEM IN  THE  LIST  
num=1
for  i  in  list1:
    print(num)
    num+=1  
    
for i in range(12):
    print(Fore.YELLOW+str(i))        


for i in range(100,112):
    print(Fore.BLUE+str(i))        
  
# Use  correct  of End  loop 
# for  ex  if  you  want  to  execute the following  command (First  method ) 
#  it  is  enough to  use  the  second method 
# as  result  "END  LOOP" ===>> USE  "else"  

# First  method====>>
val =""
for  i  in  list1:
    print(i)
    if i ==  "090876":
        val= "no"
        break
    else :
        val = "yes"
if  val  == "yes":
    print("End  loop ")
elif val == "no":
    pass    
# secend  method  =====>>>  
for  i  in  list1:
    print(i)
else:
    print("End  loop ")                               