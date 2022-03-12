#usr/local/bin/bash

cd `dirname $0`
root=$(git rev-parse --show-toplevel)
mkdir "$root"/"$CURRENT_CONTEST"
for task in 'a' 'b' 'c' 'd' 'e' 'f'
do
  dir="$root"/"$CURRENT_CONTEST"/"$task"
  mkdir "$dir"
  cp "$root"/solve.py "$dir"
  pipenv run oj dl https://atcoder.jp/contests/"$CURRENT_CONTEST"/tasks/"$CURRENT_CONTEST"_"$task" -d "$dir"/tests
done