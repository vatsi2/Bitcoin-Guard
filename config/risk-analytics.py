# risk_management/portfolio_analyzer.py

def calculate_rwa_exposure(portfolio: pd.DataFrame) -> RiskReport:
    """
    Analysis of RWA concentration in the portfolio (>20% = High Risk
    """
    rwa_assets = fetch_rwa_list(OndoFinance.API)
    portfolio['is_rwa'] = portfolio['asset'].isin(rwa_assets)
    
    exposure = portfolio[portfolio['is_rwa']]['value_usd'].sum() / portfolio['value_usd'].sum()
    
    return RiskReport(
        rwa_exposure=exposure,
        recommendation="Hedge via Mirror Protocol" if exposure > 0.2 else None
    )

def auto_hedge(portfolio: pd.DataFrame, threshold: float = 0.2):
    """
    Automatic hedging through derivatives
    """
    report = calculate_rwa_exposure(portfolio)
    
    if report.rwa_exposure > threshold:
        hedge_amount = (report.rwa_exposure - threshold) * portfolio.value_usd.sum()
        DerivatveEngine.execute_short(
            asset="RWA_INDEX",
            amount=hedge_amount,
            expiry="30d",
            platform=MirrorProtocol
        )
