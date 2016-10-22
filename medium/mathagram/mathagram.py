# https://redd.it/576o8o
# F:\Documents\dailyProgrammer\medium\mathagram
# mathagram.py
from time import clock
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
							
		self.first = first
		self.second = second
		self.third = third
		self.fourth = fourth
		self.fifth = fifth
		self.sixth = sixth
		self.seventh = seventh
		self.eighth = eighth
		self.ninth = ninth
		if self.input.count(None) == 6:
			self.level = 1
			# print "Double"
		elif self.input.count(None) == 3:
			self.level = 2
			# print "Single"
		else:
			self.level = 3
		self.unused_nums *= self.level					
							
		for opt in self.input:
			if not opt is None:
				for char_ in opt:
					try:
						if int(char_) in self.unused_nums:
							self.unused_nums.remove(int(char_))
					except ValueError:
						pass

		# print self.unused_nums
		self.unused_nums.sort()
		# print self.unused_nums
			
	def guess(self):
		abc  = []
		if self.level >= 1:
			a = list(self.first)
			b = list(self.second)
			c = list(self.third)
			abc.append(a)
			abc.append(b)
			abc.append(c)
		if self.level >= 2:
			d = list(self.fourth)
			e = list(self.fifth)
			f = list(self.sixth)
			abc.append(d)
			abc.append(e)
			abc.append(f)
		if self.level == 3:
			g = list(self.seventh)
			h = list(self.eight)
			i = list(self.ninth)
			abc.append(g)
			abc.append(h)
			abc.append(i)
		
		# solved = False
		# while solved == False:
		temp = self.unused_nums
		for idx,x in enumerate(abc):
			if x != None:
				for i, int_ in enumerate(x):
					if int_ == 'x':
						guess = randint(0, (len(temp)-1))
						replace = temp[guess]
						x[i] = str(replace)
						temp.remove(replace)
				attempt = int(''.join(x))
				abc[idx] = attempt
			# print attempt
		# print abc[0], abc[1], abc[2]
		# print "{} + {} = {} : {}".format(abc[0], abc[1], abc[2], (abc[0] + abc[1]))
		if self.level == 1:
			if (abc[0] + abc[1]) == abc[2]:
				print "{} + {} = {}".format(abc[0], abc[1], abc[2])
				return True
			else:
				print False
				return False
		elif self.level == 2:
			if (abc[0] + abc[1] + abc[2] + abc[3]) == (abc[4] + abc[5]):
				print "{} + {} + {} + {} = {} + {}".format(abc[0], abc[1], 
																					 abc[2], abc[3], 
																					 abc[4], abc[5]
																					 )
				return True
			else:
				print False
				return False
		elif self.level == 3:
			pass
			"""
			if (abc[0] + abc[1]) == abc[2]:
				print True
				solved = True #not sure why indenting this gives me an error
			else:
				print False
			"""
		
		

solved = False
c = 0

m = mathagram('xxx', 'xxx', '5x3', '123', 'xxx', '795')
m.guess()
"""

start = clock()
while solved == False:
	m = mathagram('xxx', 'xxx', '23x', '571', 'xxx', 'x82')
	solved = m.guess()
	c += 1
else:
	elapsed = (clock() - start)
	print "{} attempts in {} seconds".format(c, round(elapsed, 2))
"""