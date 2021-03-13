#!/bin/bash

result=$(amixer get Master |grep % |awk '{print $6}'|sed -e 's/\[//' -e 's/\]//')

if [ ${#result} -eq 5 ]; then
    result=$(amixer get Master |grep % |awk '{print $5}'|sed -e 's/\[//' -e 's/\]//')
    IFS=' '
    read -ra ADDR <<< "$result"
    echo "${ADDR[0]}"
else
    echo "M"
fi
