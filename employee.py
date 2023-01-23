def Input(D):
    print("Enter * when u want to exit")
    K=0
    while K!='*':
        K=input("Enter The Name of the employee ").upper()
        if K=='*':
            break
        V=int(input("Enter his phone Number"))
        D[K]=V
X={}
Input(X)

def Sort(SD):
    S_D={}
    k=list(SD.keys())
    k.sort()
    for i in k:
        S_D[i]=SD[i]
    return S_D

X=Sort(X)
print(X)
