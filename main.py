# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print(1 + 1)

def cube(number):
    return math.pow (number,3)
cube (4)

def do_it(x):
    print(x**2 + 2)
do_it(1)

import pandas as pd
age = 5
print(type(age))
weight = 45.0
print(type(weight))
name = 'Alex'
print(type(name))
endurance = 5
'I can walk for '+str(endurance)+' hours.'
next_lang = 'R'
print('Next, I will learn',next_lang,'.')
next_lang = 'R'
text = "Next, I will learn"
print(text, next_lang)
daily_sales = [2345, 3754, 2583, 4583, 7823, 10234, 14384]
len(daily_sales)
old_books = 67
damaged = 43
price = 5
score = (old_books - damaged)*price
print('I raised as much as',score,'.')
import pandas as pd
invited_guests = pd.Series(['John', 'Tom', 'Jane', 'Kate', 'Mark'])
invited_guests
respondents_age = pd.Series([19, 37, 48, 56, 32, 21, 23, 78, 35, 30, 25, 25, 18])
respondents_age[respondents_age<30]
respondents_age = pd.Series([19, 37, 48, 56, 32, 21, 23, 78, 35, 30, 25, 25, 18])
respondents_age+5 #adds 5 to all elements in the list
eu_states = pd.read_csv("eu_states.csv")# importing data into python
eu_states.tail()# viewing the last 5 rows
len(eu_states)# finding no. of rows
eu_states.columns# finding counm names
eu_states['Country']# selecting a single column
eu_states[['Country']]# showing single columns as dataframes
eu_accession_info = eu_states[['Country', 'Accession Year']]# selecting multiple columns as dataframes
changed_order = eu_states[['Country', 'Area','Population','Currency']]# Displaying columns in a given order
eu_states['GDP Per Capita'] = eu_states['GDP'] / eu_states['Population']*1000000# Adding a new column
eu_states.drop('GDP Per Capita',axis=1)# removing the added column
eu_states.iloc[2]# Selecting rows with iloc
eu_states.iloc[[2]]# selecting rows as dataframes
eu_states.set_index('Country')# setting a new index for a dataframe
eu_states.loc['Poland']# selecting rows with loc
eu_states.loc[['Poland']]# selecting rows as dataframes
eu_states = eu_states.reset_index(drop=False)# resetting the index
eu_states = eu_states.set_index('Country')
eu_states = eu_states.drop('United Kingdom', axis=0)# removing a row from  dataframe
eu_states[2:10]# Filtering rows by index show the rows from 3rd to 10th row.
eu_states.loc[2:7, ['Country','Currency']]# Filtering rows and columns with loc
eu_states.iloc[9:, :3]# Filtering rows and columns with iloc return rows from the 10th row to the end of the DataFrame for the first three columns
eu_states[eu_states['GDP']> 25000]# Filtering rows with conditions Show the countries where the GDP is greater than 25000.
res = eu_states['Currency']=='Euro'
res2 = eu_states['Accession Year']<2000
#show only those countries that use the Euro as their main currency, and were accepted into European Union before the year 2000.
eu_states[res & res2] #Filtering rows – multiple conditions AND OR
res = eu_states['Currency']=='Euro'
res2 = eu_states['Accession Year']<2000
#show only those countries that use the Euro as their main currency, or those accepted into European Union before the year 2000.
eu_states[res | res2]
#Combining loc and filtering
#Select only the Country and GDP columns for countries that joined the European Union after the year 2000, and use the Euro as their currency.
res = eu_states['Currency']=='Euro'
res2 = eu_states['Accession Year']>2000
eu_states.loc[res & res2, ['Country','GDP']]
eu_states.sort_values(by='Area')# soting rows
eu_states.sort_values(by='Area',ascending=0)# sorting rows descending
# Sort all countries in eu_states by Accession Year, and then by GDP.
eu_states.sort_values(by=['Accession Year','GDP'])# Sorting by multiple columns

movies = pd.read_csv('movies.csv')
movies.describe()# returns basic statistics for each column in our dataset
movies['rating'].max()# max value of a certain var/ column
movies['rating'].mean()# means
movies['rating'].median()# median
#median of the rating column that are below the median of this column.
movies[movies['rating']< movies_median]['rating'].median()
movies['rating'].quantile([0.1,0.2,0.8,0.9])# quantiles of movie rating
movies['box_office'].std()# standard deviation
#Count the number of movies  in the interval between mean - standard deviation and mean + standard deviation
untypical = movies['rating']< [movies['rating'].mean()- movies['rating'].std()]
uttypic = movies['rating']> [movies['rating'].mean()+ movies['rating'].std()]
movies.loc[untypical|uttypic, 'rating'].count()
movies_by_country = movies.groupby('country')# Grouping rows
movies_by_country.size()# size of groups
movies_by_country['box_office'].sum()
movies_by_director['rating'].mean().sort_values(ascending=False)
#Grouping by multiple columns
movies_by_country = movies.groupby(['country','genre'])
movies_by_country['box_office'].mean()
movies_by_genre = movies.groupby(['genre','country'])
movies_by_genre['box_office'].max()
dat.head()
dat_group = dat.groupby('year')
dat[dat['year']==2013]['production_million_metric_tons'].median()
#2014, find the value of 10th percentile of area_harvested_ha for the whole world
res = crops[crops['year']==2014].quantile([0.1])['area_harvested_ha']
result = 1976041.5
crops[crops['country']=='Germany']['area_harvested_ha'].min()

