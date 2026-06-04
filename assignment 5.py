print("Enter the marks for subjects in the range of 0 to 100\n")
sub1 = int(input("\nEnter the marks for subject 1 : "))
sub2 = int(input("\nEnter the marks for subject 2 : "))
sub3 = int(input("\nEnter the marks for subject 3 : "))
sub4 = int(input("\nEnter the marks for subject 4 : "))
sub5 = int(input("\nEnter the marks for subject 5 : "))
total_marks = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total_marks / 500) * 100
if percentage < 40 :
    print(" Failed, percentage is ", percentage)
elif percentage < 55 :
    print("\n Average, percentage is ", percentage)
elif percentage < 65 :
    print("\n Fair, percentage is ", percentage)
elif percentage < 75 :
    print("\n Good, percentage is ", percentage)
elif percentage < 85 :
    print("\n Excellent, percentage is ", percentage)
else :
    print("\n Great job, percentage is ", percentage)
