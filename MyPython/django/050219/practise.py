
try:
	
	# e # -- Name Error
	a =5
	b= 6
	# c = a + 'b ' # Type Error
	# import k # ModuleNotFouldError
	# open('file1.txt') # FileNotFoundError
	c= a + int('b') # Value Error
	print('Try Block Code True :', c)
except NameError:
	print('Name Error Exception ')
except TypeError:
	print('Type Error Exception ')
except ModuleNotFoundError:
	print('ModuleNotFouldError Exception ')
except FileNotFoundError:
	print('FileNotFoundError Exception Block')
except ValueError:
	print("Value Error Exception")
else:
	print('Try block true')

	
