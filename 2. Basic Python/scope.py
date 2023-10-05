balance = 3000
def buy_things(item,price):
    global balance
    balance=balance-price
    print('balance inside the function: ',balance)
buy_things('sunglass',1000)