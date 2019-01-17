from copy import deepcopy
from collections import defaultdict
import time


def get_transaction():
    transaction = []
    f = open('enter file path here', 'r')    ###########################################
    lines = f.readlines()
    for line in lines:
        if line.find('?') == -1:
            line = line.strip('\n')
            transaction.append(line.split(', '))
    return transaction


def find_frequent_1_itemsets(database, min_sup):
    L = []
    L1 = []
    count = 1
    data = database
    for i in range(1,16):
        exec("dic%s = {}" % i)
    for item in data:
        for i in range(1, 16):
            if i==1:
                if int(item[i - 1]) >= 10 and int(item[i - 1]) <= 19:
                    if not dic1.has_key('10~19'):
                        dic1['10~19'] = 1
                    else:
                        dic1['10~19'] += 1
                    item[i-1] = 'age10~19'
                elif int(item[i - 1]) >= 20 and int(item[i - 1]) <= 29:
                    if not dic1.has_key('20~29'):
                        dic1['20~29'] = 1
                    else:
                        dic1['20~29'] += 1
                    item[i - 1] = 'age20~29'
                elif int(item[i - 1]) >= 30 and int(item[i - 1]) <= 39:
                    if not dic1.has_key('30~39'):
                        dic1['30~39'] = 1
                    else:
                        dic1['30~39'] += 1
                    item[i - 1] = 'age30~39'
                elif int(item[i - 1]) >= 40 and int(item[i - 1]) <= 49:
                    if not dic1.has_key('40~49'):
                        dic1['40~49'] = 1
                    else:
                        dic1['40~49'] += 1
                    item[i - 1] = 'age40~49'
                elif int(item[i - 1]) >= 50 and int(item[i - 1]) <= 59:
                    if not dic1.has_key('50~59'):
                        dic1['50~59'] = 1
                    else:
                        dic1['50~59'] += 1
                    item[i - 1] = 'age50~59'
                elif int(item[i - 1]) >= 60 and int(item[i - 1]) <= 69:
                    if not dic1.has_key('60~69'):
                        dic1['60~69'] = 1
                    else:
                        dic1['60~69'] += 1
                    item[i - 1] = 'age60~69'
                elif int(item[i - 1]) >= 70 and int(item[i - 1]) <= 79:
                    if not dic1.has_key('70~79'):
                        dic1['70~79'] = 1
                    else:
                        dic1['70~79'] += 1
                    item[i - 1] = 'age70~79'
                elif int(item[i - 1]) >= 80 and int(item[i - 1]) <= 89:
                    if not dic1.has_key('80~89'):
                        dic1['80~89'] = 1
                    else:
                        dic1['80~89'] += 1
                    item[i - 1] = 'age80~89'
                elif int(item[i - 1]) >= 90 and int(item[i - 1]) <= 99:
                    if not dic1.has_key('90~99'):
                        dic1['90~99'] = 1
                    else:
                        dic1['90~99'] += 1
                    item[i - 1] = 'age90~99'
            if i==2:
                if not dic2.has_key(item[i-1]):
                    dic2[item[i-1]] = 1
                else:
                    dic2[item[i-1]] += 1
            if i==3:
                if not dic3.has_key(item[i-1]):
                    dic3[item[i-1]] = 1
                else:
                    dic3[item[i-1]] += 1
            if i==4:
                if not dic4.has_key(item[i-1]):
                    dic4[item[i-1]] = 1
                else:
                    dic4[item[i-1]] += 1
            if i==5:
                if not dic5.has_key(item[i-1]):
                    dic5[item[i-1]] = 1
                else:
                    dic5[item[i-1]] += 1
            if i==6:
                if not dic6.has_key(item[i-1]):
                    dic6[item[i-1]] = 1
                else:
                    dic6[item[i-1]] += 1
            if i==7:
                if not dic7.has_key(item[i-1]):
                    dic7[item[i-1]] = 1
                else:
                    dic7[item[i-1]] += 1
            if i==8:
                if not dic8.has_key(item[i-1]):
                    dic8[item[i-1]] = 1
                else:
                    dic8[item[i-1]] += 1
            if i==9:
                if not dic9.has_key(item[i-1]):
                    dic9[item[i-1]] = 1
                else:
                    dic9[item[i-1]] += 1
            if i==10:
                if not dic10.has_key(item[i-1]):
                    dic10[item[i-1]] = 1
                else:
                    dic10[item[i-1]] += 1
            if i==11:
                if not dic11.has_key(item[i-1]):
                    dic11[item[i-1]] = 1
                else:
                    dic11[item[i-1]] += 1
                item[i - 1] = 'capg' + item[i - 1]
            if i==12:
                if not dic12.has_key(item[i-1]):
                    dic12[item[i-1]] = 1
                else:
                    dic12[item[i-1]] += 1
                item[i - 1] = 'capl' + item[i-1]
            if i==13:
                if int(item[i-1])>=0 and int(item[i-1])<=9:
                    if not dic13.has_key('0~9'):
                        dic13['0~9']=1
                    else:
                        dic13['0~9'] += 1
                    item[i - 1] = 'hpw0~9'
                elif int(item[i-1])>=10 and int(item[i-1])<=19:
                    if not dic13.has_key('10~19'):
                        dic13['10~19']=1
                    else:
                        dic13['10~19'] += 1
                    item[i - 1] = 'hpw10~19'
                elif int(item[i-1])>=20 and int(item[i-1])<=29:
                    if not dic13.has_key('20~29'):
                        dic13['20~29']=1
                    else:
                        dic13['20~29'] += 1
                    item[i - 1] = 'hpw20~29'
                elif int(item[i-1])>=30 and int(item[i-1])<=39:
                    if not dic13.has_key('30~39'):
                        dic13['30~39']=1
                    else:
                        dic13['30~39'] += 1
                    item[i - 1] = 'hpw30~39'
                elif int(item[i-1])>=40 and int(item[i-1])<=49:
                    if not dic13.has_key('40~49'):
                        dic13['40~49']=1
                    else:
                        dic13['40~49'] += 1
                    item[i - 1] = 'hpw40~49'
                elif int(item[i-1])>=50 and int(item[i-1])<=59:
                    if not dic13.has_key('50~59'):
                        dic13['50~59']=1
                    else:
                        dic13['50~59'] += 1
                    item[i - 1] = 'hpw50~59'
                elif int(item[i-1])>=60 and int(item[i-1])<=69:
                    if not dic13.has_key('60~69'):
                        dic13['60~69']=1
                    else:
                        dic13['60~69'] += 1
                    item[i - 1] = 'hpw60~69'
                elif int(item[i-1])>=70 and int(item[i-1])<=79:
                    if not dic13.has_key('70~79'):
                        dic13['70~79']=1
                    else:
                        dic13['70~79'] += 1
                    item[i - 1] = 'hpw70~79'
                elif int(item[i-1])>=80 and int(item[i-1])<=89:
                    if not dic13.has_key('80~89'):
                        dic13['80~89']=1
                    else:
                        dic13['80~89'] += 1
                    item[i - 1] = 'hpw80~89'
                elif int(item[i-1])>=90 and int(item[i-1])<=99:
                    if not dic13.has_key('90~99'):
                        dic13['90~99']=1
                    else:
                        dic13['90~99'] += 1
                    item[i - 1] = 'hpw90~99'
            if i==14:
                if not dic14.has_key(item[i-1]):
                    dic14[item[i-1]] = 1
                else:
                    dic14[item[i-1]] += 1
            if i==15:
                if not dic15.has_key(item[i-1]):
                    dic15[item[i-1]] = 1
                else:
                    dic15[item[i-1]] += 1

    for key in dic1:
        if dic1[key] >= len(data) * min_sup:
            L.append('age'+key)
    for key in dic2:
        if dic2[key] >= len(data) * min_sup:
            L.append(key)
    for key in dic3:
        if dic3[key] >= len(data) * min_sup:
            L.append(key)
    for key in dic4:
        if dic4[key] >= len(data) * min_sup:
            L.append(key)
    for key in dic5:
        if dic5[key] >= len(data) * min_sup:
            L.append(key)
    for key in dic6:
        if dic6[key] >= len(data) * min_sup:
            L.append(key)
    for key in dic7:
        if dic7[key] >= len(data) * min_sup:
            L.append(key)
    for key in dic8:
        if dic8[key] >= len(data) * min_sup:
            L.append(key)
    for key in dic9:
        if dic9[key] >= len(data) * min_sup:
            L.append(key)
    for key in dic10:
        if dic10[key] >= len(data) * min_sup:
            L.append(key)
    for key in dic11:
        if dic11[key] >= len(data) * min_sup:
            L.append('capg'+key)
    for key in dic12:
        if dic12[key] >= len(data) * min_sup:
            L.append('capl'+key)
    for key in dic13:
        if dic13[key] >= len(data) * min_sup:
            L.append('hpw'+key)
    for key in dic14:
        if dic14[key] >= len(data) * min_sup:
            L.append(key)
    for key in dic15:
        if dic15[key] >= len(data) * min_sup:
            L.append(key)
    for item in L:
        I = []
        I.append(item)
        L1.append(frozenset(I))
    for item2 in L1:
        print item2
        print 'Count:' + str(count)
        count+=1
    return L1


