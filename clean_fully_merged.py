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
directory_contents = os.listdir(condor_dir)
dirs_with_root_files = [d.rstrip('.root') for d in directory_contents if '.root' in d]
# keep only the directory names that appear in the original list to avoid
# composite and partially merged datasets
dirs_with_root_files = list(set(directory_contents) & set(dirs_with_root_files))
fully_merged_dirs = [d for d in dirs_with_root_files if not os.path.isfile(condor_dir + d +
                                                                           '/condor_resubmit.sub')]

for d in fully_merged_dirs:
    print "Removing hist_*.root files from", d
    for f in glob.glob(condor_dir + d + "/hist*root"):
        try:
            os.remove(f)
        except Exception:
            pass
