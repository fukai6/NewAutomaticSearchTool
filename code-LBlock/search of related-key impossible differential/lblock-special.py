import sys
from gurobipy import *
def var_firstround():
    inVs = ['p'+str(j) for j in range(0,64)]
    temp = inVs[32:64] + inVs[0:32]
    return temp

def var_lastround(r):
    var1 = ['befExchange_'+str(j)+'Rd'+str(r) for j in range(0,32)]
    var2 = ['befExchange_'+str(j)+'Rd'+str(r-1) for j in range(0,32)]
    return (var1 +var2)
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

outfile = 'LBlock_imp-16.lp'    #modify
results = 'results-re-lblock-16.txt'   #modify
rs = open(results, 'a')
invar = var_firstround()
var = var_lastround(16)   #modify
for i in range(0,80):
    for j in range(0,33):
        for l in range(0,33):
    	    o = open(outfile,'r+')
    	    add_constraint_1 = 'k'+str(i)+' = 1'+'\n'
    	    add_constraint_2 = ' + '.join(['k'+str(m) for m in range(0, 80)]) + ' = 1'+'\n'
            if j < 32:
	       if l < 32:
                   add_constraint_3 = ' + '.join(['p'+str(m) for m in range(0, 64)]) + ' = 1'+'\n'
                   add_constraint_4 = ' + '.join([var[n] for n in range(0, 64)]) + ' = 1'+'\n'
                   add_constraint_5 = invar[j]+' = 1'+'\n'
                   add_constraint_6 = var[l]+' = 1'+'\n'
	       else:
                   add_constraint_3 = ' + '.join(['p'+str(m) for m in range(0, 64)]) + ' = 1'+'\n'
		   add_constraint_4 = ' + '.join([var[n] for n in range(0, 64)]) + ' = 0'+'\n'
	           add_constraint_5 = invar[j]+' = 1'+'\n'
	           add_constraint_6 = var[0]+' = 0'+'\n'		
	    else:
		if l < 32:
		   add_constraint_3 = ' + '.join(['p'+str(m) for m in range(0, 64)]) + ' = 0'+'\n'
		   add_constraint_4 = ' + '.join([var[n] for n in range(0, 64)]) + ' = 1'+'\n'
	           add_constraint_5 = invar[0]+' = 0'+'\n'
	           add_constraint_6 = var[l]+' = 1'+'\n' 
		else:
                    add_constraint_3 = ' + '.join(['p'+str(m) for m in range(0, 64)]) + ' = 0'+'\n'
		    add_constraint_4 = ' + '.join([var[n] for n in range(0, 64)]) + ' = 0'+'\n'
	            add_constraint_5 = invar[0]+' = 0'+'\n'
	            add_constraint_6 = var[0]+' = 0'+'\n'  
    	    rows = o.readlines()
    	    rows[4] = add_constraint_1
	    rows[5] = add_constraint_2
	    rows[6] = add_constraint_3
	    rows[7] = add_constraint_4
	    rows[8] = add_constraint_5
	    rows[9] = add_constraint_6
   	    o = open(outfile,'w+')
   	    o.writelines(rows)
    	    o.close()		
   	    m=read('LBlock_imp-16.lp')    #modify
    	    m.optimize(mycallback)
    	    if m.status == 3:
	       rs.write(add_constraint_1)
	       rs.write(add_constraint_2)
	       rs.write(add_constraint_3)
	       rs.write(add_constraint_4)
	       rs.write(add_constraint_5)
	       rs.write(add_constraint_6)
rs.close()

		   
		
		





