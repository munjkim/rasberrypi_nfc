import csv
import datetime
import subprocess
import pandas as pd

df = pd.read_csv('./data/data.csv')

def write_csv(card_id):
    index = df.index[(df['UID'] == card_id)]
    student_id = df['Student ID'].values[index][0]

    # 현재 시간과 날짜를 구합니다.
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # 추출한 카드 ID와 현재 시간, 날짜를 .csv 파일에 추가합니다.
    with open('./data/card_data_'+current_date+'.csv', mode='a', newline='') as csv_file:
        fieldnames = ['Student ID', 'UID', 'Time', 'Date']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writerow({'Student ID': student_id, 'UID': card_id, 'Time': current_time, 'Date': current_date})

    print("\n", student_id, current_time,"checked!")    
    #print('Student ID: ',student_id, 'Card ID:', card_id, 'Time:', current_time, 'Date:', current_date)

def read_card():
    # nfc-poll 명령어를 실행하고, 그 결과를 가져옵니다.
    output = subprocess.check_output(['/home/sidlab/libnfc/examples/nfc-poll'], stderr=subprocess.STDOUT, universal_newlines=True)

    # 가져온 결과에서 카드 ID를 추출합니다.
    card_id = output.split('UID (NFCID1): ')[1].split('\n')[0]
    return card_id

cnt = 1
while True:
    print('\n\n\n'+cnt%2*2*'*'+'3초동안 접촉 후 제거하면 인식됩니다.'+cnt%2*2*'*')
    card_id = read_card()
    if((df['UID'] == card_id).any()):
        write_csv(card_id)

    else:
        print("\n등록되지 않은 카드입니다.")
    cnt += 1