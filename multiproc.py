import time
import multiprocessing




def cal_su(number):
    for i in number:
        print("squr is" +str(i*i))



if __name__ == '__main__':
    arr=[]
    for i in range(200):
        arr.append(i)
    p1=multiprocessing.Process(target=cal_su,args=(arr,))
    p1.start()
    p1.join()
    print('DOne....')
    
    