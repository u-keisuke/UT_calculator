#series系列の成績上位x単位分の重率をwに変更するということ
def top_grades_series(s_dict, series, credits, w):
    s_dict_name_series = {}
    
    #seriesで指定された系列をs_dict内から抽出したもの
    array = []
    for s in series:
        #辞書要素に、既にあるpoint, credit, weightに加えて、seriesを追加
        for name in s_dict[s].keys():
            s_dict_name_series[name] = s
        array += list(s_dict[s].items())
    array = sorted(array, key=lambda x:x[1]["point"], reverse=True)

    for i in range(len(array)):
        if credits <= 0:
            break
        else:
            #その科目の名前
            name = array[i][0]
            #その科目の系列
            s = s_dict_name_series[name]
            
            credit = array[i][1]["credit"]
            if credit <= credits:
                modified_weight = w
            else:
                modified_weight = float( (credits*w + (credit-credits)*w*0.1) / credit )
                
            s_dict[s][name]["weight"] = modified_weight
            
            #print(name, credit, credits, modified_weight)
            
            credits -= credit
    
    return s_dict


#names内の成績上位x単位分の重率をwに変更するということ
def top_grades_name(s_dict, names, credits, w):
    s_dict_name_series = {}
    
    #seriesで指定された系列をs_dict内から抽出したもの
    array = []
    for s in s_dict.keys():
        #辞書要素に、既にあるpoint, credit, weightに加えて、seriesを追加
        for name in s_dict[s].keys():
            for n in names:
                if name in n:
                    s_dict_name_series[name] = s
                    array += list({name: s_dict[s][name]}.items())
    array = sorted(array, key=lambda x:x[1]["point"], reverse=True)

    for i in range(len(array)):
        if credits <= 0:
            break
        else:
            #その科目の名前
            name = array[i][0]
            #その科目の系列
            s = s_dict_name_series[name]
            
            credit = array[i][1]["credit"]
            if credit <= credits:
                modified_weight = w
            else:
                modified_weight = float( (credits*w + (credit-credits)*w*0.1) / credit )
                
            s_dict[s][name]["weight"] = modified_weight
            
            #print(name, credit, credits, modified_weight)
            
            credits -= credit
    
    return s_dict