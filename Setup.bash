# Install build tools
pip install build twine

# Create distribution
python -m build

# Upload to PyPI
twine upload dist/*