#国内某航空公司面临着常旅客流失、竞争力下降和航空资源未充分利用等经营危机
#要建立合理的客户价值评估模型，对客户进行分类，分析比较不同客户群体的价值，并制定相应的营销策略

#初始化 导入变量
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib import rcParams
rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False

#数据探索分析
air_data_path = r'D:\PythonProject\air_data.csv'
air_data = pd.read_csv(air_data_path,encoding='utf-8')
explore = air_data.describe(percentiles=[],include='all').T
explore['null'] = len(air_data) - explore['count']
explore = explore[['null','max','min']]
explore.columns = [u'空值数',u'最大值',u'最小值']
explore