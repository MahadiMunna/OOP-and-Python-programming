def full_name(first,last):
    name=f'full name is: {first} {last}'
    return name
name=full_name(last='Alu',first='kodu')

#take parameters in order
# print(name)

def famous_name(first,last,**addition):
    name=f'{first} {last}'
    print(addition['title'])
    for key,value in addition.items():
        print(key,value)
    return name
name= famous_name(first='Taher',last='Ali',title='hujur',addition='taheirr')
print(name)

def a_lot(num1,num2):
    sum=num1+num2
    mult=num1*num2
    sub=num1-num2
    # return [sum,mult,sub]
    return sum,mult,sub
everything= a_lot(55,21)
print(everything)

def person(**info):
    
    for key,value in info.items():
        print(key,value)
    return name
name = person(name='Munna',age=25)

def a_lot(num1,num2):
    sum=num1+num2
    mult=num1*num2
    sub=num1-num2
    # return [sum,mult,sub]
    return sum,mult,sub
everything= a_lot(55,21)
print(everything)