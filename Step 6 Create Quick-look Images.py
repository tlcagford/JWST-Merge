from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import glob

output_dir = "./abell1689_output"
merged_files = glob.glob(os.path.join(output_dir, "*_merged.fits"))

for file in merged_files:
    with fits.open(file) as hdul:
        data = hdul[1].data  # Usually SCI extension
        
    # Create preview
    plt.figure(figsize=(10, 8))
    vmin, vmax = np.percentile(data[data == data], [1, 99])
    plt.imshow(data, cmap='gray', vmin=vmin, vmax=vmax, origin='lower')
    plt.title(f"Abell 1689 - {os.path.basename(file)}")
    plt.colorbar(label='Surface Brightness')
    plt.savefig(file.replace('.fits', '_preview.png'), dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"Created preview for {os.path.basename(file)}")