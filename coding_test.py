# -*- coding: utf-8 -*- 
import sys
import os
'''
각 열별로 ID와 이름 필드로 구성된 입력 파일 A와  각 열별로 ID와 점수 필드로 구성된 입력 파일 B가 주어 졌을 때,  
B파일의  ID 값을  A 파일에서 매칭된 열의 이름 값으로 대체한 후, 점수의 내림 차순으로 정렬하는 프로그램을 작성하세요.

<A 파일 예시>
1 Alex
2 John
3 Smith

<B 파일 예시>
2  78
1  91

<결과>
Alex 91
John 78

'''
# 파일을 파싱해서 dictionary 형태로 반환하는 함수

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
        sys.exit()
    return source

def get_dict_from_file(filepath):
    try : 
        result_dict = {}
        file = open( filepath, "r" )
        new_list = file.readlines()
        file.close()
    
        for lst in new_list:               
            lst = lst.split('\n')           # lst = 1 Alex
            for item in lst:
                if item == '':
                    lst.remove('')                       # ['1 Alex']
            lst = ''.join(lst)    
            lst = lst.split(' ')
            for item2 in lst:
                if item2 == '':
                    lst.remove('')          # split('')과정에서 불필요한 item이 생겼을 경우에 대비하여 공백을 삭제해주는 과정이 필요
            result_dict[lst[0]] = lst[1]
    except Exception:
        print "error"
        sys.exit()

    return result_dict                  # {'1': 'Alex', '3': 'Smith', '2': 'John'}

A_filepath = get_file_path_input()
B_filepath = get_file_path_input()

dict_a = get_dict_from_file(A_filepath)
dict_b = get_dict_from_file(B_filepath)

dict_together = {}

for key in dict_a:
    for key2 in dict_b:
        if key == key2:
            dict_together[dict_a[key]] = dict_b[key2]
        else:
            pass

print dict_together   
sorted_tuple_list = sorted(dict_together.items()) #sorted 함수를 쓰면 key:value 값이 하나의 튜플로 묶여서 sort되어있음

for sorted_item in sorted_tuple_list:
    print sorted_item[0] + ' ' + sorted_item[1]
