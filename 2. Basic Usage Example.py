# Minimal working example
from jwst_merge import miri_processing

result = miri_processing.process_miri(
    input_files="*_cal.fits",
    output_dir="./miri_output"
)