alias ls='exa -l'
alias la='exa -la'
alias lg='exa -la --git-ignore'
alias ld='exa -l -D'
alias tree='exa --tree --level=2 -l'
alias cls='clear && ls'

alias shutdown='shutdown -h now'
alias suspend='systemctl suspend'

alias wm_class='xprop WM_CLASS'
alias rm='trash'

alias config='/usr/bin/git --git-dir=/home/joel/.cfg/ --work-tree=/home/joel'
alias libs='/usr/bin/git --git-dir=/home/datos/Documentos/Atollic_documents/.libraries/ --work-tree=/home/datos/Documentos/Atollic_documents/'

alias passi='pass insert -e'

alias el='krusader --left .'
alias er='krusader --right .'

alias addmic='pacmd load-module module-alsa-source device=hw:Loopback,1,0'

alias t='trans en:es'
alias T='trans es:en'

alias ps='procs --tree'

alias v='nvim'

alias feh='feh --draw-filename --scale-down --borderless --action "echo %n;"'
