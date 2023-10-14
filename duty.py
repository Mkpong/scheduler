import datetime as dt
from korean_lunar_calendar import KoreanLunarCalendar
# import calendar as cld
# import json

'''
기본 value 설명
[주]    0: 조간, 1: 주간, 2: 야간
[요일]  1: 월, 2: 화, 3: 수, 4: 목, 5: 금, 6: 토, 7: 일
[연] yyyy, [월] mm, [일] dd
'''

##################################### duty matching #####################################
# 특정 날짜의 주와 요일에, 해당하는 <근무 조>와 <근무 시간대> 매칭

# duty list
# key의 숫자는 요일
morning  = { 'duty' : '조간', 1 : '06~18', 2 : '06~18', 3 : '06~14', 4 : '06~14', 5 : '06~13', 6 : 'break', 7 : 'break'}
daytime  = { 'duty' : '주간', 1 : '18~06', 2 : 'break', 3 : '14~22', 4 : '14~22', 5 : '13~20', 6 : '06~18', 7 : 'break'}
nightime = { 'duty' : '야간', 1 : 'break', 2 : '18~06', 3 : '22~06', 4 : '22~06', 5 : '20~06', 6 : '18~06', 7 : 'break'}

# dutylist[0]: 조간 근무 , [1]: 주간 근무, [2] 야간 근무
dutylist = [morning, daytime, nightime]


# 특정 날짜의 주수와 요일 매칭 후, 주에 따른 <근무 조>와 요일에 따른 <근무 시간대> 리스트에 저장
def duty(yyyy, mm, dd):

    time_a = dt.datetime(2023,  10,  2) # 날짜 간격을 계산하기 위한 조간 근무 주의 월요일
    time_b = dt.datetime(yyyy, mm, dd)  # 입력 날짜
    time_c = str(time_b - time_a)       # 두 날짜의 차 (datetime 형식)
    
    # 주수와 요일 계산하기 위한 
    idx = time_c.index(" ")
    date_interval = int(time_c[0:idx])
    print(date_interval)

    weeks = (date_interval // 7) % 3    # 0이면 조간, 1이면 주간, 2면 야간
    days  = (date_interval % 7) + 1     # 요일

    duty = [dutylist[weeks]['duty'], dutylist[weeks][days]]     # duty[0] = '근무 조', duty[1] = '근무 시간대

    return(duty)


'''
break 해당 날짜
[음력]
설 당일, 전후 1일씩
[양력]
신정, 광복절.

해당하지 않는 날짜
[음력]
설과 추석의 대체 공휴일, 
[양력]
3.1절
어린이날, 부처님 오신 날, 현충일, 개천절, 한글날, 근로자의 날
'''
solar_break = [[1, 1], [8, 15]]
lunar_break = [[12, 30], [1, 1], [1, 2], [8, 14], [8, 15], [8, 16]]

solar_break.append([1, 1])



def check_break(mm, dd):
    check_break = 0
    lunar = KoreanLunarCalendar()

    





    return(check_break)