#!/bin/bash
#SBATCH --cpus-per-task=2
#SBATCH --nodes=1
#SBATCH --time=00:30:00
#SBATCH --mem=16000M
#SBATCH --job-name=geofabric
#SBATCH --mail-user=kasra.keshavarz1@ucalgary.ca
#SBATCH --mail-type=FAIL,BEGIN,END
