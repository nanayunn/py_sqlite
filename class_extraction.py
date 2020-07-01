# -*- coding: utf-8 -*- 
from redminelib import Redmine
from redminelib.exceptions import AuthError
import sqlite3

"""
1. is valid(target_list, api_key):
사이트 별 api 키를 이용해 접근권한을 획득
매개변수 : 프로젝트 목록, api key
반환값 : 획득한 접근 권한을 리스트로 반환 
(redmine_list)

2. get_issues(redmine_list):
접근권한을 이용하여 일감 묶음 추출
매개변수 : 접근권한 리스트
반환값 : 각 프로젝트 별 일감묶음 리스트
(issue_list)

3. list_to_dict(target_list, issue_list):
프로젝트 이름과 일감묶음을 딕셔너리 형태로 반환
매개변수 : 프로젝트 이름 리스트, 일감묶음 리스트
반환값 : 두 리스트 각각의 요소가 key와 value 값으로 묶인 딕셔너리
(dict(target_dict))

4. create_table(filepath, target):
db 파일에 각 프로젝트 별 테이블을 만드는 함수
매개변수 : db 파일 이름, 프로젝트 이름
반환값 : 연결된 conn 객체
(conn)

5. extract_data(filepath, dict):
각 일감묶음에서 프로젝트별로 데이터를 추출, 만들어진 테이블에 해당 일감 정보를 저장하는 함수
매개변수 : 프로젝트 이름 리스트, 일감묶음 리스트
반환값 : 성공시 conn 반환

"""
class data_extraction:
    def __init__(self):
        self.result = 0
        self.key = ''

    def is_valid(self, target_list):
        redmine_list = []
        api_key = self.key
        for index in range(0, len(target_list)):
            try:
                print(target_list[index])
                redmine = Redmine(target_list[index], key=api_key,verify=False)
                redmine_list.append(redmine)
            except:
                print target_list[index] + "is_valid : key validation Error. check API key.\n"
            finally:
                print "validation end\n"
        
        return redmine_list


    def get_issues(self, redmine_list):
        issue_list = []
        for index in range (0,len(redmine_list)):
            try:
                issues = redmine_list[index].issue.filter(status_id = '*')
                issue_list.append(issues)
            except:
                print "get_issues : unable to extract data\n"
            finally:
                print "extraction end\n"
        return issue_list
        

    def list_to_dict(self, target_list, issue_list):
        target_dict = []

        try:
            for index in range(0, len(target_list)):
                temp_list = []
                temp_list.append(target_list[index])
                temp_list.append(issue_list[index])
                target_dict.append(tuple(temp_list))
            
        except:
            print "list_to_dict : error detected\n"

        finally:
            print "list to dict end\n"
        print(dict(target_dict))
        return dict(target_dict)


    def create_table(self, filepath, target):
        try:
            conn = sqlite3.connect(filepath)
            cur = conn.cursor()
            cur.execute("drop table if exists " + target)
            cur.execute("create table " + target + 
            " ( project_name NOT NULL,issues_id integer NOT NULL PRIMARY KEY,trakcer_name text NOT NULL,status_name text NOT NULL,author_name text NOT NULL,subject text NOT NULL, created_date text NOT NULL)")
            conn.commit()
        except:
            print "create_table : error detected"
            conn.close()

        return conn


    def extract_data(self, filepath, dictionary):
        
        try:
            for key in dictionary:
                print key + " extracting start"
                conn = self.create_table(filepath, key)
                for issue in dictionary[key]:

                    dict_issue = dict(issue)

                    project = dict_issue['project']
                    status = dict_issue['status']
                    tracker = dict_issue['tracker']
                    issues_id = dict_issue['id']
                    subject = dict_issue['subject']
                    created_date = dict_issue['created_on']
                    author = dict_issue['author']

                    project_name = project['name']
                    status_name = status['name']
                    trakcer_name = tracker['name']
                    author_name = author['name']

                    issue_list = []

                    issue_list.append(project_name)
                    issue_list.append(issues_id)
                    issue_list.append(trakcer_name)
                    issue_list.append(status_name)  
                    issue_list.append(author_name)
                    issue_list.append(subject)
                    issue_list.append(created_date)

                    cur = conn.cursor()
                    cur.execute(
                            "insert into " + key +" values (?,?,?,?,?,?,?)", issue_list)
                    conn.commit()
        except:
            print "extract_data : error detected"
            conn.close()

        return conn






