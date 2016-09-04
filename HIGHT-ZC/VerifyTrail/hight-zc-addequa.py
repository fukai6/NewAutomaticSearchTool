from functools import reduce
import math
import random
from MILPSbox import *
from random import *

class hight():
    def __init__(self):
        self.BlockSize = 64

    def genVars_InVars_at_Round(self, r):
        assert r >= 1
        if r == 1:
            return ['p' + str(j) for j in range(0, 64)]
        if r > 1 :      
            temp = ['p' + str(j) + 'Rd' + str(r - 1) for j in range(0, 64)]
            
            return temp

    def rotl(self, X, n, r):
        assert r >= 1
        temp = [None]*n
        for i in range(n-r) :
            temp[i] = X[i+r]
        for i in range(n-r,n) :
            temp[i] = X[i-n+r]
        return temp

    def rotr(self, X, n, r):
        assert r >= 1
        temp = [None]*n
        for i in range(r) :
            temp[i] = X[n-r+i]
        for i in range(r,n) :
            temp[i] = X[i-r]
        return temp



    def genConstraints_of_Round(self, r):
        assert r>=1
        constraints = list()
        roundx = self.genVars_InVars_at_Round(r)
        roundy = self.genVars_InVars_at_Round(r+1)
        roundtemp = ['tmp' + str(j) + 'Rd' + str(r - 1) for j in range(0, 32)]
        roundadd  = ['afteradd' + str(j) + 'Rd' + str(r - 1) for j in range(0, 16)]
        
        x0 = roundx[0 : 8]
        x1 = roundx[8 :16]
        x2 = roundx[16:24]
        x3 = roundx[24:32]
        x4 = roundx[32:40]
        x5 = roundx[40:48]
        x6 = roundx[48:56]
        x7 = roundx[56:64]
        
        y0 = roundy[0 : 8]
        y1 = roundy[8 :16]
        y2 = roundy[16:24]
        y3 = roundy[24:32]
        y4 = roundy[32:40]
        y5 = roundy[40:48]
        y6 = roundy[48:56]
        y7 = roundy[56:64]
        
        temp0 = roundtemp[0 : 8]
        temp1 = roundtemp[8 :16]
        temp2 = roundtemp[16:24]
        temp3 = roundtemp[24:32]
        
        afteradd0 = roundadd[0 : 8]
        afteradd1 = roundadd[8 :16]
        
        middlevar = ['middle'+str(i)+'Rd'+str(r-1) for i in range(32)]
        z0 = middlevar[0 : 8]
        z1 = middlevar[8 :16]
        z2 = middlevar[16:24]
        z3 = middlevar[24:32]

        key = ['k'+str(i)+'Rd'+str(r-1) for i in range(16)]
        D = ['pro'+str(i)+'Rd'+str(r-1) for i in range(32)]
        
        #left F0
        d = ['zero_var',D[0],D[1],D[2],D[3],D[4],D[5],D[6],D[7]] 
        for i in range(8) :
            a = [x0[i],key[i],z0[i]]
            constraints = constraints + [d[i]+' - '+a[0]+' - '+a[1]+' + '+a[2]+' + '+d[i+1]+' >= 0']
            constraints = constraints + [d[i]+' + '+a[0]+' + '+a[1]+' - '+a[2]+' - '+d[i+1]+' >= 0']
            constraints = constraints + [d[i]+' + '+a[0]+' - '+a[1]+' - '+a[2]+' + '+d[i+1]+' >= 0']
            constraints = constraints + [d[i]+' - '+a[0]+' + '+a[1]+' - '+a[2]+' + '+d[i+1]+' >= 0']
            constraints = constraints + [d[i]+' + '+a[0]+' - '+a[1]+' + '+a[2]+' - '+d[i+1]+' >= 0']
            constraints = constraints + [d[i]+' - '+a[0]+' + '+a[1]+' + '+a[2]+' - '+d[i+1]+' >= 0']
            constraints = constraints + [a[0]+' - '+d[i]+' + '+a[1]+' + '+a[2]+' + '+d[i+1]+' >= 0']
            constraints = constraints + [d[i]+' + '+a[0]+' + '+a[1]+' + '+a[2]+' + '+d[i+1]+' <= 4']
        z0yxh1 = self.rotr(z0, 8, 1)
        z0yxh2 = self.rotr(z0, 8, 2)
        z0yxh7 = self.rotr(z0, 8, 7)
        tp0 = ['ta'+str(i)+'Rd'+str(r-1) for i in range(8)]
        tp1 = ['tb'+str(i)+'Rd'+str(r-1) for i in range(8)]
        constraints = constraints + ConstraintGenerator.xorConstraints(x1,  z0yxh1, tp0)
        constraints = constraints + ConstraintGenerator.xorConstraints(temp0,  z0yxh7, tp1)
        constraints = constraints + ConstraintGenerator.xorConstraints(tp1, z0yxh2, tp0)

        d = ['zero_var',D[8],D[9],D[10],D[11],D[12],D[13],D[14],D[15]]
        for i in range(8) :
            a = [afteradd0[i],x2[i],z1[i]]
            constraints = constraints + [d[i]+' - '+a[0]+' - '+a[1]+' + '+a[2]+' + '+d[i+1]+' >= 0']
            constraints = constraints + [d[i]+' + '+a[0]+' + '+a[1]+' - '+a[2]+' - '+d[i+1]+' >= 0']
            constraints = constraints + [d[i]+' + '+a[0]+' - '+a[1]+' - '+a[2]+' + '+d[i+1]+' >= 0']
            constraints = constraints + [d[i]+' - '+a[0]+' + '+a[1]+' - '+a[2]+' + '+d[i+1]+' >= 0']
            constraints = constraints + [d[i]+' + '+a[0]+' - '+a[1]+' + '+a[2]+' - '+d[i+1]+' >= 0']
            constraints = constraints + [d[i]+' - '+a[0]+' + '+a[1]+' + '+a[2]+' - '+d[i+1]+' >= 0']
            constraints = constraints + [a[0]+' - '+d[i]+' + '+a[1]+' + '+a[2]+' + '+d[i+1]+' >= 0']
            constraints = constraints + [d[i]+' + '+a[0]+' + '+a[1]+' + '+a[2]+' + '+d[i+1]+' <= 4']
        z1yxh3 = self.rotr(z1, 8, 3)
        z1yxh4 = self.rotr(z1, 8, 4)
        z1yxh6 = self.rotr(z1, 8, 6)
        tp0 = ['tc'+str(i)+'Rd'+str(r-1) for i in range(8)]
        tp1 = ['td'+str(i)+'Rd'+str(r-1) for i in range(8)]
        constraints = constraints + ConstraintGenerator.xorConstraints(x3,  z1yxh3, tp0)
        constraints = constraints + ConstraintGenerator.xorConstraints(temp1,  z1yxh6, tp1)
        constraints = constraints + ConstraintGenerator.xorConstraints(tp1, z1yxh4, tp0)

        #right F0
        d = ['zero_var',D[16],D[17],D[18],D[19],D[20],D[21],D[22],D[23]]
        for i in range(8) :
            a = [x4[i],key[8+i],z2[i]]
            constraints = constraints + [d[i]+' - '+a[0]+' - '+a[1]+' + '+a[2]+' + '+d[i+1]+' >= 0']
            constraints = constraints + [d[i]+' + '+a[0]+' + '+a[1]+' - '+a[2]+' - '+d[i+1]+' >= 0']
            constraints = constraints + [d[i]+' + '+a[0]+' - '+a[1]+' - '+a[2]+' + '+d[i+1]+' >= 0']
            constraints = constraints + [d[i]+' - '+a[0]+' + '+a[1]+' - '+a[2]+' + '+d[i+1]+' >= 0']
            constraints = constraints + [d[i]+' + '+a[0]+' - '+a[1]+' + '+a[2]+' - '+d[i+1]+' >= 0']
            constraints = constraints + [d[i]+' - '+a[0]+' + '+a[1]+' + '+a[2]+' - '+d[i+1]+' >= 0']
            constraints = constraints + [a[0]+' - '+d[i]+' + '+a[1]+' + '+a[2]+' + '+d[i+1]+' >= 0']
            constraints = constraints + [d[i]+' + '+a[0]+' + '+a[1]+' + '+a[2]+' + '+d[i+1]+' <= 4']
        z2yxh1 = self.rotr(z2, 8, 1)
        z2yxh2 = self.rotr(z2, 8, 2)
        z2yxh7 = self.rotr(z2, 8, 7)
        tp0 = ['te'+str(i)+'Rd'+str(r-1) for i in range(8)]
        tp1 = ['tf'+str(i)+'Rd'+str(r-1) for i in range(8)]
        constraints = constraints + ConstraintGenerator.xorConstraints(x5,  z2yxh1, tp0)
        constraints = constraints + ConstraintGenerator.xorConstraints(temp2,  z2yxh7, tp1)
        constraints = constraints + ConstraintGenerator.xorConstraints(tp1, z2yxh2, tp0)

        d = ['zero_var',D[24],D[25],D[26],D[27],D[28],D[29],D[30],D[31]]
        for i in range(8) :
            a = [afteradd1[i],x6[i],z3[i]]
            constraints = constraints + [d[i] + ' - ' + a[0]+' - ' + a[1]+' + '+a[2]+' + '+d[i+1]+' >= 0']
            constraints = constraints + [d[i] + ' + ' + a[0]+' + ' + a[1]+' - '+a[2]+' - '+d[i+1]+' >= 0']
            constraints = constraints + [d[i] + ' + ' + a[0]+' - ' + a[1]+' - '+a[2]+' + '+d[i+1]+' >= 0']
            constraints = constraints + [d[i] + ' - ' + a[0]+' + ' + a[1]+' - '+a[2]+' + '+d[i+1]+' >= 0']
            constraints = constraints + [d[i] + ' + ' + a[0]+' - ' + a[1]+' + '+a[2]+' - '+d[i+1]+' >= 0']
            constraints = constraints + [d[i] + ' - ' + a[0]+' + ' + a[1]+' + '+a[2]+' - '+d[i+1]+' >= 0']
            constraints = constraints + [a[0] + ' - ' + d[i]+' + ' + a[1]+' + '+a[2]+' + '+d[i+1]+' >= 0']
            constraints = constraints + [d[i] + ' + ' + a[0]+' + ' + a[1]+' + '+a[2]+' + '+d[i+1]+' <= 4']
        z3yxh3 = self.rotr(z3, 8, 3)
        z3yxh4 = self.rotr(z3, 8, 4)
        z3yxh6 = self.rotr(z3, 8, 6)
        tp0 = ['tg'+str(i)+'Rd'+str(r-1) for i in range(8)]
        tp1 = ['th'+str(i)+'Rd'+str(r-1) for i in range(8)]
        constraints = constraints + ConstraintGenerator.xorConstraints(x7,  z3yxh3, tp0)
        constraints = constraints + ConstraintGenerator.xorConstraints(temp3,  z3yxh6, tp1)
        constraints = constraints + ConstraintGenerator.xorConstraints(tp1, z3yxh4, tp0)
        
        A = x0 + afteradd0 + x4 + afteradd1 + temp0 + temp1 + temp2 + temp3
        B = y7 + y1 + y3 + y5 + y0 + y2 + y4 + y6
        
        for i in range(0, 64) :
            constraints = constraints + [str(A[i]) + ' - ' + str(B[i]) + ' = 0']
            
        return constraints

    def genObjectiveFun_to_Round(self, r):
        assert (r >= 1)
        f = list([])
        for i in range(1, 2):
            d = ['pro'+str(t)+'Rd'+str(i) for t in range(32)]
            for j in range(1):
                f.append(d[j])
        f = ' + '.join(f)
        return f
    

    def genModel(self, r):
        V = set([])
        C = list([])
        for i in range(1, r+1):
            C = C + self.genConstraints_of_Round(i)
        V = BasicTools.getVariables_From_Constraints(C)
        
        add_constraint_1 = ' + '.join(['p'+str(i) for i in range(self.BlockSize)]) + ' = 1'
        add_constraint_2 = ' + '.join(self.genVars_InVars_at_Round(r + 1)) + ' = 1'
        
        filename='hight-zc-addequa-'+str(r)+'.lp'
        o=open(filename,'w')
        
        o.write('Minimize')
        o.write('\n')
        o.write(self.genObjectiveFun_to_Round(r))
        o.write('\n')
        o.write('\n')
        o.write('Subject To')
        o.write('\n')
        o.write(add_constraint_1)
        o.write('\n')
        o.write('p15 = 1')
        o.write('\n')
        o.write(add_constraint_2)
        o.write('\n')
        o.write('p7Rd17 = 1')
        o.write('\n')
        o.write('zero_var = 0')
        o.write('\n')          
        for c in C:
            o.write(c)
            o.write('\n')
        o.write('\n')
        o.write('\n')
        o.write('Binary')
        o.write('\n')
        for v in V:
            o.write(v)
            o.write('\n')
        o.close()     
        
def main():
    print('Initialized...')
    m=hight()
    m.genModel(17)
    
if __name__ == '__main__':
    main()
