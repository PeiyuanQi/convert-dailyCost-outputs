# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

if __name__ == '__main__':
    df = pd.read_csv('dailyocostexport.csv')

    newDF = pd.DataFrame(data = {
        '类型': [],
        '时间': [],
        '类别': [],
        '金额': [],
        '账户': [],
        '备注': [],
    })
    for index, row in df.iterrows():
        if row['Sum'] >= 0:
            type = "支出"
        else:
            type = "收入"

        time = row['Date']
        time = time.replace('/','-')
        newMap = {
            "General"    : "其他",
            "Food"       : "吃喝",
            "Drinks"     : "吃喝",
            "Transfer"   : "转账",
            "App"        : "App",
            "Store"      : "采购",
            "Entertain"  : "娱乐",
            "Transport"  : "交通",
            "Personal"   : "日用杂物",
            "Books"      : "学习",
            "Computer"   : "电子产品",
            "Gifts"      : "社交",
            "Travel"     : "娱乐",
            "Shopping"   : "采购",
            "Tickets"    : "娱乐",
            "Groceries"  : "日用杂货",
            "Movies"     : "娱乐",
            "Social"     : "社交",
            "Mobile"     : "App",
            "Housing"    : "水电话租",
            "Medical"    : "医疗",
            "App Store"  : "App"
        }

        cate = newMap[row['Category']]
        #print(cate)

        price = abs(float(row['Sum']) * float(row['Rate']))
        price = round(price, 2)
        newRowData = {
            '类型': [type],
            '时间': [time],
            '类别': [cate],
            '金额': [str(price)],
            '账户': [''],
            '备注': [row['Note']],
        }

        newRow = pd.DataFrame(data = newRowData)
        frames = [newDF, newRow]
        newDF = pd.concat(frames)

    print(newDF.head())
    newDF = newDF[['类型','时间','类别','金额','账户','备注']]
    print(newDF.head())
    newDF.to_csv('standard_data.csv',encoding='utf-8')

