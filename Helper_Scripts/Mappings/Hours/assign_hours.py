
# Initialize 'hours' column with NaN values if it doesn't exist yet
if 'hours' not in anathesi_df.columns:
    anathesi_df['hours'] = pd.Series(np.nan, index=anathesi_df.index)

# Create a boolean mask where the current 'ΔΙΚΗΓΟΡΟΣ_full' is not equal to the previous one
mask = (anathesi_df['ΔΙΚΗΓΟΡΟΣ_full'] != anathesi_df['ΔΙΚΗΓΟΡΟΣ_full'].shift(1)) | (anathesi_df.index == 0)

# Expand the hours list based on where the changes occur in ΔΙΚΗΓΟΡΟΣ_full
hour_index = 0
# Replace NaN with 'Unknown'
anathesi_df['ΔΙΚΗΓΟΡΟΣ_full'].fillna('Unknown', inplace=True)

for i in range(len(anathesi_df)):
    # Check if we have available hours left
    if hour_index >= len(hours):
        print("Warning: Ran out of hours!")
        break
    
    # If the name changes or it's the first row, fetch the next available hour
    if i == 0 or anathesi_df['ΔΙΚΗΓΟΡΟΣ_full'].iloc[i] != anathesi_df['ΔΙΚΗΓΟΡΟΣ_full'].iloc[i-1]:
        anathesi_df.at[i, 'hours'] = hours[hour_index]
        hour_index += 1
    else:
        # Otherwise, copy the hour from the previous row
        anathesi_df.at[i, 'hours'] = anathesi_df['hours'].iloc[i-1]

# Optional: replace 'Unknown' with NaN if you want to revert the changes

hours_col = anathesi_df['hours']
