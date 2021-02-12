#!/bin/bash

result=$(xinput --list-props 8 | grep "Device Enabled")

arrIN=(${result//;/})
result=${arrIN[-1]}

if [ "$result" = "1" ]; then
    xinput --disable 8
else
    xinput --enable 8
fi

