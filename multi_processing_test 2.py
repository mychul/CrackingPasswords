from multiprocessing import Process, Value
import time

def x(id,num, flag):
    #print("Process #" + str(id) + " flag = " + str(flag.value) + "\n")
    while not num.value == 10000: 
        if num.value >= 1000:
                flag.value = 1
        if not flag.value == 1:
            num.value = num.value + 1
            print("Process #" + str(id) + " num = " + str(num.value) + "\n")
        else:
            #print("Process #" + str(id) + " flag = " + str(flag.value) + "\n")
            break   
        

# def y(id,num, flag):
#     #print("Process #" + str(id) + " flag = " + str(flag.value) + "\n")
#     while not num.value == 10000: 
#         if num.value >= 500:
#                 flag.value = 1
#         if not flag.value == 1:
#             num.value = num.value + 1
#             print("Process #" + str(id) + " num = " + str(num.value) + "\n")
#         else:
#             break   

if __name__ == '__main__':
    start = time.time()
    num = Value('i', 0)
    flag = Value('i', 0)
    x_process = Process(target=x, args=(1,num,flag))
    y_process = Process(target=x, args=(2,num,flag))
    z_process = Process(target=x, args=(3,num,flag))
    x_process.start()
    y_process.start()
    z_process.start()
    x_process.join()
    y_process.join()
    z_process.join()
    end = time.time()
    print(str(end - start) + " seconds")
