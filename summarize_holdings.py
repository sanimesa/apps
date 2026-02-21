import csv

mapping = {
    "1893 JP": "Penta-Ocean Construction (Japan) - Marine engineering and construction.",
    "5706 JP": "Mitsui Mining & Smelting (Japan) - Non-ferrous metal smelting and processing.",
    "5831 JP": "Shizuoka Financial Group (Japan) - Regional banking services.",
    "1803 JP": "Shimizu Corporation (Japan) - General construction and architecture.",
    "8002 JP": "Marubeni Corporation (Japan) - Diversified general trading (Sogo Shosha).",
    "9532 JP": "Osaka Gas (Japan) - Natural gas distribution and energy services.",
    "1942 JP": "Kandenko Co. (Japan) - Electrical engineering and facility installation.",
    "1801 JP": "Taisei Corporation (Japan) - Civil engineering and building construction.",
    "1812 JP": "Kajima Corporation (Japan) - Construction, real estate, and civil engineering.",
    "5713 JP": "Sumitomo Metal Mining (Japan) - Mining and refining of gold, nickel, and copper.",
    "4506 JP": "Sumitomo Pharma (Japan) - Pharmaceutical research and manufacturing.",
    "POLI IT": "Poligrafici Editoriale (Italy) - Publishing and media group.",
    "ENR GR": "Siemens Energy (Germany) - Power generation and transmission technology.",
    "TIGO": "Millicom International (US/Global) - Telecommunications services in Latin America.",
    "8267 JP": "Aeon Co. (Japan) - Retail giant operating supermarkets and malls.",
    "LUMI IT": "Lumi (Israel/Italy?) - Likely Bank Leumi (LUMI IT refers to Borsa Italiana listing).",
    "3563 JP": "Food & Life Companies (Japan) - Operator of conveyor-belt sushi restaurants (Sushiro).",
    "NN NA": "NN Group (Netherlands) - Insurance and asset management.",
    "BAYN GR": "Bayer AG (Germany) - Pharmaceutical and life sciences company.",
    "HOT GR": "Hochtief AG (Germany) - Global construction and infrastructure services.",
    "EVN AU": "Evolution Mining (Australia) - Gold mining and exploration.",
    "PST IM": "Poste Italiane (Italy) - National postal and financial services.",
    "NST AU": "Northern Star Resources (Australia) - Gold producer.",
    "NDA GR": "Nordex SE (Germany) - Wind turbine manufacturer.",
    "LYC AU": "Lynas Rare Earths (Australia) - Rare earth elements producer.",
    "RRL AU": "Regis Resources (Australia) - Gold mining.",
    "BPE IM": "BPER Banca (Italy) - Commercial banking group.",
    "JUN3 GR": "Jungheinrich AG (Germany) - Material handling equipment and forklifts.",
    "EDV CN": "Endeavour Mining (Canada/Global) - West African gold producer.",
    "SAB SM": "Banco Sabadell (Spain) - Banking and financial services.",
    "WRT1V FH": "Wartsila Oyj (Finland) - Marine and energy power solutions.",
    "INGA NA": "ING Groep (Netherlands) - Global banking and financial services.",
    "TSEM IT": "Tower Semiconductor (Israel/Italy) - Specialty foundry for semiconductors.",
    "RWE GR": "RWE AG (Germany) - Electric utilities and renewable energy.",
    "BKT SM": "Bankinter (Spain) - Retail and commercial bank.",
    "CABK SM": "CaixaBank (Spain) - Leading retail bank in Spain.",
    "BOL SS": "Boliden AB (Sweden) - Mining and smelting of base and precious metals.",
    "LDO IM": "Leonardo SpA (Italy) - Aerospace, defense, and security.",
    "BCP PL": "Bank Millennium (Poland) - Commercial bank.",
    "ESLT IT": "Elbit Systems (Israel/Italy) - International defense electronics company.",
    "RMS AU": "Ramelius Resources (Australia) - Gold mining.",
    "VAU AU": "Virgin Australia? Likely Vicinity Centres or similar if AU. VAU is often Ramelius/Evolution context.",
    "IDR SM": "Indra Sistemas (Spain) - Information technology and defense systems.",
    "TKA GR": "thyssenkrupp AG (Germany) - Industrial engineering and steel production.",
    "CBK GR": "Commerzbank AG (Germany) - Major German banking institution.",
    "GLE FP": "Societe Generale (France) - Global financial services and investment bank.",
    "DBK GR": "Deutsche Bank (Germany) - Global investment bank and financial services.",
    "SAABB SS": "Saab AB (Sweden) - Aerospace and defense company.",
    "HOLN SW": "Holcim AG (Switzerland) - Building materials (cement, aggregates).",
    "GMD AU": "Genesis Minerals (Australia) - Gold exploration and development."
}

with open('IMOM Holdings.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        ticker = row['Ticker']
        desc = mapping.get(ticker, "No description available.")
        print(f"**{ticker}**: {desc}")

