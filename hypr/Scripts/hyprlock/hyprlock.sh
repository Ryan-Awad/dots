#!/bin/bash
# inspired by https://www.reddit.com/r/hyprland/comments/1b45whm/comment/kt567np/

grim \
	-s 1.5 \
	-l 0 \
	-o eDP-1 \
	~/.cache/screenlock.png

convert \
	~/.cache/screenlock.png \
	-scale 20% \
	-blur 0x6 \
	-resize 200% \
	~/.cache/screenlock.png

hyprlock
