#!/bin/bash

# A shell script that checks for compile errors in all .py files in the current
# directory. Does not work if there are no .py files in the current directory.

echo
echo "Checking for compile errors in all .py files..."
echo

# Checks for compilation errors in all .py files.
for i in *.py
do
    echo "python3 -m py_compile `basename $i .py`.py"
    python3 -m py_compile `basename $i .py`".py"
    echo
done

echo "Compilation done."
echo