from multiprocessing import Process, Value
import time
import hashlib
import os

def to64(v, n):
    ret = ""
    base64 = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for i in range(1,n+1):
        ret += base64[v&0x3f]
        v >>= 6
    return ret

def finalization(h):
    return to64((h[0] << 16) | (h[6] << 8) | (h[12]), 4) + to64((h[1] << 16) | (h[7] << 8) | (h[13]), 4) + to64((h[2] << 16) | (h[8] << 8) | (h[14]), 4) + to64((h[3] << 16) | (h[9] << 8) | (h[15]), 4) + to64((h[4] << 16) | (h[10] << 8) | (h[5]), 4) + to64(h[11], 2)

def crack(id,num,flag):
    path = r"C:\Users\Hollow\Desktop\cs165\Project1-CrackingPasswords\CrackingPasswords\Files"
    truepath = path+"\\"+ str(id) 
    salt = "4fTgjp6q"
    encoded_salt=salt.encode()
    expected_hash= "bBkNBB2HVvMtCOMVnh5kN."
    for filename in os.listdir(truepath):
        start = time.time()
        if flag.value == 1:
            break
        with open(truepath + "\\" + filename,'r') as f:
            if flag.value == 1:
                break
            while(True):
                if flag.value == 1:
                    break
                password = f.readline().strip()
                if not password:
                    break
                    f.close()
        
                encoded_pass=password.encode()
                
                

                res = password + "$1$" + salt
                encoded_res=res.encode()
                blah = password + salt + password
                encoded_blah=blah.encode()
                
                h=hashlib.md5(encoded_blah)
                encoded_h = h.digest()
            
                l=len(password) #*2
                
                while l > 0:
                    encoded_res = encoded_res + encoded_h[0:min(16,l)]
                    l = l - 16
                
                l=len(password)
                while(l != 0):
                    if l&1:
                        encoded_res += b'\x00'
                    else: 
                        encoded_res += password[0].encode()
                    l>>=1

                encoded_h = hashlib.md5(encoded_res).digest()
                
                for x in range(0,1000):
                    tmp = b''
                    if ((x % 2) == 1): 
                        tmp += encoded_pass
                    else: 
                        tmp += encoded_h
                    if ((x % 3) != 0):
                        tmp += encoded_salt
                    if ((x % 7) != 0): 
                        tmp += encoded_pass
                    if ((x % 2) == 1): 
                        tmp += encoded_h
                    else:
                        tmp += encoded_pass

                    encoded_h = hashlib.md5(tmp).digest()
                
                result=finalization(encoded_h)

                 
                #"bBkNBB2HVvMtCOMVnh5kN."
               
                #if num.value % 10000 == 0:
                    #print("Process " + str(id) + " has reached a checkpoint. $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                num.value = num.value + 1 # count lines
                #print("Process " + str(id) + " has reached line " + str(num.value))

                if expected_hash == result:
                    print("Process " + str(id) + " has found password: " + password)
                    w = open("result.txt",'w')
                    w.write("Process " + str(id) + " has found password: " + password + ".\n")
                    w.close()
                    flag.value = 1
                    break
        if(flag.value == 0):
            if os.path.exists(path+"\\"+ str(id) + "\\" +filename):
                end = time.time()
                print("Process " + str(id) + " has finished with file in " + str(end - start) + " seconds" + ". Deleting File: " + filename)
                os.remove(path+"\\"+ str(id) + "\\" +filename)
            else:
                print("The file does not exist")    
            
if __name__ == '__main__':
    start = time.time()
    num = Value('i', 0)
    flag = Value('i', 0)
    
    first_process = Process(target=crack, args=(1,num,flag))
    second_process = Process(target=crack, args=(2,num,flag))
    third_process = Process(target=crack, args=(3,num,flag))
    #fourth_process = Process(target=crack, args=(4,num,flag))
    #fifth_process = Process(target=crack, args=(5,num,flag))
    #sixth_process = Process(target=crack, args=(6,num,flag))
    #seventh_process = Process(target=crack, args=(7,num,flag))
    #eigth_process = Process(target=crack, args=(8,num,flag))
    #nineth_process = Process(target=crack, args=(9,num,flag))
    #tenth_process = Process(target=crack, args=(10,num,flag))
    #eleventh_process = Process(target=crack, args=(11,num,flag))
    #twelve_process = Process(target=crack, args=(12,num,flag))
    #thirteen_process = Process(target=crack, args=(13,num,flag))
    #fourteen_process = Process(target=crack, args=(14,num,flag))
    #fifteen_process = Process(target=crack, args=(15,num,flag))
    #sixteen_process = Process(target=crack, args=(16,num,flag))
    #seventeen_process = Process(target=crack, args=(17,num,flag))
    #eightteen_process = Process(target=crack, args=(18,num,flag))
    #nineteen_process = Process(target=crack, args=(19,num,flag))
    #twenty_process = Process(target=crack, args=(20,num,flag))
    #twentyone_process = Process(target=crack, args=(21,num,flag))
    #twentytwo_process = Process(target=crack, args=(22,num,flag))
    #twentythree_process = Process(target=crack, args=(23,num,flag))
    
    first_process.start()
    second_process.start()
    third_process.start()
    #fourth_process.start()
    #fifth_process.start()
    #sixth_process.start()
    #seventh_process.start()
    #eigth_process.start()
    #nineth_process.start()
    #tenth_process.start()
    #eleventh_process.start()
    #twelve_process.start()
    #thirteen_process.start()
    #fourteen_process.start()
    #fifteen_process.start()
    #sixteen_process.start()
    #seventeen_process.start()
    #eightteen_process.start()
    #nineteen_process.start()
    #twenty_process.start()
    #twentyone_process.start()
    #twentytwo_process.start()
    #twentythree_process.start()
    
    first_process.join()
    second_process.join()
    third_process.join()
    #fourth_process.join()
    #fifth_process.join()
    #sixth_process.join()
    #seventh_process.join()
    #eigth_process.join()
    #nineth_process.join()
    #tenth_process.join()
    #eleventh_process.join()
    #twelve_process.join()
    #thirteen_process.join()
    #fourteen_process.join()
    #fifteen_process.join()
    #sixteen_process.join()
    #seventeen_process.join()
    #eightteen_process.join()
    #nineteen_process.join()
    #twenty_process.join()
    #twentyone_process.join()
    #twentytwo_process.join()
    #twentythree_process.join()
    
    end = time.time()
    print(str(end - start) + " seconds")
    print("Total Lines Tried: " + str(num.value))
    w = open("stats.txt",'a')
    w.write("Total Lines Tried: " + str(num.value) + " in " + str(end - start) + " seconds.\n")
    w.close()
