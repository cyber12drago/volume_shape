class Beam(object):

    def __init__(self, base, width, height):
        self.base = base
        self.width = width
        self.height = height

class VolumeCalculator(object):

    def __init__(self, shapes):

        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_volume(self):
        total = 0
        for shape in self.shapes:
            total += shape.base * shape.width * shape.height

        return total

def check_number(number):
    if (number is not None):
        if (number > 0):
            return number
        
def main():
    base1 = check_number(float(input()))
    print(base1)
    width1 = check_number(float(input()))
    height1 = check_number(float(input()))

    base2 = check_number(float(input()))
    width2 = check_number(float(input()))
    height2 = check_number(float(input()))
    
    shapes = [Beam(base1, width1, height1), Beam(base2, width2, height2)]
    calculator = VolumeCalculator(shapes)
    print ("The total area is: ", calculator.total_volume)

if __name__ == '__main__':

    main()