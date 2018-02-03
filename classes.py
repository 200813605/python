#!/usr/bin/env python

class square():
        def __init__(self,length):
		self.side = length

	def getArea(self):
		return self.side * self.side

	def getPerimiter(self):
                return self.side * 4


myshapes = [
    square(2),
    square(3),
    square(4),
    square(5)
]

myshapes.append(square(6))

for s in myshapes:
    print("My Area is %d and my perimiter is %d" % (s.getArea(), s.getPerimiter()))
