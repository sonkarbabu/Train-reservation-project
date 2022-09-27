class Train:
    def __init__(self,trainname,color,fare,seattype,seatnumber,bogienumber,root,bogietype,bogieinformation,noofstopage,time):
        self.trainname=trainname
        self.color=color
        self.fare=fare
        self.seat=seattype
        self.seatno=seatnumber
        self.bn=bogienumber
        self.root=root
        self.bt=bogietype
        self.bi=bogieinformation
        self.nos=noofstopage
        self.time=time
    def Nameinfo(self):
        print(f"name of the train is {self.trainname}")
    def Colorinfo(self):
        print(f"color of the train is {self.color}")
    def Fareinfo(self):
        print(f"fare of the train is {self.fare}")
    def Seatinfo(self):
        if(self.seatno>0):
            print(f"Your ticket is booked and your seat is {self.seat} your seat number is {self.seatno} and your bogie number is {self.bn}")
        else:
            print(f"Sorry in this train seat is not available your ticket is not booked please try in tatkal")
    def Rootinfo(self):
        print(f"Root of the train is between {self.root}")
    def Bookingtype(self):
        print(f"the booking coach is {self.bt}")
    def Bogieinfo(self):
        if(self.bi>0 and self.bi<73):
            print("you did not cross the limit of maximum seat available in this bogie and your ticket has been successfully booked")
        else:
            print("you cross the limit of maximum seat available in this bogie and your ticket has not been successfully booked")
    def Fulltaraininfo(self):
        print(f"the name of the train is {self.trainname}\n color of the train is {self.color}\n fare of the train is {self.fare}\n seat of the train is {self.seat}\n seat number of the train is {self.seatno}\n")
        print(f"bogie number of the train is {self.bn}\n root of the train is {self.root}\n bogie type of the train is {self.bt}\n number of stopage of the train is {self.nos}\n and time table of the train is {self.time}")
class Person(Train):
    def __init__(self,name,DOB,Adharnumber):
        self.name=name
        self.DOB=DOB
        self.an=Adharnumber
    def fullpersoninfo(self):
        print(f"name of the person who is booking this ticket is {self.name}\n date of birth of the person is {self.DOB}\n and adhar number of this person is {self.an}\n")
    def personname(self):
        print(f"name of the person is {self.name}")
    def persondob(self):
        print(f"date of birth of the person is {self.DOB}")
    def personadhar(self):
        print(f"adhar number of the person is {self.an}")
class Software(Person):
    def __init__(self,softwarename,loginid,loginmobilenumber,loginemail):
        self.sn=softwarename
        self.li=loginid
        self.lmn=loginmobilenumber
        self.le=loginemail
    def fullsoftwareinfo(self):
        print(f"name of the softwaare which is used to booking the ticket is {self.sn}\n loginid of this software is {self.li}\n login mobile number is {self.lmn}\n and login email id is {self.le}\n")
    def softwarename(self):
        print(f"name of the software which is used to book the ticket is {self.sn}")
    def softwareloginid(self):
        print(f"login id which is used tologin booking software is {self.li}")
    def loginmobilenumber(self):
        print(f"software login mobile number is {self.lmn}")
    def loginemailid(self):
        print(f"name of the software login emailid is {self.le}")
T=Train("Rajdhani Express Train Number is:10129","Red",3000,"Lower",45,"S6","Azamgarh to Delhi","Sleeper",65,10,"10:55AM in Azamgarh and next day 7:30 in delhi")
P=Person("Dileep sonkar","03-03-1998",837905486414)
S=Software("IRCTC","dlpsnk_077",6307702173,"dileepnita@gmail.com")
T.Fulltaraininfo()
P.fullpersoninfo() 
S.fullsoftwareinfo()
T.Bogieinfo()



