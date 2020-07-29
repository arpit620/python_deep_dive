


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive.')
        self._width = width
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('Height must be positive.')
        self._height = height

r1 = Rectangle(10, 20)

print(r1.width)
# r1.width = -10 # Error
# r2 = Rectangle(10, -20) # Error


#$end

##################################################

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        """Call on str or print object"""
        return 'Rectangle (width={0}, height={1})'.format(self.width, self.height)

    def __repr__(self):
        """print string used to recreate the object"""
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

    def __eq__(self, other):
        print('self={0}, other={1}'.format(self, other))
        if isinstance(other, Rectangle):
            return (self.width, self.height) == (other.width, other.height)
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented

r1 = Rectangle(10, 20)
print(str(r1))
print(r1)
# r1 # Rectangle(10, 20)
r2 = Rectangle(10, 20)
print(r1 is not r2)
print(r1 == r2)
print(r1 == 100)

print('*'*10)

r1 = Rectangle(100, 200)
r2 = Rectangle(10, 20)

print(r1 < r2)
print(r2 < r1)
print(r2 > r1)
# print(r2 >= r1) # Error on this as equal to not implemeneted


##################################################

# $end

fn1 = lambda x : x**2

def a():
    pass

print(fn1)
print(fn1(2))
print(a)


