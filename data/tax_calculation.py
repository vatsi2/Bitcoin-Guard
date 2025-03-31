import pandas as pd

def calculate_hifo(transactions):
    df = pd.DataFrame(transactions)
    df = df.sort_values('price', ascending=False)
    return df.groupby('asset').apply(lambda x: x.iloc[:x['sold_qty'].argmax()])
