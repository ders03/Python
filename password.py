password_input = input("Enter your new password:")

if len(password_input)>=8:
    print("Passcode is secure")

elif len(password_input)<8:
    print("Passcode is not secure")

elif len(password_input)>9 or len(password_input)<4:
    print("Invalid passcode")
