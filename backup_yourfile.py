# -*- coding: utf-8 -*- 

import os
import time


'''
1. 백업
    1-1. 백업할 대상 : 1개 이상, 경로로 입력받는 모든 파일들

    1-2. 백업 방법 : 파일 경로를 입력 받음.
        1-2-1. 입력받은 경로에 위치한 파일을 'zip' 형식으로 압축하여 백업

    1-3. 백업 리스트 : 리스트 형태로 인식
        1-3-1. 사용자에게 값을 입력받아 저장하려면 txt 파일에 사용자가 입력한 경로를 따로 저장?

    1-4. 백업 장소 : 'backup'이라는 디렉토리
        1-4-1. zip 파일이 저장되는 위치

    1-5. 백업 파일 이름 : 로컬타임에서 현재 시간을 불러와서 이름으로 지정.

2. 복원
    2-1. 복원할 대상 : 1개 이상
        
    2-2. 복원 방법 : 
        2-2-1. 복원할 파일의 이름으로 복원?
        2-2-2. 백업 파일을 저장할 때마다 백업 목록에 시간을 저장
        2-2-3. 백업 목록을 리스트로 받아와서 출력
        2-2-4. 사용자가 index + 1 값을 입력하면 해당 index값을 폴더의 이름과 비교, 복원 진행
    
    2-3. 복원 리스트 : 복원을 진행한 폴더와 날짜를 저장

    2-4. 복원 장소 : 'rollback' 이라는 디렉토리

    2-5. 복원 파일 이름 : rollback + 복원을 진행한 zip 파일의 이름

3. 필요한 변수
    1.  사용자가 입력한 파일 경로 (','로 구분됨)
        1-1. txt, list
    2. 백업을 진행한 파일 이름
        2-1. txt, list
    3. 복원을 진행한 파일 이름 및 복원 시간
        3-1. txt
    4. 사용자가 입력한 파일을 임시 저장할 변수
    5. 복원을 위해 백업할 파일을 선택한 문자열을 저장할 변수
    6. 
'''

def get_file_path_input():
    source = raw_input("Input your file path: \n")  # input 값을 source에 받는다.
    target_folder_list = []  # 사용자 입력값을 저장하기 위한 리스트

    if not os.path.exists(source):
        print "FILE PATH INPUT ERROR : please input existing file\n"

    else:
        # user_input.txt 파일을 추가하기 모드로 연 뒤, 입력한 파일 경로를 추가한다.
        print "Appending your input file-pa into user_input.txt"
        f = open('/home/nykim/user_input.txt', mode= 'at+')
        f.write(source)
        target_folder_list = list(f.readlines())
        print "Loading..."
        f.close()     
    return source, target_folder_list

user_input = []

user_input = get_file_path_input()
source = user_input[0]
target_folder_list = user_input[1]





# target_dir = '/home/nykim/backup'

# # backup 파일이 없다면 그 위치에 만들어라.
# if not os.path.exists(target_dir):
#     os.mkdir(target_dir) # make directory

# # 파일 이름 : year month date hour minute second
# today = target_dir + os.sep + time.strftime('%Y%m%d')

# now = time.strftime('%H%M%S')


# comment = raw_input('Enter a comment --> ')
# # Check if a comment was entered

# if len(comment) == 0:
#     target = today + os.sep + now + '.zip'
# else:
#     target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

# # Create the subdirectory if it isn't already there
# if not os.path.exists(today):
#     os.mkdir(today)
#     print 'Successfully created directory', today

# # 5. We use the zip command to put the files in a zip archive
# zip_command = "zip -r {0} {1}".format(target,
#                                       ' '.join(source))

# # Run the backup
# print "Zip command is:"
# print zip_command
# print "Running:"
# if os.system(zip_command) == 0:
#     print 'Successful backup to', target
# else:
#     print 'Backup FAILED'
