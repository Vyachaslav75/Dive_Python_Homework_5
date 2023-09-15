def fib():
    yield 1
    fib1=0
    fib2=1
    while True:
        fib1, fib2=fib2, fib1+fib2
        #n-=1
        yield fib2
        
f=iter(fib())
for item in range(10):
    print(f'{item+1}= {next(f)}')
