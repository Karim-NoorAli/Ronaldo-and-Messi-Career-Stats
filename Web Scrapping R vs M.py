"""
@author: Karim Noor Ali
"""


from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import numpy as np
import pandas as pd
from openpyxl import load_workbook

my_url = 'http://messivsronaldo.net/all-time-stats/'
uclient = uReq(my_url)
page_html = uclient.read()
uclient.close()

page_soup = soup(page_html,"html.parser")
page_soup.h1


#**************************Importing Ronaldo's Stats HTML************************************* 
R_con = page_soup.findAll("ul",{"class":"ronaldo stats"})
len(R_con)

#**************************Importing Messi's Stats HTML*************************************
M_con = page_soup.findAll("ul",{"class":"messi stats"})
len(M_con)


#**************************Accessing Competitions Names***************************************
labels = page_soup.findAll("h3",{"class":"middle-text"})
labels[0].text

#******Assigning Ronaldo's Specs to it's respective variables****************************
i = 0
R_goal=[]
R_label=[]
R_Assists =[]
R_Apps =[]
R_Penalties =[]
R_Missed=[]
R_Hattricks=[]
R_GoalRatio=[]

for con in R_con:
    R_goals_labels = labels[i].text
    R_goals = con.li.span.text
    Assists = con.find("li",{"class":"assists"}).text
    R_assist,garbage = Assists.split(" ")
    apps = con.find("li",{"class":"apps"}).text
    R_app,garbage2 =  apps.split(" ",1)
    R_app = R_app.replace("\n","")
    penalty = con.find("ul",{"class":"extras"}).span.text
    missed = con.find("ul",{"class":"extras"}).li.small.text
    R_miss,garbage3 =  missed.split(" ")
    R_miss = R_miss.replace("(","")
    hattrick = con.find("ul",{"class":"extras"}).li.find_next_sibling('li')
    hattricks = hattrick.text
    hattricks,garbage4 = hattricks.split(" ",1)
    Ratio = hattrick.find_next_sibling('li').text
    Ratio,garbage5 = Ratio.split(" ",1)
    i+=1
    R_GoalRatio.append(Ratio)
    R_Hattricks.append(hattricks)
    R_Missed.append(R_miss)
    R_Penalties.append(penalty)
    R_Apps.append(R_app)
    R_Assists.append(R_assist)
    R_goal.append(R_goals)
    R_label.append(R_goals_labels)

#*************1 Value have * in it, You can remove it manually then attemp this unless no need ****** 
#*************************Converting into int and float respectively*********************************    
R_goal = list(map(int, R_goal))    
R_Assists = list(map(int, R_Assists))
R_Apps = list(map(int, R_Apps))  
R_Penalties = list(map(int, R_Penalties)) 
R_Missed = list(map(int, R_Missed))
R_GoalRatio = list(map(float, R_GoalRatio))
R_Hattricks = list(map(int, R_Hattricks))

#******Assigning Messi's Specs to it's respective variables****************************
j = 0
M_goal=[]
M_label=[]
M_Assists =[]
M_Apps =[]
M_Penalties =[]
M_Missed=[]
M_Hattricks=[]
M_GoalRatio=[]

for con in M_con:
    M_goals_labels = labels[j].text
    M_goals = con.li.span.text
    Assists = con.find("li",{"class":"assists"}).text
    M_assist,garbage = Assists.split(" ")
    apps = con.find("li",{"class":"apps"}).text
    M_app,garbage2 =  apps.split(" ",1)
    M_app = M_app.replace("\n","")
    penalty = con.find("ul",{"class":"extras"}).span.text
    missed = con.find("ul",{"class":"extras"}).li.small.text
    M_miss,garbage3 =  missed.split(" ")
    M_miss = M_miss.replace("(","")
    hattrick = con.find("ul",{"class":"extras"}).li.find_next_sibling('li')
    hattricks = hattrick.text
    hattricks,garbage4 = hattricks.split(" ",1)
    Ratio = hattrick.find_next_sibling('li').text
    Ratio,garbage5 = Ratio.split(" ",1)
    j+=1
    M_GoalRatio.append(Ratio)
    M_Hattricks.append(hattricks)
    M_Missed.append(M_miss)
    M_Penalties.append(penalty)
    M_Apps.append(M_app)
    M_Assists.append(M_assist)
    M_goal.append(M_goals)
    M_label.append(M_goals_labels)

#*************************Converting into int and float respectively*********************************
M_goal = list(map(int, M_goal)) 
M_Assists = list(map(int, M_Assists))
M_Apps = list(map(int, M_Apps))
M_Penalties = list(map(int, M_Penalties)) 
M_Missed = list(map(int, M_Missed))
M_GoalRatio = list(map(float, M_GoalRatio))
M_Hattricks = list(map(int, M_Hattricks))


#*****************Combining all in a data frame***********************************************
df = pd.DataFrame({'Competition':R_label,'Caps':R_Apps,'Goals':R_goal,'Penalties':R_Penalties,'Missed':R_Missed,'Assists':R_Assists,'Hat-tricks':R_Hattricks,'Goal Ratio':R_GoalRatio})
df2 = pd.DataFrame({'Competition':M_label,'Caps':M_Apps,'Goals':M_goal,'Penalties':M_Penalties,'Missed':M_Missed,'Assists':M_Assists,'Hat-tricks':M_Hattricks,'Goal Ratio':M_GoalRatio})

#*********************Exporting to Excel*******************************************************
df.to_excel('D:\Ronaldo Stats.xlsx', sheet_name='Ronaldo Stats',columns=['Competition','Caps','Goals','Penalties','Missed','Assists','Hat-tricks','Goal Ratio'],index=False)
df2.to_excel('D:\Messi Stats.xlsx',columns=['Competition','Caps','Goals','Penalties','Missed','Assists','Hat-tricks','Goal Ratio'], sheet_name='Messi Stats',index=False)

