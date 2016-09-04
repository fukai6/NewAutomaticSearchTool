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
            return ['p'+str(j) for j in range(64)]
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
        roundy = self.genVars_InVars_at_Round(r + 1)
        roundtemp = ['tmp' + str(j) + 'Rd' + str(r - 1) for j in range(0, 32)]
        
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
        
        afterxor = ['middle'+str(i)+'Rd'+str(r-1) for i in range(32)]
        z0 = afterxor[0 : 8]
        z1 = afterxor[8 :16]
        z2 = afterxor[16:24]
        z3 = afterxor[24:32]
        
        afteradd = ['k'+str(i)+'Rd'+str(r-1) for i in range(16)]
        m0 = afteradd[0 : 8]
        m1 = afteradd[8 :16]
        m0[7] = z0[7]
        m1[7] = z2[7]
        
        #left F0
        x1zxh1 = self.rotl(x1, 8, 1)
        x1zxh2 = self.rotl(x1, 8, 2)
        x1zxh7 = self.rotl(x1, 8, 7)
        tp = ['ta'+str(i)+'Rd'+str(r-1) for i in range(8)]
        constraints = constraints + ConstraintGenerator.xorConstraints(z0,     x1zxh1, tp)
        constraints = constraints + ConstraintGenerator.xorConstraints(x1zxh2, x1zxh7, tp)   
        d = ['pro'+str(i)+'Rd'+str(r-1) for i in range(7)]
        for i in range(7) :
            b = [z0[i],  'zero_var',m0[i]]
            a = [z0[i+1],'zero_var',m0[i+1]]
            constraints = constraints + [a[1]+' - '+a[2]+' + '+d[i]+' >= 0 ']
            constraints = constraints + [a[0]+' - '+a[1]+' + '+d[i]+' >= 0 ']
            constraints = constraints + [a[2]+' - '+a[0]+' + '+d[i]+' >= 0 ']
            constraints = constraints + [a[0]+' + '+a[1]+' + '+a[2]+' + '+d[i]+' <= 3 ']
            constraints = constraints + [a[0]+' + '+a[1]+' + '+a[2]+' - '+d[i]+' >= 0 ']
            constraints = constraints + [b[0]+' + '+b[1]+' + '+b[2]+' + '+d[i]+' - '+a[1]+' >= 0 ']
            constraints = constraints + [a[1]+' + '+b[0]+' - '+b[1]+' + '+b[2]+' + '+d[i]+' >= 0 ']
            constraints = constraints + [a[1]+' - '+b[0]+' + '+b[1]+' + '+b[2]+' + '+d[i]+' >= 0 ']
            constraints = constraints + [a[0]+' + '+b[0]+' + '+b[1]+' - '+b[2]+' + '+d[i]+' >= 0 ']
            constraints = constraints + [a[2]+' - '+b[0]+' - '+b[1]+' - '+b[2]+' + '+d[i]+' >= -2 ']
            constraints = constraints + [b[0]+' - '+a[1]+' - '+b[1]+' - '+b[2]+' + '+d[i]+' >= -2 ']
            constraints = constraints + [b[1]+' - '+a[1]+' - '+b[0]+' - '+b[2]+' + '+d[i]+' >= -2 ']
            constraints = constraints + [b[2]+' - '+a[1]+' - '+b[0]+' - '+b[1]+' + '+d[i]+' >= -2 ']
        constraints = constraints + ConstraintGenerator.xorConstraints(x0, m0, temp0)
        
        #left F1
        x3zxh3 = self.rotl(x3, 8, 3)
        x3zxh4 = self.rotl(x3, 8, 4)
        x3zxh6 = self.rotl(x3, 8, 6)
        tp = ['tb'+str(i)+'Rd'+str(r-1) for i in range(8)]
        constraints = constraints + ConstraintGenerator.xorConstraints(z1,     x3zxh3, tp)
        constraints = constraints + ConstraintGenerator.xorConstraints(x3zxh4, x3zxh6, tp)
        d = ['pro'+str(i)+'Rd'+str(r-1) for i in range(7,14)]
        for i in range(7) :
            b = [z1[i],  x2[i],  temp1[i]]
            a = [z1[i+1],x2[i+1],temp1[i+1]]
            constraints = constraints + [a[1]+' - '+a[2]+' + '+d[i]+' >= 0 ']
            constraints = constraints + [a[0]+' - '+a[1]+' + '+d[i]+' >= 0 ']
            constraints = constraints + [a[2]+' - '+a[0]+' + '+d[i]+' >= 0 ']
            constraints = constraints + [a[0]+' + '+a[1]+' + '+a[2]+' + '+d[i]+' <= 3 ']
            constraints = constraints + [a[0]+' + '+a[1]+' + '+a[2]+' - '+d[i]+' >= 0 ']
            constraints = constraints + [b[0]+' + '+b[1]+' + '+b[2]+' + '+d[i]+' - '+a[1]+' >= 0 ']
            constraints = constraints + [a[1]+' + '+b[0]+' - '+b[1]+' + '+b[2]+' + '+d[i]+' >= 0 ']
            constraints = constraints + [a[1]+' - '+b[0]+' + '+b[1]+' + '+b[2]+' + '+d[i]+' >= 0 ']
            constraints = constraints + [a[0]+' + '+b[0]+' + '+b[1]+' - '+b[2]+' + '+d[i]+' >= 0 ']
            constraints = constraints + [a[2]+' - '+b[0]+' - '+b[1]+' - '+b[2]+' + '+d[i]+' >= -2 ']
            constraints = constraints + [b[0]+' - '+a[1]+' - '+b[1]+' - '+b[2]+' + '+d[i]+' >= -2 ']
            constraints = constraints + [b[1]+' - '+a[1]+' - '+b[0]+' - '+b[2]+' + '+d[i]+' >= -2 ']
            constraints = constraints + [b[2]+' - '+a[1]+' - '+b[0]+' - '+b[1]+' + '+d[i]+' >= -2 ']
        constraints = constraints + [x2[7]+' + '+z1[7]+' + '+temp1[7]+' <= 2 ']
        constraints = constraints + [x2[7]+' + '+z1[7]+' + '+temp1[7]+' - 2 tpa'+str(r-1)+' >= 0 ']
        constraints = constraints + ['tpa'+str(r-1)+' - '+x2[7]+' >= 0 ']
        constraints = constraints + ['tpa'+str(r-1)+' - '+temp1[7]+' >= 0 ']
        constraints = constraints + ['tpa'+str(r-1)+' - '+z1[7]+' >= 0 ']

        #right F0
        x5zxh1 = self.rotl(x5, 8, 1)
        x5zxh2 = self.rotl(x5, 8, 2)
        x5zxh7 = self.rotl(x5, 8, 7)
        tp = ['tc'+str(i)+'Rd'+str(r-1) for i in range(8)]
        constraints = constraints + ConstraintGenerator.xorConstraints(z2,     x5zxh1, tp)
        constraints = constraints + ConstraintGenerator.xorConstraints(x5zxh2, x5zxh7, tp)   
        d = ['pro'+str(i)+'Rd'+str(r-1) for i in range(14,21)]   
        for i in range(7) :
            b = [z2[i],  'zero_var',m1[i]]
            a = [z2[i+1],'zero_var',m1[i+1]]
            constraints = constraints + [a[1]+' - '+a[2]+' + '+d[i]+' >= 0 ']
            constraints = constraints + [a[0]+' - '+a[1]+' + '+d[i]+' >= 0 ']
            constraints = constraints + [a[2]+' - '+a[0]+' + '+d[i]+' >= 0 ']
            constraints = constraints + [a[0]+' + '+a[1]+' + '+a[2]+' + '+d[i]+' <= 3 ']
            constraints = constraints + [a[0]+' + '+a[1]+' + '+a[2]+' - '+d[i]+' >= 0 ']
            constraints = constraints + [b[0]+' + '+b[1]+' + '+b[2]+' + '+d[i]+' - '+a[1]+' >= 0 ']
            constraints = constraints + [a[1]+' + '+b[0]+' - '+b[1]+' + '+b[2]+' + '+d[i]+' >= 0 ']
            constraints = constraints + [a[1]+' - '+b[0]+' + '+b[1]+' + '+b[2]+' + '+d[i]+' >= 0 ']
            constraints = constraints + [a[0]+' + '+b[0]+' + '+b[1]+' - '+b[2]+' + '+d[i]+' >= 0 ']
            constraints = constraints + [a[2]+' - '+b[0]+' - '+b[1]+' - '+b[2]+' + '+d[i]+' >= -2 ']
            constraints = constraints + [b[0]+' - '+a[1]+' - '+b[1]+' - '+b[2]+' + '+d[i]+' >= -2 ']
            constraints = constraints + [b[1]+' - '+a[1]+' - '+b[0]+' - '+b[2]+' + '+d[i]+' >= -2 ']
            constraints = constraints + [b[2]+' - '+a[1]+' - '+b[0]+' - '+b[1]+' + '+d[i]+' >= -2 ']
        constraints = constraints + ConstraintGenerator.xorConstraints(x4, m1, temp2)

        #right F1
        x7zxh3 = self.rotl(x7, 8, 3)
        x7zxh4 = self.rotl(x7, 8, 4)
        x7zxh6 = self.rotl(x7, 8, 6)
        tp = ['td'+str(i)+'Rd'+str(r-1) for i in range(8)]
        constraints = constraints + ConstraintGenerator.xorConstraints(z3,     x7zxh3, tp)
        constraints = constraints + ConstraintGenerator.xorConstraints(x7zxh4, x7zxh6, tp)
        d = ['pro'+str(i)+'Rd'+str(r-1) for i in range(21,28)]   
        for i in range(7) :
            b = [z3[i],  x6[i],  temp3[i]]
            a = [z3[i+1],x6[i+1],temp3[i+1]]
            constraints = constraints + [a[1]+' - '+a[2]+' + '+d[i]+' >= 0 ']
            constraints = constraints + [a[0]+' - '+a[1]+' + '+d[i]+' >= 0 ']
            constraints = constraints + [a[2]+' - '+a[0]+' + '+d[i]+' >= 0 ']
            constraints = constraints + [a[0]+' + '+a[1]+' + '+a[2]+' + '+d[i]+' <= 3 ']
            constraints = constraints + [a[0]+' + '+a[1]+' + '+a[2]+' - '+d[i]+' >= 0 ']
            constraints = constraints + [b[0]+' + '+b[1]+' + '+b[2]+' + '+d[i]+' - '+a[1]+' >= 0 ']
            constraints = constraints + [a[1]+' + '+b[0]+' - '+b[1]+' + '+b[2]+' + '+d[i]+' >= 0 ']
            constraints = constraints + [a[1]+' - '+b[0]+' + '+b[1]+' + '+b[2]+' + '+d[i]+' >= 0 ']
            constraints = constraints + [a[0]+' + '+b[0]+' + '+b[1]+' - '+b[2]+' + '+d[i]+' >= 0 ']
            constraints = constraints + [a[2]+' - '+b[0]+' - '+b[1]+' - '+b[2]+' + '+d[i]+' >= -2 ']
            constraints = constraints + [b[0]+' - '+a[1]+' - '+b[1]+' - '+b[2]+' + '+d[i]+' >= -2 ']
            constraints = constraints + [b[1]+' - '+a[1]+' - '+b[0]+' - '+b[2]+' + '+d[i]+' >= -2 ']
            constraints = constraints + [b[2]+' - '+a[1]+' - '+b[0]+' - '+b[1]+' + '+d[i]+' >= -2 ']
        constraints = constraints + [x6[7]+' + '+z3[7]+' + '+temp3[7]+' <= 2 ']
        constraints = constraints + [x6[7]+' + '+z3[7]+' + '+temp3[7]+' - 2 tpb'+str(r-1)+' >= 0 ']
        constraints = constraints + ['tpb'+str(r-1)+' - '+x6[7]+' >= 0 ']
        constraints = constraints + ['tpb'+str(r-1)+' - '+temp3[7]+' >= 0 ']
        constraints = constraints + ['tpb'+str(r-1)+' - '+z3[7]+' >= 0 ']
        
        
        A = x1 + x3 + x5 + x7 + temp0 + temp1 + temp2 + temp3
        B = y0 + y2 + y4 + y6 + y7 + y1 + y3 + y5
        for i in range(0, 64) :
            constraints = constraints + [str(A[i]) + ' - ' + str(B[i]) + ' = 0']
        
        return constraints

    def genObjectiveFun_to_Round(self, r):
        assert (r >= 1)
        f = list([])
        for i in range(1):
            d = ['pro'+str(t)+'Rd'+str(i) for t in range(28)]
            for j in range(1):
                f.append(d[j])
        f = ' + '.join(f)
        return f
    

    def genModel(self, r):
        V = set([])
        C = list([])
        for i in range(10, r+1):
            C = C + self.genConstraints_of_Round(i)
        V = BasicTools.getVariables_From_Constraints(C)
        
        add_constraint_1 = ' + '.join(self.genVars_InVars_at_Round(r+1)) + ' = 1'
        
        
        filename='hight-impossible-dc-Addequa-10-'+str(r)+'.lp'
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
        o.write('p56Rd17 = 1')
        o.write('\n\n\n\n\n\n\n\n\n')
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
    
if __name__ == '__main__':
    main()
    m=hight()
    m.genModel(17)