

# Mapping επωνύμου δικηγόρων με ονοματεπώνυμο δικηγόρων
mapping_dikigoron_full_names ={}
mapping_dikigoron_full_names_keys = dikigoroi_df.iloc[:,2]
mapping_dikigoron_full_names_values = dikigoroi_df.iloc[:,0]
mapping_dikigoron_full_names = dict(zip(mapping_dikigoron_full_names_keys, mapping_dikigoron_full_names_values))
anathesi_df['ΔΙΚΗΓΟΡΟΣ_full'] = anathesi_df['Υπογράφων Δικηγόρος Ένορκης'].map(mapping_dikigoron_full_names)
