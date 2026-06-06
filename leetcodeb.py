
def minEnergy(n, brightness, intervals):
    """
    :type n: int
    :type brightness: int
    :type intervals: List[List[int]]
    :rtype: int
    """
    x=[]
    intervals.sort()

    x.append(intervals[0])
    print(x)
    for i in intervals[1:]:
        if x[-1][1]>=i[0]:
            x[-1][1]=max(x[-1][1],i[1])
        else:
            x.append(i)
    print(x)
    needed=0
    for i in x:
        needed+=i[1]-i[0]+1
    ans=needed*((brightness+2)//3)
    return ans

print(minEnergy(5,3,[6,12]))