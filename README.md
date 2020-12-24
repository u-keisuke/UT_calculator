# UT_calculator

## description
jsonファイル(input)に格納されたユーザの点数データを、main.pyによって、整形されたデータ(database)へと変換する。
新規、あるいは更新が必要なユーザの点数データだけを入力すれば良い。


## How to use
### ユーザの点数データの、データベースへの追加、更新方法
python main.py input.json database.json

### データベースから特定のユーザのデータを消去する
python remove.py removed_id.json
#### また、ユーザデータを消去すると、順位に変動があるが、それは内部プログラムによって更新される。




## データ記法
### input
refer to input.json file.

### database
refet to database.json file.

### remove
removed_id.json
