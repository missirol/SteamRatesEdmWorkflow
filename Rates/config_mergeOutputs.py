'''
This file allows you to merge the outputs of the batch jobs, and get the trigger rates. You may also draw some figures if you wish.
The resulting .csv and .root files will be located in the 'Results' directory. The figures will be in the 'Figures' directory.
'''

'''
--------------------------OPTIONS TO BE FILLED OUT-----------------------------------------
'''
#Write the average instant lumi of the json you ran over
lumi_in = 1.7617e34

#Write the TARGET lumi for which you wish to calculate rates
lumi_target = 2.0e34

#Write the HLT prescale used in the json you ran over
hlt_ps = 1100

#Maps option should be the same one you use to make the batch jobs
#maps = "nomaps"
maps = "somemaps"
#maps = "allmaps"

#Do you wish to draw the figures? If you have a slow connection, drawing might take a while
#This boolean will be set to False if you used the "nomaps" option
makeFigures = False
#makeFigures = True

#Do you wish to take input files from an unusual location (different from the default one)?
#If you do, set the following boolean to True
diffLoc = False
#If yes, please specify the directory where the job outputs are located
files_dir = "Results/Raw"
'''
-------------------------------------------------------------------------------------------
'''

# run the script
if maps == "nomaps": makeFigures = False

command = "python mergeOutputs.py -l %s -t %s -p %s -m %s" %(lumi_in, lumi_target, hlt_ps, maps)

if diffLoc:
   command += " -d %s" %(files_dir)

if makeFigures:
   command += " -f"

import os

os.system(command)

if makeFigures: 

   command_2 = "python Draw.py"

   if maps == "allmaps":
      command_2 += " -m yes"

   os.system(command_2)
