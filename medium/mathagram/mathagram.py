# https://redd.it/576o8o
from random import randint

class mathagram(object):
	
	def __init__(self, first, second, third, 
	                     fourth=None, fifth=None, sixth=None,
						 seventh=None, eighth=None, ninth=None):
		self.level = 0				 
		self.unused_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		self.input = [first, second, third, fourth, fifth, sixth, seventh, eighth, ninth]
		"""
		Need to find a way to cancel the function if the input
		doesn't have 3,6, or 9 values
		"""
							
		for opt in self.input:
			if not opt is None:
				for char_ in opt:
					try:
						if int(char_) in self.unused_nums:
							self.unused_nums.remove(int(char_))
					except ValueError:
						pass

		# print self.unused_nums
		self.first = first
		self.second = second
		self.third = third
		self.fourth = fourth
		self.fifth = fifth
		self.sixth = sixth
		if (fourth != None) and (fifth != None) and (sixth != None):
			self.level = 2
			# print "Double"
		else:
			self.level = 1
			# print "Single"
			
	def guess(self):
		a = list(self.first)
		b = list(self.second)
		c = list(self.third)
		tempList = (a, b, c)
		solved = False
		# while solved == False:
		abc = list(tempList)
		temp = self.unused_nums
		for idx,x in enumerate(abc):
			for i, int_ in enumerate(x):
				if int_ == 'x':
					g = randint(0, (len(temp)-1))
					replace = temp[g]
					x[i] = str(replace)
					temp.remove(replace)
			attempt = int(''.join(x))
			abc[idx] = attempt
			# print attempt
		# print abc[0], abc[1], abc[2]
		# print "{} + {} = {} : {}".format(abc[0], abc[1], abc[2], (abc[0] + abc[1]))
		if (abc[0] + abc[1]) == abc[2]:
			print "{} + {} = {}".format(abc[0], abc[1], abc[2])
			return True
		else:
			return False
			
			"""
			if (abc[0] + abc[1]) == abc[2]:
				print True
				solved = True #not sure why indenting this gives me an error
			else:
				print False
			"""
		
		

solved = False
c = 0
while solved == False:
	m = mathagram('xxx', 'x81', '9x4')
	solved = m.guess()
	c += 1
else:
	print c