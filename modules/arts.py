from .by_category import by_category

def arts_1(r, x_dict):
    weight_dict = {}
    
    for category in x_dict.keys():
        weight_dict[category] = {}

        #'A'の時は'A,B,C'について考える
        if category=='A':
            abcd_array = by_category([x_dict['A'], x_dict['B'], x_dict['C']].copy(), 2, r['A,B,C'], dept='l1')
            weight_dict['A'] = abcd_array[0]
            weight_dict['B'] = abcd_array[1]
            weight_dict['C'] = abcd_array[2]
        elif category in 'BC':
            pass
        
        #'D'の時は'D,E,F'について考える
        elif category=='D':
            def_array = by_category([x_dict['D'], x_dict['E'], x_dict['F']].copy(), 2, r['D,E,F'], dept='l1')
            weight_dict['D'] = def_array[0]
            weight_dict['E'] = def_array[1]
            weight_dict['F'] = def_array[2]
        elif category=='EF':
            pass
        
        #requirementsにないも科目はパス
        elif category not in r.keys():
            pass
        else:
            weight_dict[category] = by_category([x_dict[category]].copy(), 1, r[category], dept='l1')[0]
    
    return weight_dict



def arts_2(r, x_dict):
    weight_dict = {}
    
    for category in x_dict.keys():
        weight_dict[category] = {}

        #'A'の時は'A,B,C'について考える
        if category=='A':
            abcd_array = by_category([x_dict['A'], x_dict['B'], x_dict['C']].copy(), 2, r['A,B,C'], dept='l2')
            weight_dict['A'] = abcd_array[0]
            weight_dict['B'] = abcd_array[1]
            weight_dict['C'] = abcd_array[2]
        elif category in 'BC':
            pass
        
        #'D'の時は'D,E,F'について考える
        elif category=='D':
            def_array = by_category([x_dict['D'], x_dict['E'], x_dict['F']].copy(), 2, r['D,E,F'], dept='l2')
            weight_dict['D'] = def_array[0]
            weight_dict['E'] = def_array[1]
            weight_dict['F'] = def_array[2]
        elif category=='EF':
            pass
        
        #requirementsにないも科目はパス
        elif category not in r.keys():
            pass
        else:
            weight_dict[category] = by_category([x_dict[category]].copy(), 1, r[category], dept='l2')[0]
    
    return weight_dict



def arts_3(r, x_dict):
    weight_dict = {}
    
    humanities = ('哲', '倫', '歴', 'こ', '心')
    socialsciences = ('法', '政', '経', '社', '数')
    
    for category in x_dict.keys():
        weight_dict[category] = {}

        #'L'の時は'L,A,B,C'について考える
        if category=='L':
            abcd_array = by_category([x_dict['A'], x_dict['B'], x_dict['C']].copy(), 3, r['L,A,B,C'], dept='l3')
            weight_dict['L'] = abcd_array[0]
            weight_dict['A'] = abcd_array[1]
            weight_dict['B'] = abcd_array[2]
            weight_dict['C'] = abcd_array[3]
        elif category in 'ABC':
            pass
        
        #'D'の時は'D,E,F'について考える
        elif category=='D':
            def_array = by_category([x_dict['D'], x_dict['E'], x_dict['F']].copy(), 2, r['D,E,F'], dept='l3')
            weight_dict['D'] = def_array[0]
            weight_dict['E'] = def_array[1]
            weight_dict['F'] = def_array[2]
        elif category=='EF':
            pass
        
        elif category=='人文科学':
            humanities_array = [[] for i in range(len(humanities))]
            for x in x_dict[category]:
                #科目名の先頭一文字でどの分野か判別する
                which = humanities.index(x[2][0])
                humanities_array[which].append(x)
            weight_dict['人文科学'] = by_category(humanities_array.copy(), 2, r['人文科学'], dept='l3')
            
        elif category=='社会科学':
            social_array = [[] for i in range(len(socialsciences))]
            for x in x_dict[category]:
                #科目名の先頭一文字でどの分野か判別する
                which = socialsciences.index(x[2][0])
                social_array[which].append(x)
            weight_dict['社会科学'] = by_category(social_array.copy(), 2, r['社会科学'], dept='l3')
        
        #requirementsにないも科目はパス
        elif category not in r.keys():
            pass
        else:
            weight_dict[category] = by_category([x_dict[category]].copy(), 1, r[category], dept='l3')[0]
    
    return weight_dict