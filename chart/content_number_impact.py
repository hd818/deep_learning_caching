# encoding=utf-8
import matplotlib.pyplot as plt

if __name__ == '__main__':

    num1 = [0.6217934257507328, 0.5890253238057012, 0.5656656224680396, 0.547814195004016, 0.5339642569470757, 0.5239271768372565, 0.5068355057857786, 0.49330149028072323, 0.46951366684942336, 0.45179140314662175]
    num2 = [0.38548351905932654, 0.3702224661309259, 0.3721159283516613, 0.37345989647717726, 0.3732850909520906, 0.36396786365944445, 0.3458190934814942, 0.32718896653434304, 0.30335211049265587, 0.2819823106938403]
    num3 = [0.2856574603851426, 0.2856574603851453, 0.2856574603851378, 0.2856574603851409, 0.28565746038514284, 0.2760310400791698, 0.2581988269468939, 0.24008348538992424, 0.216565525969466, 0.19572471178280626]
    num = [num1,num2,num3]
    # num.reverse()
    plt.rcParams['font.sans-serif'] = ['SimHei'] # 可以解释中文无法显示的问题
    x = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
    plt.grid(ls='--')
    lable = ['FC based Caching', 'MPC based Caching', 'Proposed Caching'] # 折现名称
    markes = ['-o', '-^', '-*'] # 折现显示形状
    lable.reverse()
    print(num)
    for link in range(len(num)):
        plt.plot(x,num[link],markes[link],label = lable[link])
    plt.margins(0)
    plt.subplots_adjust(bottom=0.10)
    plt.xlabel('Number of Content')  # X轴标签
    plt.ylabel("Cache Hit Ratio")  # Y轴标签
    plt.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    plt.xticks(x)
    #plt.title("A simple plot") #标题
    plt.legend()
    plt.rcParams['savefig.dpi'] = 500  # 图片像素
    plt.rcParams['figure.dpi'] = 500  # 分辨率
    plt.savefig("content_number_impact.png")
    plt.show()