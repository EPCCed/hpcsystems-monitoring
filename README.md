# HPC Systems Monitoring with CheckMK

This repository contains custom scripts, used with [CheckMK](https://checkmk.com/) - a general use monitoring system - to monitor HPC systems using non-commodity hardware and software. The development and use of "check" scripts can enable System Administrators to simply and reliably monitor all relevant and service-critical aspects of a variety of HPC systems through a single "pane of glass" approach. All scripts are designed to integrate with the CheckMK monitoring system. In addition to the scripts, the relevant sample input and output files are also provided. 

### tesseract_node_check.py
A Python2 script that wraps for the HPE "cpower" command to provide basic status information on each compute in a HPE system. It does this by processing output from the "cpower" command and passes the data in an appropriate format to the Panopticon CheckMK server at EPCC. This script is run on the central management node provided with the [Tesseract](https://dirac.ac.uk/resources/) HPE SGI 8600 system.

### opa_switch_monitor.sh
a BASH script developed to monitor the Omnipath network on the Tesseract HPE SGI 8600 system. It uses the "opareoprt" command in order to generate monitoring information for each switch within the Tesseract Omniparth network. 



## How to run scripts