crops.head()
more = crops["year"] >= 2012
less = crops["year"] <= 2014
crops[less & more].groupby(by="country")["production_million_metric_tons"].sum().sort_values(ascending=False)
result = 'China'
#data preprocessing
import pandas as pd
ticket_statistics = pd.read_csv('ticket_statistics.csv')
ticket_statistics
ticket_statistics = ticket_statistics.fillna(0)# filling NaN with 0,
ticket_statistics.sort_values(by='tickets',ascending=1)
ticket_statistics['experience'].isnull().values.any()# checking for mising values automatically in a column
# duplicates
import pandas as pd
states_sales = pd.read_csv('states_sales.csv')
states_sales
states_sales.duplicated().values.any()# checking for duplicates automatically
states_sales = states_sales.drop_duplicates()# dropping duplicates
# checking for outliers
temperatures.sort_values('temperature',ascending=True)
temperatures = temperatures.drop(10)# removing outliers
# importing multiple files
import pandas as pd
employee_names = pd.read_csv('employee_names.csv')
employee_salaries = pd.read_csv('employee_salaries.csv')
# merging files
employee_all = employee_names.merge(employee_salaries, on = 'employee_id')
#Merging two DataFrames – different columns, step 2
stores_comparison = store_a.merge(store_b, left_on = 'year', right_on = 'period')# inner merge
stores_comparison
stores_comparison = store_a.merge(store_b, left_on='year', right_on='period', how = 'outer')# outer merge

# excercise
import pandas as pd
patient_info = pd.read_csv('patient_info.csv')
patient_results = pd.read_csv('patient_results.csv')
patient_info.duplicated().values.any()
patient_results.duplicated().values.any()
patient_info = patient_info.drop(5)
patient_info = patient_info.drop_duplicates()
patient_results = patient_results.fillna(0)
all_patient_data = patient_info.merge(patient_results, left_on = 'patient_id', right_on = 'id')

# visualization
import pandas as pd
import matplotlib.pyplot as plt
books = pd.read_csv('books.csv')

#figures and subplots
#To start drawing plots, we need to create at least one figure, with at least one subplot inside it
books = pd.read_csv('books.csv')
figure = plt.figure(figsize=(10, 6))
subplot = plt.subplot()
subplot.plot(books['romance'])
subplot.plot(books['fantasy'])
subplot.plot(books['thriller'])
subplot.legend(loc = 'upper right')# adding legend
plt.xticks(range(len(books['year'])),books['year'])# axis tick labels
subplot.set_title('Book Sales')# title
subplot.set_xlabel('year')# x label
subplot.set_ylabel('profit')# y label
subplot.grid(axis='both')# grid
plt.show()
# creating multiple subplots
salaries = pd.read_csv('salaries.csv')
figure = plt.figure(figsize=(12,4))
#add_subplot(x,y,n)/(xyn) refers to a grid of subplots with x rows and y columns, and it creates a subplot at position n
subplot1 = figure.add_subplot(131)
subplot2 = figure.add_subplot(132)
subplot3 = figure.add_subplot(133)
subplot1.hist(salaries['accounting'], facecolor='red', edgecolor='black') # histogram
subplot2.hist(salaries['it'], facecolor='orange', edgecolor='black') #histogram
subplot3.hist(salaries['consulting'], facecolor='purple', edgecolor='black') #histogram
subplot1.set_xlim([900, 2000])
subplot2.set_xlim([900, 2000])
subplot3.set_xlim([900, 2000]) # setting x limits
figure.suptitle('salary distribution by department')#   title for the whole figure
subplot1.set_title('Accounting')# title for subplot
subplot2.set_title('IT')# title for subplot
subplot3.set_title('Consulting')# title for subplot
#scatter plots
import pandas as pd
diamonds = pd.read_csv('diamond_prices.csv')
figure = plt.figure(figsize=(5,5))
ax = plt.subplot(111)
ax.set_title('Diamond Sizes and Prices')
ax.set_xlabel('price')
ax.set_ylabel('size')
plt.scatter(diamonds['price'], diamonds['size'],c='red',alpha=0.5,s=100,marker='D')# other markers '^'
#bar plots
used_cars = pd.read_csv('used_cars.csv')
figure = plt.figure(figsize=(8,5))
bar_subplot = plt.subplot(111)
bar_subplot.set_title('Avg Car Price by Make')
bar_subplot.set_xlabel('car make')
bar_subplot.set_ylabel('avg price')
plt.bar(used_cars['make'],used_cars['price'],width=0.3)
#exercise
import pandas as pd
stock_index = pd.read_csv('stock_index.csv')
figure = plt.figure(figsize=(16,4))
subplot1 = figure.add_subplot(121)
subplot2 = figure.add_subplot(122)
subplot1.plot(stock_index['Change'])
subplot1.grid(axis='y')
subplot2.hist(stock_index['Change'],edgecolor='black',facecolor='red',orientation='horizontal')
figure.suptitle('Warsaw Stock Market Index')
subplot1.set_title('Daily Change Line')
subplot2.set_title('Daily Change Histogram')
plt.show()

