#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '
[ -r /home/joel/.byobu/prompt ] && . /home/joel/.byobu/prompt   #byobu-prompt#
