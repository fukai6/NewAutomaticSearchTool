PART I
	1.Run "hight-zc-addequa.py"(need MILPSbox.pyc and on windows with python 3.*) to get 
"hight-zc-addeuqa-17.lp"(The model file of 17 round zero-correlation of hight).
	2.We select one trail in file "Find trail/result" to check, so in "hight-impossible-dc-
Addequa-17.lp", we add "p0 = 1" at line 6 and "p56Rd17 = 1" at line 8.
	3.Use gurobi to identify this trail is infeasible.
	4.We delete the equalities in between 9 and 10 round byte by byte, and leave one byte
make the model file "hight-impossible-dc-Addequa-17-LeftOneByteIn9Round.lp" still infeasible.

PART II
	1.Run "hight-impossible-dc-Addequa-1-9.py" to get "hight-impossible-dc-Addequa-1-9.lp".
	2.Run "9r-hight-idc.sh" to get the possible sets of the byte of round 9 
under the fixed input in round 1.
	3.In "txt-1", if the output byte of round 9 is impossible, it will print "infeasible"
in next line.

PART III
	1.Run "hight-impossible-dc-Addequa-10-17.py" to get "hight-impossible-dc-Addequa-10-17.lp".
	2.Run "10-17r-hight-idc.sh" to get the possible sets of the byte of round 10
under the fixed output in round 17.
	3.In "txt-2", if the output byte of round 10 is impossible, it will print "infeasible"
in next line.

	