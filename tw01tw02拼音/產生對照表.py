
import csv
from 臺灣言語工具.音標系統.閩南語.通用拼音音標 import 通用拼音音標
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


with open('1107通用.txt', 'rt') as txt檔案:
    with open('tw01tw02對照表.csv', 'wt') as csv檔案:
        writer = csv.DictWriter(
            csv檔案, fieldnames=[
                '通用', '臺羅',
            ]
        )
        writer.writeheader()
        for 通用一逝 in txt檔案.readlines():
            通用無調 = 通用一逝.split()[0]
            try:
                臺羅 = 臺灣閩南語羅馬字拼音(
                    通用拼音音標(通用無調 + '1').轉換到臺灣閩南語羅馬字拼音()
                ).音標.rstrip('18')
            except TypeError:
                臺羅 = None
            資料 = {
                '通用': 通用無調,
                '臺羅': 臺羅
            }
            writer.writerow(資料)