airbnb_dataset.loc[airbnb_dataset['reviews']>10].groupby(by='neighborhood')['overall_satisfaction'].mean().sort_values(ascending=False)
# scatter plot
airbnb_dataset_filtered = airbnb_dataset[airbnb_dataset.overall_satisfaction > 0]
scatter_figure = plt.figure(figsize=(10,5))
scatter_subplot = plt.subplot(111)
scatter_subplot.set_title('Prices vs Satisfaction')
scatter_subplot.set_xlabel('price per person')
scatter_subplot.set_ylabel('satisfaction')
plt.scatter(airbnb_dataset_filtered['price_per_person'], airbnb_dataset_filtered['overall_satisfaction'],alpha=0.5,s=120,marker='o')
#histogram
airbnb_dataset_filtered = airbnb_dataset[airbnb_dataset.overall_satisfaction > 0]
hist_figure = plt.figure(figsize=(10,5))
hist_figure = plt.subplot(111)
hist_figure.set_title('Prices in Auckland')
hist_figure.set_xlabel('price per person')
hist_figure.set_ylabel('count of offers')
plt.hist(airbnb_dataset_filtered['price_per_person'],facecolor='orange', edgecolor='black',bins=30)
#final challenge
import pandas as pd
datasett = pd.read_csv('canada.csv')
female_population = datasett.loc[(datasett['year']==2017)&(datasett['sex'] ==  'Females'),['population (x 1,000)']].sum()
canada = pd.read_csv('canada.csv')
employment_rate = canada.groupby(by='birth')['employment_rate (percentage)'].mean().sort_values()
canada = pd.read_csv('canada.csv')
canada[canada['birth']== 'Canada'].groupby('year')['unemployment_rate (percentage)'].mean().sort_values()
year = 2017
mean = 5.15
canada = pd.read_csv('canada.csv')
canada[(canada['year']==2010)&(canada['birth']!='Canada')].groupby('birth')['population (x 1,000)'].sum()
continent = 'Asia'
canada = pd.read_csv('canada.csv')
numbers = (canada[canada['year']==2015].groupby('birth')['unemployment_rate (percentage)'].mean()<6).values
counter = 0
for number in numbers:
  if number == True:
    counter +=1
print(counter)
birth_groups_number = 2
canada_labour = pd.read_csv('canada.csv')
female_2017 = canada_labour.loc[(canada_labour['year']==2017)&(canada_labour['sex']=='Females')]
female_2017['unable to work'] = female_2017['population (x 1,000)']-female_2017['labour_force (x 1,000)']
female_2017 = female_2017.drop('status',axis=1)
female_2017_immigrants = female_2017.drop(132)
canada_labour = pd.read_csv('canada.csv')
import matplotlib.pyplot as plt
figure = plt.figure(figsize=(8,4))
subplt = plt.subplot(111)
subplt.set_title('Total population in Canada')
subplt.set_xlabel('year')
subplt.set_ylabel('population (x 1,000)')
subplt.plot(canada_labour.groupby(by=['year'])['population (x 1,000)'].sum(),color='red',linewidth=3)
subplt.grid()
plt.show()
# input function
name = input('What is your name?')
print('Hello',name)

rate = input('What is your hourly rate?')
hours = input('How many hours have you worked?')
earned = float(rate)*float(hours)
print('You have earned',earned,'in total!')
#compound interest
initial_amount = float(input('What is the initial amount? '))
interest_rate = float(input('What is the annual interest rate as a percent? '))
compounding_frequency = float(input('How many times in a year is the amount compounded? '))
time = float(input('How many years are you going to wait? '))
final_amount = initial_amount*(1+(interest_rate/(100*compounding_frequency)))**(compounding_frequency*time)
print('AT the end of the period, you will have',final_amount)
#boolean
company_name = 'Everyday Store'
print(company_name.islower())
company_name = 'everyday store'
print(company_name.islower())

#IF statements
height = int(input('What is your height in centimeters? '))
if height > 185:
  print('You are very tall')
# if else statements
height = int(input('What is your height in centimeters? '))
if height > 185:
  print('You are very tall.')
else:
  print('You are not very tall.')
#elif statements
answer = input('Is Sydney the capital of Australia? ')
if answer == 'y':
  print('Wrong! Canberra is the capital')
elif answer == 'n':
  print('Correct')
else:
  print('I do not understand your answer!')
# comparison operators
answer = int(input('How old are you? '))
if answer >= 17:
  print('You can already drive a car in England')
else:
  print('You cannot drive a car in England yet.')
if answer >= 18:
  print('You can already drive a car in Portugal')
else:
  print('You cannot drive a car in Portugal.')
# multiple lines of code
answer = input('Welcome, are you a registered user? y/n: ')
if answer == 'y':
  username = input('Please provide your username:')
  print('Welcome back',username)
else:
  print('Sorry, the system does not accept new users.')
# multiple conditions with and
name = input('Provide a Polish name: ')
if name.endswith('a')and name!= 'Kuba':
  print('This is a female name')
else:
  print('This is a male name')
