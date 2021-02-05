#1725. You are given an array rectangles where rectangles[i] = [li, wi] represents the ith rectangle of length li and width wi.
# You can cut the ith rectangle to form a square with a side length of k if both k <= li and k <= wi. For example, if you have a rectangle [4,6], you can cut it to get a square with a side length of at most 4.
# Let maxLen be the side length of the largest square you can obtain from any of the given rectangles.
# Return the number of rectangles that can make a square with a side length of maxLen.
def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
    sqr = []
    for i in rectangles:
        if(i[0] < i[1]):
            sqr.append(i[0])
        else:
            sqr.append(i[1])
    sqr.sort(reverse=True)
    ret = 0
    for i in sqr:
        if(i!=sqr[0]):
            break
        ret += 1
    return ret
