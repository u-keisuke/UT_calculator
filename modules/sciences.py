from .by_category import by_category

def sciences(r, x_dict):
    weight_dict = {}
    
    for category in x_dict.keys():
        weight_dict[category] = {}

        #'A'の時は'A~D'について考える
        if category=='Ａ（思想・芸術）':
            abcd_array = by_category([x_dict['Ａ（思想・芸術）'], x_dict['Ｂ（国際・地域）'], x_dict['Ｃ（社会・制度）'], x_dict['Ｄ（人間・環境）']].copy(), 2, r['A,B,C,D'])
            weight_dict['Ａ（思想・芸術）'] = abcd_array[0]
            weight_dict['Ｂ（国際・地域）'] = abcd_array[1]
            weight_dict['Ｃ（社会・制度）'] = abcd_array[2]
            weight_dict['Ｄ（人間・環境）'] = abcd_array[3]
        elif category in ['Ｂ（国際・地域）','Ｃ（社会・制度）','Ｄ（人間・環境）']:
            pass
        
        #'E'の時は'E,F'について考える
        elif category=='Ｅ（物質・生命）':
            ef_array = by_category([x_dict['Ｅ（物質・生命）'], x_dict['Ｆ（数理・情報）']].copy(), 2, r['E,F'])
            weight_dict['Ｅ（物質・生命）'] = ef_array[0]
            weight_dict['Ｆ（数理・情報）'] = ef_array[1]
        elif category=='Ｆ（数理・情報）':
            pass
        
        #L系列
        elif category=='Ｌ（言語・コミュニケーション）':
            weight_dict[category] = by_category([x_dict[category]].copy(), 1, r['L'])[0]

        
        #requirementsにないも科目はパス
        elif category not in r.keys():
            pass
        else:
            weight_dict[category] = by_category([x_dict[category]].copy(), 1, r[category])[0]
    
    return weight_dict