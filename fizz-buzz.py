for i in range(1,101):
	s=''
	if (i%3==0):s+='Fizz'
	if (i%5==0):s+='Buzz'
	print(s) if s else print(i)
