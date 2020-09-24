#! /usr/bin/bash
# cd to desired displaced leptons directory and cmsenv

# usage: . go.sh YEAR [CHANNEL]
# omitting CHANNEL will cd to DisplacedSUSY/ instead of channel directory

year=$1
channel=${2:-}

if [ "$year" = "16" ]; then
    release="CMSSW_8_0_31"
elif [ "$year" = "17" ]; then
    release="CMSSW_9_4_8"
elif [ "$year" = "18" ]; then
    release="CMSSW_10_2_12"
else
    echo "Unknown year"
    exit 1
fi

if [ "$channel" = "ee" ]; then
    local_path="EEChannel/test"
elif [ "$channel" = "emu" ]; then
    local_path="EMuChannel/test"
elif [ "$channel" = "mumu" ]; then
    local_path="MuMuChannel/test"
else
    local_path=""
fi

cd ~
cd 'nobackup/DisplacedSUSY/'"$release"'/src/DisplacedSUSY/'"$local_path"
cmsenv
clear
