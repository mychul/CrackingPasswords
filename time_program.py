import time
start = time.time()
tmp = input("Press Anything: ") #Program runs here
end = time.time()
start_milliseconds = int(start * 1000)
end_milliseconds = int(end * 1000)
print(str(end_milliseconds - start_milliseconds) + " ms")
