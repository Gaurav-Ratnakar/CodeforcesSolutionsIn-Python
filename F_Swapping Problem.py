def PosOfLargestNumber(a):
    return a.index(max(a))

def PosOfSmallestNumber(a):
    return a.index(min(a))

def Main(a,b):
    PositionOfMaxOfa=PosOfLargestNumber(a) 
    temp=b[PosOfLargestNumber(b)]  
    b[PosOfLargestNumber(b)]=b[PositionOfMaxOfa]  
    b[PositionOfMaxOfa]=temp
    sum=0
    listoflist=[]
    listoflist.append(a)
    listoflist.append(b)
    for i,j in zip(a,b):
        sum+=abs(i-j)
    print(sum)
size=int(input())
a=[]
b=[]
a = list(map(int, input().split()))
b = list(map(int, input().split()))

Main(a,b)
