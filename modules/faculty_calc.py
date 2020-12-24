import numpy as np
from collections import defaultdict


def f_calc(s_dict):
    f_data_dict = {}
    
    for senior_faculty, array in s_dict.items():
        array = np.array(array)
        f_data_dict[senior_faculty]={}
        f_data_dict[senior_faculty]["average"] = array.mean()
        f_data_dict[senior_faculty]["std"] = array.std()
    
    return f_data_dict

#各ユーザの志望学科での平均点、DeviationScoreを計算
def f_calc_user(d_new, f_data):
    for user_id, user_data in d_new.items():
        senior_faculty = int(user_data['senior_faculty'])
        f_avg = f_data[senior_faculty]["average"]
        f_std = f_data[senior_faculty]["std"]
        if f_std < 0.0001:
            dscore = 50.0
        elif senior_faculty//100==3:
            dscore = 50 + (d_new[user_id]["avgs"]["eng_avg"] - f_avg) / f_std
        #農学部なら農学部平均点
        elif senior_faculty//100==6:
            dscore = 50 + (d_new[user_id]["avgs"]["agr_avg"] - f_avg) / f_std
        #その他は基本平均点
        else:
            dscore = 50 + (d_new[user_id]["avgs"]["base_avg"] - f_avg) / f_std
        d_new[user_id]["deviation_score"] = dscore
    
    return d_new

#第一志望学科の学科内での順位を出す
def rank_decision(database):
    grade_faculty_dict = defaultdict(lambda: defaultdict(list))
    #grade_faculty_dict['1'] = defaultdict(list)
    #grade_faculty_dict['2'] = defaultdict(list)
    for user_id, data in database.items():
        grade = data["grade"]
        num = data["senior_faculty_1"]["faculty_num"]
        avg = data["senior_faculty_1"]["average"]
        grade_faculty_dict[str(grade)][num].append((avg,user_id))
        
    #sort + rank_decision
    for g in grade_faculty_dict.keys():
        for n in grade_faculty_dict[g].keys():
            array = sorted(grade_faculty_dict[g][n], reverse=True)
            for i in range(len(array)):
                avg,user_id = array[i]
                database[user_id]["senior_faculty_1"]["rank"] = i+1
    
    return database
            
    
    
    