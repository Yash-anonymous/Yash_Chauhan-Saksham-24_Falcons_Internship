from tabulate import tabulate as t

from matplotlib import pyplot as plt

def points(win,draw):
    return win*2+draw

def nrr1(runs,overs,oruns,oovers):
    ans=(runs/overs)-(oruns/oovers)
    ref=ans
    return ref

def fill():
    matches=int(input("Enter the number of matches:"))
    win=int(input("Enter the number of wins:"))
    loss=int(input("Enter the number of loss:"))
    draw=int(input("Enter the number of draw:"))
    runs=int(input("Enter the runs scored:"))
    overs=float(input("Enter the overs played:"))
    oruns=int(input("Enter the opposition runs:"))
    oovers=float(input("Enter the overs played by opposition:"))
    nrr1(runs,overs,oruns,oovers)
    tournament_data(t_name,matches,win,loss,draw,nrr1(runs,overs,oruns,oovers))
    d1=["Win","Loss","Draw"]
    d2=[win/matches,loss/matches,draw/matches]
    plt.pie(d2,labels=d1,autopct='%0.1f%%')
    plt.show()

def tournament_data(t_name,matches,win,loss,draw,nrr):
    data=[]
    data=[[t_name,matches,win,loss,draw,points(win,draw),nrr]]
    if win==1:
        win+=1
    if loss==1:
        loss+=1
    if draw==1:
        draw+=1
    head=["Team","Matches","Wins","Losses","Draw","Points","NRR"]
    print(t(data,headers=head,tablefmt="grid"))

team_name=["INDIA","AUSTRAILIA","NEW ZELAND","SOUTH AFRICA","ENGLAND","PAKISTAN","WEST INDIES","SRI LANKA"]
print(team_name)
t_name=input("Enter a Team Name[In capital]:")
x=len(team_name)
for i in range(x):
    if t_name==team_name[i]:
        fill()
    else:
        i+=1