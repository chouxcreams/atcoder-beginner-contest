#usr/local/bin/bash

problem=$1
root=$(git rev-parse --show-toplevel)
cd "$root/$CURRENT_CONTEST/$problem"
acc submit solve.py