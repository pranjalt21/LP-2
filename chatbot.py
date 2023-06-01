def greet(bot_name, birth_year):
    print("Hello! My name is {0}.".format(bot_name))
    print("I am created by pranjal in {0}.".format(birth_year))

def remind_name():
    print('Please, remind me your name.')
    name = input()
    print("What a great name you have, {0}!".format(name))

def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is {0}; that's a good time to start programming!".format(age))
#counts to a number specified by the use
def count():
    print('Now I will prove to you that I can count to any number you want.')
    num = int(input())

    counter = 0
    while counter <= num:
        print("{0} !".format(counter))
        counter += 1
        #tests their programming knowledge
def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    answer = 2
    guess = int(input())
    while guess != answer:
        print("Please, try again.")
        guess = int(input())
    print('Completed, have a nice day!')
    print('.................................')
    print('.................................')
    print('.................................')
def end():
    print('Congratulations, have a nice day!')
    print('.................................')
    print('.................................')
    print('.................................')
    input()
 
greet('Sbot', '2002')  # change it as you need
remind_name()
guess_age()
count()
test()
end()
'''
Hello! My name is Sbot.
I am created by pranjal in 2002.
Please, remind me your name.
Dan
What a great name you have, Dan!
Let me guess your age.
Enter remainders of dividing your age by 3, 5 and 7.
1
2
1
Your age is 22; that's a good time to start programming!
Now I will prove to you that I can count to any number you want.
5
0 !
1 !
2 !
3 !
4 !
5 !
Let's test your programming knowledge.
Why do we use methods?

To repeat a statement multiple times.
To decompose a program into several small subroutines.
To determine the execution time of a program.
To interrupt the execution of a program.
3
Please, try again.
2
Completed, have a nice day!
.............................
.............................
.............................
Congratulations, have a nice day!
.............................
.............................
..........................
'''
