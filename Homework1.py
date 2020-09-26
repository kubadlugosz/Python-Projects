#Homework 1
# I worked on this by myself

#Q1a
first_name = input('What is your first name?: ')
last_name = input('What is your last name?: ')
print('Your name is'+' '+first_name+' '+last_name)

#Q1b
account_balance =float(input('What is your account balance: '))
interest_rate = float(input('What is the interest rate: '))
print((account_balance*(interest_rate/100))+account_balance)


#Q2
colors = ['red','blue','yellow','green','orange','purple']
color_choice = input('What is your favorite color?: ')
if color_choice in colors:
	print('I like that color too')
else:
	print('I do not like that color')


#Q3

yes_votes = float(input('How many yes votes:'))
no_votes = float(input('How many no votes:'))
probability = (yes_votes/(yes_votes+no_votes))
if probability > 0.5:
	print('Pass')
else:
	print('Fail')


#Q4a
list_numbers =[1,2,3,4,5,6,7,2,9,10]
def isNumberPresent(list_of_numbers, number_choice):
		if number_choice in list_of_numbers:
			return True
		else:
			return False

names =['antheil','saint-saens', 'price', 'easdale', 'nielsen']
def composers(list_of_composers):
	"""
	for i in range(0,len(list_of_composers)):
		first_letter = list_of_composers[i][0]
		last_letter = list_of_composers[i][-1]
		if first_letter == last_letter:
			print(list_of_composers[i])
	"""
	for i in list_of_composers:
		
		if i[0]==i[-1]:
			print(i)

def main():

	print(isNumberPresent(list_numbers,2))
	print(composers(names))

main()