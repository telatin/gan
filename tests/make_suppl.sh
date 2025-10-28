#!/bin/bash
set -euxo pipefail
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
JOIN="of"
DATASETS="$DIR/../the_real_final_input"
GAN="$DIR/../scripts/gan-genus.py"
VAL="$DIR/../scripts/gan-validate.py"
for i in "$DATASETS"/*; 
do
  B=$(basename $i); 
  echo $B; 
  for FILE in "$i"/[1-3].xlsx; do
  	$VAL -t -i "$FILE" > "$FILE.validation.log" 2>&1
  done
done


for i in "$DATASETS"/*; 
do
  B=$(basename $i); 
  echo $B; 
  if [[ -e "$i/1.xlsx" && -e "$i/2.xlsx" && -e "$i/3.xlsx" ]]; then
    $GAN -1 "$i/1.xlsx" -2 "$i/2.xlsx" -3 "$i/3.xlsx" --connector "$JOIN" -o "$i/" --prefix "${B/_/-}"
  elif [[ -e "$i/1.xlsx" && -e "$i/2.xlsx" ]]; then
  	$GAN -1 "$i/1.xlsx" -2 "$i/2.xlsx"                --connector "$JOIN" -o "$i/" --prefix "${B/_/-}"

  fi
done

