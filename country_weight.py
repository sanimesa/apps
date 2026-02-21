import csv
from collections import defaultdict

# Map suffixes/tickers to countries
country_map = {
    "JP": "Japan",
    "GR": "Germany",
    "IT": "Italy",
    "IM": "Italy",
    "AU": "Australia",
    "SM": "Spain",
    "NA": "Netherlands",
    "FH": "Finland",
    "PL": "Poland",
    "SW": "Switzerland",
    "SS": "Sweden",
    "FP": "France",
    "CN": "Canada",
    "TIGO": "Luxembourg/Global", # Millicom
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
        
        # Determine country from ticker
        parts = ticker.split()
        if len(parts) > 1:
            suffix = parts[-1]
            country = country_map.get(suffix, "Other/Unknown")
        elif "SS" in ticker: # Handle SAABB SS style
             country = "Sweden"
        elif ticker == "TIGO":
            country = "Luxembourg/Global"
        elif ticker in ["EUR", "Cash&Other", "FGXXX"]:
            country = "Cash/Other"
        else:
            country = "Other/Unknown"
            
        weights[country] += value

# Sort by weight descending
sorted_weights = sorted(weights.items(), key=lambda x: x[1], reverse=True)

print(f"{'Country':<20} | {'Value ($mm)':<15} | {'Weight (%)':<10}")
print("-" * 50)
for country, value in sorted_weights:
    percentage = (value / total_value) * 100 if total_value > 0 else 0
    print(f"{country:<20} | {value:<15.2f} | {percentage:<10.2f}")

