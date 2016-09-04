#! /bin/bash

var[0]="p0Rd17"
var[1]="p1Rd17"
var[2]="p2Rd17"
var[3]="p3Rd17"
var[4]="p4Rd17"
var[5]="p5Rd17"
var[6]="p6Rd17"
var[7]="p7Rd17"
var[8]="p8Rd17"
var[9]="p9Rd17"
var[10]="p10Rd17"
var[11]="p11Rd17"
var[12]="p12Rd17"
var[13]="p13Rd17"
var[14]="p14Rd17"
var[15]="p15Rd17"
var[16]="p16Rd17"
var[17]="p17Rd17"
var[18]="p18Rd17"
var[19]="p19Rd17"
var[20]="p20Rd17"
var[21]="p21Rd17"
var[22]="p22Rd17"
var[23]="p23Rd17"
var[24]="p24Rd16"
var[25]="p25Rd16"
var[26]="p26Rd16"
var[27]="p27Rd16"
var[28]="p28Rd16"
var[29]="p29Rd16"
var[30]="p30Rd16"
var[31]="p31Rd16"
var[32]="p24Rd17"
var[33]="p25Rd17"
var[34]="p26Rd17"
var[35]="p27Rd17"
var[36]="p28Rd17"
var[37]="p29Rd17"
var[38]="p30Rd17"
var[39]="p31Rd17"
var[40]="p32Rd17"
var[41]="p33Rd17"
var[42]="p34Rd17"
var[43]="p35Rd17"
var[44]="p36Rd17"
var[45]="p37Rd17"
var[46]="p38Rd17"
var[47]="p39Rd17"
var[48]="p40Rd17"
var[49]="p41Rd17"
var[50]="p42Rd17"
var[51]="p43Rd17"
var[52]="p44Rd17"
var[53]="p45Rd17"
var[54]="p46Rd17"
var[55]="p47Rd17"
var[56]="p0Rd16"
var[57]="p1Rd16"
var[58]="p2Rd16"
var[59]="p3Rd16"
var[60]="p4Rd16"
var[61]="p5Rd16"
var[62]="p6Rd16"
var[63]="p7Rd16"

rm -f result

for((i=3;i<64;i=i+4))
do
for((j=3;j<64;j=j+4))
do
echo "i = $i j = $j"  >> result
sed  -e "6c p$i = 1"  -e "8c ${var[$j]} = 1" hight-line-17.lp > impossible.lp

#Set your gurobi.sh path
/home/shawn/gurobi652/linux64/bin/gurobi.sh impossible.py

done
done
exit 0
