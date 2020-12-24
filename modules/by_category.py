#num_categories数の系列にわたって、credits数の単位を取得するということ
def by_category(array, num_categories, credits, dept='s'):
    #重みを付けて返すためのリスト
    w_array = [{} for a in array]
    
    for a in array:
        for i in range(1, 50):
            a.append((-i, 10000, '空欄埋め'))
        a.sort()
    
    #最初のnum_categories分だけは各系列から一つずつとる
    #それぞれの系列の最も高い点数の科目
    highs = [a[-1][0] for a in array]
    #昇順にsort
    highs_sorted = sorted(highs)
    #highsの中でも高いものを順にpopout
    for i in range(num_categories):
        index = highs.index(highs_sorted.pop())
        subject = array[index].pop()
        
        #もしsubject[0]==-1でもcreditsは減らしておく
        if subject[0]==-1:
            #pass
            credits -= 2
        else:
            point = subject[0]
            credit = subject[1]
            name = subject[2]
            credits -= credit
            w_array[index][name] = {'point': point, 'credit': credit, 'weight': 1}

    while True:
        #それぞれの系列の最も高い点数の科目
        highs = [a[-1][0] for a in array]

        #終了条件(全ての系列の最高値が-1になったら)
        if highs==[-2 for a in array]:
            break
            
        #highsの中でも最も高いもののインデックス
        index = max(enumerate(highs), key = lambda x:x[1])[0]
        #それをpop outする
        subject = array[index].pop()
        #もし-1なら「空欄埋め」なのでパス
        if subject[0]==-1:
            pass
        else:
            point = subject[0]
            credit = subject[1]
            name = subject[2]
            
            #当科目の単位数が残りの枠に収まっていたら
            if credit <= credits:
                w_array[index][name] = {'point': point, 'credit': credit, 'weight': 1}
                credits -= credit
            elif credit > credits:
                w_array[index][name] = {'point': point, 'credit': credit, 'weight': int( (credits*1 + (credit-credits)*0.1)/credit )}
                credits = 0
    
    return w_array