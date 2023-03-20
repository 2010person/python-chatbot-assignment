def one():
    global chat
    chat = input("What school do you go to?")
    if chat == "be quiet":
        print("so long, user")
        quit()
    elif chat == "King Edward VI School":
        print("You are going to the best school ever. Well done for passing the 11+!")
    else:
        print("Are you aware that your school is not the best?")
    main()

def two():
    global chat
    chat = input("Where do you live?")
    if chat == "be quiet":
        print("so long, user")
        quit()
    elif chat == "Buckingham Palace":
        print("Good day, Your Royal Higness")
    elif chat == "10 Downing Street":
        print("Hope you're doing well, Prime Minister.")
    else:
        print("Meh, average.")
    main()

def three():
    global chat
    chat = input("How often do you go to the library every week (enter your number as a word).")
    if chat == "be quiet":
        print("so long, user")
        quit()
    elif chat == "zero":
        print("Oh the misery!")
    elif chat == "one" or == "two":
        print("A nice little read")
    elif chat == "three" or == "four" or == "five":
        print("Wow! Nice reading habits!")
    else:
        print("Do you have your head in books all day?")
    main()

def four():
    global chat
    chat = input("How many hours of time do you have on your phone per day (enter your number as a word).")
    if chat == "be quiet":
        print("so long, user")
        quit()
    elif chat == "zero":
        print("It dosen't hurt to watch a little bit.")
    elif chat == "one" or == "two" or == "three":
        print("OK. Fair enough.")
    elif chat == "four" or == "five" or == "six":
        print("You might need to consider lowering your time a little bit.")
    elif chat == "seven" or == "eight" or == "nine":
        print("Woah, try locking away your phone for a couple of hours!")
    else:
        print("OH MY GOD! YOU SHOUD SEEK HELP! STOP BEING ADDICTED TO YOUR MOBILE PHONE!")
    main()
            
def main():
    global chat, num
    if chat == "be quiet":
        print("so long, user")
    else:
        num = num + 1
        if num == 1:
            one()
        elif num == 2:
            two()
        elif num == 3:
            three()
        else:
            four()
        print("Bye user, thanks for talking to me (MarkChat).")

chat = "default startup text"
num = 0
main()