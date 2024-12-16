'''5)The marks obtained by a student in 3 different subjects are input by the user. Your program should calc
ulate the average of subjects and display the grade. The student gets a grade as per the following rules:
Average Grade
90-100 A
80-89 B
70-79 C
60-69 D
0-59 F'''

sub1 = int(input("Enter the marks of first subject: "))
sub2 = int(input("Enter the marks of second subject: "))
sub3 = int(input("Enter the marks of third subject: "))

avg = (sub1 + sub2 + sub3) / 3
print(f"Average marks: {avg}")
if avg >= 90 and avg <= 100:
    print("A")
elif avg >= 80 and avg <= 89:
    print("B")
elif avg >= 70 and avg <= 79:
    print("C")
elif avg >= 60 and avg <= 69:
    print("D")
elif avg >= 0 and avg <= 59:
    print("F")