def psf_subtraction_anomaly_detection(enhanced_df):
    """Look for anomalous residuals in PSF subtractions"""
    
    print("=== PSF SUBTRACTION ANOMALY DETECTION ===\n")
    
    anomalies_detected = 0
    offset_candidates = 0
    
    for idx, row in enhanced_df.iterrows():
        if 'psf_model' not in row or row['psf_model'] is None:
            continue
            
        psf_data = row['psf_model']
        
        if 'data' in psf_data and psf_data['data'] is not None:
            empirical_psf = psf_data['data']
            
            try:
                # Generate ideal PSF for comparison
                ideal_psf = generate_ideal_comparison_psf(row)
                
                # Calculate residuals
                residuals = empirical_psf - ideal_psf
                
                # Look for secondary components at ~3.5" offset
                offset_detection = detect_secondary_components(residuals, row)
                
                if offset_detection['significant']:
                    offset_candidates += 1
                    print(f"Potential offset in {row.get('rootname', 'unknown')}: "
                          f"S/N = {offset_detection['snr']:.1f}")
                
                # Check for overall anomaly
                residual_norm = np.linalg.norm(residuals)
                if residual_norm > calculate_anomaly_threshold(empirical_psf):
                    anomalies_detected += 1
                    
            except Exception as e:
                continue
    
    print(f"Total anomalies detected: {anomalies_detected}/{len(enhanced_df)}")
    print(f"Offset candidates (3.5\"): {offset_candidates}/{len(enhanced_df)}")
    
    return anomalies_detected, offset_candidates

def generate_ideal_comparison_psf(row):
    """Generate ideal PSF for comparison"""
    # This could use TinyTim, WebbPSF, or an average empirical PSF
    # For now, use a simple Gaussian approximation
    shape = (51, 51)  # Typical PSF stamp size
    return generate_gaussian_psf(shape, fwhm=row.get('fwhm', 2.0))

def detect_secondary_components(residuals, metadata):
    """Look for secondary PSF components at predicted offset"""
    # Convert 3.5" to pixels (WFC3/IR: ~0.13"/pix)
    offset_pixels = 3.5 / 0.13  # ~27 pixels
    
    # Search for significant residuals at this separation
    center = np.array(residuals.shape) // 2
    y, x = np.indices(residuals.shape)
    r = np.sqrt((x - center[1])**2 + (y - center[0])**2)
    
    # Look in annulus around predicted offset
    annulus_mask = (r > offset_pixels - 5) & (r < offset_pixels + 5)
    annulus_residuals = residuals[annulus_mask]
    
    if len(annulus_residuals) > 0:
        snr = np.max(annulus_residuals) / np.std(annulus_residuals)
        return {'significant': snr > 5, 'snr': snr, 'offset_pixels': offset_pixels}
    else:
        return {'significant': False, 'snr': 0, 'offset_pixels': offset_pixels}

anomalies, offsets = psf_subtraction_anomaly_detection(enhanced_df)