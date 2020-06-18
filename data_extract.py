# -*- coding: utf-8 -*- 

from redminelib import Redmine
from redminelib.exceptions import AuthError
import sqlite3


try:
    redmine = Redmine('', key='',verify=False)
except:
    print("key validation Error. check API key.")

issue2 = redmine.issue.filter(status_id = '*')


filepath = "pask_issues.db"
conn = sqlite3.connect(filepath)

cur = conn.cursor()
cur.execute("drop table if exists pask")

cur.execute("""
    create table pask(
        project_name NOT NULL,
        issues_id integer NOT NULL PRIMARY KEY,
        trakcer_name text NOT NULL,
        status_name text NOT NULL,
        author_name text NOT NULL,
        subject text NOT NULL,
        created_date text NOT NULL
    )
""")
conn.commit()

for issue in issue2:
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

    print project_name
    print status_name
    print trakcer_name
    print issues_id
    print created_date
    print subject
    print author_name
    
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
            "insert into pask values (?,?,?,?,?,?,?)", issue_list
           
        )
    conn.commit()
conn.close()





