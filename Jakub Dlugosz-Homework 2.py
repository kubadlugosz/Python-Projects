#CSC 401 Homework #2
#I worked on this alone
#Homework 2
#I worked on this by myself

#Q1
lst =['Antheil', 'SaintSaens', 'Price', 'Easdale', 'Nielsen']
def composers(l):
	for name in l:
		first_letter = name[0]
		last_letter = name[-1]
		if first_letter == last_letter:
			print(name)
		elif first_letter.upper() == last_letter:
			print(name)
		elif first_letter == last_letter.upper():
			print(name)
		
#Q2a

def password_check(oldpwd, newpwd):
	if oldpwd != newpwd and len(newpwd)==8:
		for i in newpwd:
			if i.isdigit() or i in ['!',',','.','@','#','$','%','^','&','*','(',')']:
				return True
	else:
		return False

#Q2b
def wordOccurCounter(sentence, word):
	sentence = sentence.replace(',','').replace('.','')
	sentence = sentence.split()
	count = 0
	for i in sentence:
		if i == word.upper() or i == word.capitalize() or i== word:
			count += 1
	return count

#Q3
def multLine(line, numCount):
	product = []
	for i in range(1,numCount+1):
		product.append(line*i)
	product = str(product)
	product = product.replace('[','').replace(']','')
	print('{}: {}'.format(line, product))

#Q4a
def numVowels(filename):
	infile  =  open(filename, 'r')
	count = 0
	for line in infile.readline():
		if line in ['a', 'e', 'i', 'o', 'u'] or line.upper in ['A','E','I','O','U']:
			count += 1
	print(count)
	infile.close()

#Q4b
def merge(file1, file2):
	infile1 = open(file1,'a')
	infile2 = open(file2,'r')
	for line in infile2.readlines():
		infile1.write('{}\n'.format(line))
	infile2.close()
	infile1.close()


def main():
	composers(lst)
	print(password_check('abcde','abddy67*'))
	print(wordOccurCounter('THIS movie IS great like REALLY GREAT great Great.', 'great'))
	multLine(1, 12)
	numVowels(r'C:\CSC 401\vowels.txt')
	merge(r'C:\CSC 401\file1.txt', r'C:\CSC 401\file2.txt')
main()