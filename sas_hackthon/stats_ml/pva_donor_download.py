import pandas as pd

# Option 1: Load from local SAS file (you already have this!)
# Requires: pip install pyreadstat
try:
    import pyreadstat
    # Load the FINAL training dataset (has target variables: Response & Donation_Amt)
    # This is the correct file for analysis and modeling
    sas_path = "data/VST152/pva_donors_final.sas7bdat"
    df, meta = pyreadstat.read_sas7bdat(sas_path)
    df.to_csv("pva_donors.csv", index=False)
    
    print("=" * 70)
    print("✓ Successfully loaded PVA training data!")
    print("=" * 70)
    print(f"Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")
    print(f"\nTarget Variables:")
    print(f"  • Response: {df['Response'].dtype} - Donor response (Yes/No)")
    print(f"  • Donation_Amt: {df['Donation_Amt'].dtype} - Donation amount ($)")
    print(f"\nFeature Variables: {df.shape[1] - 3} (excluding ID and targets)")
    print(f"\nAll Columns:")
    for i, col in enumerate(df.columns, 1):
        print(f"  {i:2d}. {col}")
    print("=" * 70)

except ImportError:
    print("❌ Error: pyreadstat not installed")
    print("Install with: pip install pyreadstat")
except FileNotFoundError:
    print(f"❌ Error: File not found at {sas_path}")
    print("Available files in data/VST152/:")
    print("  • pva_donors.sas7bdat (9,686 rows, 28 columns)")
    print("  • pva_donors_final.sas7bdat (9,686 rows, 31 columns) ← RECOMMENDED")
    print("  • score_pva.sas7bdat (96,367 rows, 26 columns - no targets)")
    
    print("\nTrying UCI download...")
    import requests
    from io import StringIO
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    # PVA donor dataset from KDD Cup 1998 (UCI Repository)
    url = "https://archive.ics.uci.edu/dataset/189/kdd+cup+1998+data"
    print(f"Download manually from: {url}")
