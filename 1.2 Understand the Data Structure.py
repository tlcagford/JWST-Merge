# Initial exploration script
import os
import pandas as pd
from astropy.io import fits
import pickle

def explore_repository():
    print("=== WFC3-PSF REPOSITORY EXPLORATION ===\n")
    
    # Check what files are available
    data_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if any(ext in file for ext in ['.fits', '.pkl', '.csv', '.parquet']):
                data_files.append(os.path.join(root, file))
    
    print(f"Found {len(data_files)} data files")
    
    # Examine first few files
    for file_path in data_files[:10]:
        print(f"\n--- {os.path.basename(file_path)} ---")
        try:
            if file_path.endswith('.fits'):
                with fits.open(file_path) as hdul:
                    print(f"  Extensions: {len(hdul)}")
                    for i, hdu in enumerate(hdul):
                        print(f"    [{i}] {hdu.header.get('EXTNAME', 'PRIMARY')} - {hdu.data.shape if hasattr(hdu, 'data') else 'No data'}")
            
            elif file_path.endswith('.pkl'):
                with open(file_path, 'rb') as f:
                    data = pickle.load(f)
                    print(f"  Type: {type(data)}")
                    if hasattr(data, 'shape'):
                        print(f"  Shape: {data.shape}")
                    elif isinstance(data, dict):
                        print(f"  Keys: {list(data.keys())[:5]}...")
            
            elif file_path.endswith(('.csv', '.parquet')):
                df = pd.read_csv(file_path) if file_path.endswith('.csv') else pd.read_parquet(file_path)
                print(f"  Columns: {list(df.columns)}")
                print(f"  Rows: {len(df)}")
                
        except Exception as e:
            print(f"  Error reading: {e}")
    
    return data_files

data_files = explore_repository()