def merge_with_existing_analysis(psf_models, wfc3_metadata, original_df):
    """Merge the PSF library with your existing analysis"""
    
    print("=== MERGING DATASETS ===\n")
    
    # Check for common identifiers
    print("Original dataset columns:", original_df.columns.tolist())
    print("PSF metadata columns:", wfc3_metadata.columns.tolist())
    
    # Find common key (likely 'rootname')
    common_key = None
    for key in ['rootname', 'ROOTNAME', 'dataset']:
        if key in original_df.columns and key in wfc3_metadata.columns:
            common_key = key
            break
    
    if common_key:
        print(f"Merging on common key: {common_key}")
        
        # Merge metadata
        merged_metadata = pd.merge(original_df, wfc3_metadata, 
                                 on=common_key, how='inner', suffixes=('_orig', '_psf'))
        
        print(f"Successful merge: {len(merged_metadata)} matched entries")
        
        # Add PSF models to merged data
        merged_data = []
        for idx, row in merged_metadata.iterrows():
            rootname = row[common_key]
            if rootname in psf_models:
                merged_row = row.to_dict()
                merged_row['psf_model'] = psf_models[rootname]
                merged_data.append(merged_row)
        
        print(f"Entries with PSF models: {len(merged_data)}")
        
        return pd.DataFrame(merged_data)
    
    else:
        print("No common key found. Attempting fuzzy matching...")
        # Implement fuzzy matching if needed
        return None

# Merge the datasets
enhanced_df = merge_with_existing_analysis(psf_models, wfc3_metadata, df_full)