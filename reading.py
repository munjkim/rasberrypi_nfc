import csv
import datetime
import subprocess
import os

while True:
    # 현재 시간과 날짜를 구합니다.
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    print("Input card")
    # nfc-poll 명령어를 실행하고, 그 결과를 가져옵니다.
    output = subprocess.check_output(['/home/sidlab/libnfc/examples/nfc-poll'], stderr=subprocess.STDOUT, universal_newlines=True)

    # 가져온 결과에서 카드 ID를 추출합니다.
    card_id = output.split('UID (NFCID1): ')[1].split('\n')[0]
    print("Read end")
    
    student_id = input("Student id : ")
    # 추출한 카드 ID와 현재 시간, 날짜를 .csv 파일에 추가합니다.
    with open('reading.csv', mode='a', newline='') as csv_file:
        fieldnames = ['Student ID', 'ID', 'Time', 'Date']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writerow({'Student ID': student_id, 'ID': card_id, 'Time': current_time, 'Date': current_date})
        
    print('Student ID: ',student_id, 'Card ID:', card_id, 'Time:', current_time, 'Date:', current_date)
