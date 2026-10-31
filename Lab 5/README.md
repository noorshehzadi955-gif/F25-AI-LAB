# Description
This lab implements the Minimax and Alpha-Beta pruning algorithms on a
complete binary game tree. Both algorithms count the leaf nodes they
evaluate, so the amount of work saved by pruning can be compared.

## Files
- `minimax.py` - Python code for Minimax, Alpha-Beta pruning and the comparison tests
- `Lab5_Report_Rasikh_Ali.docx` - Lab report with output, hand traces and analysis

## How to Run
python minimax.py

## Results
- Minimax and Alpha-Beta always return the same root value.
- Alpha-Beta evaluates the same number of leaves or fewer than Minimax,
  depending on the move ordering (6, 8, 5 and 5 leaves against 8 for Minimax).
