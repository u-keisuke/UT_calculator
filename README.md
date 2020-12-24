# UT_calculator

## description
jsonファイル(input)に格納されたユーザの点数データを、main.pyによって、整形されたデータ(database)へと変換する。
新規、あるいは更新が必要なユーザの点数データだけを入力すれば良い。


## How to use
### Upadating the score database.
python main.py input.json database.json

### Removing an user from the score database.
python remove.py removed_id.json



## データ記法
### input
refer to input.json file.

### database
refet to database.json file.

### remove
removed_id.json
