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

        grade = input("Enter class:- ")
        roll  = input("Enter Roll No. :- ")
        userdata=[i for i in Student.data if i['Roll_No']==roll  and i['Class']==grade]

        if not userdata :
            info={
                "Class"    : grade,
                "Roll_No"  : roll ,
                "Name"     : input("Enter name of student:- ") ,
                "DOB"      : input("Enter day of DOB in dd formate:- ") + '/' + input("Enter month of DOB in mm formate:- ") + '/' + input("Enter year of DOB in yyyy formate:- "),
                "Phone"    : input("Enter mobile no.:-"),
                "Father"   : input("Enter father name :- "),
                "Mother"   : input("Enter Mother name :- "),
                "Aadhar"   : input("Enter Aadhar No. :- ")
            }
            Student.data.append(info)
            Student.__update()
            print("ADD SUCCESSFULLY")

        else :
            print("======================================================================")
            print(f"Roll no. {roll} in given class {grade} is already exist")
            print("Details of existing user:")
            for i in userdata[0] :
                print(f"{i} : {userdata[0][i]}")

            print("Create with another Roll no.")
            print("======================================================================")
        

#=====================================================================================================#
#===============================================Details veiw==========================================#
    def details(self):

        grade=input("Enter class:- ")
        roll=input("Enter roll no. :- ")

        userdata=[i for i in Student.data if i['Roll_No']==roll  and i['Class']==grade]   # if data exist then data will load to this list and if not present the it will be empty

        if not userdata :
            print("Student Not Found")
        else :
            print("")
            print("===========STUDENT DETAILS========")
            for i in userdata[0] :
                print(f"{i} : {userdata[0][i]}")

#=====================================================================================================#
#===============================================Updataing details=====================================#

    def update(self) :
        grade=input("Enter class:- ")
        roll=input("Enter roll no. :- ")

        userdata=[i for i in Student.data if i['Roll_No']==roll  and i['Class']==grade]   # if data exist then data will load to this list and if not present the it will be empty
        if not userdata :
            print("Student Not Found")
        else :
            print("===========EXISTING STUDENT DETAILS========")
            for i in userdata[0] :
                print(f"{i} : {userdata[0][i]}")
            print("===========================================")
            print("Enter new details , if any section is not need to update keep it as blank.")

            newgrade=input("Enter new calss :- ")
        
            if int(newgrade)>=int(userdata[0]['Class']) :
                newinfo={
                    "Class"    : newgrade ,
                    "Roll_No"  : input("Enter new roll :- "),
                    "Name"     : input("Name name of student:- ") ,
                    "DOB"      : input("Enter day of DOB in dd formate:- ") + '/' + input("Enter month of DOB in mm formate:- ") + '/' + input("Enter year of DOB in yyyy formate:- "),
                    "Phone"    : input("Enter mobile no.:-") ,
                    "Father"   : input("Enter father name :- "),
                    "Mother"   : input("Enter Mother name :- "),
                    "Aadhar"   : input("Enter Aadhar No. :- ")
                }

                if newinfo['Class']=="" :
                    newinfo['Class']=userdata[0]['Class'] 
                if newinfo['Roll_No']=="" :
                    newinfo['Roll_No']=userdata[0]['Roll_No']
                if not newinfo['Name'] :
                    newinfo['Name']=userdata[0]['Name']
                if newinfo['DOB']=="//" :
                    newinfo['DOB']=userdata[0]['DOB']
                if newinfo['Phone']=="" :
                    newinfo['Phone']=userdata[0]['Phone']
                if not newinfo['Father'] :
                    newinfo['Father']=userdata[0]['Father']
                if not newinfo['Mother'] :
                    newinfo['Mother']=userdata[0]['Mother']
                if newinfo['Aadhar']=="" :
                    newinfo['Aadhar']=userdata[0]['Aadhar']
                    for i in newinfo :   #update of newinfo inside userdata
                        userdata[0][i]=newinfo[i]
                    Student.__update()
                    print("Successfully updated")

            else :
                print("You Entered class less then current class , Not possible , student may pass then move next if fail then remains on same class")
            
            

#=====================================================================================================#
#===============================================Deleting Details=====================================#
                    
            
        

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
