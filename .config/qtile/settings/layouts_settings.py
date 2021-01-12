# -*- coding: utf-8 -*-

from libqtile import layout

from settings.common import layout_theme, calculator_title, common_font

# Imports

floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},
    {'wmclass': 'makebranch'},
    {'wmclass': 'maketag'},
    {'wname':   'branchdialog'},
    {'wname':   'pinentry'},
    {'wmclass': 'qalculate-gtk'},
    {'wmclass': 'gnote'},
    {'wname':   "Hotkeys Help"},
    {'wmclass': 'zenity'},
    {'wmclass': 'ssh-askpass'},
], **layout_theme)

layouts = {
        'max': layout.Max(**layout_theme),
        'stack': layout.Stack(
            num_stacks=2,
            **layout_theme
        ),
        'bsp': layout.Bsp(**layout_theme),
        'columns': layout.Columns(**layout_theme),
        'matrix': layout.Matrix(**layout_theme),
        'monadtall': layout.MonadTall(
            min_ratio = 0,
            max_ratio = 1,
            **layout_theme
        ),
        'monadwide': layout.MonadWide(
            min_ratio = 0,
            max_ratio = 1,
            **layout_theme
        ),
        'ratiotile': layout.RatioTile(**layout_theme),
        'tile': layout.Tile(
            shift_windows=False,
            **layout_theme
        ),
        'treetab': layout.TreeTab(
            font = common_font,
            fontsize = 8,
            sections = ["PRIM"],
            section_fontsize = 8,
            bg_color = "141414",
            active_bg = "90C435",
            active_fg = "000000",
            inactive_bg = "384323",
            inactive_fg = "a0a0a0",
            padding_y = 5,
            section_top = 10,
            panel_width = 150
            ),
        'verticaltile': layout.VerticalTile(**layout_theme),
        'zoomy': layout.Zoomy(**layout_theme),
        'floating': floating_layout,
}
