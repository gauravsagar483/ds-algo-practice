"""
Given coordinates of a source point (x1, y1) determine if it is possible to reach the destination point (x2, y2). From any point (x, y) there only two types of valid movements: 
(x, x + y) and (x + y, y). Return a boolean true if it is possible else return false. 
Note: All coordinates are positive. 

"""

# Recursion


def is_reachable(x, y, dx, dy):

    # base case

    if x > dx or y > dy:
        return False

    if x == dx and y == dy:
        return True

    return is_reachable(x, x + y, dx, dy) or is_reachable(x + y, y, dx, dy)


if __name__ == "__main__":

    res = is_reachable(2, 10, 26, 12)

    if res == True:
        print("Reachable")
    else:
        print("Not Reachable!!")
