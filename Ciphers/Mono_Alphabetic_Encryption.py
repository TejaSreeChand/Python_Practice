k=[]
k=['j','t','p','x','c','r','a','g','z','w','d','o','v','s','u','b','i','l','k','y','e','n','q','f','m','h',' ']
a=[]
a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
l=len(a)


def encrypt():
    e=input("Enter the input string for encryption:")
    el=list(e)
    b=[]
    for i in range(0,len(el)):
        for j in range(0,27):
            if el[i]==a[j]:
                b.append(k[j])

    print("encrypted text:","".join(b))
    

def decrypt():
    d=input("Enter the input string for decryption:")
    dl=list(d)
    c=[]   
    for i in range(0,len(dl)):
        for j in range(0,27):
            if dl[i]==k[j]:
                c.append(a[j])

    print("decrypted text:","".join(c))


choice=input("Enter your choice: a. Encrypt  b. Decrypt")
if choice=='a':
    encrypt()
else:
    decrypt()
