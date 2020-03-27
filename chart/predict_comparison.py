# encoding=utf-8
import matplotlib.pyplot as plt

if __name__ == '__main__':

    num1 = [0.67,0.63,0.58,0.56,0.51,0.50,0.47]
    num2 = [1.19,1.17,1.16,1.14,1.13,1.01,0.92]
    num3 = [1.3,1.29,1.27,1.25,1.24,1.21,1.11]
    num = [num1,num2,num3]
    #num.reverse()
    plt.rcParams['font.sans-serif'] = ['SimHei'] # 可以解释中文无法显示的问题
    #x = np.arange(0, 1.1, 0.1)

    x = [3,4,5,6,7,8,9]
    plt.grid(ls='--')
    lable = ['Content-Aware Model', 'CF&LFM Cache', 'NCF Model'] # 折现名称
    markes = ['->', '-^', '-o'] # 折现显示形状
    lable.reverse()
    print(num)
    for link in range(len(num)):
        plt.plot(x,num[link],markes[link],label = lable[link])
    plt.margins(0)
    plt.subplots_adjust(bottom=0.10)
    plt.xlabel('The number of samples in the training set (×10e4)')  # X轴标签
    plt.ylabel("RMSE")  # Y轴标签
    plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0])
    plt.xticks(x)
    #plt.title("A simple plot") #标题
    plt.legend()
    plt.rcParams['savefig.dpi'] = 500  # 图片像素
    plt.rcParams['figure.dpi'] = 500  # 分辨率
    plt.savefig("predict_comparison.png")
    plt.show()