
def cal_sr(number):
    sum=0
    for i in number:
        sum+=int(i*i)
    return sum


if __name__=='__main__':
    arr=[i for i in range(2300)]
    result=cal_sr(arr)
    print(result)

