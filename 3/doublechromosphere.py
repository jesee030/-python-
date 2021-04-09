from random import randrange, randint, sample
import random
def display(balls):
    """
    按照题目所要求格式输出列表中的双色球号码

    :param balls:双色球号码列表，如[9,12,16,20,30,33 3]
    :print:输出格式为09 12 16 20 30 33 | 03
    :return: 无返回值

    """
    #        请在此处添加代码       #
    # *************begin************#
    for i in range(len(balls)-1):
        print(balls[i],end=" ")
    print("|",end=" ")
    print(balls[-1],end=" ")
    print()
    # **************end*************#


def random_select():
    """
    随机选择一组号码
    :return: 返回随机选择的这一组号码，如[9,12,16,20,30,33 3]
    """
    #        请在此处添加代码       #
    # *************begin************#
    t=["%02d" % x for x in range(1, 34)]
    b=["%02d" % y for y in range(1,17)]
    t=sample(t,6)
    t.sort()
    b=sample(b,1)
    t.append(b[0])
    return t
    # **************end*************#

#n为注数
def main(n):

    for _ in range(n):
        display(random_select())
        
random.seed(3)
n = int(input())
if __name__ == '__main__':
    main(n)


