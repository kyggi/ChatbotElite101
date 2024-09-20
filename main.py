print("Welcome to the Elite 101 Chatbot!")
name_input = input("What is your name? :")
age_input = int(input("Nice to meet you "+ name_input+"! How old are you? :"))
if age_input <= 17:
    print("Oh, to be " + str(age_input) + " again! Welcome " + name_input + "! How can I help you today?")
else:
    print("Welcome " + name_input + "! How can I be of assistance today?")

print("Please choose from the following options:")
print("1. Placeholder Option 1")
print("2. Placeholder Option 2")
print("3. Placeholder Option 3")
print("4. Exit the conversation")
user_input=input("Enter the number of your choice :")
if user_input == 4:
    print("Goodbye " + name_input + "! Have a wonderful day!")
else:
    print("The placeholder options have not yet been programmed.")