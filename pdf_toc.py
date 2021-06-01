# pip install -U pdf.tocgen를 설치(python3 이상 필수)
# 원본 pdf가 있는 위치에 toc.py를 놓고 python toc.py 실행
# 그러면 newtoc.txt가 생성됨

import re # 정규식을 위한 패키지(파이썬 빌트인 패키지)
import os # 명령어 실행을 위한 패키지(파이썬 빌트인 패키지)

title = input("PDF 파일 제목만 입력하세요(띄어쓰기 없이 파일을 준비하세요): ") # pdf 제목을 입력을 위한 함수(띄어쓰기 미포함)
menu = input("1단계만 보고 싶으세요?(y/n): ")

os.system("pdftocio -H " + title + ".pdf > pagenumber_" + title + ".txt") # powershell 명령어 대신 입력해주는 함수, 이 명령어를 실행하면 쪽수가 있는 목차 txt 파일이 만들어 짐

with open("./pagenumber_" + title + ".txt", "r") as f1: # 쪽수가 있는 pagenumber_file.txt를 바탕으로 " ··· [0-9]+"를 제거한 뒤 새 파일로 저장하는 작업
    lines = f1.readlines()
    for line in lines:
        newString = re.sub(r' ··· [0-9]+', "", line)
        newString = newString.replace("    ", "_")
        newString = newString.replace("    ", "_")
        f2 = open("./nopagenumber_" + title + ".txt", "a")
        f2.write(newString)

    f2.close()

if menu == "y":
    with open("./nopagenumber_" + title + ".txt", "r") as f3:
        lines = f3.readlines()
        for line in lines:
            findString = re.sub(r'__[0-9a-zA-Z가-힣. ㄱ-ㅎ!#$%&’()*+,./:;<=>?@_`{|}~\-\[\]]*\n', "", line)
            f4 = open("./lv1_nopagenumber_" + title + ".txt", "a")
            f4.write(findString)
            