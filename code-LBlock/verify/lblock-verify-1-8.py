import sys
from gurobipy import *
def var_firstround():
    inVs = ['p'+str(j) for j in range(0,64)]
    return inVs

def var_lastround(r):
    var1 = ['p'+str(j)+'Rd'+str(r) for j in range(0,64)]
    return var1

def hammingweight(n):
    sum =0
    while n != 0:
	sum += n & 1
	n = n >>1
    return sum

def mycallback(model,where) :
    if where == GRB.Callback.MIP :
       best = model.cbGet(GRB.Callback.MIP_OBJBST)
       if best >= 0:
          m.terminate()

#filename = 'head.lp'
outfile = 'LBlock_imp-gai-1-8.lp'    #modify
results = 'results-LBlock_imp-gai-1-8.txt'   #modify
rs = open(results, 'a')
invar = var_firstround()
var = var_lastround(9)   #modify

for l in range(0,16):
    o = open(outfile,'r+')
    add_constraint_1 = var[20]+" = "+ str(l & 0x1)+'\n'
    add_constraint_2 = var[21]+" = "+ str(l>>1 & 0x1)+'\n'
    add_constraint_3 = var[22]+" = "+ str(l>>2 & 0x1)+'\n'
    add_constraint_4 = var[23]+" = "+ str(l>>3 & 0x1)+'\n'
    rows = o.readlines()
    rows[4] = add_constraint_1
    rows[5] = add_constraint_2
    rows[6] = add_constraint_3
    rows[7] = add_constraint_4		
    o = open(outfile,'w+')
    o.writelines(rows)
    o.close()		
    m=read('LBlock_imp-gai-1-8.lp')    #modify
    m.optimize(mycallback)
    if m.status != 3:
        rs.write(add_constraint_1)
	rs.write(add_constraint_2)
	rs.write(add_constraint_3)
	rs.write(add_constraint_4)
	rs.write('\n')

rs.close()

		   
		
		





