class Star_Cinema:
    hall_list=[]
    @classmethod
    def entry_hall(cls,hall):
        cls.hall_list.append(hall)
class Hall:
    def __init__(self,rows,cols,hall_no) -> None:
        self.seats={}
        self.show_list=[]
        self.rows=rows
        self.cols=cols
        self.hall_no=hall_no
        Star_Cinema.entry_hall(self)
         






while True:
    x=int(input("1. VIEW ALL SHOW TODAY\n2. VIEW AVAILABLE SEATS\n3. BOOK TICKET\n4. EXIT\nENTER OPTION: "))
    if x==1:
        print(x)
    elif x==2:
        print(x)
    elif x==3:
        print(x)
    elif x==4:
        break
    else:
        print("\n--Choose a valid option!--\n")        
    