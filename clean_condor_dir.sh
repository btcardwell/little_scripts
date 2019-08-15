#!/bin/bash

if [[ ! -d "$1" ]] ; then
    echo "$1 is not a valid directory"
    exit
fi

dir=$1

rm "$dir"/*/hist_*root
rm "$dir"/*/condor*err
rm "$dir"/*/condor*log
rm "$dir"/*/condor*out
