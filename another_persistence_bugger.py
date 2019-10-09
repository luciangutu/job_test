persistence = lambda n,c=0: persistence(reduce(lambda x,y:int(x)*int(y),str(n)),c+1) if n >=10 else c
print(persistence(39))
