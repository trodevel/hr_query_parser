#!/bin/bash

FL=languages.py

echo "from enum import Enum" > $FL
echo "class Language(int, Enum):" >> $FL
sed -e "s/, /_/" -e "s/ /_/" -e "s/\-/_/" languages.csv | awk -F";" '{printf "    %s = %s\n", $2, $1; }' >> $FL
