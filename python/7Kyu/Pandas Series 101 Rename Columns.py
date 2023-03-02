def rename_columns(df, names):  
    df = df.copy()
    for i in range(df.shape[1]): 
        df.rename(columns = {df.columns[i]: names[i]}, inplace = True)
    return df
