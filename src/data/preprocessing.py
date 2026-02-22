def clean_data(df):
    # Handle missing values
    df = df.dropna()
    return df

def format_text_columns(df, columns):
    for column in columns:
        df[column] = df[column].str.lower().str.strip()
    return df

def preprocess_data(df):
    df = clean_data(df)
    text_columns = ['title', 'overview', 'genres', 'keywords']
    df = format_text_columns(df, text_columns)
    return df