#!/bin/bash

result=$(sensors | grep "Tdie")

IFS=' '
read -ra ADDR <<< "$result"
value=${ADDR[1]}
echo ${value:1:${#value}}
