""" 
1. calculator class to do add, deduct, multiply, divide
2. Pen class. create three object with different instance attribute
3. Exam attend_to_exam get_marks 
 """

class Calculator:
    def add(self,num1,num2):
        return num1+num2
    
cal=Calculator()
print(cal.add(12,12))

class Pen:
    def __init__(self,brand,color,price) -> None:
        self.brand=brand
        self.color=color
        self.price=price

metador=Pen("Metador","Black","6")
print(metador.color)