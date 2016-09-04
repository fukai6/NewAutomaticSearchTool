import sys
from gurobipy import *


def mycallback(model,where) :
    if where == GRB.Callback.MIP :
       best = model.cbGet(GRB.Callback.MIP_OBJBST)
       if best <= 300:
          model.terminate()

m = read('impossible.lp')
m.optimize(mycallback)
if m.status == 3:
   o = open('result','a')
   o.write("infeasible \n")
   o.close()



