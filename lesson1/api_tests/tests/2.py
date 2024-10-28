class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a,2)+int(b,2))[2:]
        
#print(Solution.addBinary(1,"10011", "01"))


    def reverseBits(self, n):
        return int(bin(n)[2:][::-1],2)
    
print(Solution.reverseBits(1,43261596))

def lenth(input_data):
    # x1, y1 = int(input()), int(input())
    # x2, y2 = int(input()), int(input())
    # x, y = int(input()), int(input())
    x1,y1,x2,y2,x,y = -100,-100,100,99,-4,100
    if x1<=x<=x2:
        if y<=y2: return "S"
        if y>=y1: return "N"
    if y1<=y<=y2:
        if x<=x1: return "W"
        if x>=x2: return "E"
    if x>x2:
        if y>y2: return "NE"
        if y1>y: return "SE"
    if x1>x:
        if y>y2: return "NW"
        if y1>y: return "SW"
        
        
# #print(lenth("""
# -100
# -100
# 100
# 99
# -4
# 100
# #"""))
        