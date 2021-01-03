# -*- coding: utf-8 -*-

from libqtile.config import Key
from libqtile.lazy import lazy

from settings.common import mod, ctrl, shift, alt, terminal, group_list_names, navigator, explorer, secondary_explorer, unmute_command, mute_toggle_command, volume_down_command, volume_up_command, icons_font, HOME, captures_path
from settings.functions import get_screen_resolution, kill_all_windows, minimize_group, run_or_go, run_or_bring, run_or_exit, show_hotkeys

# Imports

width, height = get_screen_resolution()

keys = [
    ### The essentials
    Key([mod], "Return",
        lazy.spawn(terminal),
        desc='Launches My Terminal'
    ),
    Key([ctrl, shift], "Return",
        lazy.spawn('dmenu_run -p "»" -i -nf "#888888" -nb "#292d3e" -sf "#ffffff" -sb "#005577" -fn "{0}"'.format(icons_font)),
        desc='Dmenu Run Launcher'
    ),
    Key([mod, shift], "Return",
        lazy.spawn('dmenu_extended_run'),
        desc='Dmenu Extended Run Launcher'
    ),
    Key([mod, shift], "r",
        lazy.restart(),
        desc='Restart Qtile'
    ),
    Key([mod, shift], "q",
        lazy.spawn(HOME + "/.config/dmenu/dmenu-session-options.sh"),
        desc="Log out qtile"
    ),
    # Advanced commands
    Key([mod, ctrl], "q",
        kill_all_windows,
        desc="Closes all windows"
    ),
    # Window Control
    Key([mod], "Tab",
        lazy.next_layout(),
        desc='Toggle through layouts'
    ),
    Key([mod, shift], "Tab",
        lazy.prev_layout(),
        desc='Toggle through layouts in opposite direction'
    ),
    Key([alt], "Tab",
        lazy.layout.next(),
        desc='Switch window focus to next pane(s) of stack'
    ),
    Key([alt, shift], "Tab",
        lazy.layout.prev(),
        desc='Switch window focus to prev pane(s) of stack'
    ),
    Key([mod], "w",
        lazy.window.kill(),
        desc='Kill active window'
    ),
    Key([mod], "d",
        minimize_group,
        desc="Minimize current window"
    ),
    Key([mod, shift], "f",
        lazy.window.toggle_floating(),
        desc='Toggles floating'
    ),
    Key([mod], "Right",
        lazy.layout.increase_ratio().when('tile'),
        lazy.layout.shrink().when('monadtall'),
        lazy.window.set_position_floating(width // 2, 0).when('floating'),
        lazy.window.set_size_floating(width // 2, height).when('floating'),
        desc="Grows window width"
    ),
    Key([mod], "Left",
        lazy.layout.decrease_ratio().when('tile'),
        lazy.layout.grow().when('monadtall'),
        lazy.window.set_position_floating(0, 0).when('floating'),
        lazy.window.set_size_floating(width // 2, height).when('floating'),
        desc="Reduces window width"
    ),
    Key([mod], "Up",
        lazy.layout.increase_nmaster().when('tile'),
        lazy.layout.grow().when('monadwide'),
        lazy.window.set_position_floating(0, 0).when('floating'),
        lazy.window.set_size_floating(width, height // 2).when('floating'),
        desc="Reduces window height"
    ),
    Key([mod], "Down",
        lazy.layout.decrease_nmaster().when('tile'),
        lazy.layout.shrink().when('monadwide'),
        lazy.window.set_position_floating(0, height // 2).when('floating'),
        lazy.window.set_size_floating(width, height // 2).when('floating'),
        desc="Grows window height"
    ),
    Key([mod, alt], "Up",
        lazy.window.set_position_floating(0, 0).when('floating'),
        lazy.window.set_size_floating(width, height).when('floating'),
    ),
    Key([mod, alt], "Down",
        lazy.window.set_position_floating(width // 8, height // 8).when('floating'),
        lazy.window.set_size_floating(width - (1/4) * width, height - (1/4) * height).when('floating'),
    ),
    Key([mod], "space",
        lazy.layout.down(),
        lazy.layout.rotate(),
        lazy.layout.flip(),
        lazy.layout.shuffle_up().when('tile'),
        desc='Move focus up in current stack pane'
    ),
    # Groups Control
    Key([mod], "a",
        lazy.screen.toggle_group(),
        desc="Changes to the last group"
    ),
    Key([mod, alt], "Left",
        lazy.screen.prev_group(),
        desc="Changes to the prev group"
    ),
    Key([mod, alt], "Right",
        lazy.screen.next_group(),
        desc="Changes to the next group"
    ),
    # Apps
    Key([mod], "p",
        lazy.spawncmd(),
        desc='Generates a prompt to enter commands'
    ),
    Key([mod], "e",
        lazy.spawn(explorer),
        desc="Open explorer"
    ),
    Key([mod], "v",
        lazy.spawn('clipmenu -p "»"'),
        desc='Opens clipboard manager'
    ),
    Key([mod], "g",
        lazy.spawn('rofimoji'),
        desc='Opens emojis selector'
    ),
    Key([mod], "l",
        lazy.spawn("dm-tool lock"),
        desc="Locks screen"
    ),
    Key([mod], "x",
        lazy.spawn("dunstctl close-all"),
        desc="Deletes all notifications"
    ),
    Key([mod, alt], "x",
        lazy.spawn("dunstctl close"),
        desc="Deletes last notification"
    ),
    Key([mod], "h",
        show_hotkeys,
        desc="Shows a hotkeys' image depending on current window"
    ),
    Key(
        [mod, shift], "space",
        lazy.spawn("rofi -combi-modi window,drun -show combi -modi combi"),
        desc="Starts Rofi launcher"
    ),
    Key(
        [mod, alt], "e",
        lazy.spawn(secondary_explorer),
        desc="Starts the more graphical/less functional file manager/explorer"
    ),
    Key([mod, alt], "n",
        lazy.function(run_or_go(navigator)),
        desc='Opens Default Web Browser'
    ),
    Key([mod, alt], "c",
        lazy.function(run_or_bring("qalculate-gtk")),
        desc='Opens favorite calculator'
    ),
    Key(
        [mod, shift], "s",
        lazy.spawn("flameshot gui"),
        desc="Opens screenshot interface"
    ),
    Key(
        [mod, shift], "Print",
        lazy.spawn("flameshot full -p " + captures_path),
        desc="Takes a screenshot and saves it to images folder"
    ),
    Key(
        [], "Print",
        lazy.spawn("flameshot screen -c"),
        desc="Takes a screenshot and saves it to clipboard"
    ),
    Key(
        [mod, alt], "v",
        lazy.function(run_or_go("virtualbox")),
        desc="Opens Virtual Box"
    ),
    Key(
        [mod, alt], "d",
        lazy.spawn(HOME + "/.config/dmenu/dmenu-edit-configs.sh"),
        desc="Opens options to edit config files"
    ),
    Key(
        [mod, alt], "w",
        lazy.function(run_or_go("franz")),
        desc="Opens Franz social media manager"
    ),
    Key(
        [mod, alt], "u",
        lazy.spawn(HOME + "/.config/dmenu/dmenu-expulse-drives.sh"),
        desc="Launches prompt to select a drive to expulse"
    ),
    ### Admin Keys
    Key(
        [], "XF86AudioRaiseVolume",
        lazy.spawn(unmute_command),
        lazy.spawn(volume_up_command),
        desc="Ups Volume"
    ),
    Key(
        [], "XF86AudioLowerVolume",
        lazy.spawn(unmute_command),
        lazy.spawn(volume_down_command),
        desc="Downs Volume"
    ),
    Key(
        [], "XF86AudioMute",
        lazy.spawn(mute_toggle_command),
        desc="Mutes/Unmutes Volume"
    ),
    ### Music Control
    Key(
        [], "XF86Tools",
        lazy.function(run_or_go("spotify")),
        desc="Opens Spotify"
    ),
    Key(
        [], "XF86AudioPlay",
        lazy.spawn("playerctl play-pause"),
        desc="Pone play/pause en Spotify"
    ),
    Key(
        [], "XF86AudioPrev",
        lazy.spawn("playerctl previous"),
        desc="Pasa al anterior tema de la lista"
    ),
    Key(
        [], "XF86AudioNext",
        lazy.spawn("playerctl next"),
        desc="Pasa al siguiente tema de la lista"
    ),
    Key(
        [], "XF86AudioStop",
        lazy.spawn("playerctl stop"),
        desc="Pausa la cancion actual"
    ),
    ### Others Special Keys
    Key(
        [], "XF86Mail",
        lazy.spawn(navigator + " https://mail.google.com/mail/u/0/#inbox"),
        desc="Opens mail client in favorite browser"
    ),
    Key(
        [], 'XF86HomePage',
        lazy.group["TERM"].toscreen(),
        desc="Goes to home group"
    ),
    Key(
        [], 'XF86Calculator',
        lazy.function(run_or_bring("qalculate-gtk")),
        desc="Opens calculator"
    ),
    # These keys are rarely use but they are in my keyboard
    # so I wanted to give them some function :)
]

names = list(group_list_names.keys())
len_names = len(names) if len(names) < 10 else 9
for i in range(len_names):
    keys.append(Key([mod], str(i + 1), lazy.group[names[i]].toscreen()))        # Switch to another group
    keys.append(Key([mod, shift], str(i + 1), lazy.window.togroup(names[i])))   # Send current window to another group
keys.append(Key([mod], "0", lazy.group[names[9]].toscreen()))
keys.append(Key([mod, shift], "0", lazy.window.togroup(names[9])))
# To add tenth group related with 0
for i in range(1, len(names) - len_names):
    keys.append(Key([mod, ctrl], str(i), lazy.group[names[i + len_names]].toscreen()))
    keys.append(Key([mod, ctrl, shift], str(i), lazy.window.togroup(names[i + len_names])))
# To add more than 10 groups
