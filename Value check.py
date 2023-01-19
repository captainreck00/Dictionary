x={}

def Input(D):
    print("Enter * when u want to exit")
    K=0
    while K!='*':
        K=input("Enter The Key ")
        if K=='*':
            break
        V=input("Enter The Value ") 
        D[K]=V

def Value_Check(D):
    v=input("Enter the Value you want to find ")
    if v in D.values() :
        for key in D:
            if D[key]==v:
                print("The key for the value",v,"is",key)
        



Input(x)
Value_Check(x)