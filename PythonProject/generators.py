def gen_fun():
    n=2
    while n<1000:
        yield  n
        n*= 2
# this doesn't mean that gen function will run
g=gen_fun()

# for i in g:
#     print(i)

 # You can also use generator as class

 class PrimeGenerator:
     def __init__(self, end):
         self.end=end
         self.start=2

     def __next__(self):
         for n in range(self.start, self.end):
             for x in range(2,n):
                 if n%x==0:
                     break
             else:
                 self.start+=1
                 return n

         raise  StopIteration()

ob=PrimeGenerator()
next(ob)