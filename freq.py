s=input("Enter a line of text ")
s=s.strip()

x=s.split()
def dic(a,b):
    for i in b:
        if i not in a:
            a[i]=1
        else:
            a[i]=a[i]+1

y={}
dic(y,x)
print(y)
             
