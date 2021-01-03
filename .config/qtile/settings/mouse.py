# -*- coding: utf-8 -*-

from libqtile.config import Click, Drag
from libqtile.lazy import lazy

from settings.common import mod

# Imports

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size())
]
# Drag with left button moves floating window
# Drag with right button changes size