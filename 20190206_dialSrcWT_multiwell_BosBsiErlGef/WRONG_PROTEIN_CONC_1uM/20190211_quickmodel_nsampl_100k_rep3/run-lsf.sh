#!/bin/bash
#BSUB -J test_quickmodel
#BSUB -n 1
#BSUB -R span[ptile=1]
#BSUB -R rusage[mem=8]
#BSUB -W 48:00
#BSUB -o %J.stdout
#BSUB -eo %J.stderr

# make sure job's submission CWD path can be accessed on the job's execution host 
cd $LS_SUBCWD

# Activate the environment where Assaytools is installed
source activate assaytools_af411f0

# Export current conda environment requirements
conda list --export > requirements.txt

# Run my program
echo "Started running Assaytools...\n"
quickmodel --inputs 'inputs_multiple_well_dial_WT_Src_4ligs' --type 'spectra' --nsamples 100000
echo "Done."

# For full analysis run with at least 100000 samples

