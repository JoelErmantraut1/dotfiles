# -*- coding: utf-8 -*-

from libqtile import hook

# Imports

@hook.subscribe.client_focus
def float_put_over(window):
    if window.floating:
        window.cmd_bring_to_front()
# Makes new floating windows always stay at front
