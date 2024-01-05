
# 7) Συμπλήρωση φύλλου Ελέγχων path
df5 = pd.DataFrame()
df5['Επώνυμο'] = df3['Αντίδικος'].apply(lambda x : str(x).split(" ")[0])
df5['Επώνυμο_φακέλου'] = df1['Φάκελος'].apply(lambda x: os.path.basename(str(x)).split(" ")[0])
antidikos_filled = df3['Αντίδικος_1'].apply(lambda x : x.replace("-","1  2"))
df5['Επώνυμο_αγωγής'] = antidikos_filled.apply(lambda x : str(x).split(" ")[1])
df5['Έλεγχος_φακέλου']=  np.where(df5['Επώνυμο'] == df5['Επώνυμο_φακέλου']," ","Error")
df5['Έλεγχος_αγωγής'] = np.where(df5['Επώνυμο'] == df5['Επώνυμο_αγωγής']," ","Error")