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
], **layout_theme)                                      # 12

layouts = [
    layout.Max(**layout_theme),                         # 0
    layout.Stack(
        num_stacks=2,
        **layout_theme
    ),                                                  # 1
    layout.Bsp(**layout_theme),                         # 2
    layout.Columns(**layout_theme),                     # 3
    layout.Matrix(**layout_theme),                      # 4
    layout.MonadTall(
        min_ratio = 0,
        max_ratio = 1,
        **layout_theme
    ),                                                  # 5
    layout.MonadWide(
        min_ratio = 0,
        max_ratio = 1,
        **layout_theme
    ),                                                  # 6
    layout.RatioTile(**layout_theme),                   # 7
    layout.Tile(
        shift_windows=False,
        **layout_theme
    ),                                                  # 8
    layout.TreeTab(                                     # 9
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
    layout.VerticalTile(**layout_theme),                # 10
    layout.Zoomy(**layout_theme),                       # 11
    floating_layout,                                    # 12
]