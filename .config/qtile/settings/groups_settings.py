# -*- coding: utf-8 -*-

from settings.common import terminal, navigator, explorer, secondary_explorer, group_list_names
from settings.layouts_settings import layouts

from libqtile.config import Group, Match

group_names = [
   ("TERM",  {
       'layout': 'monadtall',
       'layouts': [
           layouts['matrix'],
           layouts['monadtall'],
           layouts['monadwide']
        ],
       'spawn': terminal,
       'label': group_list_names["TERM"]
       }),
   ("WEB",  {
       'layout': 'max',
       'layouts': [
           layouts['max'],
           layouts['treetab']
        ],
       'matches': [Match(wm_class=[
            "Firefox", "Opera", "Google-chrome",
            "Chromium", "brave-browser", "qutebrowser"
        ], role=["browser"]), ],
       'spawn': navigator,
       'label': group_list_names["WEB"]
    }),
   ("MAN",  {
       'layout': 'max',
       'layouts': [
           layouts['max'],
           layouts['stack'],
           layouts['monadtall']
        ],
       'matches': [Match(
            wm_class=[explorer, secondary_explorer,
                      'ranger', 'nomacs', 'xarchiver',
                      'file-roller']
        )],
       'spawn': explorer,
       'label': group_list_names["MAN"]
    }),
   ("DEV",  {
       'layout': 'tile',
       'layouts': [
           layouts['columns'],
           layouts['monadwide'],
           layouts['tile']
        ],
       'matches': [Match(
            wm_class=['sublime_text', 'Atollic TrueSTUDIO for STM32',
                      'jetbrains-pycharm-ce', 'kite', 'gedit',
                      'jetbrains-studio', 'vscodium', 'arduino']
        )],
       'label': group_list_names["DEV"]
    }),
   ("VAR",  {
       'layout': 'monadtall',
       'layouts': layouts.values(),
       # Include all layouts
       'matches': [Match(
            wm_class=['prepros', 'wps']
        )],
       'label': group_list_names["VAR"]
    }),
   ("CHAT",  {
       'layout': 'max',
       'layouts': [
           layouts['max'],
           layouts['stack'],
           layouts['monadwide']
        ],
       'matches': [Match(
          wm_class=['whatsdesk', 'Telegram','franz',
                    'discord', 'zoom', 'droidcam']
        )],
       'label': group_list_names["CHAT"]
    }),
   ("MULT",  {
       'layout': 'max',
       'layouts': [layouts['max']],
       'matches': [Match(
           wm_class=['Spotify', 'spotify', 'vlc']
        )],
       'label': group_list_names["MULT"]
    }),
   ("VBOX",  {
       'layout': 'max',
       'layouts': [
           layouts['max'],
           layouts['stack']
        ],
       'matches': [Match(wm_class=[
           'VirtualBox Manager'
        ])],
       'label': group_list_names["VBOX"]
    }),
   ("FLT",  {
       'layout': 'floating',
       'layouts': [
           layouts['stack'],
           layouts['floating']
        ],
       'label': group_list_names["FLT"]
    }),
   ("CONF", {
       'layout': 'monadtall',
       'layouts': [
           layouts['max'],
           layouts['monadtall']
        ],
       'matches': [Match(wm_class=[
           'lxappearance', 'pavucontrol',
           'gpartedbin', 'grub-customizer'
        ])],
       'label': group_list_names["CONF"]
    }),
   ("AUX", {
       'layout': 'monadtall',
       'layouts': layouts.values(),
       'label': group_list_names["AUX"]
    })
]

groups = [Group(name, **kwargs) for name, kwargs in group_names]
