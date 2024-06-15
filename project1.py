from tabulate import tabulate as t
win=0
loss=0
draw=0
def points(win,draw):
    return win*2+draw
def nrr1(runs,overs,oruns,oovers):
    ans=(runs/overs)-(oruns/oovers)
    ref=ans
    return ref
def tournament_data(t_name,matches,win,loss,draw,nrr):
    data=[]
    data=[[t_name,matches,win,loss,points(win,draw),nrr]]
    if win==1:
        win+=1
    if loss==1:
        loss+=1
    if draw==1:
        draw+=1
    head=["Team","Matches","Wins","Losses","Points","NRR"]
    print(t(data,headers=head,tablefmt="grid"))
def fill():
    t_name=input("Enter a Team Name[In capital]:")
    matches=int(input("Enter the number of matches:"))
    win=int(input("Enter the number of wins:"))
    loss=int(input("Enter the number of loss:"))
    draw=int(input("Enter the number of draw:"))
    if t_name=="INDIA":
        runs=int(input("Enter the runs scored:"))
        overs=float(input("Enter the overs played:"))
        oruns=int(input("Enter the opposition runs:"))
        oovers=float(input("Enter the overs played by opposition:"))
        nrr1(runs,overs,oruns,oovers)
    elif t_name=="AUSTRALIA":
        runs=int(input("Enter the runs scored:"))
        overs=float(input("Enter the overs played:"))
        oruns=int(input("Enter the opposition runs:"))
        oovers=float(input("Enter the overs played by opposition:"))
        nrr1(runs,overs,oruns,oovers)
    elif t_name=="ENGLAND":
        runs=int(input("Enter the runs scored:"))
        overs=float(input("Enter the overs played:"))
        oruns=int(input("Enter the opposition runs:"))
        oovers=float(input("Enter the overs played by opposition:"))
        nrr1(runs,overs,oruns,oovers)
    elif t_name=="NEW ZELAND":
        runs=int(input("Enter the runs scored:"))
        overs=float(input("Enter the overs played:"))
        oruns=int(input("Enter the opposition runs:"))
        oovers=float(input("Enter the overs played by opposition:"))
        nrr1(runs,overs,oruns,oovers)
    elif t_name=="SRI LANKA":
        runs=int(input("Enter the runs scored:"))
        overs=float(input("Enter the overs played:"))
        oruns=int(input("Enter the opposition runs:"))
        oovers=float(input("Enter the overs played by opposition:"))
        nrr1(runs,overs,oruns,oovers)
    tournament_data(t_name,matches,win,loss,draw,nrr1(runs,overs,oruns,oovers))

for _ in range(1):
    fill()
