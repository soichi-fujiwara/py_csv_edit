######################################################################
# データ加工
# (項目の数は変えずに値を置換)
######################################################################
import pandas as pd
import gzip
import os

csv_base_path = os.path.dirname(__file__)

csv_in_path = csv_base_path + "/加工前/xxxxxxx.gz"
csv_out_path = csv_base_path + "/加工後/xxxxxx.csv"

with gzip.open(csv_in_path, mode='rt', encoding='utf-8') as f:
    data = f.read()

# 改行コードで分割
data_split = data.split('\n')

edit_list = []
for data in data_split:
    wk_list = data.split(',')
    
    # 最終の空行は無視
    if wk_list == ['']:
        break

    edit_list.append(wk_list)

# 加工したい項目のインデックス
edit_idx = 10

df = pd.DataFrame(edit_list)

fix_list = []

for _l in df.values.tolist():
    ################################################################
    # ここで加工
    ################################################################
    _l[edit_idx] = ""
    ################################################################

    # 加工済みデータを格納
    fix_list.append(_l)

# 加工済みCSV保存
df_fix = pd.DataFrame(fix_list)
df_fix.to_csv(csv_out_path,header=None,index=None)

print("完了")