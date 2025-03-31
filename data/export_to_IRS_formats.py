def irs_form_8949(transactions):
    return pd.DataFrame({
        'Description': transactions['asset'],
        'Gain/Loss': transactions['taxable_gain']
    })
