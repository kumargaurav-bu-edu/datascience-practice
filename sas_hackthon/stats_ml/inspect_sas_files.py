"""
Inspect all SAS files to find which one has the target variable
"""
import subprocess
import sys

# Try to install pyreadstat if not available
try:
    import pyreadstat
except ImportError:
    print("Installing pyreadstat...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyreadstat", "-q"])
    import pyreadstat

import os

data_dir = "data/VST152"
sas_files = [
    "pva_donors.sas7bdat",
    "pva_donors_final.sas7bdat", 
    "score_pva.sas7bdat"
]

print("=" * 80)
print("INSPECTING SAS FILES FOR TARGET VARIABLE")
print("=" * 80)

for filename in sas_files:
    filepath = os.path.join(data_dir, filename)
    
    if not os.path.exists(filepath):
        print(f"\n❌ {filename}: FILE NOT FOUND")
        continue
    
    try:
        print(f"\n{'=' * 80}")
        print(f"FILE: {filename}")
        print(f"{'=' * 80}")
        
        df, meta = pyreadstat.read_sas7bdat(filepath)
        
        print(f"Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")
        print(f"\nColumns ({len(df.columns)}):")
        for i, col in enumerate(df.columns, 1):
            print(f"  {i:2d}. {col}")
        
        # Check for potential target variables
        print(f"\nPotential Target Variables:")
        target_keywords = ['target', 'response', 'donation', 'gift', 'amount', 'value', 'outcome']
        found_targets = [col for col in df.columns if any(kw in col.lower() for kw in target_keywords)]
        
        if found_targets:
            print(f"  ✅ Found: {found_targets}")
        else:
            print(f"  ❌ None found")
        
        # Show first few rows
        print(f"\nFirst 3 rows:")
        print(df.head(3).to_string())
        
    except Exception as e:
        print(f"❌ Error reading {filename}: {e}")

print("\n" + "=" * 80)
print("RECOMMENDATION:")
print("=" * 80)
print("Use 'pva_donors_final.sas7bdat' for training (has target variable)")
print("Use 'score_pva.sas7bdat' for scoring/predictions (no target)")
print("=" * 80)
