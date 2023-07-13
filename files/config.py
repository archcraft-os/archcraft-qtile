## Copyright (C) 2020-2023 Aditya Shakya <adi1090x@gmail.com>
##
## `qtile` configuration for Archcraft

## Import Libraries ------------------------

## Keys
from libqtile.config import Key, KeyChord
from libqtile.lazy import lazy

## Mouse
from libqtile.config import Click, Drag

## Groups
from libqtile.config import Group, Match

## Layouts
from libqtile import layout

## Screens
from libqtile.config import Screen
from libqtile import bar, widget

## ScratchPad and DropDown
from libqtile.config import ScratchPad, DropDown

## Startup
import os
import subprocess
from libqtile import hook

## Startup ------------------------------
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/scripts/qtile_autostart'])

## Key Bindings ------------------------------

# The mod key for the default config is 'mod4', which is typically bound to the "Super" keys,
# which are things like the windows key and the mac command key.
mod = "mod4"

# Scripts/Apps Variables
home         = os.path.expanduser('~')
terminal     = home + '/.config/qtile/scripts/qtile_term'
music_player = home + '/.config/qtile/scripts/qtile_music'
color_picker = home + '/.config/qtile/scripts/qtile_colorpicker'
brightness   = home + '/.config/qtile/scripts/qtile_brightness'
volume       = home + '/.config/qtile/scripts/qtile_volume'
screenshot   = home + '/.config/qtile/scripts/qtile_screenshot'
file_manager = 'thunar'
text_editor  = 'geany'
web_browser  = 'firefox'
alacritty    = 'alacritty --config-file ' + home + '/.config/qtile/alacritty/alacritty.yml'
rofi_applets = home + '/.config/qtile/scripts/'
notify_cmd   = 'dunstify -u low -h string:x-dunst-stack-tag:qtileconfig'

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
	
	# Terminal --
    Key(
		[mod], "Return", 
		lazy.spawn(terminal), 
		desc="Launch terminal with qtile configs"
	),
    Key(
		[mod, "shift"], "Return", 
		lazy.spawn(terminal + ' --float'), 
		desc="Launch floating terminal with qtile configs"
	),
    Key(
		[mod, "mod1"], "Return", 
		lazy.spawn(terminal + ' --full'), 
		desc="Launch fullscreen terminal with qtile configs"
	),

	# GUI Apps --
    Key(
		[mod, "shift"], "f", 
		lazy.spawn(file_manager), 
		desc="Launch file manager"
	),
    Key(
		[mod, "shift"], "e", 
		lazy.spawn(text_editor), 
		desc="Launch text editor"
	),
    Key(
		[mod, "shift"], "w", 
		lazy.spawn(web_browser), 
		desc="Launch web browser"
	),

	# CLI Apps --
    Key(
		["control", "mod1"], "v", 
		lazy.spawn(alacritty + ' -e vim'), 
		desc="Open vim in qtile's terminal"
	),
    Key(
		["control", "mod1"], "r", 
		lazy.spawn(alacritty + ' -e ranger'), 
		desc="Open ranger in qtile's terminal"
	),
    Key(
		["control", "mod1"], "h", 
		lazy.spawn(alacritty + ' -e htop'), 
		desc="Open htop in qtile's terminal"
	),
    Key(
		["control", "mod1"], "m", 
		lazy.spawn(music_player), 
		desc="Open ncmpcpp in qtile's terminal"
	),

	# Rofi Applets --
    Key(
		["mod1"], "F1", 
		lazy.spawn(rofi_applets + 'rofi_launcher'), 
		desc="Run application launcher"
	),
    Key(
		["mod1"], "F2", 
		lazy.spawn(rofi_applets + 'rofi_runner'), 
		desc="Run command runner"
	),
    Key(
		[mod], "n", 
		lazy.spawn(rofi_applets + 'network_menu'), 
		desc="Run network manager applet"
	),
    Key(
		[mod], "x", 
		lazy.spawn(rofi_applets + 'rofi_powermenu'), 
		desc="Run powermenu applet"
	),
    Key(
		[mod], "m", 
		lazy.spawn(rofi_applets + 'rofi_music'), 
		desc="Run music player applet"
	),
    Key(
		[mod], "r", 
		lazy.spawn(rofi_applets + 'rofi_asroot'), 
		desc="Run asroot applet"
	),
    Key(
		[mod], "s", 
		lazy.spawn(rofi_applets + 'rofi_screenshot'), 
		desc="Run screenshot applet"
	),

	# Function keys : Brightness --
    Key(
		[], "XF86MonBrightnessUp", 
		lazy.spawn(brightness + ' --inc'),
		desc="Increase display brightness"	
	),
    Key(
		[], "XF86MonBrightnessDown", 
		lazy.spawn(brightness + ' --dec'),
		desc="Decrease display brightness"	
	),

	# Function keys : Volume --
    Key(
		[], "XF86AudioRaiseVolume", 
		lazy.spawn(volume + ' --inc'),
		desc="Raise speaker volume"	
	),
    Key(
		[], "XF86AudioLowerVolume", 
		lazy.spawn(volume + ' --dec'),
		desc="Lower speaker volume"	
	),
    Key(
		[], "XF86AudioMute", 
		lazy.spawn(volume + ' --toggle'),
		desc="Toggle mute"	
	),
    Key(
		[], "XF86AudioMicMute", 
		lazy.spawn(volume + ' --toggle-mic'),
		desc="Toggle mute for mic"
	),

	# Function keys : Media --
    Key(
		[], "XF86AudioNext", 
		lazy.spawn("mpc next"),
		desc="Next track"
	),
    Key(
		[], "XF86AudioPrev", 
		lazy.spawn("mpc prev"),
		desc="Previous track"
	),
    Key(
		[], "XF86AudioPlay", 
		lazy.spawn("mpc toggle"),
		desc="Toggle play/pause"
	),
    Key(
		[], "XF86AudioStop", 
		lazy.spawn("mpc stop"),
		desc="Stop playing"
	),

	# Screenshots --
    Key(
		[], "Print", 
		lazy.spawn(screenshot + ' --now'),
		desc="Take Screenshot"
	),
    Key(
		["control"], "Print", 
		lazy.spawn(screenshot + ' --in5'),
		desc="Take Screenshot in 5 seconds"
	),
    Key(
		["shift"], "Print", 
		lazy.spawn(screenshot + ' --in10'),
		desc="Take Screenshot in 10 seconds"
	),
    Key(
		["control", "shift"], "Print", 
		lazy.spawn(screenshot + ' --win'),
		desc="Take Screenshot of active window"
	),
    Key(
		[mod], "Print", 
		lazy.spawn(screenshot + ' --area'),
		desc="Take Screenshot of selected area"
	),

	# Misc --
    Key(
		[mod], "p", 
		lazy.spawn(color_picker),
		desc="Run colorpicker"
	),
    Key(
		["mod1", "control"], "l", 
		lazy.spawn("betterlockscreen --lock"),
		desc="Run lockscreen"
	),

	# WM Specific --
    Key(
		[mod], "c", 
		lazy.window.kill(), 
		desc="Kill focused window"
	),
    Key(
		[mod], "q", 
		lazy.window.kill(), 
		desc="Kill focused window"
	),

	# Control Qtile
    Key(
		[mod, "control"], "r", 
		lazy.reload_config(),
		lazy.spawn(notify_cmd + ' "Configuration Reloaded!"'),
		desc="Reload the config"
	),
    Key(
		[mod, "control"], "s", 
		lazy.restart(), 
		lazy.spawn(notify_cmd + ' "Restarting Qtile..."'),
		desc="Restart Qtile"
	),
    Key(
		[mod, "control"], "q", 
		lazy.shutdown(), 
		lazy.spawn(notify_cmd + ' "Exiting Qtile..."'),
		desc="Shutdown Qtile"
	),

    # Switch between windows
    Key(
		[mod], "Left", 
		lazy.layout.left(), 
		desc="Move focus to left"
	),
    Key(
		[mod], "Right",
		lazy.layout.right(), 
		desc="Move focus to right"
	),
    Key(
		[mod], "Down", 
		lazy.layout.down(), 
		desc="Move focus down"
	),
    Key(
		[mod], "Up",
		lazy.layout.up(), 
		desc="Move focus up"
	),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
		[mod, "shift"], "Left", 
		lazy.layout.shuffle_left(), 
		desc="Move window to the left"
	),
    Key(
		[mod, "shift"], "Right",
		lazy.layout.shuffle_right(), 
		desc="Move window to the right"
	),
    Key(
		[mod, "shift"], "Down", 
		lazy.layout.shuffle_down(), 
		desc="Move window down"
	),
    Key(
		[mod, "shift"], "Up",
		lazy.layout.shuffle_up(), 
		desc="Move window up"
	),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key(
		[mod, "control"], "Left", 
		lazy.layout.grow_left(), 
		desc="Grow window to the left"
	),
    Key(
		[mod, "control"], "Right", 
		lazy.layout.grow_right(), 
		desc="Grow window to the right"
	),
    Key(
		[mod, "control"], "Down", 
		lazy.layout.grow_down(), 
		desc="Grow window down"
	),
    Key(
		[mod, "control"], "Up", 
		lazy.layout.grow_up(), 
		desc="Grow window up"
	),
    Key(
		[mod, "control"], "Return", 
		lazy.layout.normalize(), 
		desc="Reset all window sizes"
	),

	# Toggle floating and fullscreen
    Key(
		[mod], "space", 
		lazy.window.toggle_floating(), 
		desc="Put the focused window to/from floating mode"
	),
    Key(
		[mod], "f", 
		lazy.window.toggle_fullscreen(), 
		desc="Put the focused window to/from fullscreen mode"
	),

	# Go to next/prev group
    Key(
		[mod, "mod1"], "Right", 
		lazy.screen.next_group(), 
		desc="Move to the group on the right"
	),
    Key(
		[mod, "mod1"], "Left", 
		lazy.screen.prev_group(), 
		desc="Move to the group on the left"
	),

    # Back-n-forth groups
    Key(
		[mod], "b", 
		lazy.screen.toggle_group(), 
		desc="Move to the last visited group"
	),

	# Change focus to other window
    Key(
		[mod], "Tab", 
		lazy.layout.next(), 
		desc="Move window focus to other window"
	),

    # Toggle between different layouts as defined below
    Key(
		[mod, "shift"], "space", 
		lazy.next_layout(), 
		desc="Toggle between layouts"
	),

	# Increase the space for master window at the expense of slave windows
    Key(
		[mod], "equal", 
		lazy.layout.increase_ratio(), 
		desc="Increase the space for master window"
	),

	# Decrease the space for master window in the advantage of slave windows
    Key(
		[mod], "minus", 
		lazy.layout.decrease_ratio(), 
		desc="Decrease the space for master window"
	),

    # Toggle between split and unsplit sides of stack.
    Key(
        [mod, "shift"], "s",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

	# Modes: Reize
    KeyChord([mod, "shift"], "r", [
        Key([], "Left", lazy.layout.grow_left()),
        Key([], "Right", lazy.layout.grow_right()),
        Key([], "Down", lazy.layout.grow_down()),
        Key([], "Up", lazy.layout.grow_up())],
        mode=True,
        name="Resize"
    ),

	# Modes: Layouts
    KeyChord([mod, "shift"], "l", [
        Key([], "Left", lazy.prev_layout()),
        Key([], "Right", lazy.next_layout())],
        mode=True,
        name="Layouts"
    )

]

