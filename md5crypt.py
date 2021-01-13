import hashlib
import binascii
def to64(v, n):
    ret = ""
    base64 = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for i in range(1,n+1):
        ret += base64[v&0x3f]
        #print(ret)
        #input("press enter")
        v >>= 6
    return ret

#def finalization(h):
    #return to64((int(h[0]) << 16) | (int(h[6]) << 8) | (int(h[12])), 4) + to64((int(h[1]) << 16) | (int(h[7]) << 8) | (int(h[13])), 4) + to64((int(h[2]) << 16) | (int(h[8]) << 8) | (int(h[14])), 4) + to64((int(h[3]) << 16) | (int(h[9]) << 8) | (int(h[15])), 4) + to64((int(h[4]) << 16) | (int(h[10]) << 8) | (int(h[5])), 4) + to64(int(h[11]), 2)
def finalization(h):
    return to64((h[0] << 16) | (h[6] << 8) | (h[12]), 4) + to64((h[1] << 16) | (h[7] << 8) | (h[13]), 4) + to64((h[2] << 16) | (h[8] << 8) | (h[14]), 4) + to64((h[3] << 16) | (h[9] << 8) | (h[15]), 4) + to64((h[4] << 16) | (h[10] << 8) | (h[5]), 4) + to64(h[11], 2)

def main():
    #initialization
    password = "zhgnnd"
    salt = "hfT7jp2q"

    res = password + "$1$" + salt
    blah = password + salt + password
    #print(blah)
    h=hashlib.md5(blah.encode())
    #print(h.hexdigest())
    h=h.hexdigest()
    l=len(password)*2
    #############################################
    #print(l)
    while l > 0:
        res = res + h[0:min(16,l)]
        l = l - 16
    print(res)

    #print(hashlib.md5(res.encode()).hexdigest())
    l=len(password)
    while(l != 0):
        if l&1:
            res += '\x00'
            #print("Adding hex nul")
            #print(res)
        else: 
            res += password[0]
            #print("Adding first character of pass")
            #print(res)
        l>>=1
    #print(l)

    h = hashlib.md5(res.encode())
    #print(h.hexdigest())
    
    for x in range(0,1000):
        tmp = ""
        if ((x % 2) == 1): 
            tmp += password
        else: 
            tmp += h.hexdigest()
        if ((x % 3) != 0):
            tmp += salt
        if ((x % 7) != 0): 
            tmp += password
        if (x % 2 == 1): 
            tmp += h.hexdigest()
        else:
            tmp += password

        h = hashlib.md5(tmp.encode())
    #print(h.hexdigest())

    print(finalization(h.digest()))
    

if __name__ == "__main__":
    main()