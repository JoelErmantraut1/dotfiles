# -*- coding: utf-8 -*-

import subprocess
import re
import screeninfo

from libqtile.lazy import lazy
from libqtile import widget

from settings.common import colors, widget_colors, icons_font, HOME

# Imports

def get_screen_resolution():
    """
    Gets screen resolution.
    """
    screen = screeninfo.get_monitors()[0]
    width = screen.width
    height = screen.height

    return width, height

@lazy.function
def kill_all_windows(qtile):
    """
    Closes all windows.
    """
    for group in qtile.groups:
        for window in group.windows:
            window.kill()

@lazy.function
def minimize_group(qtile):
    for window in qtile.current_group.windows:
        window.cmd_toggle_minimize()

def run_or_go(app):
    """
    If app is open, go to it in any group. Otherwise, open it.
    """
    def f(qtile):
        success = 0
        for group in qtile.groups:
            for window in group.windows:
                inspection = window.cmd_inspect()
                app_name = re.search(r"[a-z]*", inspection["wm_class"][0].lower()).group(0)
                # Gets the first word separated by any non-alfabetic character

                if app_name == app and group != qtile.current_group:
                    group.cmd_toscreen()
                    success = 1
                elif app_name == app and group == qtile.current_group:
                    success = 1

        if not success:
            qtile.cmd_spawn(app)

    return f

def run_or_bring(app):
    """
    If app is open, send it to current group. Otherwise, open it in current group.
    """
    def f_0(qtile):
        success = 0
        for group in qtile.groups:
            for window in group.windows:
                inspection = window.cmd_inspect()
                app_name = re.search(r"[a-z]*", inspection["wm_class"][0].lower()).group(0)
                # Gets the first word separated by any non-alfabetic character

                if app_name == app:
                    window.cmd_togroup(qtile.current_group.name)
                    success = 1
                elif app_name == app and group == qtile.current_group:
                    success = 1

        if not success:
            qtile.cmd_spawn(app)

    return f_0

def run_or_exit(app):
    """
    If app is open, closes it. Otherwise, opens the app.
    """
    def f_1(qtile):
        success = 0
        for group in qtile.groups:
            for window in group.windows:
                inspection = window.cmd_inspect()
                app_name = re.search(r"[a-z]*", inspection["wm_class"][0].lower()).group(0)
                # Gets the first word separated by any non-alfabetic character

                if app_name == app:
                    window.cmd_kill()
                    success = 1
                elif app_name == app and group == qtile.current_group:
                    success = 1

        if not success:
            qtile.cmd_spawn(app)

    return f_1

@lazy.function
def show_hotkeys(qtile):
    """
    Shows a hotkey list depending on the current window.
    """
    app = "hotkeysapp"

    for group in qtile.groups:
        for window in group.windows:
            inspection = window.cmd_inspect()
            app_name = re.search(r"[a-z]*", inspection["wm_class"][0].lower()).group(0)
            # Gets the first word separated by any non-alfabetic character

            with open("/home/joel/Documentos/Centro/log.txt", 'a') as file:
                file.write(app_name + '\n')

            if app_name == app:
                window.cmd_kill()
                return

    # If window wasn't found, opens it

    command = "alacritty -e python " + HOME + "/apps/hotkey_show/hotkeys_cheat_sheet.py {0} -t 'Hotkeys Help' -d 1x1"

    inspection = qtile.current_window.cmd_inspect()
    app_class = inspection["wm_class"]
    app_name = inspection["name"]
    if app_class in []:
        app = app_class
    elif app_name in ["ranger", "nvim"]:
        app = app_name
    else:
        app = "qtile"

    qtile.cmd_spawn(command.format(app.lower()))

# -----------------------------------------------------------------

def spacers(space_group_center):
    return widget.Spacer(
        length = space_group_center,
        background = colors[0]
    )

def separator():
    return widget.Sep(
        linewidth = 0,
        padding = 10,
        foreground = colors[2],
        background = colors[0]
    )

def widget_separator(colors_pack):
    return widget.TextBox(
        text = '',
        background = colors_pack[1],
        foreground = colors_pack[0],
        padding = -11,
        margin = 0,
        fontsize = 55
    )

def widget_icons(icon, background):
    return widget.TextBox(
        text = icon,
        foreground = colors[2],
        background = background[0],
        fontsize = 13,
        font = icons_font,
    )

def change_wallpaper(qtile):
    """
    Changes wallpaper using the nitrogen command.
    """
    qtile.cmd_spawn("nitrogen --random --set-zoom-fill")
