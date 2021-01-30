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
    shapes = [Beam(5, 8, 10), Beam(14, 8, 10)]
    calculator = AreaCalculator(shapes)
    print ("The total area is: ", calculator.total_area)

if __name__ == '__main__':

    main()