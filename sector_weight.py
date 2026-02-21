import csv
from collections import defaultdict

# Sector mapping based on earlier descriptions
sector_map = {
    # Japan
    "1893 JP": "Industrials/Construction",
    "5706 JP": "Materials/Mining",
    "5831 JP": "Financials/Banking",
    "1803 JP": "Industrials/Construction",
    "8002 JP": "Industrials/Trading",
    "9532 JP": "Utilities",
    "1942 JP": "Industrials/Engineering",
    "1801 JP": "Industrials/Construction",
    "1812 JP": "Industrials/Construction",
    "5713 JP": "Materials/Mining",
    "4506 JP": "Healthcare/Pharma",
    "3563 JP": "Consumer Discretionary",
    "8267 JP": "Consumer Staples/Retail",
    
    # Europe
    "ENR GR": "Industrials/Energy",
    "POLI IT": "Communication Services",
    "NN NA": "Financials/Insurance",
    "BAYN GR": "Healthcare/Life Sciences",
    "HOT GR": "Industrials/Construction",
    "PST IM": "Financials/Services",
    "NDA GR": "Industrials/Renewables",
    "BPE IM": "Financials/Banking",
    "JUN3 GR": "Industrials/Equipment",
    "SAB SM": "Financials/Banking",
    "WRT1V FH": "Industrials/Marine & Energy",
    "INGA NA": "Financials/Banking",
    "RWE GR": "Utilities",
    "BKT SM": "Financials/Banking",
    "CABK SM": "Financials/Banking",
    "LDO IM": "Industrials/Aerospace & Defense",
    "BCP PL": "Financials/Banking",
    "IDR SM": "Information Technology",
    "TKA GR": "Industrials/Materials",
    "CBK GR": "Financials/Banking",
    "GLE FP": "Financials/Banking",
    "DBK GR": "Financials/Banking",
    "SAABB SS": "Industrials/Aerospace & Defense",
    "HOLN SW": "Materials",
    
    # Australia / Mining / Others
    "EVN AU": "Materials/Mining",
    "NST AU": "Materials/Mining",
    "LYC AU": "Materials/Mining",
    "RRL AU": "Materials/Mining",
    "EDV CN": "Materials/Mining",
    "BOL SS": "Materials/Mining",
    "RMS AU": "Materials/Mining",
    "VAU AU": "Materials/Mining",
    "GMD AU": "Materials/Mining",
    "TSEM IT": "Information Technology",
    "ESLT IT": "Industrials/Aerospace & Defense",
    "TIGO": "Communication Services",
}

weights = defaultdict(float)
total_value = 0.0

with open('IMOM Holdings.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        ticker = row['Ticker']
        try:
            value = float(row['Market Value ($mm)'])
        except ValueError:
            continue
            
        total_value += value
        
        # Determine sector
        sector = sector_map.get(ticker, "Other/Unknown")
        if ticker in ["EUR", "Cash&Other", "FGXXX"]:
            sector = "Cash/Other"
            
        weights[sector] += value

# Sort by weight descending
sorted_weights = sorted(weights.items(), key=lambda x: x[1], reverse=True)

print(f"{'Sector':<30} | {'Value ($mm)':<15} | {'Weight (%)':<10}")
print("-" * 60)
for sector, value in sorted_weights:
    percentage = (value / total_value) * 100 if total_value > 0 else 0
    print(f"{sector:<30} | {value:<15.2f} | {percentage:<10.2f}")

