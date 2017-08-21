from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音聲母表
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音通行韻母表
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.音標系統.閩南語綜合標音 import 閩南語綜合標音
import csv


with open('對照表.csv', 'wt') as 檔案:
    writer = csv.DictWriter(
        檔案, fieldnames=[
            'IPA', '吳守禮方音', '臺羅數字調', '臺羅正式調', '通用數字調'
        ]
    )
    writer.writeheader()
    for 聲 in sorted(臺灣閩南語羅馬字拼音聲母表):
        for 韻 in sorted(臺灣閩南語羅馬字拼音通行韻母表):
            if (
                韻.endswith('p') or
                韻.endswith('t') or
                韻.endswith('k') or
                韻.endswith('h')
            ):
                調號 = [4, 8]
            else:
                調號 = [1, 2, 3, 5, 7]
            for 調 in 調號:
                音節 = '{}{}{}'.format(聲, 韻, 調)
                拼音 = 臺灣閩南語羅馬字拼音(音節)
                if 拼音.音標 is not None:
                    資料 = 閩南語綜合標音(拆文分析器.對齊字物件(音節, 音節)).轉json格式()[0]
                    資料.pop('漢字')
                    資料['臺羅正式調'] = 資料.pop('臺羅閏號調')
                    資料['IPA'] = ''.join(拼音.音值())
                    writer.writerow(資料)
