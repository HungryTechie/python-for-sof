print('''
Exercise #1
Suppose you have $100, which you can invest with a 10% return each year.
After one year, it's 100×1.1=110 dollars, and after two years
it's 100×1.1×1.1=121.
Use Python's print() function
to calculate how much money you end up with after 7 years.
-------------------------------------------------------------------------
Exercise #2
Create a variable called savings and equal to 100. 
Create a variable factor, equal to 1.10.
Use savings and factor to calculate the amount of money you end up with
after 7 years. Store the result in a new variable, result.
Print out the value of result.
-------------------------------------------------------------------------
Exercise #3
Create a new string, desc, with the value "compound interest".
Create a new boolean, profitable, with the value True
-------------------------------------------------------------------------
Exercise #4
Find the type of the following variables used in the exercises 1-3 :
savings, factor, 'compound interest'and profitable.
Have Python output each data type. 
Exercise #5
Let's combine date types.
Add a message that prints the following: 'I started with $( insert your
savings variable) and now I have $( result variable). Great!'
''')
money_string = input("How much money do you have? ")
money = float(money_string)
year_string = input("How many years are you investing? ")
year = float(year_string)
year_invest = 1.1 ** year
money_returned = money * year_invest
print("After ", year, " year(s), you will have $",money_returned, " in your account.")

print('''
#1 
What does this program print? Pay close attention to spaces.
print("Hello", "World", "!")
''')
print("It will print 'Hello World !'")
print('''
#2
What is the compile-time error in this program?
print("Hello", "World!)
''')
print("The error will be as a result of the lack of an apostrophe at the end of the World!")
print('''
#3
Write three versions of the hello.py program that have different compile-time errors.
Write a version that has a run-time error.
''')
print("""
print(hello world)
print(hello, world)
print(Helllo, "world!")
""")
print('''
#4
How do you discover compile-time errors? How do you discover run-time errors?
''')
print("By compiling and running the program.")
print('''
#5
Write a program that prints a greeting of your choice, perhaps in a language other
than English.
''')
print("""
print("مرحبا بالعالم!")
""")
print('''
#6
Write a program that prints the sum of the first ten positive integers, 1 + 2 + … + 10.
''')
print(1+2+3+4+5+6+7+8+9+10)
print('''
#7
Write a program that prints the product of the first ten positive integers, 1 × 2 × … × 10. (Use * to indicate multiplication in Python.)
''')
print("""
value = 1*2*3*4*5*6*7*8*9*10
print(value)
""")
print('''
#8
 Write a program that prints the balance of an account after the first, second, and
third year. The account has an initial balance of $1,000 and earns 5 percent interest
per year.
''')
print("""
balance = 1000
year1 = 1000 * 1.05
year2 = 1000 * 1.05 ** 2
year3 = 1000 * 1.05 ** 3
print('''
"Initial Balance:", balance,
"After year 1, balance is", year1
"After year 2, balance is", year2
"After year 3, balance is", year3
''')
""")
print('''#9 
Write a program that displays your name inside a box on the screen, like this:
''')
print("""
_____
|Max|
-----
""")
print('''# 10 
Write a program that prints your name in large letters.
''')
print("""
┏━┓┏━┓╋╋╋╋╋╋╋╋╋╋┏┓
┃┃┗┛┃┃╋╋╋╋╋╋╋╋╋╋┃┃
┃┏┓┏┓┣━━┳┓┏┳┳┓┏┳┫┃┏┳━━┳━┓
┃┃┃┃┃┃┏┓┣╋╋╋┫┗┛┣┫┃┣┫┏┓┃┏┓┓
┃┃┃┃┃┃┏┓┣╋╋┫┃┃┃┃┃┗┫┃┏┓┃┃┃┃
┗┛┗┛┗┻┛┗┻┛┗┻┻┻┻┻┻━┻┻┛┗┻┛┗┛
""")
print('''
# 11
Write a program that prints a face.
''')
print("""
   ___
 //---\\
|| o o ||
\|  >  |/
 | \_/ |
 \_____/
""")
