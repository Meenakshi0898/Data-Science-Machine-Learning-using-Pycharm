'''To convert the given data range in the list'''
var=[]
for x in range (1111):
    if x%222==0:
        var.append(x)
        print(var)
print('--------------------------------------------------------------------------')
'''In simplification'''
var=[x for x in range(1111) if x%222==0]
print(var)
