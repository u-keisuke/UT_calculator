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
input.json
{
    id: {
        "grade": 進振り年度(数値),
        "type": 科類(s1,s2,s3,l1,l2,or l3),
        "senior_faculty_1": 第1志望学科,
        "senior_faculty_2": 第2志望学科,
        "senior_faculty_3": 第3志望学科,
        "points":{
            "科目No.": 点数 (※ただし、点数のない科目については101(合格)or-1(不合格))（科目NO.は./static_data/class_list.csvを参照）
        }
    }
}
### database
database.json
{
    id: {
        "grade": 進振り年度,
        "base_avg": 基本平均点,
        "senior_faculty_1": {
            "faculty_num": 学科番号,
            "average": 平均点,
            "subjects": {
                系列: {
                    科目id : {
                        "point": 点数, 
                        "credit": 単位数,
                        "weight": 重率
                    }
                }
            }
            "rank": 順位(第1志望学科の時のみ)
        },
        "senior_faculty_2": {
            "faculty_num": 学科番号,
            "average": 平均点,
            "subjects": {
                系列: {
                    科目id : {
                        "point": 点数, 
                        "credit": 単位数,
                        "weight": 重率
                    }
                }
            }
        },
        "senior_faculty_3": {
            "faculty_num": 学科番号,
            "average": 平均点,
            "subjects": {
                系列: {
                    科目id : {
                        "point": 点数, 
                        "credit": 単位数,
                        "weight": 重率
                    }
                }
            }
        }
    }
}
### remove
removed_id.json
{
    removed_id: [
        ユーザid 
    ]
}


#テストデータ
input.json
{   
    "00Vy4f7HHcc0aFExZmeVU7za1tG3":{
        "grade": 2020,
        "type": "s1",
        "senior_faculty_1": "0801",
        "senior_faculty_2": "0802",
        "senior_faculty_3": "0803",
        "points": {
            "30078": 82,
            "30402": 87,
            "50320": 79,
            "30374": 83,
            "30031": 85,
            "30064": 88,
            "50063": 90,
            "30044": 89,
            "30045": 75,
            "50082": 92,
            "60004": 92,
            "30030": 80,
            "50043": 86,
            "30140": 83,
            "40002": 90,
            "50065": 86,
            "40072": 85,
            "50481": 67,
            "40008": 89,
            "50118": 72,
            "50119": 69,
            "30776": 93,
            "50540": 70,
            "30052": 95,
            "50057": 88,
            "30021": 85,
            "30393": 83,
            "30343": 81,
            "31562": 89,
            "30001": 80,
            "50001": 75
        }
    }, 
    "00Vy4f7HHccdfaga465ayg5e634":{
        "grade": 2020,
        "type": "s1",
        "senior_faculty_1": "0801",
        "senior_faculty_2": "0802",
        "senior_faculty_3": "0803",
        "points": {
            "30078": 82,
            "30402": 87,
            "50320": 79,
            "30374": 40,
            "30031": 85,
            "30064": 88,
            "50063": 90,
            "30044": 89,
            "30045": 75,
            "50082": 92,
            "60004": 92,
            "30030": 80,
            "50043": 86,
            "30140": 83,
            "40002": 90,
            "50065": 86,
            "40072": 85,
            "50481": 67,
            "40008": 89,
            "50118": 72,
            "50119": 69,
            "30776": 93,
            "50540": 70,
            "30052": 95,
            "50057": 88,
            "30021": 85,
            "30393": 83,
            "30343": 81,
            "31562": 89,
            "30001": 80,
            "50001": 75
        }
    }
}

