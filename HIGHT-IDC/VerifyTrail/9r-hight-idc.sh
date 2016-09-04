#! /bin/bash

for((i=0;i<8;i=i+1))
do
    var[i]="p$((i+56))Rd9"
done

rm -f txt-1
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
echo "i = $i j = $j k = $k l = $l m = $m n = $n o = $o p = $p"  >> txt-1

sed  -e "7c ${var[0]} = $i" \
     -e "8c ${var[1]} = $j" \
     -e "9c ${var[2]} = $k" \
     -e "10c ${var[3]} = $l" \
     -e "11c ${var[4]} = $m" \
     -e "12c ${var[5]} = $n" \
     -e "13c ${var[6]} = $o" \
     -e "14c ${var[7]} = $p" hight-impossible-dc-Addequa-1-9.lp > impossible-1.lp

gurobi.sh impossible-1.py

done
done
done
done
done
done
done
done
exit 0
