'''def in_area(x_1, y_1, x_2, y_2):
    # Absolutely, did not work.
    x_spots = [i for i in range((x_2 - x_1)+1)]
    y_spots = [j for j in range((y_2 - y_1))]
    #print(f"X positions: {x_spots}")
    #print(f"Y positions: {y_spots}")

in_area(0, 1, 2, 2)

def in_area(x, y):
    if x < 0 or x > 2:
        print(False)
    elif y < 1 or y > 2:
        print(False)
    else:
        print(f"({x}, {y}) is in the dragon's breath")

def fire_blast(x, y, range):
    #(x,y) center of blast
    fire_x1 = x - range
    fire_y1 = y - range
    fire_x2 = x + range
    fire_y2 = y + range
    print(f"({fire_x1}, {fire_y1}) and ({fire_x2}, {fire_y2})",)


#Tests 
in_area(1,1) # True
in_area(0,2) # True
in_area(-1,2) # False
fire_blast(1, 2, 1)'''

class Rectangle:
    def overlaps(self, rect):
        if self.get_left_x() <= rect.get_right_x():
            print("True left is on or let of right")
        else:
            print("False")
            return False

        if self.get_right_x() >= rect.get_left_x():
            print("True right is on or right of left")
        else:
            print("False")
            return False

        if self.get_top_y() >= rect.get_bottom_y():
            print("True top is on or above bottom")
        else:
            print("False")
            return False

        if self.get_bottom_y() <= rect.get_top_y():
            print("True bottom is on or below top")
        else:
            print("False")
            return False

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        if self.__x1 < self.__x2:
            return self.__x1
        return self.__x2

    def get_right_x(self):
        if self.__x1 > self.__x2:
            return self.__x1
        return self.__x2

    def get_top_y(self):
        if self.__y1 > self.__y2:
            return self.__y1
        return self.__y2

    def get_bottom_y(self):
        if self.__y1 < self.__y2:
            return self.__y1
        return self.__y2

    def __repr__(self):
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"
    
A = Rectangle(0, 0, 1, 1)
B = Rectangle(4, 4, 5, 5)
A.overlaps(B)

'''

        value = True
        
        if self.get_left_x() <= rect.get_right_x():
            value = True
        else:
            return False

        if self.get_right_x() >= rect.get_left_x():
            value = True
        else:
            return False

        if self.get_top_y() >= rect.get_bottom_y():
            value = True
        else:
            return False
            
        if self.get_bottom_y() <= rect.get_top_y():
            value = True
        else:
            return False
            
        return value



'''