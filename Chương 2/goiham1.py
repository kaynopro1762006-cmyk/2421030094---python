def sum (a,b):
    return (a + b)
#vd
def square (x):
    return x*x
print(rquere(4))
#vd nhap 1 so n hay viet ham de tinh sam do
def giai_thua(m):
    gt = 1
    for i in range (1,m+1):
        gt = gt *i
        return
    n = int(input("nhap vao 1 so nguyen duong:"))
    print("%d! = l.d"(n, giai_thua(n)))
    #tham so va truyen tham so
    def sum (a,b = 10):
        return
    print(sum(1,2))
    print(sum(5))
    #vd
    def sum(a,b,*p):
        gt = a + b
        for i in p:
            s = s + i
        return s
    print(sum(1,2))
    print(sum(1,2,3))
    print(sum(1,2,3,4,5,6))
    #pham vi bien
    def msg ():
        a = 10
        print("gia tri cua a la:",a)
        return
    msg()
    print(a)
#bien toan cuc
b = 20
def msg ():
    a = 10
    print("gia tri cua a la:",a)
    print("gia tri cua b la:",b)
    msg()
    print(b)
    #ham vo danh
    nhan_doi = lam_da a: a*2
    print(nhan_doi(10))
    #dung ham lilter() de loc cac so chan
    list_goc = [10,9,8,7,6,5,4,3,2,1]
    list_moi = list(filter(lambda a:(a%2 == 0)))
    print(list_moi)
    #hamlambda voi ham map()
    list_goc = [10,9,8,7,6,5,1,2,3,4,5]
    list_moi = list(map(lambda a : a*2;list_goc))
    print(list_moi)
    