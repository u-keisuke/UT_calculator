import json
import sys
import numpy as np
import pandas as pd
from collections import defaultdict
import time

from main import main


def remover(remove_file_path, db_file_path):
    #databaseの読み込み
    try:
        with open(db_file_path, 'r') as f:
            database = json.load(f)
    except:
        print('Error: cannot find database file.')
        return 0
    #removedファイルの読み込み
    try:
        with open(remove_file_path, 'r') as f:
            removed_id = json.load(f)["removed_id"]
    except:
        print('Error: cannot find remover file.')
        return 0
    
    existing_id = database.keys()
    for user_id in removed_id:
        if user_id in existing_id:
            del database[user_id]
            print('Completed: deleted data: '+user_id)
        else:
            print('Warning: designated user cannot be found: '+user_id)
    
    #一旦データベースに書き込む
    with open(db_file_path, 'w') as f:
        json.dump(database, f, indent=4, ensure_ascii=False)
    
    #順位を更新するために、空のjsonファイルを作り、それをmain.pyにinputとして渡す。そのときに同時にデータベースファイルも更新される。
    cache_file_path = './cache/cache.json'
    with open(cache_file_path, 'w') as f:
        json.dump({}, f, indent=4, ensure_ascii=False)
    main(cache_file_path, db_file_path)
    

        
#get cl arguments
if __name__ == '__main__':
    args = sys.argv
    remove_file_path = "removed_id.json"
    db_file_path = "database.json"
    #デフォルトの値を設定
    if 1 <= len(args):
        remove_file_path = sys.argv[1]
        db_file_path = sys.argv[2]
        remover(remove_file_path,db_file_path)
        print("done")
    else:
        print('Arguments are too short')
