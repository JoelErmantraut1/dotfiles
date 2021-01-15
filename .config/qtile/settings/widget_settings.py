# -*- coding: utf-8 -*-

from settings.common import *
from settings.functions import (
    get_screen_resolution, spacers, separator, 
    widget_separator, widget_icons, change_wallpaper,
    run_or_go, run_or_bring
)

from libqtile import widget
from libqtile.widget import base

import threading, subprocess

# Imports

# class CheckUpdates(base._TextBox):
    # """Widget to see updates available."""
    # def __init__(self, **config):
        # base._TextBox.__init__(self, text="N/A", **config)
        # self.text = None
        # self.update_time = 1800
        # self.no_updates_string = "N/A"
        # self.update()
        # threading.Timer(10, self.update).start()

    # def get_updates(self):
        # result = subprocess.run(['checkupdates'], capture_output=True).stdout
        # result = len(result.decode().split("\n")) - 1

        # if result == 0:
            # return self.no_updates_string
        # else:
            # return "Pacman: " + str(result)

    # def update(self):
        # self.text = self.get_updates()

        # threading.Timer(self.update_time, self.update).start()

# Own Widgets

width, height = get_screen_resolution()

widget_defaults = dict(
    font=common_font,
    fontsize = 12,
    padding = 2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()

groupbox_padding_x = 15
group_box_fontsize = 14
groups_number = len(group_list_names.keys())
space_group_center = (width - (group_box_fontsize + (groupbox_padding_x * 2)) * groups_number) // 2

widgets_top = [
    spacers(space_group_center),
    widget.GroupBox(
        font = icons_font,
        fontsize = group_box_fontsize,
        margin_x = 0,
        padding_y = 0,
        padding_x = groupbox_padding_x,
        borderwidth = 0,
        active = colors[2],
        inactive = colors[2],
        rounded = True,
        highlight_color = colors[5],
        highlight_method = "line",
        this_current_screen_border = colors[6],
        this_screen_border = colors[4],
        other_current_screen_border = colors[0],
        other_screen_border = colors[0],
        foreground = colors[2],
        background = colors[0],
        disable_drag = True,
        use_mouse_wheel = False,
    ),
    spacers(space_group_center)
]

widgets_bottom = [
    widget.Prompt(
        prompt = "cmd: ",
        padding = 10,
        foreground = colors[6],
        background = colors[0]
    ),
    separator(),
    widget.TaskList(
        foreground = colors[6],
        background = colors[0],
        margin=0, # Use to center the window name
        padding=2,
        rounded=True,
        highlight_method='block',
        txt_floating = "🗗 ",
        txt_maximized = "🗖 ",
        txt_minimized = "🗕 ",
        title_width_method = "uniform",
        max_title_width = 120
    ),
    separator(),
    widget.Systray(
        background = colors[0],
    ),
    separator(),
    widget_separator(widget_colors[8]),
    widget.TextBox(
        text = " ",
        foreground = colors[2],
        background = widget_colors[8][0],
        fontsize = 13,
        font = icons_font,
    ),
    widget.TextBox(
        text="Fondos",
        foreground = colors[2],
        background = widget_colors[8][0],
        mouse_callbacks = {"Button1": change_wallpaper}
    ),
    widget_separator(widget_colors[7]),
    widget_icons(" ", widget_colors[7]),
    widget.CPU(
        background = widget_colors[7][0],
        foreground = colors[2],
        update_interval = 10,
        format = "{freq_current}GHz | {load_percent}%",
        mouse_callbacks = {"Button1": lambda qtile: qtile.cmd_spawn(terminal + " -e htop")}
    ),
    widget_separator(widget_colors[6]),
    widget_icons(" ", widget_colors[6]),
    widget.Memory(
        background = widget_colors[6][0],
        foreground = colors[2],
        update_interval = 10,
        padding = 2,
        format = "{MemUsed}M"
    ),
    widget_separator(widget_colors[0]),
    widget_icons(" ", widget_colors[0]),
    widget.ThermalSensor(
        background = widget_colors[0][0],
        foreground = colors[2],
        update_interval = 10,
        threshold = 80,
        foreground_alert = "ff0000"
    ),
    widget_separator(widget_colors[1]),
    widget_icons(" ", widget_colors[1]),
    widget.Volume(
        foreground = colors[2],
        background = widget_colors[1][0],
        padding = 5,
        step = volume_step
    ),
    # Para que el volumen funcione bien, instalar
    # alsa-utils, pulseaudio y pulseaudio-alsa
    widget_separator(widget_colors[2]),
    widget_icons(" ", widget_colors[2]),
    widget.KeyboardLayout(
        foreground = colors[2],
        background = widget_colors[2][0],
        configured_keyboards=['latam', 'dvorak']
    ),
    widget_separator(widget_colors[3]),
    widget.CurrentLayoutIcon(
        # custom_icon_paths = [HOME + "/.config/qtile/icons"],
        foreground = colors[2],
        background = widget_colors[3][0],
        padding = 0,
        scale = 0.7,
    ),
    widget.CurrentLayout(
        foreground = colors[2],
        background = widget_colors[3][0],
        padding = 5,
    ),
    widget_separator(widget_colors[4]),
    widget_icons(' ', widget_colors[4]),
    widget.Clock(
        foreground = colors[2],
        background = widget_colors[4][0],
        format = "%a - %d/%m - %H:%M",
        mouse_callbacks = {
            'Button1': lambda qtile: qtile.cmd_function(run_or_go("zenity --calendar --text=''")),
            'Button3': lambda qtile: qtile.cmd_function(run_or_go("franz"))
        }
    )
]
