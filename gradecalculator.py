m = int(input("entre marks in math"))
s = int(input("entre marks in science"))
e = int(input("enter marks in english"))
total_marks = m+s+e
average = total_marks/3
percentage = (total_marks/300)*100
grade = " "
if percentage > 90:
    grade = "A"
elif percentage > 80:
    grade = "B" 
elif percentage > 70:
    grade = "c"
else:
    grade = "p"
print("total marks:", total_marks)
print("average marks:", average)
print("grade:A", grade)




