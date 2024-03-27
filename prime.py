import math

num = 1
res = (math.factorial(num - 1) + 1) / num
print(res)
if type(res) == "int":
	print("Prime")
else:
	print("Not Prime")
