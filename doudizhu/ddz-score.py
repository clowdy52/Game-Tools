import time

name=["p1","p2","p3"]
score=[0,0,0]
history=[]

def info():
    global name
    print("three player:",name[0],",",name[1],",",name[2])
    print("=======================")
    print("r to rewrite player name, c to clear, s to show score-table, i to init score-table,")
    print("p to print score to text, h to show help, q to quit.")
    print("usage: <player_name> <basic_score> [<bomb>] <win(1)/lose(0)>")

def show_score():
    global name,score
    print("       | ",name[0],"\t| ",name[1],"\t| ",name[2])
    print("-------|--------|-------|--------")
    print(" score | ",score[0],"\t| ",score[1],"\t| ",score[2])

def show_all():
    global name,score,history
    print("       | ",name[0],"\t| ",name[1],"\t| ",name[2])
    if len(history):
        print("-------|--------|-------|--------")
    for sc in history:
        print("       |  {0}\t|  {1}\t|  {2}".format(sc[0],sc[1],sc[2]))
    print("-------|--------|-------|--------")
    print(" score | ",score[0],"\t| ",score[1],"\t| ",score[2])

info()
while True:
    c=input("")
    if c=="s":
        show_all()
    elif c=="r":
        name[0]=input("player1:")
        name[1]=input("player2:")
        name[2]=input("player3:")
        info()
    elif c=="c":
        score=[0,0,0]
        history=[]
    elif c=="q":
        break
    elif c=='h':
        info()
    elif c=='p':
        fname = "{0}.txt".format(time.strftime("%Y%m%d-%H:%M:%S",time.localtime()))
        with open(fname,'w') as f:
            f.write("       | {0}\t| {1}\t| {2}\n".format(name[0],name[1],name[2]))
            if len(history):
                f.write("-------|------|------|--------\n")
            for sc in history:
                f.write("       | {0}\t| {1}\t| {2}\n".format(sc[0],sc[1],sc[2]))
            f.write("-------|------|------|--------\n")
            f.write(" score | {0}\t| {1}\t| {2}\n".format(score[0],score[1],score[2]))
        print("score is written to {0}".format(fname))
    elif c=="i":
        try:
            init_score=[int(input("{0} 's score: ".format(name[i]))) for i in range(3)]
        except ValueError:
            print("input error")
            continue
        history=[[init_score[0],init_score[1],init_score[2]]]
        score=init_score
        show_score()
        # n test
    elif c.split()[0] in name and 3 <= len(c.split()) <= 4:
        sp=c.split()
        if len(sp) == 3:
            n,s,w = sp
            p='0'
        else:
            n,s,p,w = sp
        # s,p test
        if not s.isdigit() or not p.isdigit():
            print("error input")
            continue
        # w test
        if w=='win' or w=='1':
            ss=int(s)*(2**int(p))
        elif w=='lose' or w=='0':
            ss=-int(s)*(2**int(p))
        else:
            print("error input")
            continue
        # score cacul & storage
        pl=[0,0,0]
        for i in range(3):
            if n==name[i]:
                pl[i]=ss*2
            else:
                pl[i]=-ss
        score=[score[i]+pl[i] for i in range(3)]
        history.append(pl)
        show_score()
    else:
        print("error input")
