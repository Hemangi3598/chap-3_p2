# wapp to read length and breadth of rect
# find area and perimeter 

length = float(input(" enter length "))
breadth = float(input(" enter breadth "))
if length <= 0 or breadth <= 0:
	print(" invalid data")
else:
	area = length * breadth
	perimeter = 2* (length + breadth )
	print("area = ", round(area, 2))
	print("perimeter = ", round(perimeter , 2))
	
