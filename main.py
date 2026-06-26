import json
import string
from pathlib import Path

class Student() :


    database="data.json"  # i added path of data.json in database (attribute) . 
    data=[]  # make a dummy data for first updataing in this file and then push this to json .

    try :
        if Path(database).exists() :  # here i check for existance of path of json file .
            with open(database,'r') as db :
                data=json.loads(db.read())   # all the data is stored in dummy data . 
        else:
            print("Path does not exist")
    except Exception as err :
        print(f"some error is {err} . ")


#=====================================================================================================#
#=====================================for json file update============================================#
    @classmethod
    def __update(cls) :
        with open(Student.database,'w') as db :
            db.write(json.dumps(Student.data,indent=4))

#=====================================================================================================#
#=================================Create new student details==========================================#
    def add(self):

        info={
            "Name"     : input("Enter name of student:- ") ,
            "Roll_No"  : int(input("Enter Roll No. :- ")) ,
            "Class"    : int(input("Enter calss:- ")),
            "DOB"      : input("Enter day of DOB in dd formate:- ") + '/' + input("Enter month of DOB in mm formate:- ") + '/' + input("Enter year of DOB in yyyy formate:- "),
            "Phone"    : int(input("Enter mobile no.:-")) ,
            "Father"   : input("Enter father name :- "),
            "Mother"   : input("Enter Mother name :- "),
            "Aadhar"   : int(input("Enter aadhar no. :- "))
        }
        Student.data.append(info)
        Student.__update()

#=====================================================================================================#
#===============================================Details veiw==========================================#



    




user=Student()

#===========================================================================#
print("Enter 1 for Adding New student Details.")
print("Enter 2 for Seeing Details of existing student. ")
print("Enter 3 for updating Details .")
print("Enter 4 for Deleting student data .")

op=int(input("Enter your choise:- "))

if op==1 :
    user.add()
elif op==2 :
    user.details()
elif op==3 :
    user.update()
elif op==4 :
    user.delete()
else :
    print("Entered choise is not valid.")
