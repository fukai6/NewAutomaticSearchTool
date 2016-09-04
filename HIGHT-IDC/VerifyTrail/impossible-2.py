import sys
from gurobipy import *


def mycallback(model,where) :
    if where == GRB.Callback.MIP :
       best = model.cbGet(GRB.Callback.MIP_OBJBST)
       if best <= 400:
          model.terminate()

m = read('impossible-2.lp')
m.Params.LogFile='hight-impossible-dc-Addequa-10-17.log'
m.optimize(mycallback)
if m.status == 3:
   o = open('txt-2','a')
   o.write("infeasible \n")
   o.close()



