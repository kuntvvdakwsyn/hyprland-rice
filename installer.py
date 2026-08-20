import sys
import os 
import shutil

def change_file(path,symb,symb1):
    with open(path,"r") as r:
        file = r.read()
    new_file = file.replace(symb,symb1)
    with open(path,"w") as w:
        w.write(new_file)



user = input("Write your username: ")

config = "/home/" + user + "/.config/"

my_os = input('''Write your os :

(1 - arch)
(2 - nixos)
(3 - fedora)
(4 - gentoo)

Write your option: ''')
if my_os == "1":
    print("sudo pacman -S fastfetch foot rofi swaybg waybar hyprland nvim tree-sitter ttf-jetbrains-mono-nerd git yazi")
    os.system("sudo pacman -S fastfetch foot rofi swaybg waybar hyprland nvim tree-sitter ttf-jetbrains-mono-nerd git yazi")
elif my_os == "2":
    print("Write in configuration.nix: \nfastfetch\nfoot\nrofi\nswaybg\nwaybar\nhyprland\nnvim\ntree-sitter\nttf-jetbrains-mono-nerd\ngit\nyazi")
    print("To continue press Enter: ", end="")
    p = input()
    del p
elif my_os == "3":
    print("sudo dnf install -y fastfetch foot rofi swaybg waybar hyprland nvim tree-sitter ttf-jetbrains-mono-nerd git yazi")
    os.system("sudo dnf install -y fastfetch foot rofi swaybg waybar hyprland nvim tree-sitter ttf-jetbrains-mono-nerd git yazi")
elif my_os == "4":
    print("sudo emerge --ask app-misc/fastfetch gui-apps/foot x11-misc/rofi gui-apps/swaybg gui-apps/waybar gui-hypr/hyprland app-editors/neovim dev-util/tree-sitter media-fonts/jetbrainsmono-nerd dev-vcs/git app-misc/yazi")
    os.system("sudo emerge --ask app-misc/fastfetch gui-apps/foot x11-misc/rofi gui-apps/swaybg gui-apps/waybar gui-hypr/hyprland app-editors/neovim dev-util/tree-sitter media-fonts/jetbrainsmono-nerd dev-vcs/git app-misc/yazi")
else:
    print("Invalid argument!")
    sys.exit(1)


os.system(f"mkdir -p {config}")

#fastfetch
os.system(f"mkdir -p {config}fastfetch")
os.system(f"cp -r ./fastfetch/* {config}fastfetch")

#foot
os.system(f"mkdir {config}foot -p")
path_zsh = shutil.which("zsh")
if not path_zsh:
    path_zsh = input("Error locating zsh path. Please enter it manually:")

change_file("./foot/foot.ini","X",path_zsh)
os.system(f"cp -r ./foot/* {config}foot")

#rofi
os.system(f"mkdir -p {config}rofi")
change_file("./rofi/config.rasi","X",user)
os.system(f"cp -r ./rofi/* {config}rofi")

#hyprland conf
os.system(f"mkdir -p {config}hypr")
path_wall = input("Enter path to wallpaper: ")
if not path_wall:
    print("You dont want a wallpaper.Ok... Skip")
    change_file("./hypr/hyprland.conf","XX","")
else:
    if path_wall[0] == "~":
        path_wall = f"/home/{user}{path_wall[1:]}"      #Transform ~ to /home/user
    change_file("./hypr/hyprland.conf","XX",f"swaybg -i {path_wall}") 
os.system(f"cp -r ./hypr/hyprland.conf {config}hypr/")
print(f"Succesfuly installed wallpaper to the path {path_wall}!")

#nvim
os.system(f"mkdir -p {config}nvim")
os.system(f"cp -r ./nvim/* {config}nvim")

#yazi
os.system(f"mkdir -p {config}yazi")
os.system(f"cp -r ./yazi/* {config}yazi")


