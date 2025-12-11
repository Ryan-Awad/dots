#!/bin/bash
# Please run this script as root.

if [ "$(id -u)" -ne 0 ]; then
	echo "Please run this script as root."
	exit 1
fi

read -p "Do you want to proceed? (y/N): " yn

case $yn in 
	y ) echo "proceeding...";;
	* ) echo "bye!";
		exit;;
esac

pacman -Syu \
	waybar \
	hyprlock \
	hyprpaper \
	rofi \
	kitty \
	ttf-font-awesome \
	nwg-displays \
	ly

pacman -Syu \
	btop \
	neovim \
	htop \
	nvtop

pacman -Syu \
	yazi \
	zellij \
	fastfetch \
	bat \
	unzip 

pacman -Syu \
	firefox

wget -P /tmp https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/CascadiaCode.zip
mkdir -p /usr/share/fonts/CascadiaCove
unzip /tmp/CascadiaCode.zip -d /usr/share/fonts/CascadiaCove
