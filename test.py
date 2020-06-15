#!/usr/bin/python
#-*- coding:utf-8 -*-

import io
import csv
import sqlite3

# db파일에 순서대로 데이터를 입력할 빈 리스트
data_list = []

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
# .csv 파일은 실행되는 파이썬 파일과 동일 디렉토리에 있도록 한다. 
with io.open('issues.csv', 'r', encoding='euc-kr') as f:
    # 파일을 읽어온 것을 data에 담고,
    for data in f.readlines():
        # csv 파일을 읽어오면 한줄에 들어가는 데이터가 ',' 콤마로 구분되므로, 콤마를 기준으로 split()을 사용하여 리스트화 한다.
        data_list = data.split(',')
        # 맨 뒤의 추정 시간은 1775개 중 1000개 이상이 비어있어 리스트화를 할 때 12개의 리스트가 만들어져야 하는데 
        # 13개로 만들어지는 오류를 만들어내는 경우가 많아 가공을 한다.
        data_list = data_list[:11]

        # 앞서 만든 쿼리의 컬럼에 맞추어 data_list의 값이 순서대로 들어가게 된다.
        cur = conn.cursor()
        # 1회 실행 후, 'insert or replace 구문으로 바꾸어 update를 진행할 예정
        cur.execute( "insert into pask values (?,?,?,?,?,?,?,?,?,?,?)",
        data_list
        )
        # 쿼리 진행 후 커밋.
        conn.commit()
