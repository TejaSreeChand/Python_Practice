s=input("Enter the input string:")
il=list(s)
k=[]
k=['j','t','p','x','c','r','a','g','z','w','d','o','v','s','u','b','i','l','k','y','e','n','q','f','m','h',' ']
a=[]
a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
l=len(a)
b=[]
for i in range(0,len(il)):
    for j in range(0,27):
        if il[i]==a[j]:
            b.append(k[j])

print("encrypted text:","".join(b))
    