def has_infrequent_subset(c, Lk_1):
    for item in c:
        k_1_set = c - frozenset([item])
        if((k_1_set in Lk_1)==False):
            return True
    return False


def apriori_gen(Lk_1, k):
    Ck = []
    for i in Lk_1:
        for j in Lk_1:
            c = i.union(j)
            if(len(c) == k):
                if(has_infrequent_subset(c,Lk_1)==False):
                    Ck.append(c)
    remove_duplicate = set(Ck)
    return list(remove_duplicate)


def apriori(database, min_sup):
    count = 19
    L = []
    L.append(frozenset())
    L.append(find_frequent_1_itemsets(database, min_sup))
    S = []
    for row in database:
        S.append(frozenset(row))
    k = 2
    C = []
    C.append(frozenset())
    C.append(frozenset())
    number_of_transaction = len(S)
    while(len(L[k-1])!=0):
        C.append(apriori_gen(L[k-1],k))
        c_count = defaultdict(int)
        for c in C[k]:
            for s in S:
                if c.issubset(s):
                    if c_count[c] >= 6940:          #improvement is here
                        break
                    else:
                        c_count[c] += 1


        I = []
        for key, value in c_count.items():
            if float(value)/number_of_transaction >= min_sup:
                print key
                print 'Count:' + str(count)
                count += 1
                I.append(key)
        L.append(frozenset(I))
        k += 1
    return L


if __name__ == '__main__':
    time_start = time.time()
    apriori(get_transaction(), 0.23)
    time_end = time.time()
    print 'time ' + str(time_end-time_start)
