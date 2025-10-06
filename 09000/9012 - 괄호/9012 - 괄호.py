# BOJ 9012 - 괄호
def RemoveBrackets(strParam):
    op = 0
    sm = 0
    for c in strParam:
        if c == "(":
            op += 1
        elif c == ")":
            if op >= 1:
                op -= 1
            else:
                sm += 1
    if sm + op == 0:
        return "YES"
    else:
        return "NO"


for i in range(int(input())):
    print(RemoveBrackets(input()))
