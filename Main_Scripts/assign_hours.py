import numpy as np
import pandas as pd
from Data.Lists.config import hours

def assign_hours(anathesi_df):
    # Initialize 'hours' column with NaN values if it doesn't exist
    if 'hours' not in anathesi_df.columns:
        anathesi_df['hours'] = np.nan
        
    # Assign hours based on unique groups
    hour_assignments = {}
    hour_index = 0

    for name in anathesi_df['Ονοματεπώνυμο_Δικηγόρου'].unique():
        if hour_index < len(hours):
            hour_assignments[name] = hours[hour_index]
            hour_index += 1
        else:
            hour_assignments[name] = np.nan  # No more hours to assign

    # Map assigned hours to the dataframe
    anathesi_df['hours'] = anathesi_df['Ονοματεπώνυμο_Δικηγόρου'].map(hour_assignments)
    
    return anathesi_df
