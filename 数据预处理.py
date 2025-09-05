import os
import pandas as pd

os.makedirs(os.path.join('..','data'),exist_ok=True)
data_file = os.path.join('..','data','house_tiny.csv')
with open(data_file, 'w') as f:
    f.write('NumRooms,Alley,Price\n')   # 列名
    f.write('NA,Pave,127500\n')         # 每行表示一个数据样本
    f.write('2,NA,106000\n')
    f.write('4,NA,178100\n')
    f.write('NA,NA,140000\n')

data = pd.read_csv(data_file)
print(data)

# 处理缺失值
#为了处理缺失的数据，
# 典型的方法包括插值法和删除法，
# 其中插值法用一个替代值弥补缺失值，
# 而删除法则直接忽略缺失值。
# 在这里，我们将考虑插值法。