## Mouse Bindings ------------------------------

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

## Groups ------------------------------
groups = [Group(i) for i in "12345678"]

for i in groups:
    keys.extend(
        [
            # mod + number of group = switch to group
            Key(
                [mod], i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod + shift + number of group = switch to & move focused window to group
            Key(
                [mod, "shift"], i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

## Layouts ------------------------------
var_bg_color = '#2e3440'
var_active_bg_color = '#81A1C1'
var_active_fg_color = '#2e3440'
var_inactive_bg_color = '#3d4555'
var_inactive_fg_color = '#D8DEE9'
var_urgent_bg_color = '#BF616A'
var_urgent_fg_color = '#D8DEE9'
var_section_fg_color = '#EBCB8B'
var_active_color = '#81A1C1'
var_normal_color = '#3d4555'
var_border_width = 2
var_margin = [5,5,5,5]
var_gap_top = 45
var_gap_bottom = 5
var_gap_left = 5
var_gap_right = 5
var_font_name = 'JetBrainsMono Nerd Font'

layouts = [
	# Extension of the Stack layout
    layout.Columns(
		border_focus=var_active_color,
		border_normal=var_normal_color,
		border_on_single=False,
		border_width=var_border_width,
		fair=False,
		grow_amount=10,
		insert_position=0,
		margin=var_margin,
		margin_on_single=None,
		num_columns=2,
		split=True,
		wrap_focus_columns=True,
		wrap_focus_rows=True,
		wrap_focus_stacks=True
	),

	# Layout inspired by bspwm
    layout.Bsp(
		border_focus=var_active_color,
		border_normal=var_normal_color,
		border_on_single=False,
		border_width=var_border_width,
		fair=True,
		grow_amount=10,
		lower_right=True,
		margin=var_margin,
		margin_on_single=None,
		ratio=1.6,
		wrap_clients=False
    ),

	# This layout divides the screen into a matrix of equally sized cells and places one window in each cell.
    layout.Matrix(
		border_focus=var_active_color,
		border_normal=var_normal_color,
		border_width=var_border_width,    
		columns=2,
		margin=var_margin
    ),

	# Maximized layout
    layout.Max(
		border_focus=var_active_color,
		border_normal=var_normal_color,
		border_width=var_border_width,    
		margin=0
    ),

	# Emulate the behavior of XMonad's default tiling scheme.
    layout.MonadTall(
		align=0,
		border_focus=var_active_color,
		border_normal=var_normal_color,
		border_width=var_border_width,
		change_ratio=0.05,
		change_size=20,
		margin=0,
		max_ratio=0.75,
		min_ratio=0.25,
		min_secondary_size=85,
		new_client_position='after_current',
		ratio=0.5,
		single_border_width=None,
		single_margin=None
    ),

	# Emulate the behavior of XMonad's ThreeColumns layout.
    layout.MonadThreeCol(
		align=0,
		border_focus=var_active_color,
		border_normal=var_normal_color,
		border_width=var_border_width,
		change_ratio=0.05,
		change_size=20,
		main_centered=True,
		margin=0,
		max_ratio=0.75,
		min_ratio=0.25,
		min_secondary_size=85,
		new_client_position='top',
		ratio=0.5,
		single_border_width=None,
		single_margin=None    
    ),

	# Emulate the behavior of XMonad's horizontal tiling scheme.
    layout.MonadWide(
		align=0,
		border_focus=var_active_color,
		border_normal=var_normal_color,
		border_width=var_border_width,
		change_ratio=0.05,
		change_size=20,
		margin=0,
		max_ratio=0.75,
		min_ratio=0.25,
		min_secondary_size=85,
		new_client_position='after_current',
		ratio=0.5,
		single_border_width=None,
		single_margin=None    
    ),

	# Tries to tile all windows in the width/height ratio passed in
    layout.RatioTile(
		border_focus=var_active_color,
		border_normal=var_normal_color,
		border_width=var_border_width,
		fancy=False,
		margin=var_margin,
		ratio=1.618,
		ratio_increment=0.1
    ),

	# This layout cuts piece of screen_rect and places a single window on that piece, and delegates other window placement to other layout
    layout.Slice(
		match=None,
		side='left',
		width=256
    ),

	# A mathematical layout, Renders windows in a spiral form by splitting the screen based on a selected ratio.
    layout.Spiral(
		border_focus=var_active_color,
		border_normal=var_normal_color,
		border_width=var_border_width,
		clockwise=True,
		main_pane='left',
		main_pane_ratio=None,
		margin=0,
		new_client_position='top',
		ratio=0.6180469715698392,
		ratio_increment=0.1
    ),
    
	# A layout composed of stacks of windows
    layout.Stack(
		autosplit=False,
		border_focus=var_active_color,
		border_normal=var_normal_color,
		border_width=var_border_width,
		fair=False,
		margin=var_margin,
		num_stacks=2
    ),

	# A layout with two stacks of windows dividing the screen
    layout.Tile(
		add_after_last=False,
		add_on_top=True,
		border_focus=var_active_color,
		border_normal=var_normal_color,
		border_on_single=False,
		border_width=var_border_width,
		expand=True,
		margin=var_margin,
		margin_on_single=None,
		master_length=1,
		master_match=None,
		max_ratio=0.85,
		min_ratio=0.15,
		ratio=0.618,
		ratio_increment=0.05,
		shift_windows=False
    ),

	# This layout works just like Max but displays tree of the windows at the left border of the screen_rect, which allows you to overview all opened windows.
    layout.TreeTab(
		active_bg=var_active_bg_color,
		active_fg=var_active_fg_color,
		bg_color=var_bg_color,
		border_width=var_border_width,
		font=var_font_name,
		fontshadow=None,
		fontsize=14,
		inactive_bg=var_inactive_bg_color,
		inactive_fg=var_inactive_fg_color,
		level_shift=0,
		margin_left=0,
		margin_y=0,
		padding_left=10,
		padding_x=10,
		padding_y=10,
		panel_width=200,
		place_right=False,
		previous_on_rm=False,
		section_bottom=0,
		section_fg=var_section_fg_color,
		section_fontsize=14,
		section_left=10,
		section_padding=10,
		section_top=10,
		sections=['Default'],
		urgent_bg=var_urgent_bg_color,
		urgent_fg=var_urgent_fg_color,
		vspace=5
    ),

	# Tiling layout that works nice on vertically mounted monitors
    layout.VerticalTile(
		border_focus=var_active_color,
		border_normal=var_normal_color,
		border_width=var_border_width,
		margin=var_margin
    ),

	# A layout with single active windows, and few other previews at the right
    layout.Zoomy(
		columnwidth=300,
		margin=var_margin,
		property_big='1.0',
		property_name='ZOOM',
		property_small='0.1'
    ),

	# Floating layout, which does nothing with windows but handles focus order
    layout.Floating(
		border_focus=var_active_color,
		border_normal=var_normal_color,
		border_width=var_border_width,
		fullscreen_border_width=0,
		max_border_width=0
	)
]

## Screens ------------------------------

# Default Qtile Bar (commented)
"""
screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                #widget.StatusNotifier(),
                widget.Systray(),
                widget.Clock(format="%I:%M %p"),
                widget.QuickExit(),
            ],
            34,
            background=["000000", "101010"],
            margin=[0,0,0,0],
            opacity=1.0,
            border_width=[2, 0, 0, 0],
            border_color=["303030", "000000", "000000", "000000"]
        ),
    ),
]
"""

# Any third-party statusbar (polybar) with Gaps
screens = [
    Screen(
        right=bar.Gap(var_gap_right),
        left=bar.Gap(var_gap_left),
        bottom=bar.Gap(var_gap_bottom),
        top=bar.Gap(var_gap_top)
    )
]

## General Configuration Variables ------------------------------

# If a window requests to be fullscreen, it is automatically fullscreened. 
# Set this to false if you only want windows to be fullscreen if you ask them to be.
auto_fullscreen = False

# When clicked, should the window be brought to the front or not. 
# If this is set to "floating_only", only floating windows will get affected (This sets the X Stack Mode to Above.)
bring_front_click = False

# If true, the cursor follows the focus as directed by the keyboard, warping to the center of the focused window. 
# When switching focus between screens, If there are no windows in the screen, the cursor will warp to the center of the screen.
cursor_warp = False

# A function which generates group binding hotkeys. It takes a single argument, the DGroups object, and can use that to set up dynamic key bindings.
# A sample implementation is available in 'libqtile/dgroups.py' called `simple_key_binder()`, which will bind groups to "mod+shift+0-10" by default.
dgroups_key_binder = None

# A list of Rule objects which can send windows to various groups based on matching criteria.
dgroups_app_rules = []  # type: list

# The default floating layout to use. This allows you to set custom floating rules among other things if you wish.
floating_layout = layout.Floating(
	border_focus=var_active_color,
	border_normal=var_normal_color,
	border_width=var_border_width,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="alacritty-float|Music"),
        Match(wm_class="Lxappearance|Nitrogen"),
        Match(wm_class="Pavucontrol|Xfce4-power-manager-settings|Nm-connection-editor"),
        Match(wm_class="feh|Viewnior|Gpicview|Gimp|MPlayer|Vlc|Spotify"),
        Match(wm_class="Kvantum Manager|qt5ct"),
        Match(wm_class="VirtualBox Manager|qemu|Qemu-system-x86_64"),
        Match(title="branchdialog"),
    ]
)

# Behavior of the _NET_ACTIVATE_WINDOW message sent by applications
#
# urgent: urgent flag is set for the window
# focus: automatically focus the window
# smart: automatically focus if the window is in the current group
# never: never automatically focus any window that requests it
focus_on_window_activation = "smart"

# Controls whether or not focus follows the mouse around as it moves across windows in a layout.
follow_mouse_focus = True

# Default settings for bar widgets.
widget_defaults = dict(
    font=var_font_name,
    fontsize=14,
    padding=5,
)

# Same as `widget_defaults`, Default settings for extensions.
extension_defaults = widget_defaults.copy()

# Controls whether or not to automatically reconfigure screens when there are changes in randr output configuration.
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
#wmname = "LG3D"

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None
