def in_area(x_1, y_1, x_2, y_2):
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
fire_blast(1, 2, 1)