# Clone the repository
git clone https://github.com/tlcagford/JWST-Merge
cd JWST-Merge

# Create a conda environment (recommended)
conda create -n jwst-merge python=3.9
conda activate jwst-merge

# Install dependencies
pip install -r requirements.txt

# Additional JWST packages you might need
pip install jwst astropy photutils