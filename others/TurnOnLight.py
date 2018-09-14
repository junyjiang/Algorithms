def turnon(t,p):
    a = list(range(1, t + 1))#将灯的位置放置到list中作为后续确认开关的索引
    b=[]
    for i in a:#对应每一盏灯
        for j in range(1, p+1):#每一个人都会对自己的倍数所对应的灯
            if j % i == 0:
                a[j-1] = a[j-1] * -1#操作一次对应更改一次开关状态
    for n in range(0, (len(a))):
        if a[n] < 0:
            b.append(-a[n])
    return b

if __name__ == '__main__':
    i = int(input('请输入灯的数量：'))
    j = int(input('请输入人的数量：'))
    c = turnon(i,j)
    print('最终被点亮的灯分别是：', c)