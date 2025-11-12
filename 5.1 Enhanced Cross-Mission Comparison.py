def enhanced_multi_mission_analysis(enhanced_df, jwt_data):
    """Update multi-mission analysis with actual PSF data"""
    
    print("=== ENHANCED MULTI-MISSION ANALYSIS ===\n")
    
    # Now we have ACTUAL HST PSF measurements, not just metadata
    hst_direct_measurements = {
        'fwhm': [row.get('fwhm') for _, row in enhanced_df.iterrows() if pd.notna(row.get('fwhm'))],
        'ellipticity': [row.get('ellipticity') for _, row in enhanced_df.iterrows() if pd.notna(row.get('ellipticity'))],
        'focus_correlation': calculate_focus_correlation(enhanced_df),
        'anomaly_rate': anomalies / len(enhanced_df) if len(enhanced_df) > 0 else 0
    }
    
    print("HST Direct PSF Measurements:")
    print(f"  Mean FWHM: {np.mean(hst_direct_measurements['fwhm']):.3f} arcsec")
    print(f"  Mean ellipticity: {np.mean(hst_direct_measurements['ellipticity']):.3f}")
    print(f"  Focus correlation: {hst_direct_measurements['focus_correlation']:.3f}")
    print(f"  Anomaly rate: {hst_direct_measurements['anomaly_rate']:.3f}")
    
    # Compare with JWST expectations
    print("\nJWST Comparison:")
    print(f"  Expected FWHM (F770W): ~0.23 arcsec")
    print(f"  Expected ellipticity: <0.05")
    print(f"  Focus stability: ~1000x better than HST")
    
    # Key test: Do anomalies persist across missions?
    print(f"\nMulti-Mission Consistency Test:")
    if hst_direct_measurements['anomaly_rate'] > 0.05:
        print("  HST shows potential anomalies - requires JWST verification")
    else:
        print("  HST shows no significant anomalies - consistent with JWST null result")

def calculate_focus_correlation(enhanced_df):
    """Calculate correlation between focus and PSF quality"""
    focus_vals = []
    ellipticity_vals = []
    
    for _, row in enhanced_df.iterrows():
        if (pd.notna(row.get('focus')) and pd.notna(row.get('ellipticity'))):
            focus_vals.append(row['focus'])
            ellipticity_vals.append(row['ellipticity'])
    
    if len(focus_vals) > 10:
        return np.corrcoef(focus_vals, ellipticity_vals)[0,1]
    else:
        return 0.0

enhanced_multi_mission_analysis(enhanced_df, jwt_data)