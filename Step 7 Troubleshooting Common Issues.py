# Debug script - check file compatibility
from jwst import datamodels

def check_files(file_list):
    for file in file_list[:3]:  # Check first 3 files
        try:
            with datamodels.open(file) as model:
                print(f"✓ {os.path.basename(file)}:")
                print(f"  Shape: {model.data.shape}")
                print(f"  Filter: {model.meta.instrument.filter}")
                print(f"  Module: {model.meta.instrument.module}")
        except Exception as e:
            print(f"✗ {os.path.basename(file)}: {e}")

check_files(cal_files)