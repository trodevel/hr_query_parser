#!/bin/bash

FL=../languages.py

echo "from enum import Enum" > $FL
echo "class Language(int, Enum):" >> $FL
tail -n +2 languages.csv | tr "\t" ";" | awk -F";" '{ printf "%s;%s\n", $2, $1; }' | nl -s";" -nln -w1 | awk -F";" '{printf "    %s = %s # %s\n", $2, $1, $3; }' >> $FL
