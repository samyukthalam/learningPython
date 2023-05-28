# Print a triagnle with swtars
i=1
while i<=5:
    print(i*'*')
    i=i+1

# Guess the number until correct
desired_Num=9
guess_Limit=5
guess_count=0
while guess_count<guess_Limit:
    guess_Num = int(input('Enter a number >> '))
    guess_count+=1
    if guess_Num == desired_Num:
        print('You Won!')
        break
else:
        print('You lost')


command =""
while command!='quit':
    command=input('>').lower()
    if command=='start':
        print('Program Started')
    elif command=='stop':
        print('Program stopped')
    elif command=='help':
        print("""
        Type start to start the program
        Type stop to stop the program
        Type quit to quit the program
        """)
    elif command=='quit':
        break
    else:
        print("Sorry, You have typed wrong command")