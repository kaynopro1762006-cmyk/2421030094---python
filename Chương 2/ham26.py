#cach khoi tao tuple
>>> tuple = (1,2,3,4)
>>> tuple
91 (1,2,3,4)
>>> e_tuple = ()
>>> e_tuple
()
#ma tran
>>> tuple = ((1,2,3),[4,5])
>>> tuple [0]
(1,2,3)
>>> tuple [0] {2}
3
>>> tuple [1] [0]
4 
#phuong thuc count()
>>> tuple = (1,5,3,5,6,1,1)
>>> tuple.count(1)
3
>>> tuple.count(4)
0
#in ra tung hang theo cot khong dung for
print(*matrix [0])
print(*matrix [1])
print(*matrix [2])
print(*matrix [3])