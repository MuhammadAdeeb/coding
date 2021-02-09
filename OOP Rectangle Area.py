# why have getters and setters and how

class Square:
    def __init__(self, height=0, width=0):
        self.height = 0
        self.width = 0

    @property  # allow us to refer to these indiv fields inside of here to get these values
    def height(self):
        print("Retrieving the Height")

        return self.__height  # __ to protect the data

    @height.setter
    def height(self, value):
        # to protect height from bad values(alphabets etc)
        if isinstance(value, float):
            self.__height = value
        else:
            print("Please only numerical value for height")

    @property  # same thing for width
    def width(self):
        print("Retrieving the Width")

        return self.__width  # __ to protect the data

    @height.setter
    def width(self, value):
        # to protect height from bad values(alphabets etc)
        if isinstance(value, float):
            self.__width = value
        else:
            print("Please only numerical value for width")

    def getArea(self):
        return self.__width * self.__height


def main():
    aSquare = Square()

    height = input("Enter Height: ")
    width = input("Enter Width: ")

    height = float(height)
    width = float(width)

    aSquare.width = width
    aSquare.height = height

    print("Height = ", height)
    print("Width = ", width)

    print("The Area is ", aSquare.getArea())


main()

