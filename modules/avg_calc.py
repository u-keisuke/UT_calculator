import numpy as np

def avgs(s_dict):
    avg_dict = {}
    
    x_base = np.array([])
    w_base = np.array([])
    x_eng = np.array([])
    w_eng = np.array([])
    credit_sum = 0
    
    for category, subject in s_dict.items():
        for data in subject.values():
            x_base = np.append(x_base, data['point'])
            w_base = np.append(w_base, data['weight']*data['credit'])
            x_eng = np.append(x_eng, 0 if data['point']<49 else min((data['point']-45)//5, 10) )
            w_eng = np.append(w_eng, data['weight']*data['credit'])
            credit_sum += data['credit']
    
    avg_dict['base_avg'] = float(np.average(x_base, weights=w_base))
    avg_dict['eng_avg'] = float(np.average(x_eng, weights=w_eng))
    avg_dict['agr_avg'] = avg_dict['base_avg'] * credit_sum
    
    return avg_dict