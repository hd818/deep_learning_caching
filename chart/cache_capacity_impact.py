# encoding=utf-8
import matplotlib.pyplot as plt

if __name__ == '__main__':

    num1 = [0.0, 0.51, 0.56, 0.583, 0.591, 0.593, 0.594, 0.594, 0.594, 0.594, 0.594]
    num2 = [0.0,0.23, 0.33, 0.395, 0.45, 0.485, 0.52, 0.55, 0.57, 0.58, 0.587]
    num3 = [0.0,0.09,0.160,0.225,0.300,0.355,0.403,0.450,0.489,0.527,0.558]
    num = [num1,num2,num3]
    # num.reverse()
    plt.rcParams['font.sans-serif'] = ['SimHei'] # 可以解释中文无法显示的问题
    x = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45 ,50]
    plt.grid(ls='--')
    lable = ['FC based Caching', 'MPC based Caching', 'Proposed Caching'] # 折现名称
    markes = ['-o', '-^', '-*'] # 折现显示形状
    lable.reverse()
    print(num)
    for link in range(len(num)):
        plt.plot(x,num[link],markes[link],label = lable[link])
    plt.margins(0)
    plt.subplots_adjust(bottom=0.10)
    plt.xlabel('Cache Capacity of Mobile Device')  # X轴标签
    plt.ylabel("Cache Hit Ratio")  # Y轴标签
    plt.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
    plt.xticks(x)
    #plt.title("A simple plot") #标题
    plt.legend()
    plt.rcParams['savefig.dpi'] = 500  # 图片像素
    plt.rcParams['figure.dpi'] = 500  # 分辨率
    plt.savefig("cache_capacity_impact.png")
    plt.show()