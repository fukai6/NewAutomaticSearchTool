import sys
from gurobipy import *


def mycallback(model,where) :
    if where == GRB.Callback.MIP :
       best = model.cbGet(GRB.Callback.MIP_OBJBST)
       if best <= 400:
          model.terminate()

m = read('impossible-1.lp')
m.Params.LogFile='hight-impossible-dc-Addequa-1-9.log'
m.optimize(mycallback)
if m.status == 3:
   o = open('txt-1','a')
   o.write("infeasible \n")
   o.close()



