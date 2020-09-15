class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        sign = '+' if self.imag >= 0 else ''
        return '{}{}{}i'.format(self.real, sign, self.imag)

    __repr__ = __str__

    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return Complex(real, imag)

    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return Complex(real, imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.imag * other.real + self.real * other.imag
        return Complex(real, imag)

    def __truediv__(self, other):
        x = self.real * other.real + self.imag * other.imag
        y = self.imag * other.real - self.real * other.imag
        z = other.real ** 2 + other.imag ** 2
        self.new_real = x / z
        self.new_imag = y / z
        if self.new_imag > 0:
            result = "{}+{}i".format(self.new_real, self.new_imag)
        else:
            result = "{}{}i".format(self.new_real, self.new_imag)
        return result


a = Complex(1, 2)
b = Complex(3, 4)
c = a / b
print(c)
