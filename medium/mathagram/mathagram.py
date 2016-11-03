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
		self.unused_nums = range(1, 10)
		self.input = [first, second, third, fourth, fifth, sixth, seventh, eighth, ninth]
		if self.input.count(None) == 6:
			self.level = 1
		elif self.input.count(None) == 3:
			self.level = 2
		else:
			self.level = 3
		self.unused_nums *= self.level					
		#remove used numbers					
		for opt in self.input:
			if not opt is None:
				for char_ in opt:
					try:
						if int(char_) in self.unused_nums:
							self.unused_nums.remove(int(char_))
					except ValueError:
						pass
		self.unused_nums.sort() # sorted for shits and giggles
			
	def guess(self):
		abc  = []
		if self.level >= 1:
			a, b, c = list(self.input[0:3])
			abc.extend([a, b, c])
		if self.level >= 2:
			d, e, f = list(self.input[3:6])
			abc.extend([d, e, f,])
		if self.level == 3:
			g, h, i = list(self.input[6:9])
			abc.extend([g, h, i])
		# basically replaces 'x' with a random unused number
		for idx,currStr in enumerate(abc):
			if currStr != None:
				currStr = list(currStr)
				for idx_, int_ in enumerate(currStr):
					if int_ == 'x':
						guess = randint(0, (len(self.unused_nums)-1))
						replace = self.unused_nums[guess]
						currStr[idx_] = str(replace)
						self.unused_nums.remove(replace)
				attempt = int(''.join(currStr))
				abc[idx] = attempt
		
		if self.level == 1:
			if (abc[0] + abc[1]) == abc[2]:
				print "{} + {} = {}".format(*abc[0:3])
				return True
			else:
				return False
		elif self.level == 2:
			if (abc[0] + abc[1] + abc[2] + abc[3]) == (abc[4] + abc[5]):
				print "{} + {} + {} + {} = {} + {}".format(*abc[0:6])
				return True
			else:
				return False
		elif self.level == 3:
			if (abc[0] + abc[1] + abc[2] + abc[3] + abc[4]) == (abc[5] + abc[6] + abc[7] + abc[8]):
				print "{} + {} + {} + {} + {} = {} + {} + {} + {}".format(*abc[0:10])
				return True
			else:
				return False
# end of class
# running the class to make the calculations and print pretty things
programStart = clock()
tests = [('1xx', 'xxx', '468'),
		  ('xxx', 'x81', '9x4'),
		  ('xxx', '5x1', '86x'),
		  ('xxx', '39x', 'x75'),
		  ('xxx', 'xxx', '5x3', '123', 'xxx', '795'),
		  ('xxx', 'xxx', '23x', '571', 'xxx', 'x82'),
		  ('xxx', 'xxx', 'xx7', '212', 'xxx', '889'),
		  ('xxx', 'xxx', '1x6', '142', 'xxx', '533'),
		  ('xxx', 'xxx', 'xxx', 'x29', '821', 'xxx', 'xxx', '8xx', '867'),
		  ('xxx', 'xxx', 'xxx', '4x1', '689', 'xxx', 'xxx', 'x5x', '957'),
		  ('xxx', 'xxx', 'xxx', '64x', '581', 'xxx', 'xxx', 'xx2', '623'),
		  ('xxx', 'xxx', 'xxx', 'x81', '759', 'xxx', 'xxx', '8xx', '462'),
		  ('xxx', 'xxx', 'xxx', '6x3', '299', 'xxx', 'xxx', 'x8x', '423'),
		  ('xxx', 'xxx', 'xxx', '58x', '561', 'xxx', 'xxx', 'xx7', '993'),
		  # the one below takes 5-30 minutes to solve
		  ('xxx', 'xxx', 'xxx', 'xxx', 'xxx', '987', '944', '921', '8x5'),
		  ('987', '978', '111', '222', '33x', 'xxx', 'xxx', 'xxx', 'xxx')
		  ]
# main guessing occurs here. Make a new object each time. Not sure if safe.		  
for equation in tests:
	solved = False
	c = 0
	loopStart = clock()
	while solved == False and c <= 1000000:
		m = mathagram(*equation) # <== I learned something new!
		solved = m.guess()
		c += 1
	else:
		if c >= 1000000:
			print "Guessed a hundred thousand times. No answer this time."
			print equation
		else:
			loopElapsed = (clock() - loopStart)
			print "{} attempts in {} seconds.".format(c, round(loopElapsed, 3))
#finalize and beautify
programElapsed = (clock() - programStart)
if programElapsed > 60:
	pMinutes = programElapsed // 60
	pSeconds = programElapsed % 60
	print "All mathagrams calculated in {}:{} minutes.".format(int(pMinutes), round(pSeconds, 3))
else:
	print "All mathagrams calculated in {} seconds.".format(round(programElapsed, 3))
