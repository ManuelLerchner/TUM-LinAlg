from eulerPhi import phi

(n,e)=(3149, 563)
phiN=phi(n)

cypher=[1263,996,1102,3039,2177,2311 ]

print("cypher:",cypher)

for d in range(n):
    if(e*d % phiN==1):
        break
    
print(f"d={d}")

decrypted=[pow(cp,d,n) for cp in cypher]

print("decrypted:",decrypted)

message=[]
for n in decrypted:
    (first,second)=(n//100,n%100)
  
    firstLetter=chr(ord("a")+first)
    secondLetter=chr(ord("a")+second)

    message.append(firstLetter+secondLetter)

print("message:", " ".join(message))


