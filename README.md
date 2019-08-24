# HPC Systems Monitoring with CheckMK

This repository contains custom scripts, used with [CheckMK](https://checkmk.com/) - a general use monitoring system - to monitor HPC systems using non-commodity hardware and software. The development and use of "check" scripts can enable System Administrators to simply and reliably monitor all relevant and service-critical aspects of a variety of HPC systems through a single "pane of glass" approach. 

## Custom monitoring scripts
Both scripts are designed to integrate with the CheckMK monitoring system. In addition to the scripts, the relevant sample input and output files are also provided. 

### tesseract_node_check.py
A Python2 script that wraps for the HPE "cpower" command to provide basic status information on each compute in a HPE system. It does this by processing output from the "cpower" command and passes the data in an appropriate format to the Panopticon CheckMK server at EPCC. This script is run on the central management node provided with the [Tesseract](https://dirac.ac.uk/resources/) HPE SGI 8600 system.

### opa_switch_monitor.sh
a BASH script developed to monitor the Omnipath network on the Tesseract HPE SGI 8600 system. It uses the "opareoprt" command in order to generate monitoring information for each switch within the Tesseract Omniparth network. 

A useful outline of developing custom checks in the manner used at EPCC can be found in the CheckMK guide [here](https://checkmk.com/cms_localchecks.html).

## Dependencies
The scripts require CheckMK.

## How to run scripts
The custom scripts described above are setup in one of two ways:

(1) Scripts are run directly by the CheckMK agent on the client node.
(2) cron, or other automatic process, runs the relevant script and data is output to an appropriate spool directory that CheckMK reads.

Method (1) is used by the tesseract_node_check.py script, whilst method (2) is used by the opa_switch_monitor.sh script.

The **tesseract_node_check.py** script should be reproducible on any similar HPE system - or in fact any system where the "cpower" command provides suitably formatted output. With CheckMK client installed on the management node this script can be place in the relevant directory (/var/lib/checkmk on our system) and discovered at the CheckMK server as described [here](https://checkmk.com/cms_localchecks.html). 

A sample of the node listing maintained by the HPE software stack for dsh (/etc/dsh/group/ice-compute) can be found in file : tesseract_node_check_sample_input. This is used to determine the base node list for monitoring. 

Sample output from this script when run manually can be found in file: tesseract_node_check_sample_output. Note this is the output for the same 12 nodes listed in the sample input.

This **opa_switch_monitor.sh** script is run on the "rack leader" for rack 1 of the system - this rack leader also acts as one of two fabric managers for the Omnipath network. This script could however be run from any node from which the "opareport" command can interrogate the network. 

This script outputs to the /var/lib/check\_mk\_agent/spool directory - this location may vary depending on the OS and version of CheckMK involved. This script should be simply reproducible on any system with an Omnipath network and CheckMK. A cron or other automatic mechanism should be used to run the script at an appropriate interval. A sample of the switch list used to identify which switches should be monitored can be found in file: opa_switch_monitor_switch.list. Sample output from this script can be found in file: opa_switch_monitor_output



