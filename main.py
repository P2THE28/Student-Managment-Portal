import json
from pathlib import Path


print("Enter 1 for Adding New student Details.")
print("Enter 2 for Seeing Details of existing student. ")
print("Enter 3 for updating Details .")
print("Enter 4 for Deleting student data .")

op=int(input("Enter your choise:- "))

if(op==1):
    Student.add()
elif(op==2):
    Student.details()
elif(op==3):
    Student.update()
elif(op==4):
    studen.delete()
else :
    print("Entered choise is not valid.")
