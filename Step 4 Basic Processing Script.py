import glob
import os
from jwst_merge import merge_jwst
from astropy.io import fits
import matplotlib.pyplot as plt

# Configuration
input_dir = "./abell1689_data"
output_dir = "./abell1689_output"

# Find all calibrated files
cal_files = glob.glob(os.path.join(input_dir, "*_cal.fits"))
print(f"Found {len(cal_files)} calibrated files")

# Group by filter
filters = {}
for file in cal_files:
    with fits.open(file) as hdul:
        header = hdul[0].header
        filt = header.get('FILTER', 'unknown')
        if filt not in filters:
            filters[filt] = []
        filters[filt].append(file)

print("Files by filter:")
for filt, files in filters.items():
    print(f"  {filt}: {len(files)} files")

# Process each filter
for filter_name, file_list in filters.items():
    if len(file_list) < 2:
        continue
        
    print(f"\nProcessing {filter_name} with {len(file_list)} files...")
    
    try:
        # Run JWST-Merge
        result = merge_jwst.process(
            input_files=file_list,
            output_dir=output_dir,
            output_prefix=f"abell1689_{filter_name}",
            background_match=True,
            cosmic_ray_rejection=True,
            save_steps=True
        )
        
        print(f"Successfully processed {filter_name}")
        
    except Exception as e:
        print(f"Error processing {filter_name}: {e}")