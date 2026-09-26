# hyprland rice

# Cloning the repo:
``` bash
git clone https://github.com/kuntvvdakwsyn/hyprland-rice/
```

# Make dir - configs:
``` bash
cd ~/.config
mkdir foot rofi hypr waybar
```

# For arch and arch-based:
- Install packages:
``` bash
sudo pacman -S fastfetch hyprland swaybg nvim evince foot rofi waybar ripgrep fd gcc make unzip curl tar nodejs npm ttf-jetbrains-mono-nerd
```
# For debian and debian-based:
``` bash
sudo apt install fastfetch hyprland swaybg nvim evince foot rofi waybar ripgrep fd gcc make unzip curl tar nodejs npm ttf-jetbrains-mono-nerd
```
# For gentoo and gentoo-based(using emerge):
``` bash
sudo emerge --ask \
    app-misc/fastfetch \
    gui-wm/hyprland \
    gui-apps/swaybg \
    app-editors/neovim \
    app-text/evince \
    gui-apps/foot \
    gui-apps/rofi \
    gui-apps/waybar \
    sys-apps/ripgrep \
    sys-apps/fd \
    sys-devel/gcc \
    sys-devel/make \
    app-arch/unzip \
    net-misc/curl \
    app-arch/tar \
    net-libs/nodejs \
    media-fonts/jetbrains-mono-nerd-font
```

# For nixos:
``` nix
#/etc/nixos/configuration.nix under environment.systemPackages
# ...
environment.systemPackages = with pkgs; [
  fastfetch
  hyprland
  swaybg
  neovim
  evince
  foot
  rofi
  waybar
  ripgrep
  fd
  gcc
  gnumake
  unzip
  curl
  gnutar
  nodejs
  nodePackages.npm
  nerd-fonts.jetbrains-mono
];
# ...
```
