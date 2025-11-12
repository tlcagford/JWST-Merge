def save_enhanced_results(enhanced_df, analysis_results):
    """Save the enhanced analysis results"""
    
    print("=== SAVING ENHANCED RESULTS ===\n")
    
    # Save the merged dataset
    enhanced_df.to_csv('enhanced_psf_analysis.csv', index=False)
    
    # Save analysis results
    with open('enhanced_analysis_results.pkl', 'wb') as f:
        pickle.dump(analysis_results, f)
    
    # Create summary report
    summary = {
        'total_psf_models': len(enhanced_df),
        'filters_available': enhanced_df['filter'].unique().tolist(),
        'focus_range': [enhanced_df['focus'].min(), enhanced_df['focus'].max()],
        'mean_fwhm': np.mean([x for x in enhanced_df['fwhm'] if pd.notna(x)]),
        'anomalies_detected': anomalies,
        'offset_candidates': offsets,
        'power_law_rejection': f"{power_law_z_score:.1f}σ" if 'power_law_z_score' in locals() else "N/A"
    }
    
    with open('analysis_summary.json', 'w') as f:
        json.dump(summary, f, indent=2)
    
    print("Enhanced analysis complete!")
    print(f"Results saved for {len(enhanced_df)} PSF models")
    print(f"Summary: {summary}")

# Save everything
analysis_results = {
    'shape_analysis': shape_results,
    'power_law_indices': power_law_indices,
    'anomalies_detected': anomalies,
    'offset_candidates': offsets
}

save_enhanced_results(enhanced_df, analysis_results)