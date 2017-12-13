'''
Write a program that prints the integers from 1 to 100.
But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both, print "FizzBuzz".
'''

l = range(1,100)
for i in xrange(len(l)):
	if(i%3==0 and i%5==0):
		l[i-1]="FizzBuzz"
	elif(i%3==0):
		l[i-1]="Fizz"
	elif(i%5==0):
		l[i-1]="Buzz"



print l
