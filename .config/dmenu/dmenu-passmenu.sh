#!/usr/bin/env bash

shopt -s nullglob globstar

typeit=1
if [[ $1 == "--type" ]]; then
	typeit=1
	shift
fi

prefix=${PASSWORD_STORE_DIR-~/.password-store}
password_files=( "$prefix"/**/*.gpg )
password_files=( "${password_files[@]#"$prefix"/}" )
password_files=( "${password_files[@]%.gpg}" )

password=$(printf '%s\n' "${password_files[@]}" | dmenu -p 'Config: ' -i -nf '#888888' -nb '#292d3e' -sf '#ffffff' -sb '#005577' -fn 'UbuntuMono Nerd Font' "$@")

[[ -n $password ]] || exit

if [[ $typeit -eq 0 ]]; then
	pass show -c "$password" 2>/dev/null
else
	pass show "$password" | { IFS= read -r pass; printf %s "$pass"; } |
		xdotool type --clearmodifiers --file -
        xdotool key KP_Enter
        # Writes password and presses Enter key
    #notify-send -a "Passmenu" -t 1000 "Contraseña Escrita" -u low
fi
