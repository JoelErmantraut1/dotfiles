# -*- coding: utf-8 -*-

import os.path

# Imports

HOME = os.path.expanduser('~')
# Files

mod = "mod4"
alt = "mod1"                                                # Sets mod key to SUPER/WINDOWS
shift = "shift"
ctrl = "control"
# Keys

terminal = "alacritty"
myConfig = HOME + "/.config/qtile/config.py"                # The Qtile config file location
navigator = "brave"
captures_path = HOME + "/Imagenes/Capturas"
calculator_title = "Qalculate!"
explorer = 'krusader'
secondary_explorer = 'pcmanfm'
note_app = 'gnote'
# Apps

common_font = "Ubuntu Mono"
icons_font = "UbuntuMono Nerd Font"
# Fonts

volume_step = 2
mute_toggle_command = "amixer -D pulse sset Master toggle"
unmute_command = "amixer -D pulse sset Master unmute"
volume_up_command = "amixer -D pulse sset Master {0}%+".format(volume_step)
volume_down_command = "amixer -D pulse sset Master {0}%-".format(volume_step)
# Commands

group_list_names = {
    "TERM": " ",
    "WEB": " ",
    "MAN": " ",
    "DEV": " ",
    "VAR": " ",
    "CHAT": " ",
    "MULT": "",
    "VBOX": " ",
    "FLT": " ",
    "CONF": " ",
    "AUX": ""
}
# Spaces are added to center the icons

group_list_keys = [
    'exclam',
    'quotedbl',
    'numbersign',
    'dollar',
    'percent',
    'ampersand',
    'slash',
    'parenleft',
    'parenright',
    'equal'
]
# Numbers associated with icons in keyboard layout

# Groups

colors = [
    ["#292d3e", "#292d3e"], # panel background
    ["#434758", "#434758"], # background for current screen tab
    ["#ffffff", "#ffffff"], # font color for group symbols
    ["#ff5555", "#ff5555"], # border line color for current tab
    ["#8d62a9", "#8d62a9"], # border line color for other tab and odd widgets
    ["#668bd7", "#668bd7"], # color for the even widgets
    ["#15C9EE", "#15C9EE"]
] # window name

# widget_colors = [
#     [["#668bd7", "#668bd7"], ["#60119D", "#60119D"]], # Temperature
#     [["#FF8E24", "#FF8E24"], ["#668bd7", "#668bd7"]], # Volume
#     [["#1F9C73", "#1F9C73"], ["#FF8E24", "#FF8E24"]], # Keyboard
#     [["#006A74", "#006A74"], ["#1F9C73", "#1F9C73"]], # Layout
#     [["#FF6666", "#FF6666"], ["#006A74", "#006A74"]], # Date
#     [["#292d3e", "#292d3e"], ["#006A74", "#006A74"]], # CheckUpdates
#     [["#60119D", "#60119D"], ["#0C2F66", "#0C2F66"]], # RAM
#     [["#0C2F66", "#0C2F66"], ["#FFDA00", "#FFDA00"]], # CPU
#     [["#FFDA00", "#FFDA00"], ["#292d3e", "#292d3e"]], # Wallpaper change widget
# ]

widget_colors = [
    [["#668bd7", "#668bd7"], ["#60119D", "#60119D"]], # Temperature
    [["#60119D", "#60119D"], ["#668bd7", "#668bd7"]], # Volume
    [["#668bd7", "#668bd7"], ["#60119D", "#60119D"]], # Keyboard
    [["#60119D", "#60119D"], ["#668bd7", "#668bd7"]], # Layout
    [["#668bd7", "#668bd7"], ["#60119D", "#60119D"]], # Date
    [["#60119D", "#60119D"], ["#668bd7", "#668bd7"]], # CheckUpdates
    [["#60119D", "#60119D"], ["#668bd7", "#668bd7"]], # RAM
    [["#668bd7", "#668bd7"], ["#60119D", "#60119D"]], # CPU
    [["#60119D", "#60119D"], ["#292d3e", "#292d3e"]], # Wallpaper change widget
]

# Background first
# Foreground second

layout_theme = {
    "border_width": 2,
    "margin": 3,
    "border_focus": "349beb",
    "border_normal": "1D2330",
}

# Styles
