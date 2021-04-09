def triangle(row):
    '''
       根据row值，打印三个三角形
       :row:三角形行数
       :return: 无返回值
       '''
    #        请在此处添加代码       #
    # *************begin************#
    for i in range(1,row+1):
            print('*'*i,end='')
            print('\n',end='')

    for i in range(1,row+1):
        for j in range(1,row+1):
            if i+j<=row:
                print(' ',end='')
            else:
                print('*',end='')
        print()

    for i in range(1,row+1):
        for j in range(0,row-i):
            print(end=' ')
       # for k in range(row-i,row):

        print('*'*(i*2-1),end='')


        print()
    # **************end*************#


row = int(input())
triangle(row)