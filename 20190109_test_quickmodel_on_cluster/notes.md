# 2019/01/09

## Test for running quickmodel on Lilac cluster

run-torque.sh file in this directory is what I have been using to run jobs in HAL cluster. I need an LSF script for Lilac.

### Install assaytools to new environment: assaytools_af411f0

$ conda create -n assaytools_af411f0 python=3.6
$ source activate assaytools_af411f0
$ conda install numpy
$ cd ~/repos/assaytools/
$ python setup.py install

$ conda install lxml
$ conda install pymc
$ conda install seaborn
$ conda install pymbar

### Submit a CPU job to lilac queue

I adjusted the run-lsf.sh file to request 1 process in 1 node, 2 hours and 4 G for testing 1000 samples.
For 100000 samples my guess is that it will require 8 hours, and 8 G mem.

$ bsub < run-lsf.sh
