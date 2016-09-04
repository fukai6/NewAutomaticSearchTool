#! /bin/bash

var[0]="p0Rd16"
var[1]="p1Rd16"
var[2]="p2Rd16"
var[3]="p3Rd16"
var[4]="p4Rd16"
var[5]="p5Rd16"
var[6]="p6Rd16"
var[7]="p7Rd16"
var[8]="p0Rd17"
var[9]="p1Rd17"
var[10]="p2Rd17"
var[11]="p3Rd17"
var[12]="p4Rd17"
var[13]="p5Rd17"
var[14]="p6Rd17"
var[15]="p7Rd17"
var[16]="p8Rd16"
var[17]="p9Rd16"
var[18]="p10Rd16"
var[19]="p11Rd16"
var[20]="p12Rd16"
var[21]="p13Rd16"
var[22]="p14Rd16"
var[23]="p15Rd16"
var[24]="p8Rd17"
var[25]="p9Rd17"
var[26]="p10Rd17"
var[27]="p11Rd17"
var[28]="p12Rd17"
var[29]="p13Rd17"
var[30]="p14Rd17"
var[31]="p15Rd17"
var[32]="p16Rd16"
var[33]="p17Rd16"
var[34]="p18Rd16"
var[35]="p19Rd16"
var[36]="p20Rd16"
var[37]="p21Rd16"
var[38]="p22Rd16"
var[39]="p23Rd16"
var[40]="p16Rd17"
var[41]="p17Rd17"
var[42]="p18Rd17"
var[43]="p19Rd17"
var[44]="p20Rd17"
var[45]="p21Rd17"
var[46]="p22Rd17"
var[47]="p23Rd17"
var[48]="p24Rd16"
var[49]="p25Rd16"
var[50]="p26Rd16"
var[51]="p27Rd16"
var[52]="p28Rd16"
var[53]="p29Rd16"
var[54]="p30Rd16"
var[55]="p31Rd16"
var[56]="p24Rd17"
var[57]="p25Rd17"
var[58]="p26Rd17"
var[59]="p27Rd17"
var[60]="p28Rd17"
var[61]="p29Rd17"
var[62]="p30Rd17"
var[63]="p31Rd17"

rm -f result
for((i=0;i<64;i=i+1))
do
for((j=0;j<64;j=j+1))
do
echo "i = $i j = $j"  >> result
sed  -e "6c p$i = 1"  -e "8c ${var[$j]} = 1" hight-impossible-dc-17.lp > impossible.lp

gurobi.sh impossible.py

done
done
exit 0
