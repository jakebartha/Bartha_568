age = int(input("What is your age? "))
if age < 65:
    ret_age = 65 - age
    print('you can retire in {0} years'.format(ret_age))

else:
    print("you are retired")

