#!/bin/bash
#SBATCH --job-name=sockeye_tutorial       
#SBATCH --account=st-puranga-1-gpu
#SBATCH --nodes=1                               # Number of nodes
#SBATCH --ntasks=1                              # Number of MPI process
#SBATCH --ntasks-per-node=1                     # Number of distributed process per compute node
#SBATCH --cpus-per-task=4                       # CPU cores per MPI process
#SBATCH --mem=2GB                               # memory per node
#SBATCH --time=00:10:00                         # time
#SBATCH --gpus-per-node=1                       # number of GPUs per node
#SBATCH --output=./%j.out        
#SBATCH --error=./%j.err
#SBATCH --mail-user=nimakondori@ece.ubc.ca
#SBATCH --mail-type=ALL  
 
################################################################################

module restore nima-torch-jobs
module load http_proxy

conda init
source ~/.bashrc
conda activate /project/st-puranga-1/conda_envs/soc_tut

cd $SLURM_SUBMIT_DIR
cd ../../

python main.py