# multiple statements with or
weight = float(input('What is your weight in kg? '))
height = float(input('What is your height in centimeters? '))
if weight < 45 or height < 130:
  print('You can take a ride!')
else:
  print('Sorry, you cannot take a ride!')
# multiple conditions with not
password = input('Please provide a password: ')
if (len(password) >=8)and not password.startswith('@'):
  print('Correct password')
else:
  print('Incorrect password!')
# using or and
purchase_days_ago = int(input('How many days ago have you purchased the item? '))
is_used = input('Have you used the item at all [y/n]? ')
is_broken = input('Has the item broken down on its own [y/n]? ')
if purchase_days_ago <= 14 and is_used == 'n' or is_broken == 'y':
  print('Refund')
else:
  print('No refund')

# finding leap years
year = int(input('Provide a year: '))
if year%4 == 0:
  if year%100 == 0:
    if year%400 == 0:
      print('leap year')
    else:
      print('not a leap year')
  else:
    print('leap year')
else:
  print('not a leap year')
# finding even numbers in a program
user_number = int(input('Provide a number: '))
if user_number%2 == 0:
  print('even number')
else:
  print('odd number')

hours = int(input('Provide the number of hours worked in a month: '))
if hours <= 160:
  print('total earnings', (hours * 10))
else:
  print('total earings',((hours * 10) + (hours - 160)*15))

# grades
score = int(input('What was the test score? '))
if score > 89:
  print('A')
elif (score > 79):
  print('B')
elif (score > 69):
  print('C')
elif (score > 59):
  print('D')
else:
  print('F')

# LOOPS
for i in range(1, 11):
  print('Current value:', i)
for number in range(1,21):
  print('number:',number)

current_age = int(input('What is your age? '))
for i in range(2, 6):
  future_age = int(current_age) + i
  print('In ' + str(i) + ' years, you will be ' + str(future_age) + ' years')

# loop with strings
user_input = input('Please provide a password: ')
digits = 0
for number in user_input:
  if number.isnumeric(): digits += 1
print('Your password contains',digits,'digits.')

# while loop
counter = 1
while counter <= 10:
  print('Current value:', counter)
  counter = counter + 1
counter = 2
while counter <= 10:
  print('Current value:', counter)
  counter = counter + 2
value = 2
print('Here are some powers of 2!')
while value <= 1024:
  print(value)
  value *= 2
else:
  print('That\'s enough')

# while loops for use input
user_input = input('Please provide a number: ')
while not user_input.isnumeric():
  user_input = input('Not a number! Please provide a number: ')
print('Your number is:', user_input)

# loops for user input
secret_number = 7
user_input = int(input('Guess the secret number (0-9): '))
while user_input != secret_number:
  user_input = int(input('Wrong, Try again (0-9):'))
print('Correct')

# nested
for i in range (1, 11):
  for j in range (1, 11):
    print(i, 'x', j, '=', i*j)

#nested for loops
line = ''
for i in range (1,10):
  for j in range (0,9):
    line += str(i)
  print(line)
  line = ''

# nested while loops
final_score = 0
counter = 0

while counter < 10:
  current_number = input('Please provide a number to add: ')
  while not current_number.isnumeric():
    current_number = input('That\'s not a number! Try again: ')
  final_score += int(current_number)
  counter += 1

print('The score is', final_score)

# nested while loops
n_numbers = int(input("How many numbers will be given? "))
counter = 0
sum = 0
while counter < n_numbers:
  new_no = input('Provide a number:')
  while not new_no.isnumeric():
    new_no = input('Wrong! That\'s not a number! Try again:')
  sum += int(new_no)
  counter += 1
print('Mean:',sum/ n_numbers)

# using break with loops
user_input = input('Please provide a number: ')
while True:
  if user_input.isnumeric():
    break
  user_input = input('Not a number! Please provide a number: ')
print('Your number is:', user_input)

year = input('In which year was Python first released? ')
while True:
  if int(year) == 1990:
    break
  year = input('In which year was Python first released?')
print('Correct', year)

# break with for loops
user_input = input('Please provide a nickname for yourself. Don\'t use digits! ')
is_valid = True
for character in user_input:
  if character.isdigit():
    is_valid = False
    break

if is_valid == True:
  print('Nickname correct!')
else:
  print('Nickname incorrect!')

user_number = int(input('Please provide a number from 2 to 1000: '))
prime = True
if user_number >= 2 & user_number <= 1000:
  for i in range(2,user_number):
    if user_number % i == 0:
      prime = False
      break
  if prime == True:
    print(user_number,'is prime!')
  else:
    print(user_number,'is not prime!')
else:
  print('Incorrect number!')

#continue with while loops
current_value = 0
while current_value < 100:
  current_value += 2
  if current_value % 6 == 0:
    continue
  print(current_value)
print('That\'s enough!')

for number in range(1,16):
  if (number % 5== 0):
    continue
  print('The remainder of dividing'+ str(number) +'by 5 is'+ str(number % 5))


#Use a loop to calculate and print the value of 10 factorial (10!)
score = 1
for i in range(1,11):
  score *= i
print(score)
# program that checks numbers
secret_number = 8
answer = input('Guess our secret number! ')
while True:
  if int(answer) == secret_number:
    break
  elif int(answer) < secret_number:
    print('Too small')
  elif int(answer) > secret_number:
    print('Too big')
  answer = input('Try again')
