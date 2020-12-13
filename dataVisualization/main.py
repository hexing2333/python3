import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
#作业一
def job1():
    plt.style.use('seaborn-bright')
    fig, ax = plt.subplots()
    ax.set_title("function x*x+x")
    x = np.arange(-10, 11, 1)
    ax.set_xlim(-11, 11)
    ax.set_xticks(x)
    y = x * x + x
    plt.bar(x, y, color='g', label='y=x*x+x')
    plt.legend(loc='upper left')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True, linestyle='-.', alpha=1)
    for a, b in zip(x, y):
        plt.text(a, b / 2, '%d' % b, ha='center', va='bottom', fontsize=10)
    plt.show()

#作业二
def job2():
    def count_elements(scores):
        scorescount = {}
        for i in scores:
            scorescount[int(i)] = scorescount.get(int(i), 0) + 1
        _scorescount = {}
        i = 60
        while (i < 95):
            for j in range(5):
                _scorescount[str(i) + "-" + str(i + 4)] = _scorescount.get(str(i) + "-" + str(i + 4),
                                                                           0) + scorescount.get(i + j, 0)
            i += 5
        return _scorescount

    filename = "data1402.csv"
    scores = []
    with open(filename, 'r') as csvfile:
        f_csv = csv.reader(csvfile)
        for row in f_csv:
            scores.append(float(row[0]))

    counted = count_elements(scores)
    plt.ylim(0, 100)
    plt.bar(counted.keys(), counted.values(), 0.5, alpha=0.5, color='b')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.xlabel("成绩分布")
    plt.ylabel("人数")
    plt.title("分段成绩直方图")
    plt.legend(["人数"],loc='upper left')
    plt.grid(True, linestyle='-.', alpha=1)
    for a, b in zip(counted.keys(), counted.values()):
        plt.text(a, b + 0.3, '%d' % b, ha='center', va='bottom', fontsize=10)
    plt.show()

#作业三
def job3():
    # 随机生成10x3数组(范围1-200)
    rank = np.random.randint(1, 201, size=(10, 3))
    print(rank)
    fig,ax=plt.subplots()
    plt.rcParams['font.sans-serif']=['SimHei']
    Semester1 = []
    Semester2 = []
    Semester3 = []
    for row in rank:
        Semester1.append(int(row[0]))
        Semester2.append(int(row[1]))
        Semester3.append(int(row[2]))
    x= np.arange(1,11)
    plt.bar(x-0.3,Semester1,0.3,alpha=0.5,color='g')
    plt.bar(x, Semester2, 0.3, alpha=0.5, color='b')
    plt.bar(x+0.3,Semester3,0.3,alpha=0.5,color='r')
    for a, b in zip(x, Semester1):
        plt.text(a - 0.3, b + 0.2, '%d' % b, ha='center', va='bottom', fontsize=10)
    for a, b in zip(x, Semester2):
        plt.text(a, b + 0.2, '%d' % b, ha='center', va='bottom', fontsize=10)
    for a, b in zip(x, Semester3):
        plt.text(a + 0.3, b + 0.2, '%d' % b, ha='center', va='bottom', fontsize=10)
    ax.set_xticks(x)
    plt.ylim(0, 250)
    plt.legend(['第一学期', '第二学期', '第三学期'], loc='upper left')
    plt.title('10名学生排名数据直方图')
    plt.xlabel('学生序号')
    plt.ylabel('名次')
    plt.grid(True, linestyle='-.', alpha=1)
    plt.show()

def job4():
    fig,ax=plt.subplots()
    x=np.linspace(-5*np.pi,5*np.pi,640)
    cos,sin=2*np.cos(x),np.sin(x*3)
    ax.set_xticks([i * np.pi for i in range(-5, 6)])
    plt.plot(x, cos, color="blue", linewidth=2, linestyle="-", label="cos")
    plt.plot(x, sin, color="red", linewidth=2, linestyle="--", label="sin")
    plt.legend(loc='lower left')
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines['bottom'].set_position(('data', 0))
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['left'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')

    plt.show()

def job5():
    fileNameStr = 'BeijingPM20100101_20151231.csv'
    df = pd.read_csv(fileNameStr, encoding='utf-8')
    df.drop(df.columns[[range(10, 18)]], axis=1, inplace=True)
    # 去掉三列PM数据全部为空的行
    df.dropna(axis=0, how='all', subset=['PM_Dongsi', 'PM_Dongsihuan', 'PM_Nongzhanguan', 'PM_US Post'], inplace=True)
    df['sum'] = df[['PM_Dongsi', 'PM_Dongsihuan', 'PM_Nongzhanguan', 'PM_US Post']].sum(axis=1)
    df['count'] = df[['PM_Dongsi', 'PM_Dongsihuan', 'PM_Nongzhanguan', 'PM_US Post']].count(axis=1)
    df['ave'] = round(df['sum'] / df['count'], 2)
    bj2 = df.groupby(['year', 'month'])['ave'].mean()#按月份计算平均值
    am =pd.DataFrame(bj2).reset_index()
    year_2010 = []
    year_2011 = []
    year_2012 = []
    year_2013 = []
    year_2014 = []
    year_2015 = []
    for i in range(0, 12):
        print(am.iloc[i]['ave'])
        year_2010.append(am.iloc[i]['ave'])
        year_2011.append(am.iloc[i + 12]['ave'])
        year_2012.append(am.iloc[i + 24]['ave'])
        year_2013.append(am.iloc[i + 36]['ave'])
        year_2014.append(am.iloc[i + 48]['ave'])
        year_2015.append(am.iloc[i + 60]['ave'])

    plt.rcParams['font.sans-serif'] = ['SimHei']
    x = np.arange(1, 13)
    plt.xticks(range(1, 13))
    plt.title('10-15年PM指数月平均数据变化情况')
    plt.xlabel('月份')
    plt.ylabel('PM指数')
    plt.plot(x, year_2010, color="b", linewidth=2, linestyle="-", label="2010")
    plt.plot(x, year_2011, color="g", linewidth=2, linestyle="-", label="2011")
    plt.plot(x, year_2012, color="r", linewidth=2, linestyle="-", label="2012")
    plt.plot(x, year_2013, color="c", linewidth=2, linestyle="-", label="2013")
    plt.plot(x, year_2014, color="m", linewidth=2, linestyle="-", label="2014")
    plt.plot(x, year_2015, color="y", linewidth=2, linestyle="-", label="2015")
    plt.legend(loc='upper right')
    plt.show()

if __name__ == '__main__':
    job1()
    job2()
    job3()
    job4()
    job5()


