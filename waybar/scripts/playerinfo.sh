#!/bin/bash

artist=$(playerctl metadata artist)

metadata=$(playerctl metadata --format '{{duration(position)}} / {{duration(mpris:length)}} ♫')
if [ -z "$artist" ]; then
    metadata="$metadata $(playerctl metadata --format '{{title}}')"
else
    metadata="$metadata $(playerctl metadata --format '{{artist}} — {{title}}')"
fi

status=$(playerctl status)
if [[ $status == "Playing" ]]; then
    metadata="▶ $metadata"
elif [[ $status == "Paused" ]]; then
    metadata="⏸ $metadata"
fi

echo $metadata | awk '{if (length($0) > 45) print substr($0, 1, 42) "..."; else print}'
