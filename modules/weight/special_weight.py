from .top_grades import top_grades_series, top_grades_name

def w_adjuster_series(s_dict, faculty, user_type):
    if faculty == 801:
        s_dict = top_grades_series(s_dict, ["既修外国語"], 4, 1.5)
        s_dict = top_grades_series(s_dict, ["初修外国語"], 4, 1.5)
                            
    elif faculty == 802:
        s_dict = top_grades_series(s_dict, ["社会科学"], 8, 2)
        s_dict = top_grades_name(s_dict, ["現代哲学", "思想史", "科学史", "国際関係論", "歴史世界論", "法と社会", "現代社会論", "相関社会科学", "経済と社会", "統計学"], 8, 2)
    
    elif faculty == 803:
        #理科全類の時
        if 's' in user_type:
            s_dict = top_grades_series(s_dict, ["情報", "物質科学", "数理科学", "生命科学", "基礎実験"], 8, 1.5)
    
    elif faculty == 804:
        s_dict = top_grades_name(s_dict, ["振動・波動論", "解析力学", "相対論", "量子論", "統計物理学", "有機反応科学", "化学平衡と反応速度", "分子システムの化学", "現代生命科学Ⅰ（文科生、理一生）", "現代生命科学Ⅱ（文科生、理一生）", "自然現象とモデル", "生物物理学"], 8, 2)

    elif faculty == 805:
        s_dict = top_grades_name(s_dict, ["力学A", "力学B", "熱力学", "化学熱力学", "物性化学", "生命科学", "生命科学Ⅰ", "生命科学Ⅱ", "振動・波動論", "有機反応科学", "化学平衡と反応速度", "動物科学", "植物科学", "現代生命科学Ⅰ（文科生、理一生）", "現代生命科学Ⅱ（文科生、理一生）", "生物物理学"], 8, 1.5)
    
    elif faculty == 809:
        s_dict = top_grades_series(s_dict, ["既修外国語"], 1000, 2)
    
    elif faculty//100 == 3 and not faculty in [304, 305, 319]:
        s_dict = top_grades_name(s_dict, ["初年次ゼミナール文科"], 2, 0)
        
    #elif faculty == 313:
    
    #elif faculty == 319:
    
    elif faculty//100 == 5 and not faculty in [504, 507] and user_type[0]=='l':
        s_dict = top_grades_series(s_dict, ["情報", "物質科学", "数理科学", "生命科学", "基礎実験"], 1000, 1)

    elif faculty == 504:
        s_dict = top_grades_name(s_dict, ["数理科学基礎", "微分積分学①", "微分積分学②" "線型代数学①", "線型代数学②", "力学", "電磁気学", "熱力学", "化学熱力学"], 14, 2)
    
    elif faculty == 507 and user_type[0]=='s':
        s_dict = top_grades_series(s_dict, ["Ｅ（物質・生命）", "Ｆ（数理・情報）"], 6, 2)
        s_dict = top_grades_series(s_dict, ["Ｌ（言語・コミュニケーション）", "Ａ（思想・芸術）", "Ｂ（国際・地域）", "Ｃ（社会・制度）", "Ｄ（人間・環境）", "Ｅ（物質・生命）", "Ｆ（数理・情報）"], 6, 2)
    
    return s_dict