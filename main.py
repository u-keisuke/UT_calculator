import json
import sys
import numpy as np
import pandas as pd
from collections import defaultdict
import time

from modules.sciences import sciences
from modules.arts import arts_1, arts_2, arts_3
from modules.avg_calc import avgs
from modules.faculty_calc import f_calc, f_calc_user, rank_decision
from modules.weight.special_weight import w_adjuster_series


#JSONへのコンバータ
def myconverter(obj):
    if isinstance(obj, np.integer):
        return int(obj)
    elif isinstance(obj, np.floating):
        return float(obj)
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, datetime.datetime):
        return obj.__str__()


def main(input_file_path, db_file_path):
    #データ読み込み
    df_class = pd.read_csv('./static_data/class_list.csv')
    df_faculty = pd.read_csv('./static_data/faculty_course_list.csv')
    senior_faculty_list = list(df_faculty["id"])
    #df_classの一部の要素を統一
    df_class = df_class.replace(['人文科学ゼミナール', '自然科学ゼミナール', '社会科学ゼミナール'], '展開科目').replace(['全学自由研究ゼミナール', '全学体験ゼミナール', '学術フロンティア講義', '国際研修'], '主題科目')
    #category_subの一覧
    category_list = df_class['category_sub'].unique()
    
    #データ読み込み
    #input
    try:
        with open(input_file_path, 'r') as f:
            json_load = json.load(f)
    except:
        print('Error: cannot find input file.')
        return 0
    #database
    try:
        with open(db_file_path, 'r') as f:
            database = json.load(f)
    except:
        print('Error: cannot find database file.')
        return 0
    #requirements
    try:
        with open('./static_data/requirements.json', 'r') as f:
            json_load2 = json.load(f)
    except:
        print('Error: cannot find requirements.json')
        return 0
    
    d_new = defaultdict(lambda: defaultdict(dict))
    #進振り先別の平均点、偏差など
    dict_faculty = defaultdict(list)
    
    begi = time.time()
    
    for user_id, user_data in json_load.items(): 
        #ユーザの学年
        user_grade = int(user_data['grade'])
        #ユーザの科類
        user_type = user_data['type']
        #ユーザの点数一覧
        points = user_data['points']
        #ユーザの希望進学先
        senior_faculty_dict = {}
        for i in range(1,4):
            try:
                senior_faculty_dict['senior_faculty_{}'.format(i)] = int(user_data['senior_faculty_{}'.format(i)])
            except:
                raise ValueError("The senior_faculty of an user does not exist.")
        
        for s, senior_faculty in senior_faculty_dict.items():
            #前期課程修了要件
            requirements = json_load2[user_type]

            subjects = {}
            for key in category_list:
                if key != "その他":
                    subjects[key] = []

            for num, point in points.items():
                #科目id
                num = int(num)
                #単位数
                credit = df_class['credit'][df_class['id']==num].values[0]
                #サブカテゴリー
                category_sub = df_class['category_sub'][df_class['id']==num].values[0]
                #科目名
                name = df_class['name'][df_class['id']==num].values[0]
                subjects[category_sub].append((point, credit, name))

            #各カテゴリーで点数の低い順にsort
            for category in subjects.values():
                category.sort()


            if user_type[0] == 's':
                dict_subjects = sciences(r=requirements.copy(), x_dict=subjects.copy())
            elif user_type == 'l1':
                dict_subjects = arts_1(r=requirements.copy(), x_dict=subjects.copy())
            elif user_type == 'l2':
                dict_subjects = arts_2(r=requirements.copy(), x_dict=subjects.copy())
            elif user_type == 'l3':
                dict_subjects = arts_3(r=requirements.copy(), x_dict=subjects.copy())
            else:
                print("Error: The user-type key is invalid.")
            
            #学年を登録
            d_new[user_id]["grade"] = user_grade
            #学科ごとの特殊性を反映する前に基本平均点を計算
            averages = avgs(dict_subjects)
            d_new[user_id]["base_avg"] = averages["base_avg"]

            #学科ごとの重率の特殊性を反映
            dict_subjects = w_adjuster_series(dict_subjects, senior_faculty, user_type)
            
            d_new[user_id][s]["faculty_num"] = senior_faculty_dict[s]
            d_new[user_id][s]["subjects"] = dict_subjects
            averages = avgs(dict_subjects)
            #工学部なら工学部平均点
            if senior_faculty//100==3:
                d_new[user_id][s]["average"] = averages["eng_avg"]
            #農学部なら農学部平均点
            elif senior_faculty//100==6:
                d_new[user_id][s]["average"] = averages["agr_avg"]
            #その他は基本平均点
            else:
                d_new[user_id][s]["average"] = averages["base_avg"]
            
    
    #志望学科の平均点、STDの計算
    f_data = f_calc(dict_faculty)
    
    #各ユーザの志望学科での平均点、DeviationScoreを計算
    #d_new = f_calc_user(d_new, f_data)
    
    end = time.time()
    print('Time: {}'.format(end-begi))
    
    for key, value in d_new.items():
        database[key] = value
        
    database = rank_decision(database)
    
    #データベースに書き込み
    with open(db_file_path, 'w') as f:
        json.dump(database, f, indent=4, ensure_ascii=False, default=myconverter)


#get cl arguments
if __name__ == '__main__':
    args = sys.argv
    #デフォルトの値を設定
    input_file_path = "input.json"
    db_file_path = "database.json"
    
    if 2 <= len(args):
        input_file_path = sys.argv[1]
        db_file_path = sys.argv[2]
        main(input_file_path, db_file_path)
        print("done")
    else:
        print('Arguments are too short')