print('Correct!')

# printing line patterns
printing_line = ''
for i in range(8):
  for j in range (12):
    if (i+j) % 2:
      printing_line += '='
    else:
      printing_line += '-'
  print(printing_line)
  printing_line = ''

#Functions
def show_amazing_skills():
  print('I can write my own function!')
# function that prints numbers
def print_numbers_to(number):
  for i in range(1,number + 1):
    print(i)
print_numbers_to(50)
#Conversion
def convert(amount,rate):
  print('Amount:',amount,'Rate:',rate,'Conversion:',amount*rate)
convert(55,1.75)

#Functions with return
def return_bigger(a,b):
  if a > b:
    return a
  elif b > a:
    return b
  else:
    return 0
def factorial(number):
  score = 1
  while number > 1:
    score = score * number
    number = number - 1
  return score

def find_divisors(x):
  for i in range(2,x):
    if x % i == 0:
      print(i)
find_divisors(20)

##defining default values
def dog_to_human_age(dog_age=1):
  return dog_age*7
print(dog_to_human_age(3))
print(dog_to_human_age())

def water_supply(age=75,amount=2):
  litres = age*365*amount
  return litres
##mandatory and optional arguments
def calculate_area(r,pi=3.14): ##start listing the mandatory arguments first
  area = pi*r*r
  return area
def calculate_cone_area(r=1, pi=3.14, h=1):
  return (1.0/3) * pi * r * r * h
calculate_cone_area(r=5, h=3)

##Using NONE
def safe_division(x, y):
  if y == 0:
    return None
  else:
    return x/y

print(safe_division(2, 5))
print(safe_division(2, 0))

def sum_between(a,b):
  if b < a:
    return None
  sum = 0
  for i in range(a, b+1):
    sum += i
  return sum
sum_between(1,3)
##PASS 'do nothing': signify that you've still yet to write the actual implementation.
def do_nothing():
  pass
print(do_nothing())

#Invoing functions within functions
def contains_digits(word):
  for letter in word:
    if letter.isnumeric():
      return True
  return False

def contains_letters(word):
  for letter in word:
    if letter.isalpha():
      return True
  return False

def validate_password(password):
  if not contains_letters(password) or not contains_digits(password):
    return False
  else:
    return True

#Calculating tax, Invoking function within functions
def calculate_social_contribution(amount):
  if amount < 200:
    return 0
  elif amount < 1000:
    return 100
  else:
    return 200
def calculate_tax(amount):
  if amount >3000:
    return 300+(0.2*(amount-3000))
  else:
    return 0.1*amount
def convert_gross_to_net(salary):
  print('Your salary gross:',salary)
  after_social = salary - calculate_social_contribution(salary)
  print('Salary after social contribution:',after_social)
  after_tax = after_social - calculate_tax(after_social)
  print('Net salary after tax:',after_tax)

#Documenting functions
def calculate_price(weight, price_per_pound=1.5, tax=0.15):
  """Calculate price for a amount

  Keyword arguments:
  weight -- weight expressed in pounds
  price_per_pound -- price paid per one pound
  tax -- the tax value that needs to the price
  """
  return weight * price_per_pound * (1 + tax)

##Factorial
def factorial(number):
  score = 1
  for i in range(1, number+1):
    score = score * i
  return score

##Functon that Draws patterns
def draw_pattern(rows=5,columns=8):
  line_to_print = ''
  for i in range (0,rows):
    for j in range(0,columns):
      if i % 2 == 0:
        if j % 2 == 0: line_to_print += '-'
        else: line_to_print += '='
      else:
        if j % 2 == 0: line_to_print += '='
        else: line_to_print += '-'
    print(line_to_print)
    line_to_print = ''

def find_monthly_savings(amount,years):
  if amount < 0 or years <= 0:
      return None
  else:
    return amount/(years*12)

