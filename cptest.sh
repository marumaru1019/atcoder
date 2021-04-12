#!/bin/bash

# format problem_name = abc134 rank:a
problem_name=$1
rank=$2
test_dir=test/${problem_name}
# base_url=${problem_name%_*}

rm -R test

# make test directory
if [ ! -e ${test_dir} ]; then
    oj d https://atcoder.jp/contests/${problem_name}/tasks/${problem_name}_${rank}
fi

oj test -c "python3 problems/${problem_name}_${rank}.py" -d test/