# encoding=utf-8
import matplotlib.pyplot as plt

if __name__ == '__main__':

    num1 = [0.195, 0.380, 0.493, 0.531, 0.551, 0.567, 0.579, 0.589, 0.597, 0.603]
    num2 = [0.085, 0.135, 0.175, 0.199, 0.211, 0.220, 0.232, 0.243, 0.253, 0.263]
    num3 = [0.015, 0.035, 0.050, 0.065, 0.08, 0.095, 0.110, 0.125, 0.140, 0.155]
    num = [num1,num2,num3]
    num.reverse()
    plt.rcParams['font.sans-serif'] = ['SimHei'] # 可以解释中文无法显示的问题
    x = [10, 20, 30, 40, 50, 60, 70, 80, 90 ,100]
    plt.grid(ls='--')
    lable = ['FC based Caching', 'MPC based Caching', 'Proposed Caching'] # 折现名称
    markes = ['-o', '-^', '-*'] # 折现显示形状
    lable.reverse()
    print(num)
    for link in range(len(num)):
        plt.plot(x,num[link],markes[link],label = lable[link])
    plt.margins(0)
    plt.subplots_adjust(bottom=0.10)
    plt.xlabel('Total User Numbers')  # X轴标签
    plt.ylabel("Cache Hit Ratio")  # Y轴标签
    plt.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
    plt.xticks(x)
    #plt.title("A simple plot") #标题
    plt.legend()
    plt.rcParams['savefig.dpi'] = 500  # 图片像素
    plt.rcParams['figure.dpi'] = 500  # 分辨率
    plt.savefig("part2_total_user_numbers.png")
    plt.show()