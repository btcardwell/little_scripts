#!/usr/bin/env python
import sys
import os
import glob
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-w", "--workDirectory", dest="condorDir",
                  help="condor working directory")

(arguments, args) = parser.parse_args()

if arguments.condorDir:
    condor_dir= "condor/" + arguments.condorDir + "/"
else:
    print "Please specify a condor directory with -w"
    sys.exit(1)

# find all directories with an associated root file and no resubmit file
dir_contents = [condor_dir + d for d in os.listdir(condor_dir)]
subdirs = filter(os.path.isdir, dir_contents)
dirs_with_resubmit = [d for d in subdirs if os.path.isfile(d + '/condor_resubmit.sub')]

for d in dirs_with_resubmit:
    print os.path.split(d)[1]

