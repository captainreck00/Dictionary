month={"january" : 31 , "february" : 28 , "march" : 31 , "april" : 30 , "may" : 31 , "june" : 30 , "july" : 31 , "august" : 31 , "september" : 30 , "october" : 31 , "november" : 30 , "december" : 31}

def a(k):
    inp=input("Enter a month name ").lower()
    print("The number of days in",inp,"is",k[inp])

def b(l):
    for key in l:
        if l[key]==31:
            print("The month with 31 days is",key)    

def c(m):
    sorted(m)
    print(m.keys())   

