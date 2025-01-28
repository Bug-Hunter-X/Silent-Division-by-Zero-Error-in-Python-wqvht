# Silent Division by Zero Error in Python

This repository demonstrates a subtle bug in a Python function that handles division by zero without explicitly raising an exception. The function incorrectly returns the non-zero argument in case of zero division, leading to unexpected results and making the error difficult to detect.

The `bug.py` file contains the erroneous code. The `bugSolution.py` provides a corrected version. 

This example highlights the importance of explicit error handling in preventing unexpected behavior and making code more robust.