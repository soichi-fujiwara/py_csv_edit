######################################################################
# Pythonコマンド 引数受け取り
######################################################################
import argparse

# ==========================================================
# コマンド引数の解析
# ==========================================================
parser = argparse.ArgumentParser()
parser.add_argument('--path', help='参照ディレクトリ', required=True)
parser.add_argument('--fname', help='ファイル名', required=True)
parsed, extra = parser.parse_known_args()

_path = parsed.path
_fname = parsed.fname

