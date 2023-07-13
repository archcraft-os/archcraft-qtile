# Maintainer: Aditya Shakya <adi1090x@gmail.com>

pkgname=archcraft-qtile
pkgver=1.0
pkgrel=1
pkgdesc="Qtile Configurations for Archcraft"
url="https://github.com/archcraft-os/archcraft-qtile"
arch=('any')
license=('GPL3')
makedepends=('git')
depends=('qtile' 'python-pywlroots' 'python-dbus-next' 'hsetroot'
		'alacritty' 'thunar' 'geany'
		'rofi' 'polybar' 'dunst'
		'mpd' 'mpc'
		'maim' 'xclip' 'viewnior'
		'ksuperkey' 
		'betterlockscreen'
		'xfce4-power-manager' 
		'xsettingsd'
		'xorg-xsetroot'
		'wmname'
		'pulsemixer' 'light' 'xcolor'
)
conflicts=('archcraft-qtile-premium')
provides=("${pkgname}")
options=(!strip !emptydirs)
install="${pkgname}.install"

prepare() {
	cp -af ../files/. ${srcdir}
}

package() {
	local _config=${pkgdir}/etc/skel/.config/qtile
	mkdir -p "$_config"

	# Copy qtile config files
	cp -r ${srcdir}/alacritty 		"$_config"
	cp -r ${srcdir}/scripts 		"$_config"
	cp -r ${srcdir}/theme 			"$_config"

	chmod +x "$_config"/scripts/*
	chmod +x "$_config"/theme/polybar.sh
	chmod +x "$_config"/theme/polybar/launch.sh
	chmod +x "$_config"/theme/polybar/scripts/bluetooth.sh

	install -Dm 644 config.py   			"$_config"/config.py
	install -Dm 644 dunstrc   				"$_config"/dunstrc
	install -Dm 644 picom.conf   			"$_config"/picom.conf
	install -Dm 644 picom-ibhagwan.conf   	"$_config"/picom-ibhagwan.conf
	install -Dm 644 picom-jonaburg.conf   	"$_config"/picom-jonaburg.conf
	install -Dm 644 picom-original.conf   	"$_config"/picom-original.conf
	install -Dm 644 xsettingsd   			"$_config"/xsettingsd
}
