#!/bin/bash
# remove hist_*root, condor_*err, condor_*log, and condor_*out files after condor
# directory has been merged.

# usage: clean_condor_dir PATHTODIR

if [[ ! -d "$1" ]] ; then
    echo "$1 is not a valid directory"
    exit
fi

dir=$1

rm "$dir"/*/hist_*root
rm "$dir"/*/condor_*err
rm "$dir"/*/condor_*log
rm "$dir"/*/condor_*out
