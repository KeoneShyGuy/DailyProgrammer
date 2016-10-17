# https://redd.it/56tbds
# F:\Documents\dailyProgrammer\easy\Kaprekar
# python KaprekarRoutine.py 56

class KaprekarRoutine(object):
	def __init__(self, num__):
		if 0 <= num__ <10000 and str(num__).count(str(num__)[0]) != 4:	#make sure it's a positive, 4-digit number
			self.num__ = int(num__)
		else:
			print "That number won't work"
			raise StandardError		
		self.numString = str(self.num)
		if len(self.numString) <= 4:
			self.numString = self.numString.zfill(4)
		self.numArray = list(self.numString)
		
	@property	
	def largest_digit(self):
		largest = 0
		for int__ in self.numString:
			if int(int__) > largest:
				largest = int(int__)
		return largest
	
	def ascend_digits(self, ):
		arr__ = sorted(self.numArray)
		ascend = ''.join(arr__)
		return int(ascend)

	def descend_digits(self):
		arr__ = sorted(self.numArray)
		arr__.reverse()
		descend = ''.join(arr__)
		return int(descend)
		
	@property
	def num_string(self):
		return self.numString
	@property
	def num(self):
		return self.num__
		
	@num.setter
	def num(self, num):
		self.num__ = num
		self.numArray = list(str(self.num).zfill(4))
		
	def diff(self):
		return self.descend_digits() - self.ascend_digits()
		
	def routine(self):
		c = 0
		while self.num != 6174:
			self.num = self.diff()
			# print self.num
			c += 1
		return c

"""
if __name__ == "__main__":
	from sys import argv
	script, number = argv
	kr = KaprekarRoutine(int(number))
	print kr.routine()
"""	
largest = 0
winner = 0
winners = []

for i in range(1, 10000):
	if str(i).count(str(i)[0]) != 4:
		temp = KaprekarRoutine(i)
		steps = temp.routine()
		# print "Number: {} | Step: {}".format(i, steps)
		if steps > largest:
			winners = []
			winners.append(i)
			largest = steps
			winner = i
		elif steps == largest:
			winners.append(i)

print winners
print "There are {} numbers that have {} steps".format(len(winners), largest)