# JWST-Merge: MIRI and NIRCam Image Mosaicking Pipeline

[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![JWST](https://img.shields.io/badge/JWST-Data_Processing-orange.svg)](https://jwst.stsci.edu/)

A Python-based pipeline for merging and processing James Webb Space Telescope (JWST) MIRI and NIRCam imaging data. This tool handles background matching, cosmic ray rejection, and creates seamless mosaics from multiple exposures.

## Features

- **Multi-instrument Support**: Process both MIRI and NIRCam data
- **Background Matching**: Automatic background leveling across exposures
- **Cosmic Ray Rejection**: Advanced cosmic ray identification and removal
- **Seamless Mosaicking**: Create continuous field mosaics from dithered observations
- **Source Extraction**: Generate segmentation maps and source catalogs
- **Calibration-ready**: Works with JWST pipeline products (`_cal.fits`, `_rate.fits`)
- **Memory Efficient**: Handles large JWST datasets efficiently

## Installation

### Prerequisites
- Python 3.8 or higher
- JWST calibration pipeline
- 4GB+ RAM recommended for large mosaics

### Quick Install
```bash
git clone https://github.com/tlcagford/JWST-Merge
cd JWST-Merge
pip install -r requirements.txt