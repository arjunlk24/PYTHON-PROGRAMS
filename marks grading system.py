marks = 100
dist_marks = int(input("obtain marks:"))
if(marks == dist_marks):
    print("pass excelent")
elif(marks < dist_marks):
    print("please enter valid no.")    
elif(dist_marks >= 33):
    print("Pass")
elif(dist_marks <= 33):
    print("pass")
else:
    ("better luck next time")