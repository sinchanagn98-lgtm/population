def total_population(df):
    return int(df["Population"].max())

def avg_fertility(df):
    return round(df["Fertility Rate"].mean(), 2)

def max_density(df):
    return int(df["Density (P/Km²)"].max())

def urban_population(df):
    return int(df["Urban Population"].max())
