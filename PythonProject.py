
a=10000
d=0
def Mr_John():
    print("Name: Mr.John")
    print("Cash available in your account: Rs-",a)

def deposit():
    global d
    d=int(input("Deposit Amount: "))
    print("Cash available in your account: Rs-",a+d)
def withdraw():
    w=int(input("Withdraw amount: "))
    x=(a+d)-w
    print("Now cash available: Rs-",x)
    if x<5000:
        print("Low balance")
def exit():
    print("Thank You")      

  
Mr_John()
deposit()
withdraw()
exit()