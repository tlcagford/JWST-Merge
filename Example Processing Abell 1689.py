import glob
from jwst_merge import merge_jwst

# Find all calibrated files
cal_files = glob.glob("abell1689/*_cal.fits")

# Process each filter separately
for filter_name in ['F115W', 'F150W', 'F200W']:
    filter_files = [f for f in cal_files if filter_name in f]
    
    merge_jwst.process(
        input_files=filter_files,
        output_dir=f"./abell1689_{filter_name}",
        background_match=True,
        save_steps=True
    )