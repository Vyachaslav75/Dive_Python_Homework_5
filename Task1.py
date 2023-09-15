def gen_simple_number(n):
    from math import sqrt
    simple_nums=[2]
    yield 2
    for i in range(3, n+1, 2):
        if i>10 and i%10==5:
            continue
        for j in simple_nums:
            if j>int(sqrt(i))+1:
                simple_nums.append(i)
                yield i
                break
            if i%j==0:
                break
                
        else:
            simple_nums.append(i)
            yield i
            
def gen_simple_number_eratosfen(n):
    resheto=[x for x in range(n+1)]
    resheto[1]=0
    
    i=2
    while i<=n:
        if resheto[i]!=0:
            simple=resheto[i]
            for j in range(i, n+1, i):
                resheto[j]=0
            yield simple
        i+=1



for item in gen_simple_number(1000):
     print(f'{item = }')


for item in gen_simple_number_eratosfen(1000):
     print(f'{item = }')