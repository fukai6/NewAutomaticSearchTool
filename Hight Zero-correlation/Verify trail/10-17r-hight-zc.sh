#! /bin/bash

for((i=0;i<8;i=i+1))
do
    var[i]="p$((i))Rd9"
done

rm -f txt-2
for((i=0;i<2;i=i+1))
do
for((j=0;j<2;j=j+1))
do
for((k=0;k<2;k=k+1))
do
for((l=0;l<2;l=l+1))
do
for((m=0;m<2;m=m+1))
do
for((n=0;n<2;n=n+1))
do
for((o=0;o<2;o=o+1))
do
for((p=0;p<2;p=p+1))
do
echo "i = $i j = $j k = $k l = $l m = $m n = $n o = $o p = $p"  >> txt-2

sed  -e "7c ${var[0]} = $i" \
     -e "8c ${var[1]} = $j" \
     -e "9c ${var[2]} = $k" \
     -e "10c ${var[3]} = $l" \
     -e "11c ${var[4]} = $m" \
     -e "12c ${var[5]} = $n" \
     -e "13c ${var[6]} = $o" \
     -e "14c ${var[7]} = $p" hight-zc-addequa-10-17.lp > impossible-2.lp

gurobi.sh impossible-2.py

done
done
done
done
done
done
done
done
exit 0
