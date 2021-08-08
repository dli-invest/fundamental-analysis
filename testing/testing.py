import yahoo_fin.stock_info as si

aapl_earnings_hist = si.get_earnings_history("vph.cn")
print(aapl_earnings_hist)