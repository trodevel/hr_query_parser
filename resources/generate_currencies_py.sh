#!/bin/bash

FL=../currencies.py

echo "from enum import Enum" > $FL
echo "class Currency(int, Enum):" >> $FL
awk -F"\t" '{printf "    %s = %s # %s\n", $1, $2, $4; }' currencies.csv >> $FL