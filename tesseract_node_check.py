#!/usr/bin/env python

############################################################################### 
# python 2
#                                                                              
# Script to take "cpower" status for all nodes and format appropriately for     
# monitoring
#
#
# Authors:  Philip Cass                                                    
#           HPC Systems team, EPCC, University of Edinburgh                               
#                                                                               
#           2019-08-01                                                                    
#                                                                               
# MIT License                                                                   
#                                                                               
###############################################################################




import subprocess
import sys

# Access list of nodes presented by HPE management system
nodes=[x[:-5] for x in  open("/etc/dsh/group/ice-compute").readlines()]

# Create a subprocess running the HPE providede "cpower" command
command = ["/opt/sgi/sbin/cpower","node","status","r*i*n*"]
p = subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,stderror = p.communicate()

# Operate over each line of output from the cpower subprocess.
# Output appropriate status based on the status presented by cpower
# Remove node from list of nodes to be checked
for line in output.split("\n"):
    if len(line)>1:
        words = line.split(" ")
        node="ts-" + words[0]
        nodes.remove(words[0])
        state=words[-1]
        print "<<<<{0}>>>>".format(node)
        print "<<<local>>>"
        if state=="BOOTED":
            print "0 node_power - cpower command on the SAC reports node booted"
        elif state=="ON":
            print "1 node_power - cpower command on the SAC reports node on, but not booted"
        elif state=="OFF":
            print "2 node_power - cpower command on the SAC reports node as off"
        else:
            print "3 node_power - cpower command on the SAC reports node as unknown state {0}".format(state)
        print "<<<<>>>>"

# Output relevant information for nodes not found in cpower check
for node in nodes:
    node="ts-" + node
    print "<<<<{0}>>>>".format(node)
    print "<<<local>>>"
    print "3 node_power - node not found in cpower output on the SAC"
    print "<<<<>>>>"

# Check for successful completion of the cpower subprocess, output appropriately
print "<<<local>>>"
if len(stderror)>0:
  lines = "\\n".join(stderror.split("\n"))
  print "1 node_power - cpower command on the SAC reported at least one error: \\n" + lines
else:
  print "0 node_power - cpower command on the SAC successfully queried all nodes"
