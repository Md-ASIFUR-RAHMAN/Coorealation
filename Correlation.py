import math
sumx1 = 0
sumy1 = 0
sqx = 0
sqy= 0
x = []
y = []
xli = []
yli = []
s_multi = 0
nx1 = int(input("Enter How many x1 : "))
print("\n")
for i in range(nx1):
    x1 = int(input("Enter x1 : "))
    x.append(x1)
    sumx1 = sumx1 + x1
meanx1 = sumx1 / nx1
print("\n")
print("Mean of x1 : ",meanx1)


for i in range(len(x)):
    xsq = (x[i] - meanx1) * (x[i] - meanx1)

    sqx = sqx + xsq
    xx = x[i] - meanx1
    xli.append(xx)

    print("x1 - x' : ",xx)


for i in range(len(x)):
    xsq = (x[i] - meanx1) * (x[i] - meanx1)

    print("(x1 - x')^2 : ",xsq)
print("\n")
print("SUM OF (x1 - x')^2 :",sqx)




ny1 = int(input("Enter How many y1 : "))
print("\n")
for i in range(ny1):
    y1 = int(input("Enter y1 : "))
    y.append(y1)
    sumy1 = sumy1 + y1
meany1 = sumy1 / ny1
print("Mean of y1 : ",meany1)


for i in range(len(y)):
    ysq = (y[i] - meany1) * (y[i] - meany1)
    sqy =  sqy + ysq
    yy = y[i] - meany1
    yli.append(yy)

    print("y1 - y' :",yy)
    #print("(y1 - y')^2 :",ysq)


for i in range(len(y)):
    ysq = (y[i] - meany1) * (y[i] - meany1)
    print("(y1 - y')^2 : ",ysq)
print("\n")
print("Sum of (y1 - y')^2 :",sqy)


for i in range(nx1):
    multi = xli[i] * yli[i]
    s_multi = s_multi + multi
    print("(x1 - x'  * y1 - y') :",multi)
print("\n")
print(" SUM OF (x1 - x'  * y1 - y')",s_multi)
print("\n")

s = (sqx * sqy)
s1 = math.sqrt(s)
r = s_multi/s1
print("CORREALATION :",r)
