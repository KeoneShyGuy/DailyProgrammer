class KaprekarRoutine(object):

	def __init__(self, num__):
		if 0 <= num__ <10000:	#make sure it's a positive, 4-digit number
			self.num = int(num__)
		else:
			print "That number won't work"
		self.numString = str(self.num)
		self.numArray = list(self.numString)
		
	def largest_digit(self):
		largest = 0
		for int__ in self.numString:
			if int(int__) > largest:
				largest = int(int__)
		return largest
		
	def descend_digits(self):
		arr__ = sorted(self.numArray)
		arr__.reverse()
		descend = ''.join(arr__)
		return descend
		
			
kr = KaprekarRoutine(9897)
print kr.largest_digit()
print kr.descend_digits()