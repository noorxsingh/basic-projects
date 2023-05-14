text = 'HELLooo' 
print(text.lower())

print('Welcome to my quiz!') 
playing = input("Do you wnat to play? " )
if playing.lower() != 'yes':
    quit()

score = 0
print("Okay! Let's PLay: ")
answer = input('What is the definition of Ai? ')
if answer.lower() == 'artificial intelligence':
    print('Correct!!!')
    score += 1
else: print('Incorrect :(')


answer = input('What does CPU stand for? ')
if answer.lower() == 'central processing unit':
    print('Correct!!!')
    score += 1
else: print('Incorrect :(')


answer = input('Is playstation better than Xbox? ')
if answer.lower() == 'yes':
    print('Correct!!!')
    score += 1
else: print('Incorrect :(')


answer = input('Is coding fun? ')
if answer.lower() == 'yes':
    print('Correct!!!')
    score += 1
else: print('Incorrect :(')


answer = input('What is the best beginner programming language? ')
if answer.lower() == 'python':
    print('Correct!!!')
    score += 1
else: print('Incorrect :(')

print("You got " + str(score) + " questions correct! ")
print("That's " + str((score/5) * 100) + "%")
if score < 3:
    print("You failed") 
else: print("You passed") 