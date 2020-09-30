#!/bin/bash

set -euo pipefail

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"

INPUT=$DIR/../input_test/
OUTPUT=$DIR/../output/
SCRIPTS=$DIR/../scripts/
bold=$(tput bold)
normal=$(tput sgr0)
R1="$INPUT"/test_input_genera_part1.xlsx
R2="$INPUT"/test_input_genera_part2.xlsx
R3="$INPUT"/test_input_genera_part3.xlsx

for i in $R1 $R2 $R3;
do
  echo "$bold * Validating: $(basename $i)$normal"
  if [ -e "$i" ]; then
    $SCRIPTS/gan-validate.py -p -i "$i"
  else
    echo "ERROR: $i not found."
    exit 1
  fi
done

echo "$bold * Genera: three roots$normal"
set -x pipefail
mkdir -p $OUTPUT/
$SCRIPTS/gan-genus.py -1 "$R1" -2 "$R2" -3 "$R3" -o $OUTPUT/ > $OUTPUT/genera_3.html
set +x

echo "$bold * Genera: two roots$normal"
$SCRIPTS/gan-genus.py -1 "$R1" -2 "$R3"  -o $OUTPUT/ > $OUTPUT/genera_2.html

