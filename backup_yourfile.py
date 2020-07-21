# -*- coding: utf-8 -*- 

import os
import time

def get_file_path_input():
    source = raw_input("Input your file path: \n")  # input 값을 source에 받는다.
    try : 
        if not os.path.exists(source):
            print "FILE PATH INPUT ERROR : please input existing file\n"

        else:
            print "Loading..."
            print "Your target file is here : " + source
    except Exception:
        print "Exception\n"

    return source
    
def rollback_file(backup_list):
    
    zipped_folder_list = []
    index = 1
    try: 
        file = open(backup_list, "r+")
        select_list = file.readlines()
        file.close()

        #로그 파일 내에서, 파일의 이름값만 빼온다.
        for item in select_list:
            item = item.split(',')
            item = item[0]
            print item
            zipped_folder_list.append(item)
        print zipped_folder_list
            #사용자가 보고 선택할 수 있도록 프린트
        print "==================select number=================="
        for item2 in zipped_folder_list:
            
            print "folder number : " + str(index) , "|| zip file name: " + item2
            index += 1
    except:
        print "error"


    # 사용자에게 숫자로 리스트의 인덱스를 입력받는다. 범위값 예외 처리
    user_input = raw_input("select number of folder you want to rollback : ")
    if int(user_input) > index + 1 or int(user_input) < 1:
        print index
        print "out of range. start program again\n"
    else:
        # index는 1부터 시작하므로 실제로 사용자가 입력한 숫자의 리스트 index는 index -1 
        target_zip = zipped_folder_list[int(user_input) - 1]
        print target_zip
        if os.path.exists(target_zip):
            print "found zip file"
            # unzip한 파일을 위치시킬 폴더 위치를 입력 받는다.
            place_to_rollback = raw_input("input file name where you want to place unzipped file : ")

            #실행할 unzip 명령어
            unzip_command = "unzip {0} -d {1}".format(target_zip,''.join(place_to_rollback))
                    
            #unzip 실행
            print "Unzip command is:"
            print unzip_command
            print "Running:"
            if os.system(unzip_command) == 0:
                print 'Successful unzip to', place_to_rollback
            else:
                print 'Unzip FAILED'
        else:
            print "none"

#============== zip 파일 생성 ==============#

source = get_file_path_input()
parse_source = source.split('/')
new_source = []
for source2 in parse_source:
    if source2 is '':
        pass
    else:
        new_source.append(source2)
parse_source = new_source[-1]
print new_source
print parse_source

backup_dir = '/home/nykim/backup' # 백업 디렉토리 위치
# backup 파일이 없다면 그 위치에 만들어라.
if not os.path.exists(backup_dir):
    os.mkdir(backup_dir) # make directory

print backup_dir

# 파일 이름 : year month date hour minute second
backup_day = time.strftime('%Y%m%d')

today_backup = backup_dir + os.sep + backup_day

# 백업을 진행하기 전, 백업을 실행하는 날짜를 기준으로 서브 디렉토리 생성
if not os.path.exists(today_backup):
    os.mkdir(today_backup)
    print 'Successfully created directory', today_backup


# 백업하는 파일 경로 + 백업할 당시의 시간대를 zip 파일의 이름으로 설정
rightnow = time.strftime('%Y%m%d%H%M%S')
backup_file_name = today_backup + os.sep + rightnow + '_' + parse_source + '.zip'
print backup_file_name
# # # 5. -r 옵션은 해당 폴더 경로의 하위 폴더까지 모두 합쳐서 압축한다는 옵션
zip_command = "zip -r {0} {1}".format(backup_file_name,''.join(source))
print "source :" + source

# # Run the backup
print "Zip command is:"
print zip_command
print "Running:"
if os.system(zip_command) == 0:
    print 'Successful backup ', source
else:
    print 'Backup FAILED'

# #============== rollback을 위한 코드  ==============#


# zip 파일 생성을 실행할 때마다, 동시에 zip 파일로 생성된 백업 파일의 이름을 txt 파일에 저장한다.
backup_list = '/home/nykim/backup/backup_created_log.txt' 

if not os.path.exists(backup_list):
    try: 
        file = open(backup_list, "wt+") # 파일이 없다면 생성
        print backup_file_name
        file.write(backup_file_name + ",Backup Text file created.\n")
        file.close()
    except Exception:
        print "backup created log file error"

else:
    try: 
        file = open(backup_list, "at+") #파일이 있다면 append 모드로 설정
        file.write(backup_file_name + ",Backup Text file created.\n")
        print backup_file_name
        file.close()

    except Exception:
        print "backup created log file error"


rollback_file(backup_list)