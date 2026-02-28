#! /bin/bash

artist=$(playerctl metadata artist)

if [ -z "$artist" ]; then
    metadata=$(playerctl metadata --format '{{title}}')
else
    metadata=$(playerctl metadata --format '{{artist}} — {{title}}')
fi

echo $metadata | awk '{if (length($0) > 45) print substr($0, 1, 42) "..."; else print}'