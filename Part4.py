age = int(input("What is your age? "))
if age < 65:
    ret_age = 65 - age
    print('you can retire in {0} years'.format(ret_age))

else:
    print("you are retired")
else: # Rejection statement is the entered input is not a number
    print "'" + age + "'" + " is not a number."
