def enhanced_psf_shape_analysis(enhanced_df):
    """Analyze actual PSF shapes from the library"""
    
    print("=== ENHANCED PSF SHAPE ANALYSIS ===\n")
    
    # Extract direct measurements
    fwhm_values = []
    ellipticity_values = []
    focus_values = []
    
    for idx, row in enhanced_df.iterrows():
        if 'psf_model' in row and row['psf_model'] is not None:
            psf_data = row['psf_model']
            
            # Extract measurements
            if 'fwhm' in psf_data and psf_data['fwhm']:
                fwhm_values.append(psf_data['fwhm'])
            if 'ellipticity' in psf_data and psf_data['ellipticity']:
                ellipticity_values.append(psf_data['ellipticity'])
            if 'focus' in psf_data and psf_data['focus']:
                focus_values.append(psf_data['focus'])
    
    # Statistical analysis
    print(f"PSF FWHM: {np.mean(fwhm_values):.3f} ± {np.std(fwhm_values):.3f} arcsec")
    print(f"PSF Ellipticity: {np.mean(ellipticity_values):.3f} ± {np.std(ellipticity_values):.3f}")
    print(f"Focus range: {np.min(focus_values):.2f} to {np.max(focus_values):.2f}")
    
    # Focus correlation
    if len(focus_values) == len(fwhm_values):
        focus_fwhm_corr = np.corrcoef(focus_values, fwhm_values)[0,1]
        print(f"Focus-FWHM correlation: {focus_fwhm_corr:.3f}")
    
    return {
        'fwhm_values': fwhm_values,
        'ellipticity_values': ellipticity_values, 
        'focus_values': focus_values
    }

shape_results = enhanced_psf_shape_analysis(enhanced_df)