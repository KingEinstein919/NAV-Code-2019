import random

def caller (wifi):
    dic={}
    if wifi == 0:
        dic = {"Casino":random.randrange(0, 100), "Bar":random.randrange(0, 100),"Pool":random.randrange(0, 100)}
    elif wifi == 1:
        dic = {"Bar":random.randrange(0, 100), "Pool":random.randrange(0, 100),"Theater":random.randrange(0, 100)}
    elif wifi == 2:
        dic = {"Pool":random.randrange(0, 100), "Theater":random.randrange(0, 100),"Library":random.randrange(0, 100)}

    return (dic)

amey_in = random.randrange(0,2)

ans = caller(amey_in)

loc = list(ans.keys())

per = list(ans.values())

print ('loc ',loc)

print ('per ',per)
