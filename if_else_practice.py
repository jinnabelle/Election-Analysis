temperature = int(input("What is the temperature outside?"))

if temperature > 80:
    print("Turn on the AC.")
else: 
    print("Open the windows.")

#ask test score
score = int(input("what is your test score?"))

#determine the letter grade. 
if score >= 90:
    print("your grade is an A.")
elif score >= 80:
    print("your grade is a B.")
elif score >= 70:
    print("your grade is a C.")
elif score >= 60: 
    print("your grade is a D.")
else:
    print("your grade is an F.")