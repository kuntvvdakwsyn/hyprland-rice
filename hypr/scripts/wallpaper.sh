#!/bin/bash

WALLPAPER_DIR="$HOME/wallpapers"
OUTPUT="$HOME/.config/hypr/local/wall.jpg"
SELECTED="/tmp/yazi-wallpaper"

rm -f "$SELECTED"

foot yazi "$WALLPAPER_DIR" --chooser-file="$SELECTED"

if [ ! -s "$SELECTED" ]; then
    exit 0
fi

IMAGE=$(cat "$SELECTED")

if [ ! -f "$IMAGE" ]; then
    exit 1
fi

cp "$IMAGE" "$OUTPUT"

OLD_PIDS=$(pgrep swaybg)

swaybg -i "$OUTPUT" -m fill &
NEW_PID=$!

sleep 0.1

if [ -n "$OLD_PIDS" ]; then
    kill $OLD_PIDS 2>/dev/null
fi
