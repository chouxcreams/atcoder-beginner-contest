#usr/local/bin/bash

root=$(git rev-parse --show-toplevel)
cd "$root" || return
acc new "$CURRENT_CONTEST" --template python