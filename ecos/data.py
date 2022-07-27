import json

import pandas as pd
import requests
from FinanceDataReader._utils import _validate_dates


class EcosReader:
    def __init__(self, symbol, start=None, end=None):

        # TODO symbol : stat code, item code

        self.symbol = symbol
        start, end = _validate_dates(start, end)
        self.start = start
        self.end = end

    def read(self):
        api_key = 'QKDE3D49GGBIS42GAACH'

        stat_code = self.symbol

        # 통계 세부항목 조회 : 주기(cycle) 획득
        url_stat_item = f'http://ecos.bok.or.kr/api/StatisticItemList/{api_key}/json/kr/1/1/{stat_code}'
        resp_stat_item = requests.get(url_stat_item)
        json_stat_item = json.loads(resp_stat_item.text)
        # TODO http response error handling
        cycle = json_stat_item['StatisticItemList']['row'][0]['CYCLE']
        # item_code = json_stat_item['StatisticItemList']['row'][0]['ITEM_CODE']

        # 주기별 조희기간 형식 변경
        if cycle == 'A':
            time_fmt = "%Y"
        elif cycle == 'M':
            time_fmt = "%Y%m"
        elif cycle == 'D':
            time_fmt = "%Y%m%d"
        start = self.start.strftime(time_fmt)
        end = self.end.strftime(time_fmt)

        # TODO 주기, 수록시작일자/종료일자 정보로 시간(start/end) 유효성 검증

        # 통계 조회
        url_stat_srch = f'http://ecos.bok.or.kr/api/StatisticSearch/{api_key}/json/kr/1/10000/{stat_code}/{cycle}/{start}/{end}'
        resp_stat_srch = requests.get(url_stat_srch)
        json_stat_srch = json.loads(resp_stat_srch.text)
        res_stat_srch = pd.json_normalize(json_stat_srch['StatisticSearch']['row'])

        # 단위, 시점, 값 column 선택
        res_stat_srch = res_stat_srch[['UNIT_NAME', 'TIME', 'DATA_VALUE']]
        # 정규화 : column 이름, date 형식
        col_map = {'UNIT_NAME': 'Unit', 'TIME': 'Date', 'DATA_VALUE': 'Value'}
        res_stat_srch = res_stat_srch.rename(columns=col_map)

        return res_stat_srch

if __name__ == "__main__":
    symbol = '104Y014'  # 예금은행 총수신(평잔)
    reader = EcosReader(symbol, '2021', '2022')
    df = reader.read()
    print(df)