#Function to calculate printing costs
count_posters = int(input('How many posters will be printed? '))
cost = ((count_posters+199)//200)*50 + count_posters * 1.25
print('This will cost', cost, 'USD.')

#Code that prints the smallest letters
a = int(input('a=? '))
b = int(input('b=? '))
c = int(input('c=? '))
if a<b and a <c:
  print (a)
elif b<c:
  print (b)
else:
  print (c)

#Code that asks user for numbers and finds the mean for the numbers
count_numbers = int(input('How many numbers do you have? '))
average_value = 0
for i in range(0,count_numbers):
  count_number = int(input('Provide a number:'))
  average_value += count_number
print('The average is', average_value/count_numbers)

#Code that calculates the cost of cr rental that offers free in day 7
def calculate_rental_cost(days=1,age=30):
  if age < 30:
    fare = 220
  else:
    fare = 100
  discount = days // 7
  days = days - dis
  return days * fare

#code that asks user's name
name = input('Hello, what is your name?')
print('Hello',name)

#code that checks for odd/ even numbers
def print_parity(number):
  if number % 2 == 0:
    print('You provided an even number')
  else:
    print('You provided an odd number')

#code that prints multiples of numbers
def print_multiples(n,max):
  for i in range(n,max+1):
    if i%n==0:
      print(i)
print_multiples(4,28)

#Working with Lists
water_level = [730,709,682,712,733,751,740]
print(water_level)
print(water_level[2])# python is zero indexed
water_level = [730, 709, 682, 712, 733, 751, 740]
water_level.append(772) ##Appending values/ elements to a list
print(water_level)
water_lele = [745, 675, 745]
water_level = water_level + water_lele ##Adding lists/ combining/ merging
del water_level[0] ##Deleting an element in a list
water_level.remove(730) ##Deleting elements by value

## the IN operator
tourist_arrivals = [7.8, 9.0, 10.4, 10.9, 14.7, 15.6, 22.7, 22.3, 14.8, 11.4, 8.6, 9.1]
number = float(input('Enter monthly arrivals: '))
if number in tourist_arrivals:
  print('Value found')
else:
  print('Value not found')

#length
tourist_arrivals = [7.8, 9.0, 10.4, 10.9, 14.7, 22.7, 22.3, 14.8, 11.4, 8.6, 9.1]
if len(tourist_arrivals) != 12:
    print('Incorrect number of months.')

#Iterating over elements
tourist_arrivals = [7.8, 9.0, 10.5, 10.6, 14.7, 15.6, 22.5, 22.5, 14.1, 11.1, 8.6, 9.1]
for i in tourist_arrivals:
  print(str(i)+' million tourist should increase to '+str(i *1.08))

#Iterating over elements with indicies
tourist_arrivals = [7.8, 9.0, 10.4, 10.9, 14.7, 15.6, 22.7, 22.3, 14.8, 11.4, 8.6, 9.1]
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
for i in range(0,len(tourist_arrivals)):
  print('Tourist arrivals in '+months[i]+' 2016 were '+str(tourist_arrivals[i])+' million people')

#Lists with if and loops
supermarkets = ['Tesco', 'Aldi', 'Morrisons', 'Co-op', 'Iceland']
if 'Lidl' not in supermarkets:
  supermarkets.append('Lidl')

#Lists with if and loops
world_population = [7128, 7213, 7299, 7383, 7467, 7550, 7633]
for i in range(1,len(world_population)):
  if (world_population[i] - world_population[i-1]) > 0:
    print('In year '+str(2012+i)+', the increase in population was '+str(world_population[i] - world_population[i-1])+' millions')

#Lists as function arguments
def count_even(numbers):
  counter = 0
  for evenn in numbers:
    if evenn % 2 == 0:
      counter +=1
  return counter ## program that returns/ counts even numbers given a lists

#del in lists
def delete_first_element(input_list):
  del input_list[0]
sample_list = [1, 2, 3, 4, 5]
print(sample_list)
delete_first_element(sample_list)
print(sample_list)

#Returning lists from functions
def delete_first_element(input_list):
  copy_list = list(input_list)
  del copy_list[0]
  return copy_list
sample_list = [1, 2, 3, 4, 5]
print(sample_list)
new_list = delete_first_element(sample_list)
print(sample_list, new_list)

#Function of list that returns absolute values
def get_absolute_values(list_a):
  for i in range(0,len(list_a)):
    if list_a[i]<0:
      list_a[i] = -list_a[i] ## a program ensuring all numbers in a list are absolute

absolutes = [13, -15, 42, -165, 32, -678, 1, 41]
def get_absolute_values(input_list):
  copy_list = list(input_list)
  for i in range(0, len(copy_list)):
    if copy_list[i] < 0:
      copy_list[i] = -copy_list[i]
  return    ### a program ensuring all numbers in a list are absolute
get_absolute_values(absolutes)

experiment_results = [12, 47, 8, 9, 1, 7]
experiment_results.remove(max(experiment_results))##deleting max value
experiment_results.remove(min(experiment_results))## deleting min value

##DICTIONARIES
os_releases = {2015:'Windows 10',2013:'Windows 8.1',2012:'Windows 8',2009:'Windows 7',2007:'Windows Vista'}
print(os_releases[2012])# accessing dictionaries
os_releases[2001]='Windows XP'##adding/ editing elements in a dictionary
del os_releases[2001] ##deleting an element from a dictionary

##The in and not in operators
user_key = int(input('Enter a year between 2000 and 2018 to check if there was a major Windows release. '))
if user_key in os_releases:
  print('A major version found:',os_releases[user_key])
else:
  print('No major version found')

#Iterating over dictionaries - keys()
os_releases = {
  2015: 'Windows 10',
  2013: 'Windows 8.1',
  2012: 'Windows 8',
  2009: 'Windows 7',
  2007: 'Windows Vista',
  2001: 'Windows XP'
}
for key in os_releases.keys():
  print(os_releases[key],'was released in',key)

##Iterating over dictionary elements
os_lengths = dict()  #creating a new empty dictionary
for value in os_releases.values():
  os_lengths[value] = len(value)

##Iterating over dictionary items
os_releases = {
  2015: 'Windows 10',
  2013: 'Windows 8.1',
  2012: 'Windows 8',
  2009: 'Windows 7',
  2007: 'Windows Vista',
  2001: 'Windows XP'}
for key, value in os_releases.items():
  print(value, 'was released in', key, '-', (key-1985), 'years after Windows 1.0')

##Prrogram that splits words in a dictionary
user_input = input('Please provide some text: ')
word_frequencies = dict()
for word in user_input.split():  ##we use split() to enable us iterate over the words and not characters
  if word in word_frequencies:
    word_frequencies[word]+=1
  else:
    word_frequencies[word]=1

# dictionaries as function arguments
def max_value(diction):
  max = 0
  for value in diction.values():
    if value > max:
      max = value
  return max

##NB we modify the original dictionary, so any changes inside will affect the dictionary passed in as the argument.
def zero_negative(dictionary_to_check):
  for key in dictionary_to_check.keys():
    if dictionary_to_check[key] < 0:
      dictionary_to_check[key] = 0

def add_ten(dictioanry):
  for key in dictioanry.keys():
    if dictioanry[key] % 2 == 0:
      dictioanry[key] += 10  ##The function should add 10 to every even value in the dictionary.

##Returning dictionaries from functions
def add_ten(dictionary):
  new_dictionary = dictionary.copy()
  for key in new_dictionary.keys():
    if new_dictionary[key] % 2 == 0:
      new_dictionary[key] += 10
  return new_dictionary

base_prices = {'shoes': 235,'t-shirt': 49,'pullover': 109}
discounts = {'shoes': 40,'pullover': 9}

def calculate_discount(base_prices, discounts):
  discounted_prices = base_prices.copy()
  for key, value in base_prices.items():  ## iterating over dictionary use
    if key in discounts:
      discounted_prices[key] -= discounts[key]
  return discounted_prices ## program that checks for discounts in items in a dictionary

## code that maps letters to morse code
morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
         'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
         'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
         'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
         'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
         '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
         '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--'}
