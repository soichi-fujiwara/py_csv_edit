######################################################################
# 項目追加
######################################################################
import pandas as pd
import gzip
import os

csv_base_path = os.path.dirname(__file__)

csv_in_path = csv_base_path + "/加工前/xxxxxxxxxxxxxx.csv.gz"
csv_out_path = csv_base_path + "/加工後/xxxxxxxxxxxxxx.csv"

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

    # 追加項目
    new_col_dict = {
        'add_col1':'00',
        'add_col2':'01',
        'add_col3':'02',
    }

    # 項目追加
    for val in new_col_dict:
        wk_list.append(new_col_dict[val])

    edit_list.append(wk_list)

################################################################################
# ソートを行う
################################################################################
# ソートしたい項目は1項目目なのでindexは0を指定
sort_col_idx1 = 0
# ソートしたい項目は6項目目なのでindexは5を指定
sort_col_idx2 = 5

df = pd.DataFrame(edit_list)
# ソート
df_s = df.sort_values([sort_col_idx1,sort_col2_idx],ascending=[True,True])

fix_list = []

for _l in df_s.values.tolist():
    # 加工済みデータを格納
    fix_list.append(_l)

# 加工済みCSV保存
df_fix = pd.DataFrame(fix_list)
df_fix.to_csv(csv_out_path,header=None,index=None)

print("完了")