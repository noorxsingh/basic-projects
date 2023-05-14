print("Hello and welcome to my game")
name = input("Type in your name to begin playing: ")
print("Hello", name,"you will play as Noor and try to make good decisions for the day to make mom proud!")


answer = input("You wake up in the morning and you notice mom has left to work, should you take a shower or go on phone. (shower/go on phone): ").lower()

if answer == "shower":
    answer = input("Good decision, now you have freshened up, now you can either make your bed or go and eat breakfast. (make bed/eat breakfast): ").lower()

    if answer == "make bed":
        new = input("Good choice, now you can either be productive for the day or go on your phone. (phone/productive): ").lower()
        
        if new == "phone":
            print("You wasted your whole day on your phone. Mom is not proud of you")
        elif new == "productive":
            print("You did good today. Mom is very proud of you")
        else:
            print("Not a option. You did not make Mom prou")

    elif answer == "eat breakfast": 
        print("Bad decision, Mom has found you have not made your bed... she is not proud of you")
    else:
        print("Not a option. You did not make Mom proud")
elif answer == "go on phone":
    print("You wasted your whole day on your phone. Mom is not proud of you")

else:
    print("Not a option. You did not make Mom prud")
