import torch
import numpy as np
# 全是1的张量
#print(torch.ones(2,3,4))

# 其中的每个元素都从均值为0、标准差为1的标准高斯分布（正态分布）中随机采样。
#print(torch.randn(2,3,4))

#我们使用逗号来表示一个具有5个元素的元组，其中每个元素都是按元素操作的结果。
#x= torch.tensor([1.0,2,4,8])
#y = torch.tensor([2,2,2,2])
#print(x+y)
#print(x-y)
#print(x*y)
#print(x/y)
#print(x**y) # 开方

#print(torch.exp(x))

# 拼接
#X=torch.arange(12,dtype=torch.float32).reshape((3,4))
#Y = torch.tensor([[2.0,1,4,3],[1,2,3,4],[4,3,2,1]])
#Z = torch.cat((X,Y),dim = 0), torch.cat((X,Y),dim = 1)

#print(X)
#print(Y)
#print(Z)

# 广播机制
#a = torch.arange(3).reshape((3,1))
#b = torch.arange(2).reshape((1,2))
#由于a和b分别是3x1和2x1矩阵, 相加的话形状不匹配。将两个矩阵广播为一个更大的3x2矩阵，矩阵a复制列，矩阵b复制行，然后按照元素相加
#print(a+b)

# 索引和切片
# 就像在任何其他Python数组中一样，张量中的元素可以通过索引访问。 与任何Python数组一样：第一个元素的索引是0，最后一个元素索引是-1； 可以指定范围以包含第一个元素和最后一个之前的元素。
#X=torch.arange(10).reshape(2,5)
#print(X)
#X[1,1]=9
#print(X)
#X[0:2,3:5]=9
#print(X)


# 节省内存
# 使用切片表示法将操作的结果分配给先前分配的数组
X = torch.ones(20).reshape(4,5)
Y = torch.arange(20).reshape(4,5)
Z = torch.zeros_like(Y)
print('id(Z):', id(Z))
Z[:] = X+Y               # 关键：使用切片赋值, 在原有Z的内存空间中更新数据，不改变Z的内存地址
print('id(Z):', id(Z))
#如果在后续计算中没有重复使用X， 我们也可以使用X[:] = X + Y或X += Y来减少操作的内存开销。

# 转换为其他Python对象

A = X.numpy()
B = torch.tensor(A)
print(type(A),type(B))

# 要将大小为1的张量转换为Python标量，我们可以调用item函数或Python的内置函数。
a = torch.tensor([3.5])
print(a,a.item(),float(a),int(a))
