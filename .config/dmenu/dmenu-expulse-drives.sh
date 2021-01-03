#!/bin/bash

pens=()
pens_name=()
index=0

getIndex() {
	while [ ${pens_name[$index]} != $choice ] && [ $index -lt "${#pens_name[@]}" ]; do ((index++)); done
	if [ $index -lt "${#pens_name[@]}" ]; then
		echo $index
	else
		echo 'Not Found'
	fi
}

for device in /run/media/joel/*
do
    pens+=("$device")
    readarray -d / -t strarr <<< "$device"
    pens_name+=("${strarr[-1]}")
done

choice="$(echo -e "${pens_name[@]}" | dmenu -p 'Desmontar: ' -i -nf '#888888' -nb '#292d3e' -sf '#ffffff' -sb '#005577' -fn 'UbuntuMono Nerd Font')" || exit 1

getIndex

umount "${pens[$index]}"
