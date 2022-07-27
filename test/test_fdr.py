import sys
import DataReader as fdr

# import FinanceDataReader as fdr
import requests
import pandas as pd
from io import StringIO


df = fdr.DataReader('tsla', '2022')
# # df = fdr.StockListing('NASDAQ') # 상장종목 리스팅
print(df)