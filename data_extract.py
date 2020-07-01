# -*- coding: utf-8 -*- 
#!/usr/bin/python

from class_extraction import data_extraction
from subprocess import call
import os
import time

def check_and_replace(filepath, mount_folder, final_file_path):
    
    if not os.path.exists(final_file_path):
        try:
            os.system('mv ' + filepath + ' ' + mount_folder) #temp 폴더 내의 issues.db를 mount 폴더 경로로 옮긴다.
        except:
            print "fail to mv file to folder\n"
    elif os.path.exists(final_file_path):
        try:
            os.system('rm ' + final_file_path) # 마운트 폴더에 db 파일이 존재한다면 삭제
            os.system('mv ' + filepath + ' ' + mount_folder) # 이후 폴더 내로 옮긴다.
        except:
            print "check_and_replace :check_and_replace error detected\n"
            return -1
    else:
        print "check_and_replace : nothing happend. need to check up\n"
        return -1

    return 0

webfront_k = ''
tifront = ''
pas_k = ''

data_base = ".db" #db 파일 이름

temp_filepath = "" + data_base # bluerocket 인스턴스 내의 temp 폴더 위치

mount_folder = "" # docker와 마운트 된 폴더의 위치

final_file_path = mount_folder + os.sep + data_base


date = time.localtime

# class 객체 생성
de = data_extraction()

# 일감 추출할 제품의 사이트 이슈 페이지 주소 목록
target_list = [webfront_k, tifront, pas_k]
project_list = ['', '', '']


# api key로 일감 추출할 제품을 각각 validation 체크
redmine_list = de.is_valid(target_list)

# validation이 체크되면 해당 target의 일감 정보에 접근할 수 있게 됨
# 일감 정보를 (모든 상태의 일감)으로 필터링 후 각 target 별 issues를 추출
issue_list = de.get_issues(redmine_list)

# 각 프로젝트 별 이슈 목록을 딕셔너리 형태로 매칭
each_issue_of_target = de.list_to_dict(project_list, issue_list)

# 추출해서 각 프로젝트 별 테이블에 insert, conn 객체 반환
last_conn = de.extract_data(temp_filepath, each_issue_of_target)

# 객체를 닫아줌
last_conn.close()


result = check_and_replace(temp_filepath, mount_folder, final_file_path)

if result is not 0:
    print "error caused for moving file. please check up, wrong end.\n"
else:
    print "end"
