from multiprocessing import Process, Value

def x(num):
    for i in range(10):
        num.value = num.value + 1

#def y(num):
#    for i in range(10):
#        num.value = num.value + 1

if __name__ == '__main__':
    num = Value('i', 0)

    x_process = Process(target=x, args=(num,))
    y_process = Process(target=x, args=(num,))
    z_process = Process(target=x, args=(num,))

    x_process.start()
    y_process.start()
    z_process.start()

    x_process.join()
    y_process.join()
    z_process.join()

    print(num.value)
