#usr/local/bin/bash

root=$(git rev-parse --show-toplevel)
problem=$1
cd "$root" || return
pipenv run oj t -c "python $root/$CURRENT_CONTEST/$problem/solve.py" -d "${CURRENT_CONTEST}"/"${problem}"/tests/
