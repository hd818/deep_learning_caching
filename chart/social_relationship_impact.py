# encoding=utf-8
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    num1 = [0.01, 0.345, 0.539, 0.580, 0.593, 0.595, 0.597, 0.601, 0.599, 0.602, 0.601]
    num2 = [0.01, 0.15, 0.266, 0.293, 0.310, 0.311, 0.312, 0.314, 0.310, 0.313, 0.312]
    num3 = [0.01, 0.11, 0.21000000000000002, 0.22999999999999998, 0.235, 0.239, 0.242, 0.241, 0.243, 0.246, 0.245]
    num = [num1,num2,num3]
    num.reverse()
    plt.rcParams['font.sans-serif'] = ['SimHei'] # 可以解释中文无法显示的问题
    x = np.arange(0, 1.1, 0.1)

    #x = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    plt.grid(ls='--')
    lable = ['FC based Caching', 'MPC based Caching', 'Proposed Caching'] # 折现名称
    markes = ['-o', '-^', '-*'] # 折现显示形状
    # lable.reverse()
    print(num)
    for link in range(len(num)):
        plt.plot(x,num[link],markes[link],label = lable[link])
    plt.margins(0)
    plt.subplots_adjust(bottom=0.10)
    plt.xlabel('Comprehensive Social Relationship(L)')  # X轴标签
    plt.ylabel("Cache Hit Ratio")  # Y轴标签
    plt.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
    plt.xticks(x)
    #plt.title("A simple plot") #标题
    plt.legend()
    plt.rcParams['savefig.dpi'] = 500  # 图片像素
    plt.rcParams['figure.dpi'] = 500  # 分辨率
    plt.savefig("social_relationship_impact.png")
    plt.show()