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

def main():
    base1 = int(input())
    width1 = int(input())
    height1 = int(input())

    base2 = int(input())
    width2 = int(input())
    height2 = int(input())
    
    shapes = [Beam(base1, width1, height1), Beam(base2, width2, height2)]
    calculator = VolumeCalculator(shapes)
    print ("The total area is: ", calculator.total_volume)

if __name__ == '__main__':

    main()