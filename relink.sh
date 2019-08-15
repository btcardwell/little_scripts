#!/bin/bash

link=$1
old=$2
new=$3
target=$(readlink -- "$1")

target=${target/"$old"/"$new"}

#echo ln -s -- "$target" "$link"

rm $link
ln -s -- "$target" "$link"
