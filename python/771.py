def numJewelsInStones(jewels: str, stones: str) -> int:
    count = 0
    for i in jewels:
        for j in stones:
            if(i == j):
                count+=1
    return count

print(numJewelsInStones("aA", "aAABBBBB"))