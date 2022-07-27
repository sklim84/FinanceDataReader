from ecos.data import EcosReader


def test_create_class():
    symbol = '104Y014'  # 예금은행 총수신(평잔)
    reader = EcosReader(symbol, '2021', '2022')
    assert reader != None

def test_read():
    symbol = '104Y014'  # 예금은행 총수신(평잔)
    reader = EcosReader(symbol, '2021', '2022')
    df = reader.read()
    print(df)
    assert len(df) != 0


# symbol = '104Y014'  # 예금은행 총수신(평잔)
# reader = EcosReader(symbol, '2021', '2022')
# df = reader.read()
# print(df)

# j = requests.post('https://ecos.bok.or.kr/serviceEndpoint/httpService/request.json', payload.encode('utf-8')).json()
# j

# import requests
# import json
# import pandas as pd
#
# api_key = 'QKDE3D49GGBIS42GAACH'
#
# statcode = '901Y009'
# freq, start, end, item = 'M', '200001', '202207', '0'
#
# #url = f'http://ecos.bok.or.kr/api/StatisticSearch/{api_key}/json/kr/1/10000/{statcode}/{freq}/{start}/{end}/{item}'
# url = f'http://ecos.bok.or.kr/api/StatisticTableList/{api_key}/json/kr/1/10000'
#
# r = requests.get(url)
# jo = json.loads(r.text)
# result_table = pd.json_normalize(jo['StatisticTableList']['row'])
#
# statcode = result_table.iloc[47,1]
# freq = result_table.iloc[47,3]
# start, end, item = '201201', '202201', '0'
# url = f'http://ecos.bok.or.kr/api/StatisticSearch/{api_key}/json/kr/1/10000/{statcode}/{freq}/{start}/{end}'
# print(url)
# r = requests.get(url)
# jo = json.loads(r.text)
# result_search = pd.json_normalize(jo['StatisticSearch']['row'])
# print(result_search.columns)
# print(result_search)