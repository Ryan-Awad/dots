#! /bin/bash

playerctl metadata --format '{{artist}} — {{title}}' | awk '{if (length($0) > 60) print substr($0, 1, 57) "..."; else print}'
