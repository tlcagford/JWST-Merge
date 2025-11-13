# Install MAST query tools
pip install astroquery

# Query and download data
python -c "
from astroquery.mast import Observations
import numpy as np

# Search for Abell 1689 JWST observations
obs_table = Observations.query_criteria(objectname='Abell 1689', 
                                      instrument_name='NIRCam/*',
                                      obs_collection='JWST')

print(f'Found {len(obs_table)} observations')
for obs in obs_table[:5]:
    print(f'Observation ID: {obs['obs_id']}, Instrument: {obs['instrument_name']}')

# Download the data
 Observations.download_products(obs_table['obsid'], 
                               productType=['CALIBRATED'],
                               extension='fits')
"