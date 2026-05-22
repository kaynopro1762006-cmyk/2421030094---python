#vd  
#for x = 3,4,5,6:.....
for x in range(3,7):
    print('valice of x=',x)
#for x = 0,1,2,3,4,5
for x in range(6):
    print("value of x =", x)
#su dung for va mang....
fruits = ["apple","banana","'chersy"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
#vong lap ofor
adj = ["red","big","tasty"]
fruits = ['apple',"banana","chery"]
for x in adj:
    for y in fruits:
        print(x,y)
    #vd ......
a = []
s = 0
n = int(input("nhap so phan tu cua day so:"))
for 1 in range(1, n + 1):
    k = int(input("nhap phan tu"+ str(i)+""))
    for i in a:
        print("tong cua day so la:"+ str(s))
#phuong trinh cho phep nhap vao ma tran gom m hang,n cot......
m = int(input("Nhap m="))
n = int(input("Nhap n="))
a = []
for i in range (0,m):
    a.append([])
    for j in range (0,n):
        x = float(input("Nhap phan tu a[%d][$d]:"%(i + 1,j + 1)))
a [i].append(x)
print("many vua nhap la:")
for i in range (0,m):
    for j in range (0,n):
        print("%8.2"a[i][j],end='')
        print()
#vd viet pt hien sau 1 ki tu.....
ss = "CNTT"
index = 0
while index < len(s):
    letter = s[index]
    print(letter)
    index = index + 1
#vd 5 nhap vao 1 so kiem tra xem so do co phai hoan hao ko .....
n = int(input("n="))
s = 0
for i in range (1,n):
    if n %i == 0:
        s = s + i
        if s == n:
            print(n,"n la so hoan hao")
        else:
            print(n,"n khong la so hoan hao")
#vd6 tim so hoan hao.....
s = int(input("Nhap gioi han: "))
for n in range(1, s + 1):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong = tong + i
    if tong == n:
        print(n)
#vd....
n = int (input("nhap vao 1 so nguyen:"))
if ('n% 2 == '):
    print("so" + repr(n) + "la so chan")
else:
    print("so" + repr(n) + "la so le")
#vd ax + b = 0.....
a = float(input("nhap he so a="))
b = float(input("nhap he so b="))
if(a==0):
 if(b==0):
    print("phuong trinh vo so nhiem")
else:
    print("phuong trinh vo so nhiem")
X = -a/b 
print("x =",x)   