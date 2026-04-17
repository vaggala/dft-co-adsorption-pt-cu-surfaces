#!/bin/bash
#SBATCH --job-name=co_adsorption
#SBATCH --output=job.out
#SBATCH --error=job.err
#SBATCH --time=04:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4

# Load environment
module purge
module load intel/2021.9.0
module load intel-oneapi-mkl/2023.1.0
module load mvapich2
module load anaconda3

source activate sparc

export ASE_SPARC_COMMAND="srun /home/hice1/vaggala3/scratch/SPARC/lib/sparc"
export SPARC_PSP_PATH=/home/hice1/vaggala3/scratch/SPARC/psps

# Run workflow

# clean slab
cd pt111/clean
python build_pt111.py
python clean_energy.py

# atop
cd ../atop
python build_pt111_atop.py
python atop_energy.py

# fcc hollow
cd ../fcc_hollow
python build_pt111_fcc_hollow.py
python fcc_energy.py

# CO reference
cd ../../co
python build_co.py
python co_energy.py

# analysis
cd ../pt111
python pt111_analysis.py