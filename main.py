import datetime as dt
import calendar as cld
import json
import duty


'''
기본 value 설명
[주]    0: 조간, 1: 주간, 2: 야간
[요일]  1: 월, 2: 화, 3: 수, 4: 목, 5: 금, 6: 토, 7: 일
[연] yyyy, [월] mm, [일] dd
'''

########################################### print calendar ###########################################

# 월의 문자 표현. dictonary 쓸 때 month_eng[mm] 형태로 불러오기
month_eng = { 1 : 'January', 2 : 'February', 3 : 'March', 4 : 'April', 5 : 'May', 6 : 'June',
         7 : 'July', 8 : 'August', 9 : 'September', 10 : 'October', 11 : 'November', 12 : 'December'}

# 날짜를 입력하면 그에 맞는 달력 출력. clean ver (duty 표시 x)
class print_clean_monthly_calendar:
    def __init__(self, yyyy, mm):

        self.yyyy   = yyyy
        self.mm     = mm
  
        self.first_weekday  = cld.monthrange(self.yyyy, self.mm)[0] + 1     # 01일의 요일, 월요일은 1 저장, 일요일은 7 저장
        self.last_day       = cld.monthrange(self.yyyy, self.mm)[1]         # 월의 마지막 일 저장
        self.cnt_weekday    = self.first_weekday                            # dd 출력시 필요

    def days(self, yyyy, mm):

        self.yyyy = yyyy
        self.mm = mm

        self.first_weekday  = cld.monthrange(self.yyyy, self.mm)[0] + 1
        self.last_day       = cld.monthrange(self.yyyy, self.mm)[1]
        self.cnt_weekday    = self.first_weekday
    
    def print_mm_yyyy_weekday_blank(self):
        
        eng_mm_yyyy = str(month_eng[self.mm]) + " " + str(self.yyyy)       # ex. January 2023 이런 문자열
        
        # 영문 월, 연도 출력
        print("=========" * 7)
        print("{0:^63}".format(eng_mm_yyyy))
        print("=========" * 7)

        # 요일 출력 / 간격 7
        print("{0:^9}".format('Sun') + "{0:^9}".format('Mon') + "{0:^9}".format('Tue') + "{0:^9}".format('Wed') +
              "{0:^9}".format('Thu') + "{0:^9}".format('Fri') + "{0:^9}".format('Sat')); print("")
        
        # 1일 출력 전 공백
        if self.first_weekday != 7 :    # 일요일이 아닌 경우 공백 출력
            print("       " * self.first_weekday, end = "")     # ex. 월요일이면 요일 숫자가 1이니 1번 공백 출력
        
        else :  # 일요일인 경우
            self.cnt_weekday = 0

    def print_dd_clean_ver(self):
        
        # dd 출력
        for cnt_days in range (1, self.last_day + 1) :

            # 오늘이 아닌 날짜를 출력하는 경우
            # 공백 7칸에 날짜 가운데 정렬
            if (dt.date(self.yyyy, self.mm, cnt_days)) != (dt.date.today()) :
                print("{0:^9}".format(cnt_days), end = '')
                self.cnt_weekday += 1
            
            # 오늘 날짜를 출력하는 경우
            # '\033[38;5; ___m]'에서 이 ___자리가 ASNI 색상 값.
            else :
                print('\033[38;5;200m' + "{0:^9}".format(cnt_days) + '\033[0m', end = '')
                self.cnt_weekday += 1


            # 줄바꿈. 일요일이거나 / 일요일은 아니지만 월의 마지막 날인 경우
            if (self.cnt_weekday == 7) or ((self.cnt_weekday != 7) and (cnt_days == self.last_day)):
                print("\n" * 4, end ='')    # 줄바꿈 수 조정 가능
                self.cnt_weekday = 0
        
        print("=========" * 7)    # 달력의 마지막 부분
    
    # Json 보내려고 
    def clean_monthly_calendar_json (self):
        
        return_json = {"yyyy" : self.yyyy, "mm" : self.mm, "first_weekday" : self.first_weekday, "last_day" : self.last_day}

        return return_json
    
    
today = dt.date.today()
# 캘린더 정상 작동 확인
a = print_clean_monthly_calendar(today.year, today.month)
a.print_mm_yyyy_weekday_blank()
a.print_dd_clean_ver()


# json 확인
print("ddddddddddddd")
print(a.clean_monthly_calendar_json())
d = a.clean_monthly_calendar_json()

jsonn = json.dumps(d, ensure_ascii=False)
print(type(jsonn))

