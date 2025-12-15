#!/bin/bash

confirm_proceed() {
	if [ "$1" != "" ]; then
		echo $1
	fi
	read -p "Do you want to proceed? (y/N): " yn
	case $yn in 
		y ) echo "proceeding...";;
		* ) echo "bye!";
			exit;;
	esac
}

install_pkgs() {
	sudo pacman -Syu \
		zsh \
		waybar \
		hyprlock \
		hyprpaper \
		rofi \
		kitty \
		ttf-font-awesome \
		nwg-displays \
		ly \
		brightnessctl

	sudo pacman -Syu \
		btop \
		neovim \
		htop \
		nvtop

	sudo pacman -Syu \
		yazi \
		zellij \
		fastfetch \
		imagemagick \
		bat \
		unzip 

	sudo pacman -Syu \
		firefox

	# installing oh-my-zsh
	sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
}

configure_symlinks() { # issue with files that already exist
	ln -s ~/.config/fonts ~/.local/share/fonts
	ln -s ~/.config/.oh-my-zsh ~/.oh-my-zsh
	ln -s ~/.config/.zshrc ~/.zshrc
}

main() {
	confirm_proceed "Configuring the following user: $(whoami)"

	echo "[!] Installing the following packages: "
	declare -f install_pkgs
	confirm_proceed
	install_pkgs

	echo "[!] Creating the following symlinks:"
	declare -f configure_symlinks
	confirm_proceed
	configure_symlinks
}

main