def translate_into_morse(text):
  text = text.upper()
  target = ''
  for letter in text:
    if letter in morse.keys():
      target += morse[letter]
    else:
      target += letter
  return target
## code tht calculates prices based on a customer's order
pricelist = {'bread': 2.37, 'ham': 3.48, 'cheese': 3.09, 'water': 1.19, 'coke': 2.58, 'juice': 4.18, 'butter': 5.18}
def calculate_price(order):
  amount = 0.0
  for key, value in order.items():
    if key in pricelist:
      amount += value * pricelist[key]
  return amount

## Operating files in python
##Text files
file = open('daily_sales.txt') ##open() function opens a file whose filename is given as the argument.
print(file.read()) #file.read(). As you can see, you can pass that result to print() to show the file's contents
file.close() #closes the file so you can no longer read it (unless you open it again).

##The open() function can actually take a second (optional) argument: the mode in which the file should be opened.
# When the second argument is not provided, the default value is chosen as 'r' (read only). The most basic modes are:
# 'r' – read: a file can only be read,
# 'w' – write: a file with the given name is created (or overwritten if it already exists) for writing only,
# 'a' – append: a file with the given name is opened for adding new information at the end.
file = open('daily_sales.txt', 'r')
print(file.read())
file.close()

## writing to a file
nickname = input('What is your nickname? ')
age = input('What is your age? ')
file = open('user_data.txt', 'w')
file.write('Nickname: ' + nickname + '\n')
file.write('Age: ' + age)
file.close()

## Appending to a file
file = open('daily_sales.txt','a')
file.write('\nDay 8 (Monday): 19432.19')
file.write('\nDay 9 (Tuesday): 18233.76')
file.write('\nDay 10 (Wednesday): 23432.43')
file.close()

## reading files line by line
# NB files are sequences in python
max_no = 0
file = open('random_numbers.txt','r')
for line in file:
  if int(line) > max_no:
    max_no = int(line)
file.close()
print(max_no)

#A student wants to download past examinations in all the subjects given in the subjects list of the template code
subjects = ['math', 'biology', 'chemistry', 'physics']
file = open('urls.txt','w')
for subject in subjects:
  for i in range(2010, 2019):
    file.write('http://imaginary-site.com/download/'+str(subject)+'-'+str(i)+'\n')
file.close()

## Using the WITH statement
with open('employees.txt', 'r') as file:
  for line in file:
    print('Employee: ' + line)

nickname = input('What is your nickname? ')
age = input('What is your age? ')
with open('user_data.txt', 'w') as file:
  file.write('Nickname: ' + nickname + '\n')
  file.write('Age: ' + age)

##Exceptions and IOerror (IO - Input Output error)
file_name = input('Provide a file name: ')
try:
  with open(file_name, 'r') as file:
    print('Read the file successfully!')
    print(file.read())
except IOError:
  print('The file does not exist!')

# ValueError
while True:
  try:
    x = int(input('Provide a number: '))
    break
  except ValueError:
    print('That is not a number! Try again. ')
#Ex 2
while True:
  try:
    file_name = input('Provide a file name: ')
    with open(file_name,'r') as file:
      print(file.read())
    break
  except IOError:
    print('Could not read the file. Try another one.')


##Count the number of positive numbers in the file, and print that value to the output.
# Some lines may contain letters instead of digits. In such cases, simply ignore them and move on to subsequent lines.
number = 0
with open('question_2.txt') as file:
  for line in file:
    try:
      if int(line) > 0:
        number += 1
    except ValueError:
      continue
print(number)

