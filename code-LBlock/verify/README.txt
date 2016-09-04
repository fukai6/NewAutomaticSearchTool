Instructions:

Target related-key impossible differential: 
input and output difference are both zero, 
the most significant bit of master key difference is 1 and others are all 0.

1. use "LBlock-re-imp(gai).py" to produce the model "LBlock_imp-gai-1-16.lp";

2. try to remove all unnecessary equalities bewteen the output difference of round 8 and    the input difference of round 9;
   About 4 equalities are remained, see "LBlock_imp-small-contradiction-16.lp"
   This means the contradiction is on such 4-bit input difference of round 9.

3. produce the model for rounds 1-8: "LBlock_imp-gai-1-8.lp";
   produce the model for rounds 9-16: "LBlock_imp-gai-9-16.lp";
   run "lblock-verify-1-8.py" to obtain the first solution set on the contradictory 4       bits from the first model;
   run "lblock-verify-9-16.py" to obtain the second solution set on the contradictory 4     bits from the second model;
   compare these two sets, they have no intersection;