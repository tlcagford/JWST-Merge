import numpy as np
from astropy.table import Table
import glob

def load_wfc3_psf_library():
    """Load the complete WFC3-PSF library"""
    
    print("=== LOADING WFC3-PSF LIBRARY ===\n")
    
    # Initialize data structures
    psf_models = {}
    metadata_list = []
    
    # Look for PSF model files
    psf_files = glob.glob('**/*.fits', recursive=True) + glob.glob('**/*.pkl', recursive=True)
    
    for psf_file in psf_files:
        try:
            if psf_file.endswith('.fits'):
                # Load FITS PSF models
                with fits.open(psf_file) as hdul:
                    # Extract metadata from header
                    header = hdul[0].header
                    rootname = header.get('ROOTNAME', 'unknown')
                    
                    psf_models[rootname] = {
                        'data': hdul[0].data,
                        'header': header,
                        'fwhm': header.get('FWHM', None),
                        'ellipticity': header.get('ELLIPTIC', None),
                        'focus': header.get('FOCUS', None),
                        'filter': header.get('FILTER', None),
                        'mjd': header.get('MJD', None)
                    }
                    
                    metadata_list.append({
                        'rootname': rootname,
                        'filter': header.get('FILTER', None),
                        'focus': header.get('FOCUS', None),
                        'fwhm': header.get('FWHM', None),
                        'ellipticity': header.get('ELLIPTIC', None),
                        'mjd': header.get('MJD', None),
                        'target': header.get('TARGNAME', None),
                        'exptime': header.get('EXPTIME', None)
                    })
                    
            elif psf_file.endswith('.pkl'):
                # Load pickle PSF models
                with open(psf_file, 'rb') as f:
                    psf_data = pickle.load(f)
                    # Structure will depend on how the pickle was saved
                    if isinstance(psf_data, dict):
                        for key, model in psf_data.items():
                            psf_models[key] = model
                    
        except Exception as e:
            print(f"Warning: Could not load {psf_file}: {e}")
            continue
    
    # Create metadata DataFrame
    metadata_df = pd.DataFrame(metadata_list)
    
    print(f"Loaded {len(psf_models)} PSF models")
    print(f"Metadata entries: {len(metadata_df)}")
    print(f"Filters: {metadata_df['filter'].unique()}")
    
    return psf_models, metadata_df

psf_models, wfc3_metadata = load_wfc3_psf_library()