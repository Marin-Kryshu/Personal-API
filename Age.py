#!Local\Microsoft\WindowsApps\python3.9.exe
import random
print("\n\nHey, here's my little program that'll\ntell you how old you are.\n\nPlease try not to mess with it :)\n\n")

run = 1
counter = 1
d1 = ["oh for sure, so you're a dino? no.","Bruh, no you aint", "come on man!", "you really thought you could get away with that huh?", "Not even gonna entertain that",]
d2 = ["Man's is still chillin in the womb!","ohhh, I get it. Back to the future huh?"]
d3 = ["bro, literally learn to type","Wwwwooooooowwww! you think you can break me? hah!", "Did you forget that age is defined by numbers? Embarrassing!","Bruh, have you heard of numbers?","lol! get a load of this guy!"]


while run == 1:
    age1 = input("\n\n\nEnter your age:")
    age = ""
    try:
        age = float(age1)
        if age > 0:
            if age < 100:
                print("\n\nYour age is:", age)
                if counter > 10:
                    print ("phew! that took a while huh?")
                run = run - 1
                print("you tried to mess with me %s times!" % counter)
            elif age > 100:
                choice = random.randint(0, len(d1) - 1)
                print("\n",d1[choice])
                counter = counter + 1
        elif age < 0:
            choice = random.randint(0, len(d2) - 1)
            print("\n",d2[choice])
            print("your age cant be negative")
            counter = counter + 1
    except:
        choice = random.randint(0, len(d3) - 1)
        print("\n",d3[choice])
        print("please use numbers!")
        counter = counter + 1


endPrompt = input("\n\nPress any key to continue...")
