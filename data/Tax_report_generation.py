def generate_tax_report(user, method='HIFO'):
    transactions = load_transactions(user)
    report = TaxReport(transactions, method=method)
    report.export_pdf(f'{user}_tax_2024.pdf')
