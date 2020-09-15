class Point:
	
	def __init__(self,  x,  y,  z):		
		self._x = x
		self._y = y
		self._z = z
		
	@property
	def x(self):
		return self._x
		
	@x.setter
	def x(self, value):
		self._x = value
		
	@property
	def y(self):
		return self._y
		
	@y.setter
	def y(self, value):
		self._y = value
		
	@property
	def z(self):
		return self._z
		
	@z.setter
	def z(self, value):
		self._z = value
		
	def __add__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		z = self.z + other.z
		return x, y, z
		
	def __sub__(self, other):
		x = self.x - other.x
		y = self.y - other.y
		z = self.z - other.z
		return x, y, z
		
	def __mul__(self, other):
		x = self.x * other.x
		y = self.y * other.y
		z = self.z * other.z
		return x, y, z
		
	def __truediv__(self, other):
		try:
			x = self.x / other.x
			y = self.y / other.y
			z = self.z / other.z
		except ZeroDivisionError:
			print("Error. You can't divide by zero !")
		else:
			return x, y, z
		
	def __abs__(self):
		x = abs(self.x)
		y = abs(self.y)
		z = abs(self.z)
		return x, y, z
	