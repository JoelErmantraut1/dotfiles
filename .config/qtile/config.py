"""
INTERESTING FUNCTION TO ADD:

    - Finish with hotkeys (do images)
    - Change icons on layouts
    - That when I want to open calendar, can open Franz in Calendar tab
    - Spotify problem, not starting in the correct group

"""

# -*- coding: utf-8 -*-
from libqtile import bar, hook
from libqtile.config import Screen
# Qtile imports

from settings.common import colors
from settings.mouse import mouse
from settings.hooks import float_put_over  
from settings.key_settings import keys
from settings.groups_settings import groups
from settings.layouts_settings import floating_layout
from settings.widget_settings import widgets_top, widgets_bottom

screens = [
    Screen(
        top=bar.Bar(
            widgets_top,
            opacity = 0.9,
            size=20,
            background=colors[0]
        ),
        bottom=bar.Bar(
            widgets_bottom,
            opacity=0.9,
            size=20,
        )
    ),
    Screen() # For projection if needed
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = False
bring_front_click = True
# Click brings to front of floating windows
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "focus"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

"""
INTERESTING TOOLS CURRENTLY NOT IN USE

def is_running(process):
    s = subprocess.Popen(["ps", "axw"], stdout=subprocess.PIPE)
    for x in s.stdout:
        if re.search(process, x):
            return True
        return False

def execute_once(process):
    if not is_running(process):
        return subprocess.Popen(process.split())

@hook.subscribe.startup
def start():
    pass

"""
