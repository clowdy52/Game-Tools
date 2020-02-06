
name=["p1","p2","p3"]
score=[0,0,0]

def info():
    global name
    print("three player:",name[0],",",name[1],",",name[2])
    print("=======================")
    print("r to rewrite player name, c to clear, s to show score-table, q to quit.")

def show_score():
    global name,score
    print("       | ",name[0],"\t| ",name[1],"\t| ",name[2])
    print("-------|--------|-------|--------")
    print(" score | ",score[0],"\t| ",score[1],"\t| ",score[2])

info()
while True:
    c=input("")
    if c=="s":
        show_score()
    elif c=="r":
        name[0]=input("player1:")
        name[1]=input("player2:")
        name[2]=input("player3:")
        info()
    elif c=="c":
        score=[0,0,0]
    elif c=="q":
        break
    elif c.split()[0] in name:
        n,s,p=c.split()     # s>0地主胜 s<0地主败
        ss=int(s)*(2**int(p))
        for i in range(3):
            if n==name[i]:
                score[i]+=ss*2
            else:
                score[i]-=ss
        show_score()
    else:
        print("error input")
