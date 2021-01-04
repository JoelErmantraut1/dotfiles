#!/bin/bash

declare options=("Apagar
Reiniciar
Suspender
Bloquear
Salir")

choice=$(echo -e "${options[@]}" | dmenu -p "»" -i -nf '#888888' -nb '#292d3e' -sf '#ffffff' -sb '#005577' -fn 'UbuntuMono Nerd Font') || exit 1

case "$choice" in
    Apagar)
        choice="shutdown -h now"
    ;;
    Reiniciar)
        choice="reboot"
    ;;
    Suspender)
        choice="systemctl suspend"
    ;;
    Bloquear)
        choice="dm-tool lock"
    ;;
    Salir)
        choice="kill -9 -1"
    ;;
esac
alacritty -e $choice
