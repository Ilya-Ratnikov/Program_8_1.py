def qwerty(a):
    s = [ "0","I","Z","E","!","S","b","J","#","P"]
    if a>0:
        print(s[a%10],end="")
        qwerty(a//10)
a = input()
a=int(a+a[0])
qwerty(a)

