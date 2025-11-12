def analyze_radial_profiles(enhanced_df):
    """Analyze empirical radial profiles to test solitonic prediction"""
    
    print("=== RADIAL PROFILE ANALYSIS ===\n")
    
    from scipy.optimize import curve_fit
    
    def power_law(r, a, b):
        return a * r**(-b)
    
    power_law_indices = []
    profiles_analyzed = 0
    
    for idx, row in enhanced_df.iterrows():
        if 'psf_model' not in row or row['psf_model'] is None:
            continue
            
        psf_data = row['psf_model']
        
        # Check if we have the PSF image data
        if 'data' in psf_data and psf_data['data'] is not None:
            psf_image = psf_data['data']
            
            try:
                # Calculate radial profile
                profile, radii = extract_radial_profile(psf_image)
                
                # Fit power law (avoiding the very center where sampling is poor)
                if len(radii) > 10 and len(profile) > 10:
                    mask = radii > 2.0  # Start fitting beyond the core
                    popt, pcov = curve_fit(power_law, radii[mask], profile[mask], 
                                         p0=[1.0, 2.0], maxfev=5000)
                    
                    beta = popt[1]
                    power_law_indices.append(beta)
                    profiles_analyzed += 1
                    
            except Exception as e:
                continue
    
    # Statistical test against PDPD prediction
    pdpd_prediction = 9.0
    if power_law_indices:
        empirical_beta = np.mean(power_law_indices)
        empirical_std = np.std(power_law_indices)
        
        z_score = abs(pdpd_prediction - empirical_beta) / empirical_std
        
        print(f"Profiles analyzed: {profiles_analyzed}")
        print(f"Empirical power law index: {empirical_beta:.2f} ± {empirical_std:.2f}")
        print(f"PDPD prediction: β = {pdpd_prediction}")
        print(f"Statistical rejection: {z_score:.1f}σ")
        
        if z_score > 5:
            print("🚫 STRONG REJECTION of solitonic profile prediction")
        else:
            print("⚠️  Inconclusive - cannot strongly reject solitonic profile")
    
    return power_law_indices

def extract_radial_profile(psf_image):
    """Extract radial profile from PSF image"""
    center = np.array(psf_image.shape) // 2
    y, x = np.indices(psf_image.shape)
    r = np.sqrt((x - center[1])**2 + (y - center[0])**2)
    
    # Bin by radius
    r_flat = r.flatten()
    intensity_flat = psf_image.flatten()
    
    r_bins = np.linspace(0, min(center), 50)
    digitized = np.digitize(r_flat, r_bins)
    
    profile = np.array([intensity_flat[digitized == i].mean() for i in range(1, len(r_bins))])
    radii = (r_bins[1:] + r_bins[:-1]) / 2
    
    return profile, radii

power_law_indices = analyze_radial_profiles(enhanced_df)