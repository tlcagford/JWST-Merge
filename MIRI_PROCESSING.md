# JWST-Merge: MIRI and NIRCam Image Mosaicking Pipeline

A Python-based pipeline for merging and processing James Webb Space Telescope (JWST) MIRI and NIRCam imaging data. This tool handles background matching, cosmic ray rejection, and creates seamless mosaics from multiple exposures.

## Features

- **Multi-instrument Support**: Process both MIRI and NIRCam data
- **Background Matching**: Automatic background leveling across exposures
- **Cosmic Ray Rejection**: Advanced cosmic ray identification and removal
- **Seamless Mosaicking**: Create continuous field mosaics from dithered observations
- **Source Extraction**: Generate segmentation maps and source catalogs
- **Calibration-ready**: Works with JWST pipeline products (`_cal.fits`, `_rate.fits`)

## Installation

### Prerequisites
- Python 3.8+
- JWST calibration pipeline
- Astropy, Photutils, and other astronomy packages

### Quick Install
```bash
git clone https://github.com/tlcagford/JWST-Merge
cd JWST-Merge
pip install -r requirements.txt
