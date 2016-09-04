Instructions:

1. Run "LBlock-re-imp.py" to produce a basic model for 16-round LBlock;
   Open "LBlock-re-imp.py", then click F5 to run, then produce a "LBlock_imp-16.lp" file.

2. Under the path of Gurobi, run "lblock-special.py";
   For example: cd ****/gurobi605/linux/bin
		./gurobi.sh lblock-special.py
   The search result is stored in file "results-re-lblock-16.txt".

Note that in the paper, the most significant bit (msb) of LBlock master key is $k_79$, but in the "LBlock-re-imp.py" the msb is $k_0$, which means the master key orders in paper and in code are inverse.