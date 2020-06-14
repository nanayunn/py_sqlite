#!/usr/bin/python
#-*- coding:utf-8 -*-

import io
import csv
import sqlite3

data_list = []
insert = []

# #db 생성하기
filepath = "pask_issues.db"

# #해당 path로 db 접속
conn = sqlite3.connect(filepath)
cur = conn.cursor()

# # 생성된 table이 있다면 삭제 후 실행(최초 1회만 실행)
cur.execute("drop table if exists pask")

# # issues 테이블 생성(테스트용 - 실제 테이블 생성 시 제품별 생성 예정, 
# # 혹은 project_id 별로 구분하여 redash에서 쿼리로 추출해야함)
cur.execute("""
    create table pask(
        issues_id int primary key,
        start_date date,
        project_name str,
        tracker_name str,
        status_name str,
        priority_name str,
        subject str,
        assigned_to str,
        range str,
        target_version str,
        up_to_date date
        
    )
""")
conn.commit()

with io.open('issues.csv', 'r', encoding='euc-kr') as f:
 #   for data in f:
 #       for data2 in f.readlines():
 #           print(data2.split(',')[6].encode('utf-8'))
    for data in f.readlines():
        data_list = data.split(',')
        print(len(data_list))
        data_list = data_list[:11]
        print(data_list)
        if data in data_list == '#':
            continue
    # for index in data_list:

    #     print(index)

    #     for index in data_list:
    #         index = index.split(',')
    #         for i in index:
    #             print i
    #             index_list.append(i)
    #         index_list = index_list[:12]

        cur = conn.cursor()
        cur.execute( "insert into pask values (?,?,?,?,?,?,?,?,?,?,?)",
        data_list
        )
    #     # db insert 정보 저장
        conn.commit()

    #    # print data_list
       # for data2 in data_list:
        #    print data2.encode('utf-8')
#print(data_list)

# #db 생성하기

