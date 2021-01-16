from multiprocessing import Process, Value

def x(id,num, flag):
    #print("Process #" + str(id) + " flag = " + str(flag.value) + "\n")
    while not num.value == 25: 
        if num.value >= 15:
                flag.value = 1
        if not flag.value == 1:
            num.value = num.value + 1
            print("Process #" + str(id) + " num = " + str(num.value) + "\n")
        else:
            #print("Process #" + str(id) + " flag = " + str(flag.value) + "\n")
            break   
        

#def y(num):
#    for i in range(10):
#        num.value = num.value + 1

if __name__ == '__main__':
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

    print(num.value)