##Write a function named is_palindrome(word) that takes a word and returns either True or False.
def is_palindrome(word):
  letters = list(word)
  while len(letters) > 1:
    if letters[0] != letters[len(letters)-1]:
      return False
    else:
      del letters[0]
      del letters[len(letters)-1]
  return True

def count_word(file, word):
  counter = 0
  with open(file, 'r') as file:
    for line in file:
      if word in line:
        counter += 1
  return counter

# Write a function named find_total_product_price(pricelist, product, quantity),
# where pricelist is a dictionary with String keys (product names) and float values (prices for single pieces).
# If product is present in pricelist, return the total price for {quantity} pieces of {product}.
# If the product is not present in 'pricelist', return 0.0 instead.

def find_total_product_price(pricelist, product, quantity):
  if product in pricelist:
    return pricelist[product] * quantity
  else:
    return 0.0

##Write a function named second_powers() that accepts a natural number x.
##Next, the function returns a dictionary that will map each even number from 2 to x to its second power.
def second_powers(x):
  dictionary = {}
  for x in range (2, x+1):
    if x % 2 == 0:
      dictionary [x] = x*x
  return dictionary
second_powers(6)

## Tuples
##lists are typically homogeneous (storing values of a single type),
# while tuples may be heterogeneous (storing values of multiple types)
train_connection = ('Paris','Lyon',393,45.00)
train_conn = () ## empty tuple
from_city = ('Paris',)  ## single element tuple
print(train_connection[3]) ## selecting the last element
print(train_connection[1:3])  # selecting the 1 and 2 element
## NB tuples are immutable (cannot be changed)

# Iterating over tuples
train_connection = ('Paris', 'Lyon', 393, 45.00)
for item in train_connection:
  print('Train connection data of type', type(item), 'found:', item)

##Count the number of train connections that contain the string 'Paris'. Then, print the following information:
train_connections = [
  ('Paris', 'Lyon', 393, 45.00),
  ('Marseille', 'Nice', 200, 24.00),
  ('Nantes', 'Paris', 380, 42.00),
  ('Nantes', 'Montpellier', 811, 91.00),
  ('Paris', 'Grenoble', 580, 67.00),
]
number = 0
for i in train_connections:
  if 'Paris' in i:
    number += 1
print('There are ', number, 'train connections from/to Paris.')

#ex 2
train_connections = [
  ('Paris', 'Lyon', 393, 45.00),
  ('Marseille', 'Nice', 200, 24.00),
  ('Nantes', 'Paris', 380, 42.00),
  ('Nantes', 380, 42.00),
  ('Nantes', 'Montpellier', 811, 91.00),
  ('Paris', 'Grenoble', 580, 67.00),
  ('Paris', 'Nice', 580),
]
for item in train_connections:
  if len(item) < 4:
    print('Missing train information for tuple: ',item)

## unpacking tuples to independent variables
train_connection = ('Nantes', 'Montpellier', 811, 91.00)
from_city, to_city, distance, price = train_connection

## This function should accept a list of tuples containing train connection data.
# Your task is to add up all the distances from each connection and store the result in a variable named total_distance.
# Similarly, add up all the ticket prices and store the result in a variable named total_price.
# The function should return a tuple with the following elements: (total_distance, total_price)

train_connections = [
  ('Paris', 'Lyon', 393, 45.00),
  ('Lyon', 'Nice', 200, 24.00),
  ('Nice', 'Nantes', 380, 42.00),
  ('Nantes', 'Montpellier', 811, 91.00)
]
def get_total_distance_price(train_connections):
  total_distance = 0
  total_price = 0.0
  for item in train_connections:
    total_distance += item[2]
    total_price += item[3]
  return (total_distance, total_price)
get_total_distance_price(train_connections)

##The function should accept any number of arguments and
# return the difference between the greatest and smallest numbers.
# If zero or one argument is passed, return 0.

def min_max_difference(*args):
  if len(args) == 0:
    return 0
  min = args[0]
  max = args[0]
  for item in args:
    if item > max:
      max = item
    if item < min:
      min = item
  return max - min

#Write a function named get_circle_circumference_area(r) that
# accepts a single argument – the radius of a circle – and calculates its circumference and area.
# Return a tuple with both of these values in that order (circumference first, then area).
def get_circle_circumference_area(r):
  circumference = 2 * 3.14 * r
  area = 3.14 * r * r
  return (circumference, area)


##Write a function named get_biggest_apartment_area_price(apartments).
## The function should accept a list of tuples with apartment data.
# For the apartment with the biggest area, return a tuple with two elements: (area, price).
apartments = [
  ('12 Park Ave', 2, 78.5, 475000),
  ('15 Washington St', 3, 97.0, 685000),
  ('27 Lake St', 1, 46.7, 380000),
  ('3 Lake Ave', 2, 62.3, 420000)
]
def get_biggest_apartment_area_price(apartments):
  area = apartments [0][2]
  price = apartments [0] [3]
  for item in apartments:
    if item[2] > area:
      area = item[2]
    if item[3] > price:
      price = item [3]
  return (area, price)


#Importing Kmeans into python
from sklearn.cluster import Kmeans
Y = Kmeans(n_clusters = 3, random_state=random_state).fit_predict(X)
