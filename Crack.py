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

def main():
    found_flag=False
    path = r"C:\Users\Hollow\Desktop\cs165\Project1-CrackingPasswords\CrackingPasswords\Files"
    for filename in os.listdir(path):
        
        if found_flag==True:
            break
        with open(path+"\\"+filename,'r') as f:
            if found_flag==True:
                break
            while(True):

                password = f.readline().strip()
                if not password:
                    break
        
                encoded_pass=password.encode()
                salt = "hfT7jp2q"
                encoded_salt=salt.encode()

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

                expected_hash= "dVJs.MzjBrYL40PwzHylg."

                if expected_hash == result:
                    w = open("result.txt",'w')
                    w.write(password)
                    w.close()
                    found_flag = True
                    break
    

if __name__ == "__main__":
    main()