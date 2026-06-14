def student():
  a = input("Enter your name : ")
  b = int(input("Enter which sem : "))
  c = int(input("Enter your enroll no. : "))


def teacher():
   a = input("Enter your name : ")
   b = input("Enter you UID : ")

person = input("Are you a student or teacher? : ")
if person.lower() == "student":
   student()
else:
   teacher()   
  


