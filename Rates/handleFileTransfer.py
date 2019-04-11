#!/usr/bin/env python
import os

from aux import mergeNames

from optparse import OptionParser

def move_file_to_dir(file_path, directory_path):

    if os.path.isfile(file_path):

       if not os.path.isdir(directory_path): os.system("mkdir -p %s"%(directory_path))

       os.system("mv %s %s"%(file_path, directory_path))

    else:

       print 'file not found:', file_path

    return

parser=OptionParser()
parser.add_option("-d","--directory",dest="dir",type="str",default="nodir",help="working DIRECTORY",metavar="DIRECTORY")
parser.add_option("-s","--finalstring",dest="fstr",type="str",default="nostr",help="final STRING",metavar="STRING")

(opts, args) = parser.parse_args()

for filename in mergeNames.keys():
    move_file_to_dir('Jobs/%s.%s.csv'%(filename, opts.fstr), "%s/Results/Raw/%s"%(opts.dir, mergeNames[filename]))

move_file_to_dir("Jobs/output.global.%s.csv"%(opts.fstr), "%s/Results/Raw/Global"%(opts.dir))
move_file_to_dir("Jobs/histos.%s.root"      %(opts.fstr), "%s/Results/Raw/Root"  %(opts.dir))
