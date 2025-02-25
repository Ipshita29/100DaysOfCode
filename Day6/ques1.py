#There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. 
# The biker starts his trip on point 0 with altitude equal 0
#. Return the highest altitude of a point.
def largestAltitude(gain):
    arr=0
    _sum=0
    for i in gain:
        _sum+=i
        arr = max(arr, _sum)
    return arr
