Ppl = 600000 #People
Immuned = 1
S = Ppl - 1 - Immuned
I = 1
R = Immuned#Выборка 100 человек для примера, I = 1 — нулевой пациент
DeathsToday = 0
import matplotlib.pyplot as plt
import datetime
from datetime import timedelta
import random
import math

'''
from bs4 import BeautifulSoup as bs
import requests as req

def parse():
    resp = req.get("https://news.mail.ru/coronavirus/stat/russia/")
    html = bs(resp.content, 'html.parser')
    
    for el in html.select(".coronavirus_1_0_bg > rect"):
        title = el.select('.coronavirus_1_0_bg > onmouseover')
        print("TITLE: ", title[0].text)


#import random as rnd

c = 0
RtIndex = [0] * 60
with open("C:\Vaxxed.txt", "r") as file:
    for line in file.readlines():
        RtIndex[c] += float(line)
        c += 1
    
print('\n-----')
'''
'''
c = 0
HowRtChanges = [0] * 15
with open("C:\Infected.txt", "r") as file:
    for line in file.readlines():
        HowRtChanges[c] += int(line)
        c += 1

r0 = 0
r1 = 3
r2 = 4
r3 = 7
s1 = 0
s2 = 0

RtArr = [0] * 7
cn = 0

while r3 <= 13:
    for i in range(r0,r1):
        s1 += HowRtChanges[i]
    for i in range(r2,r3):
        s2 += HowRtChanges[i]
    print(s2/s1)
    RtArr[cn] = s2/s1
    r0 += 1
    r1 += 1
    r2 += 1
    r3 += 1
    cn += 1'''
    
print('\n-----')
    
RtArr = [0] * 7
cn = 0
avg = 0
RtDif = [0] * 6
for i in range(6):
    RtDif[i] = RtArr[i + 1] - RtArr[i]
    
for i in range(6):
    avg += RtDif[i]
avg /= 6
print(avg)

AsympthDays = 2
CycleCount = 0
RecTime = 5#days
BeforeSympthoms = 0#days
AsympthPeriod = [0] * AsympthDays
Days = 1000
InfectedYesterday = I
InfectedToday = I
Infected14DaysAgo = [0] * RecTime
ArrS = [0] * Days
ArrInf = [0] * Days
ArrR = [0] * Days
ArrInfToday = [0] * Days
ArrInfTodayMasks = [0] * Days
ArrInfTodayMasks = [0] * Days
ArrImmunedNow = [0] * Days
ArrDeathsToday = [0] * Days
ArrRecToday = [0] * Days
Infected14DaysAgo[0] = 0

cnt = 0
Rt1 = 0
Rt2 = 0
'''
with open("C:\Rt.txt", "r") as f:
    for line in f.readlines():
        if 0 <= cnt <= 3:
            Rt2 += int(line)
        else:
            Rt1 += int(line)
        cnt += 1'''
        
