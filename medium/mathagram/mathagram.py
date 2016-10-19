class mathagram(object):
	
	def __init__(self, first, second, third, 
	                     fourth=None, fifth=None, sixth=None,
						 seventh=None, eighth=None, ninth=None):
		self.level = 0				 
		self.unused_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		self.input = [first, second, third, fourth, fifth, sixth,
							seventh, eighth, ninth]
		for i,var_ in enumerate(self.input):
			var_[i] = str(var_)
		for option in self.input:
			for char in option:
				try:
					self.unused_nums.remove(char)
				except:
					StandardError
		self.first = first
		self.second = second
		self.third = third
		self.fourth = fourth
		self.fifth = fifth
		self.sixth = sixth
		if (fourth != None) and (fifth != None) and (sixth != None):
			self.level = 2
			print "Double"
		else:
			self.level = 1
			print "Single"
			
		@property
		def level(self):
			return self.level
			
		
		
m = mathagram(7, 6, 9, 1, 3)
print m.level
