from libqtile.config import Key
from libqtile.command import lazy
from settings.shortcut import *
from settings.path import *
from settings.groups import groups
keys = [
    # FUNCTION KEYS
    Key([], "F12", lazy.spawn("xfce4-terminal --drop-down")),
    # SUPER + FUNCTION KEYS
    Key([mod], "a", lazy.spawn("android-studio")),
    Key([mod], "b", lazy.spawn("bitwarden-desktop")),
    # Key([mod], "c", lazy.spawn("")),
    Key([mod], "d", lazy.spawn("drawio")),
    Key([mod], "e", lazy.spawn(editor)),
    Key([mod], "f", lazy.spawn("firefox")),
    Key([mod], "g", lazy.spawn("gparted")),
    # Key([mod], "h", lazy.spawn('')),
    Key([mod], "i", lazy.spawn("idea")),
    # Key([mod], "j", lazy.spawn('')),
    Key([mod], "k", lazy.spawn("krita")),
    # Key([mod], "l", lazy.spawn('')),
    Key([mod], "m", lazy.spawn("pragha")),
    # Key([mod], "n", lazy.spawn('')),
    Key([mod], "o", lazy.spawn("obs")),
    Key([mod], "p", lazy.spawn("pycharm")),
    Key([mod], "q", lazy.window.kill()),
    # Key([mod], "r", lazy.spawn('')),
    Key([mod], "s", lazy.spawn("pamac-manager")),
    Key([mod], "t", lazy.spawn("timeshift")),
    # Key([mod], "u", lazy.spawn('')),
    Key([mod], "v", lazy.spawn("vlc --video-on-top")),
    # Key([mod], "w", lazy.spawn('')),
    Key([mod], "x", lazy.spawn("arcolinux-logout")),
    # Key([mod], "y", lazy.spawn('')),
    # Key([mod], "z", lazy.spawn('')),
    # Key([mod], "c", lazy.spawn('conky-toggle')),
    # Key([mod], "f", lazy.window.toggle_fullscreen()),
    # Key([mod], "v", lazy.spawn('pavucontrol')),
    Key([mod], "Escape", lazy.spawn("xkill")),
    Key([mod], "Return", lazy.spawn(terminal)),
    # Key([mod], "KP_Enter", lazy.spawn('termite')),
    Key([mod], "KP_Enter", lazy.spawn("gnome-calculator")),
    Key([mod], "F1", lazy.spawn(browser)),
    Key([mod], "F2", lazy.spawn(editor)),
    Key([mod], "F3", lazy.spawn("inkscape")),
    Key([mod], "F4", lazy.spawn("gimp")),
    Key([mod], "F5", lazy.spawn("meld")),
    Key([mod], "F6", lazy.spawn("vlc --video-on-top")),
    Key([mod], "F7", lazy.spawn("virtualbox")),
    Key([mod], "F8", lazy.spawn(fileManager)),
    Key([mod], "F9", lazy.spawn("evolution")),
    Key([mod], "F10", lazy.spawn("spotify")),
    Key([mod], "F11", lazy.spawn("rofi -show run -fullscreen")),
    Key([mod], "F12", lazy.spawn("rofi -show run")),
    # SUPER + SHIFT KEYS
    Key([mod, "shift"], "Return", lazy.spawn(fileManager)),
    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "shift"], "x", lazy.shutdown()),
    # CONTROL + ALT KEYS
    Key(["mod1", "control"], "Next", lazy.spawn("conky-rotate -n")),
    Key(["mod1", "control"], "Prior", lazy.spawn("conky-rotate -p")),
    Key(["mod1", "control"], "a", lazy.spawn("xfce4-appfinder")),
    Key(["mod1", "control"], "b", lazy.spawn(fileManager)),
    Key(["mod1", "control"], "c", lazy.spawn("catfish")),
    Key(["mod1", "control"], "e", lazy.spawn("arcolinux-tweak-tool")),
    Key(["mod1", "control"], "f", lazy.spawn("firefox")),
    Key(["mod1", "control"], "g", lazy.spawn(
        "chromium -no-default-browser-check")),
    # Key(["mod1", "control"], "h", lazy.spawn('')),
    Key(["mod1", "control"], "i", lazy.spawn("nitrogen")),
    # Key(["mod1", "control"], "j", lazy.spawn('')),
    Key(["mod1", "control"], "k", lazy.spawn("arcolinux-logout")),
    # Key(["mod1", "control"], "l", lazy.spawn('')),
    Key(["mod1", "control"], "m", lazy.spawn("xfce4-settings-manager")),
    # Key(["mod1", "control"], "n", lazy.spawn('')),
    Key(["mod1", "control"], "o", lazy.spawn(
        qtile_scripts + "/picom-toggle.sh")),
    Key(["mod1", "control"], "p", lazy.spawn("pamac-manager")),
    # Key(["mod1", "control"], "q", lazy.spawn('')),
    Key(["mod1", "control"], "r", lazy.spawn("rofi-theme-selector")),
    Key(["mod1", "control"], "s", lazy.spawn("spotify")),
    Key(["mod1", "control"], "t", lazy.spawn(terminal)),
    Key(["mod1", "control"], "u", lazy.spawn("pavucontrol")),
    Key(["mod1", "control"], "v", lazy.spawn("vivaldi-stable")),
    Key(["mod1", "control"], "w", lazy.spawn("arcolinux-welcome-app")),
    Key(["mod1", "control"], "x", lazy.spawn("arcolinux-logout")),
    # Key(["mod1", "control"], "y", lazy.spawn('')),
    # Key(["mod1", "control"], "z", lazy.spawn('')),
    Key(["mod1", "control"], "Return", lazy.spawn(terminal)),
    # ALT + ... KEYS
    Key(["mod1"], "f", lazy.spawn("variety -f")),
    Key(["mod1"], "h", lazy.spawn("urxvt -e htop")),
    Key(["mod1"], "n", lazy.spawn("variety -n")),
    Key(["mod1"], "p", lazy.spawn("variety -p")),
    Key(["mod1"], "t", lazy.spawn("variety -t")),
    Key(["mod1"], "Up", lazy.spawn("variety --pause")),
    Key(["mod1"], "Down", lazy.spawn("variety --resume")),
    Key(["mod1"], "Left", lazy.spawn("variety -p")),
    Key(["mod1"], "Right", lazy.spawn("variety -n")),
    Key(["mod1"], "F2", lazy.spawn("gmrun")),
    Key(["mod1"], "F3", lazy.spawn("xfce4-appfinder")),
    # VARIETY KEYS WITH PYWAL
    Key(["mod1", "shift"], "f", lazy.spawn(
        qtile_scripts + "/set-pywal.sh -f")),
    Key(["mod1", "shift"], "p", lazy.spawn(
        qtile_scripts + "/set-pywal.sh -p")),
    Key(["mod1", "shift"], "n", lazy.spawn(
        qtile_scripts + "/set-pywal.sh -n")),
    Key(["mod1", "shift"], "u", lazy.spawn(
        qtile_scripts + "/set-pywal.sh -u")),
    # CONTROL + SHIFT KEYS
    Key([mod2, "shift"], "Escape", lazy.spawn("xfce4-taskmanager")),
    # SCREENSHOTS
    Key([], "Print",
        lazy.spawn(
        "scrot 'screenshot_%Y%m%d_%H%M%S.jpg' -e 'mv $f $$(xdg-user-dir PICTURES)'"),
        ),
    Key([mod2], "Print", lazy.spawn("xfce4-screenshooter")),
    Key([mod2, "shift"], "Print", lazy.spawn("gnome-screenshot -i")),
    # MULTIMEDIA KEYS
    # INCREASE/DECREASE BRIGHTNESS
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),
    # INCREASE/DECREASE/MUTE VOLUME
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

    # Switch focus of monitors
    Key(
        [mod], "period",
        lazy.next_screen(),
    ),
    Key(
        [mod], "comma",
        lazy.prev_screen(),
    ),
    # Switch focus to specific monitor
    Key(
        [mod, "shift"], "period",
        lazy.to_screen(0),
    ),
    Key(
        [mod, "shift"], "comma",
        lazy.to_screen(1),
    ),
    # QTILE LAYOUT KEYS
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout()),
    # FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "f", lazy.layout.flip()),
    # TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),
    # CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    # RESIZE UP, DOWN, LEFT, RIGHT
    Key(
        [mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
    ),
    Key(
        [mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
    ),
    Key(
        [mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
    ),
    Key(
        [mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
    ),
    Key(
        [mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        lazy.layout.section_up(),
    ),
    Key(
        [mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        lazy.layout.section_up(),
    ),
    Key(
        [mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        lazy.layout.section_down(),
    ),
    Key(
        [mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        lazy.layout.section_down(),
    ),
    # FLIP LAYOUT FOR BSP
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),
    # MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key(
        [mod, "shift"], "h",
        lazy.layout.shuffle_left(),
        lazy.layout.swap_left()
    ),
    Key(
        [mod, "shift"], "l",
        lazy.layout.shuffle_right(),
        lazy.layout.swap_right()
    ),
    # MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key(
        [mod, "shift"], "Left",
        lazy.layout.swap_left(),
        lazy.layout.shuffle_left()
    ),
    Key(
        [mod, "shift"], "Right",
        lazy.layout.swap_right(),
        lazy.layout.shuffle_right()
    ),
]

for i in groups:
    keys.extend(
        [
            # CHANGE WORKSPACES
            Key([mod], i.name, lazy.group[i.name].toscreen()),
            Key([mod], "Tab", lazy.screen.next_group()),
            Key(["mod1"], "Tab", lazy.screen.next_group()),
            Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),
            # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
        ]
    )