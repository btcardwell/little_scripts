#!/usr/bin/env python
import sys
import os
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-w", "--eosDirectory", dest="eosDir", help="eos working directory")
parser.add_option("-c", "--channelName", dest="channelName", help="channel name")

(arguments, args) = parser.parse_args()

if arguments.eosDir:
    eos_dir = arguments.eosDir
else:
    print "Please specify an eos directory with -w"
    sys.exit(1)

if arguments.channelName:
    channel = arguments.channelName
else:
    print "Please specify a channel with -c"
    sys.exit(1)


dir_contents = [eos_dir + d for d in os.listdir(eos_dir)]
subdirs = filter(os.path.isdir, dir_contents)
datasets = [d.split('/')[-1] for d in subdirs]
for dataset in datasets:
    command = "eoscp {}{}/{{,{}/}}datasetInfo_{}_cfg.py".format(eos_dir, dataset, channel, dataset)
    print command
    os.system(command)
