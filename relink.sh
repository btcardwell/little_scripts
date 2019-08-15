#!/bin/bash
# update symlink target when part of the target path has been changed

# usage: relink LINK_NAME PART_OF_TARGET_TO_REPLACE REPLACEMENT_TEXT
# e.g. if path/to/link points to old/target/path, then
# relink /path/to/link old new
# will make path/to/link point to new/target/path

link=$1
old=$2
new=$3
target=$(readlink -- "$1")

target=${target/"$old"/"$new"}

#echo ln -s -- "$target" "$link"

rm $link
ln -s -- "$target" "$link"
