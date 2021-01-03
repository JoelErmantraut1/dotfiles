# -*- coding: utf-8 -*-

from libqtile import hook

# Imports

# Always display launcher in current group
@hook.subscribe.client_new
def albert_open(window):
    if window.name == "Albert":
        window.cmd_togroup()