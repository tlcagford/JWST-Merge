from jwst_merge import merge_jwst

# Process a set of JWST observations
result = merge_jwst.process(
    input_files="jw*.fits",
    output_dir="./merged_output",
    background_match=True,
    cosmic_ray_rejection=True,
    output_prefix="my_target"
)