#Rt = Rt2 / Rt1
#print(Rt)
StartDate = datetime.date(2020, 3, 13)
Duration = datetime.timedelta(days=1)
Period = 77
print(Ppl, 0, 0)
print(S, I, R)
ind = 0
Rt = RtArr[0]
Rt = 1.33
TempCount = 0
DWOSC = 1#6.67 #difference with official statistics coefficient
Stops = 1 #stops coefficient is 1 if there are no stops;
Masks = 0.53
Uses = 1
'''
Masks: -11.2% I (60+: -34.7% I) false?
'''
e1 = 0.000023333 * Ppl #350 * Ppl / 15000000
e2 = 0.000014667 * Ppl #220 * Ppl / 15000000
e3 = 0.00001 * Ppl #150 * Ppl / 15000000
e4 = 0.000003333 * Ppl #50 * Ppl / 15000000
Mortality = 0.01
Flag, Pick, PickFlag, PickInd = 0, 0, 0, 0
ArrInfToday[0] = I
ImmunedArray = [0] * 150
FlagsOfImmunization = [0] * Days
imlow = 0
NewWaveFlag = 1
ind2 = 0
ImmunedEnoughFlag = 1
ImmunedCoeff = 0
while ind < Days:
    print("---DAY--- ", ind + 1)
    CycleCount += 1
    #if (NewWaveFlag == 1):
    if (ind == 0):
        Every = 0.0000024 * Ppl #36 * DWOSC * Stops
    if (ind == 60):
        Every = e1 * DWOSC * Stops# + random.randint(-10,100)
    if (ind == 74): #+2 weeks
        Every = e2 * DWOSC * Stops# + random.randint(-30,100)
    if (ind == PickInd and PickInd != 0):
        Every = e3 * DWOSC * Stops# + random.randint(-30,100)
    if (ind == PickInd + 33 and PickInd != 0):
        Every = e4 * DWOSC * Stops# + random.randint(-30,100)
    #if (Every == e4 * DWOSC * Stops):
     #   NewWaveFlag = 0
    #if (ind % 5 == 0): #oscillations for the next waves
     #   Every -= 1 * DWOSC
    #Every += random.uniform(-30,30) #random oscillations
    if S > 0 and InfectedToday > 0:# and Rt >= 0:
        #InfectedToday = int(I * Rt)#Rt
        if (ImmunedEnoughFlag != 0 and Flag == 0):#0.0006 or 0.004 (is right) / if ImmunedEnoughFlag == 0 
            InfectedToday = ArrInfToday[ind - 1] + Every# + random.randint(-200,200)
            InfectedToday *= ImmunedEnoughFlag
            InfectedToday -= InfectedToday * ImmunedCoeff
            #Every -= 1
        else:
            InfectedToday = ArrInfToday[ind - 1] - Every #to use math.ceil
            Flag = 1
            InfectedToday *= ImmunedEnoughFlag
            InfectedToday -= InfectedToday * ImmunedCoeff
            #Every +=10000
        if (InfectedToday < ArrInfToday[ind - 1] and PickFlag == 0):
            Pick = ArrInfToday[ind - 1]
            PickFlag = 1
            PickInd = ind + 1
            '''
        if (InfectedToday > 0):
            Every -= 2
        else:
            Every = 0'''
        
    else:
        InfectedToday = 0
    ArrInfToday[ind] = InfectedToday
    if CycleCount >= RecTime:
        for i in range(RecTime):
            if i == RecTime - 1:
                Infected14DaysAgo[i] = InfectedToday
                break
            Infected14DaysAgo[i] = Infected14DaysAgo[i + 1]
    else:
        Infected14DaysAgo[CycleCount] = InfectedToday#CycleCount - RecTime  RecTimesCount
    if S > 0 and I + InfectedToday <= Ppl:
        I += InfectedToday
        '''
        if BeforeSympthoms < AsympthDays:
            AsympthPeriod[BeforeSympthoms] = InfectedToday
            BeforeSympthoms += 1
        else:
            I -= AsympthPeriod[0]
        '''
            
    elif I + InfectedToday > Ppl:
        I = Ppl
    if S > 0 and S - InfectedToday >= 0:
        S -= InfectedToday
    elif S - InfectedToday < 0:
        S = 0
    if CycleCount >= RecTime:
        #if I - Infected14DaysAgo[0] >= 0:
        DeathsToday = int(Infected14DaysAgo[0] * Mortality)#round
        ArrDeathsToday[ind] = DeathsToday
        I -= Infected14DaysAgo[0]
       # else:
        #    I = 0
        if R + Infected14DaysAgo[0] <= Ppl:
            R += Infected14DaysAgo[0]
        else:
            R = Ppl
        ArrRecToday[ind] = Infected14DaysAgo[0] - DeathsToday
    InfectedYesterday = InfectedToday
    #print(S, I, R)
    print("Infs: ", InfectedToday, "; Dths: ", DeathsToday)
    ArrS[ind] = S
    ArrInf[ind] = I
    ArrR[ind] = R
    ind += 1
    StartDate = StartDate + Duration
    Immuned += ArrRecToday[ind - 1]
    if (ind >= 150): #это действует только единожды - нужно также для последующих волн
        Immuned -= ArrRecToday[imlow]
        imlow += 1
        
    print("IMMUNED: ", Immuned, "; PERCENTAGE: ", round(Immuned / Ppl * 100), "%")
    ArrImmunedNow[ind - 1] = Immuned
    if (Immuned > Ppl / 2):#60%-70%-80%?
        FlagsOfImmunization[ind - 1] = 1000000#set value 100000 to see
    else:
        FlagsOfImmunization[ind - 1] = 0
    if (FlagsOfImmunization[ind - 1] == 0 and FlagsOfImmunization[ind - 2] == 1000000):
        1#InfectedToday = 1
        #Flag = 0
        #Every = e3
        #InfectedToday = 1
        #Every = 0.0000024 * Ppl #36 * DWOSC * Stops
    if (FlagsOfImmunization[ind - 1] == 0):
        ImmunedEnoughFlag = 1
    else:
        ImmunedEnoughFlag = 0 #надо понять, нужно ли это
    '''
    Чем меньше необходимый уровень колл. иммунитета, тем больше волн
    а должно быть совсем наоборот. Также надо сделать волны до набора колл. имм. выше к-н порога'''
    ImmunedCoeff = Immuned / Ppl #Ура! Теперь заболеваемость зависит от иммунитета! Бинго!!!

ArrDays = [0] * Days
for i in range(Days):
    ArrDays[i] = i + 1
#plt.plot(ArrDays,ArrS)
#plt.plot(ArrDays,ArrInf)
#plt.plot(ArrDays,ArrR)
plt.plot(ArrDays,ArrInfToday)
#plt.plot(ArrDays,ArrInf)
#plt.plot(ArrDays,ArrImmunedNow)
#plt.plot(ArrDays,FlagsOfImmunization)
for i in range(Days):
    #ArrInfTodayMasks[i] = ArrInfToday[i] * (Stops - Masks) + random.uniform(-150,100)
    ArrInfTodayMasks[i] = ArrInfToday[i] * (Stops - Masks * Uses)# + random.uniform(-50,50)
#plt.plot(ArrDays,ArrInfTodayMasks)
#plt.plot(ArrDays,ArrDeathsToday)
#plt.plot(ArrDays,ArrRecToday)
plt.show()
print("PICK ", Pick, " ON DAY ", PickInd)
print("I: ", I)
print(Immuned)