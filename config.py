#!/usr/bin/python3
# Configuration file

import os
from datetime import datetime
import constants

DATA_FILES_BASE_URL = "https://www.bls.gov/cex/pumd/data/comma/"
EXTRACT_FOLDER_NAME = "extracted_data_files"
DOWNLOAD_FOLDER_NAME = "pumd_data_files"
YEAR_BUCKET = 5

# Make changes to download path here...
# DOWNLOAD_PATH = os.path.join(os.path.expanduser("~"), "Downloads")
DOWNLOAD_PATH = "/Volumes/Transcend"
DATA_FILES_PATH = os.path.join(DOWNLOAD_PATH, DOWNLOAD_FOLDER_NAME)
today = datetime.now().strftime('%b%d').lower()
EXPORT_FILES_PATH = os.path.join(DATA_FILES_PATH, "processed_data_{}yrs_bucket_{}".format(YEAR_BUCKET, today))

YEAR_BUCKET_MULTIPLIERS = {
    3: 12,
    5: 20
}

AGE_THRESHOLDS = {
    "min": 20,
    "max": 80
}

