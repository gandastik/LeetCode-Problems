#657. There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.
# The move sequence is represented by a string, and the character moves[i] represents its ith move. Valid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.
def judgeCircle(moves: str) -> bool:
    x = 0
    y = 0
    for i in moves:
        if(i == "U"):
            y += 1
        elif(i == "D"):
            y -= 1
        elif(i == "L"):
            x -= 1
        elif(i == "R"):
            x += 1
    if(x == 0 and y == 0):
        return True
    return False

moves = str(input())
print(judgeCircle(moves))