database.json
{
    "00Vy4f7HHccdfaga465ayg5e634": {
        "grade": 2020,
        "base_avg": 83.02272727272727,
        "senior_faculty_1": {
            "faculty_num": 801,
            "subjects": {
                "Ｌ（言語・コミュニケーション）": {
                    "英語中級（クラス指定セメスター型）": {
                        "point": 85,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "英語中級（クラス指定ターム型）": {
                        "point": 83,
                        "credit": 1.0,
                        "weight": 1
                    }
                },
                "物質科学": {
                    "熱力学": {
                        "point": 95,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "力学Ａ": {
                        "point": 93,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "構造化学": {
                        "point": 88,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "電磁気学Ａ": {
                        "point": 70,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "数理科学": {
                    "微分積分学①": {
                        "point": 90,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "数学基礎理論演習": {
                        "point": 89,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "微分積分学②": {
                        "point": 86,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "線型代数学①": {
                        "point": 85,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "数理科学基礎演習": {
                        "point": 83,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "数理科学基礎": {
                        "point": 82,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "微分積分学演習": {
                        "point": 72,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "線型代数学演習": {
                        "point": 69,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "線型代数学②": {
                        "point": 67,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "Ｅ（物質・生命）": {},
                "Ｆ（数理・情報）": {},
                "基礎実験": {
                    "基礎実験Ⅱ(物理学)": {
                        "point": 92,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "基礎実験Ⅰ(物理学)": {
                        "point": 92,
                        "credit": 1.0,
                        "weight": 1
                    }
                },
                "生命科学": {},
                "主題科目": {},
                "Ｄ（人間・環境）": {
                    "環境・エネルギー工学基礎Ⅰ": {
                        "point": 89,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "既修外国語": {
                    "英語一列①": {
                        "point": 87,
                        "credit": 1.0,
                        "weight": 1.5
                    },
                    "英語二列Ｗ（ALESA）": {
                        "point": 85,
                        "credit": 2.0,
                        "weight": 1.5
                    },
                    "英語一列②": {
                        "point": 79,
                        "credit": 1.0,
                        "weight": 1.5
                    },
                    "英語二列Ｓ（FLOW）": {
                        "point": 40,
                        "credit": 1.0,
                        "weight": 1
                    }
                },
                "初修外国語": {
                    "スペイン語一列②": {
                        "point": 90,
                        "credit": 2.0,
                        "weight": 1.5
                    },
                    "スペイン語二列": {
                        "point": 89,
                        "credit": 2.0,
                        "weight": 1.5
                    },
                    "スペイン語一列①": {
                        "point": 88,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "Ｂ（国際・地域）": {
                    "現代国際社会論": {
                        "point": 81,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "初年次ゼミナール": {},
                "身体運動・健康科学実習": {
                    "身体運動・健康科学実習Ⅱ": {
                        "point": 86,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "身体運動・健康科学実習Ⅰ": {
                        "point": 80,
                        "credit": 1.0,
                        "weight": 1
                    }
                },
                "Ａ（思想・芸術）": {},
                "Ｃ（社会・制度）": {},
                "数理科学、物質・生命科学": {},
                "情報": {
                    "情報": {
                        "point": 75,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "社会科学": {},
                "人文科学": {},
                "社会科学・人文科学": {},
                "展開科目": {},
                "初年次ゼミナール理科": {},
                "初年次ゼミナール文科": {},
                "身体運動・健康科学実習(PEAK)": {},
                "人文・社会科学ゼミナール": {}
            },
            "average": 83.33333333333333,
            "rank": 2
        },
        "senior_faculty_2": {
            "faculty_num": 802,
            "subjects": {
                "Ｌ（言語・コミュニケーション）": {
                    "英語中級（クラス指定セメスター型）": {
                        "point": 85,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "英語中級（クラス指定ターム型）": {
                        "point": 83,
                        "credit": 1.0,
                        "weight": 1
                    }
                },
                "物質科学": {
                    "熱力学": {
                        "point": 95,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "力学Ａ": {
                        "point": 93,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "構造化学": {
                        "point": 88,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "電磁気学Ａ": {
                        "point": 70,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "数理科学": {
                    "微分積分学①": {
                        "point": 90,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "数学基礎理論演習": {
                        "point": 89,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "微分積分学②": {
                        "point": 86,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "線型代数学①": {
                        "point": 85,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "数理科学基礎演習": {
                        "point": 83,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "数理科学基礎": {
                        "point": 82,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "微分積分学演習": {
                        "point": 72,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "線型代数学演習": {
                        "point": 69,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "線型代数学②": {
                        "point": 67,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "Ｅ（物質・生命）": {},
                "Ｆ（数理・情報）": {},
                "基礎実験": {
                    "基礎実験Ⅱ(物理学)": {
                        "point": 92,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "基礎実験Ⅰ(物理学)": {
                        "point": 92,
                        "credit": 1.0,
                        "weight": 1
                    }
                },
                "生命科学": {},
                "主題科目": {},
                "Ｄ（人間・環境）": {
                    "環境・エネルギー工学基礎Ⅰ": {
                        "point": 89,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "既修外国語": {
                    "英語一列①": {
                        "point": 87,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "英語二列Ｗ（ALESA）": {
                        "point": 85,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "英語一列②": {
                        "point": 79,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "英語二列Ｓ（FLOW）": {
                        "point": 40,
                        "credit": 1.0,
                        "weight": 1
                    }
                },
                "初修外国語": {
                    "スペイン語一列②": {
                        "point": 90,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "スペイン語二列": {
                        "point": 89,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "スペイン語一列①": {
                        "point": 88,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "Ｂ（国際・地域）": {
                    "現代国際社会論": {
                        "point": 81,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "初年次ゼミナール": {},
                "身体運動・健康科学実習": {
                    "身体運動・健康科学実習Ⅱ": {
                        "point": 86,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "身体運動・健康科学実習Ⅰ": {
                        "point": 80,
                        "credit": 1.0,
                        "weight": 1
                    }
                },
                "Ａ（思想・芸術）": {},
                "Ｃ（社会・制度）": {},
                "数理科学、物質・生命科学": {},
                "情報": {
                    "情報": {
                        "point": 75,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "社会科学": {},
                "人文科学": {},
                "社会科学・人文科学": {},
                "展開科目": {},
                "初年次ゼミナール理科": {},
                "初年次ゼミナール文科": {},
                "身体運動・健康科学実習(PEAK)": {},
                "人文・社会科学ゼミナール": {}
            },
            "average": 83.02272727272727
        },
        "senior_faculty_3": {
            "faculty_num": 803,
            "subjects": {
                "Ｌ（言語・コミュニケーション）": {
                    "英語中級（クラス指定セメスター型）": {
                        "point": 85,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "英語中級（クラス指定ターム型）": {
                        "point": 83,
                        "credit": 1.0,
                        "weight": 1
                    }
                },
                "物質科学": {
                    "熱力学": {
                        "point": 95,
                        "credit": 2.0,
                        "weight": 1.5
                    },
                    "力学Ａ": {
                        "point": 93,
                        "credit": 2.0,
                        "weight": 1.5
                    },
                    "構造化学": {
                        "point": 88,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "電磁気学Ａ": {
                        "point": 70,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "数理科学": {
                    "微分積分学①": {
                        "point": 90,
                        "credit": 1.0,
                        "weight": 1.5
                    },
                    "数学基礎理論演習": {
                        "point": 89,
                        "credit": 1.0,
                        "weight": 1.5
                    },
                    "微分積分学②": {
                        "point": 86,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "線型代数学①": {
                        "point": 85,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "数理科学基礎演習": {
                        "point": 83,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "数理科学基礎": {
                        "point": 82,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "微分積分学演習": {
                        "point": 72,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "線型代数学演習": {
                        "point": 69,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "線型代数学②": {
                        "point": 67,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "Ｅ（物質・生命）": {},
                "Ｆ（数理・情報）": {},
                "基礎実験": {
                    "基礎実験Ⅱ(物理学)": {
                        "point": 92,
                        "credit": 1.0,
                        "weight": 1.5
                    },
                    "基礎実験Ⅰ(物理学)": {
                        "point": 92,
                        "credit": 1.0,
                        "weight": 1.5
                    }
                },
                "生命科学": {},
                "主題科目": {},
                "Ｄ（人間・環境）": {
                    "環境・エネルギー工学基礎Ⅰ": {
                        "point": 89,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "既修外国語": {
                    "英語一列①": {
                        "point": 87,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "英語二列Ｗ（ALESA）": {
                        "point": 85,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "英語一列②": {
                        "point": 79,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "英語二列Ｓ（FLOW）": {
                        "point": 40,
                        "credit": 1.0,
                        "weight": 1
                    }
                },
                "初修外国語": {
                    "スペイン語一列②": {
                        "point": 90,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "スペイン語二列": {
                        "point": 89,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "スペイン語一列①": {
                        "point": 88,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "Ｂ（国際・地域）": {
                    "現代国際社会論": {
                        "point": 81,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "初年次ゼミナール": {},
                "身体運動・健康科学実習": {
                    "身体運動・健康科学実習Ⅱ": {
                        "point": 86,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "身体運動・健康科学実習Ⅰ": {
                        "point": 80,
                        "credit": 1.0,
                        "weight": 1
                    }
                },
                "Ａ（思想・芸術）": {},
                "Ｃ（社会・制度）": {},
                "数理科学、物質・生命科学": {},
                "情報": {
                    "情報": {
                        "point": 75,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "社会科学": {},
                "人文科学": {},
                "社会科学・人文科学": {},
                "展開科目": {},
                "初年次ゼミナール理科": {},
                "初年次ゼミナール文科": {},
                "身体運動・健康科学実習(PEAK)": {},
                "人文・社会科学ゼミナール": {}
            },
            "average": 83.80208333333333
        }
    },
    "00Vy4f7HHcc0aFExZmeVU7za1tG3": {
        "grade": 2020,
        "base_avg": 84.0,
        "senior_faculty_1": {
            "faculty_num": 801,
            "subjects": {
                "Ｌ（言語・コミュニケーション）": {
                    "英語中級（クラス指定セメスター型）": {
                        "point": 85,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "英語中級（クラス指定ターム型）": {
                        "point": 83,
                        "credit": 1.0,
                        "weight": 1
                    }
                },
                "物質科学": {
                    "熱力学": {
                        "point": 95,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "力学Ａ": {
                        "point": 93,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "構造化学": {
                        "point": 88,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "電磁気学Ａ": {
                        "point": 70,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "数理科学": {
                    "微分積分学①": {
                        "point": 90,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "数学基礎理論演習": {
                        "point": 89,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "微分積分学②": {
                        "point": 86,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "線型代数学①": {
                        "point": 85,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "数理科学基礎演習": {
                        "point": 83,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "数理科学基礎": {
                        "point": 82,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "微分積分学演習": {
                        "point": 72,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "線型代数学演習": {
                        "point": 69,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "線型代数学②": {
                        "point": 67,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "Ｅ（物質・生命）": {},
                "Ｆ（数理・情報）": {},
                "基礎実験": {
                    "基礎実験Ⅱ(物理学)": {
                        "point": 92,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "基礎実験Ⅰ(物理学)": {
                        "point": 92,
                        "credit": 1.0,
                        "weight": 1
                    }
                },
                "生命科学": {},
                "主題科目": {},
                "Ｄ（人間・環境）": {
                    "環境・エネルギー工学基礎Ⅰ": {
                        "point": 89,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "既修外国語": {
                    "英語一列①": {
                        "point": 87,
                        "credit": 1.0,
                        "weight": 1.5
                    },
                    "英語二列Ｗ（ALESA）": {
                        "point": 85,
                        "credit": 2.0,
                        "weight": 1.5
                    },
                    "英語二列Ｓ（FLOW）": {
                        "point": 83,
                        "credit": 1.0,
                        "weight": 1.5
                    },
                    "英語一列②": {
                        "point": 79,
                        "credit": 1.0,
                        "weight": 1
                    }
                },
                "初修外国語": {
                    "スペイン語一列②": {
                        "point": 90,
                        "credit": 2.0,
                        "weight": 1.5
                    },
                    "スペイン語二列": {
                        "point": 89,
                        "credit": 2.0,
                        "weight": 1.5
                    },
                    "スペイン語一列①": {
                        "point": 88,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "Ｂ（国際・地域）": {
                    "現代国際社会論": {
                        "point": 81,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "初年次ゼミナール": {},
                "身体運動・健康科学実習": {
                    "身体運動・健康科学実習Ⅱ": {
                        "point": 86,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "身体運動・健康科学実習Ⅰ": {
                        "point": 80,
                        "credit": 1.0,
                        "weight": 1
                    }
                },
                "Ａ（思想・芸術）": {},
                "Ｃ（社会・制度）": {},
                "数理科学、物質・生命科学": {},
                "情報": {
                    "情報": {
                        "point": 75,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "社会科学": {},
                "人文科学": {},
                "社会科学・人文科学": {},
                "展開科目": {},
                "初年次ゼミナール理科": {},
                "初年次ゼミナール文科": {},
                "身体運動・健康科学実習(PEAK)": {},
                "人文・社会科学ゼミナール": {}
            },
            "average": 84.27083333333333,
            "rank": 1
        },
        "senior_faculty_2": {
            "faculty_num": 802,
            "subjects": {
                "Ｌ（言語・コミュニケーション）": {
                    "英語中級（クラス指定セメスター型）": {
                        "point": 85,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "英語中級（クラス指定ターム型）": {
                        "point": 83,
                        "credit": 1.0,
                        "weight": 1
                    }
                },
                "物質科学": {
                    "熱力学": {
                        "point": 95,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "力学Ａ": {
                        "point": 93,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "構造化学": {
                        "point": 88,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "電磁気学Ａ": {
                        "point": 70,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "数理科学": {
                    "微分積分学①": {
                        "point": 90,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "数学基礎理論演習": {
                        "point": 89,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "微分積分学②": {
                        "point": 86,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "線型代数学①": {
                        "point": 85,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "数理科学基礎演習": {
                        "point": 83,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "数理科学基礎": {
                        "point": 82,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "微分積分学演習": {
                        "point": 72,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "線型代数学演習": {
                        "point": 69,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "線型代数学②": {
                        "point": 67,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "Ｅ（物質・生命）": {},
                "Ｆ（数理・情報）": {},
                "基礎実験": {
                    "基礎実験Ⅱ(物理学)": {
                        "point": 92,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "基礎実験Ⅰ(物理学)": {
                        "point": 92,
                        "credit": 1.0,
                        "weight": 1
                    }
                },
                "生命科学": {},
                "主題科目": {},
                "Ｄ（人間・環境）": {
                    "環境・エネルギー工学基礎Ⅰ": {
                        "point": 89,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "既修外国語": {
                    "英語一列①": {
                        "point": 87,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "英語二列Ｗ（ALESA）": {
                        "point": 85,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "英語二列Ｓ（FLOW）": {
                        "point": 83,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "英語一列②": {
                        "point": 79,
                        "credit": 1.0,
                        "weight": 1
                    }
                },
                "初修外国語": {
                    "スペイン語一列②": {
                        "point": 90,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "スペイン語二列": {
                        "point": 89,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "スペイン語一列①": {
                        "point": 88,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "Ｂ（国際・地域）": {
                    "現代国際社会論": {
                        "point": 81,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "初年次ゼミナール": {},
                "身体運動・健康科学実習": {
                    "身体運動・健康科学実習Ⅱ": {
                        "point": 86,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "身体運動・健康科学実習Ⅰ": {
                        "point": 80,
                        "credit": 1.0,
                        "weight": 1
                    }
                },
                "Ａ（思想・芸術）": {},
                "Ｃ（社会・制度）": {},
                "数理科学、物質・生命科学": {},
                "情報": {
                    "情報": {
                        "point": 75,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "社会科学": {},
                "人文科学": {},
                "社会科学・人文科学": {},
                "展開科目": {},
                "初年次ゼミナール理科": {},
                "初年次ゼミナール文科": {},
                "身体運動・健康科学実習(PEAK)": {},
                "人文・社会科学ゼミナール": {}
            },
            "average": 84.0
        },
        "senior_faculty_3": {
            "faculty_num": 803,
            "subjects": {
                "Ｌ（言語・コミュニケーション）": {
                    "英語中級（クラス指定セメスター型）": {
                        "point": 85,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "英語中級（クラス指定ターム型）": {
                        "point": 83,
                        "credit": 1.0,
                        "weight": 1
                    }
                },
                "物質科学": {
                    "熱力学": {
                        "point": 95,
                        "credit": 2.0,
                        "weight": 1.5
                    },
                    "力学Ａ": {
                        "point": 93,
                        "credit": 2.0,
                        "weight": 1.5
                    },
                    "構造化学": {
                        "point": 88,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "電磁気学Ａ": {
                        "point": 70,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "数理科学": {
                    "微分積分学①": {
                        "point": 90,
                        "credit": 1.0,
                        "weight": 1.5
                    },
                    "数学基礎理論演習": {
                        "point": 89,
                        "credit": 1.0,
                        "weight": 1.5
                    },
                    "微分積分学②": {
                        "point": 86,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "線型代数学①": {
                        "point": 85,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "数理科学基礎演習": {
                        "point": 83,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "数理科学基礎": {
                        "point": 82,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "微分積分学演習": {
                        "point": 72,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "線型代数学演習": {
                        "point": 69,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "線型代数学②": {
                        "point": 67,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "Ｅ（物質・生命）": {},
                "Ｆ（数理・情報）": {},
                "基礎実験": {
                    "基礎実験Ⅱ(物理学)": {
                        "point": 92,
                        "credit": 1.0,
                        "weight": 1.5
                    },
                    "基礎実験Ⅰ(物理学)": {
                        "point": 92,
                        "credit": 1.0,
                        "weight": 1.5
                    }
                },
                "生命科学": {},
                "主題科目": {},
                "Ｄ（人間・環境）": {
                    "環境・エネルギー工学基礎Ⅰ": {
                        "point": 89,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "既修外国語": {
                    "英語一列①": {
                        "point": 87,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "英語二列Ｗ（ALESA）": {
                        "point": 85,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "英語二列Ｓ（FLOW）": {
                        "point": 83,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "英語一列②": {
                        "point": 79,
                        "credit": 1.0,
                        "weight": 1
                    }
                },
                "初修外国語": {
                    "スペイン語一列②": {
                        "point": 90,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "スペイン語二列": {
                        "point": 89,
                        "credit": 2.0,
                        "weight": 1
                    },
                    "スペイン語一列①": {
                        "point": 88,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "Ｂ（国際・地域）": {
                    "現代国際社会論": {
                        "point": 81,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "初年次ゼミナール": {},
                "身体運動・健康科学実習": {
                    "身体運動・健康科学実習Ⅱ": {
                        "point": 86,
                        "credit": 1.0,
                        "weight": 1
                    },
                    "身体運動・健康科学実習Ⅰ": {
                        "point": 80,
                        "credit": 1.0,
                        "weight": 1
                    }
                },
                "Ａ（思想・芸術）": {},
                "Ｃ（社会・制度）": {},
                "数理科学、物質・生命科学": {},
                "情報": {
                    "情報": {
                        "point": 75,
                        "credit": 2.0,
                        "weight": 1
                    }
                },
                "社会科学": {},
                "人文科学": {},
                "社会科学・人文科学": {},
                "展開科目": {},
                "初年次ゼミナール理科": {},
                "初年次ゼミナール文科": {},
                "身体運動・健康科学実習(PEAK)": {},
                "人文・社会科学ゼミナール": {}
            },
            "average": 84.69791666666667
        }
    }
}

removed.json
{   
    "removed_id":[
        "00Vy4f7HHcc0aFExZmeVU7za1tG3"
    ]
}
