from itertools import zip_longest

################ SAMPLE INPUT  #############
schedule1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
limits1 = ['9:00', '20:00']
schedule2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
limits2 = ['10:00', '18:30']
####################################################

def time_to_unit(time):
    return (int(time.split(':')[0])*10 + (5 if time[-2] == '3' else 0))

def unit_to_time(unit):
    return str(unit)[:2] + (':30' if str(unit)[-1] == '5' else ':00')

def get_available_frames(start, end, schedule1, schedule2):
    ret = {x:True for x in range(start, end, 5)}

    for (b1, e1), (b2,e2) in zip_longest(schedule1, schedule2, fillvalue=(0,0)):
        for n1 in range(b1,e1,5):
            if n1 in ret:
                ret[n1] = False
        for n2 in range(b2,e2,5):
            if n2 in ret:
                ret[n2] = False
    return ret

def format_time_frames(time_stamps):
    ans = []
    aux = []
    change = True
    for k, v in time_stamps.items():
        if v:
            if change:
                aux.append(k)
                change = False
        else:
            if not change:
                aux.append(k)
                ans.append(list(map(unit_to_time, aux)))
                aux = []
                change = True
    if not change:
        aux.append(aux[0] + 5)
        ans.append(list(map(unit_to_time ,aux)))
    return ans



if __name__=="__main__":
    schedule1 = [list(map(time_to_unit, x)) for x in schedule1]
    limits1 = list(map(time_to_unit, limits1))
    schedule2 = [list(map(time_to_unit, x)) for x in schedule2]
    limits2 = list(map(time_to_unit, limits2))
    start = max(limits1[0], limits2[0])
    end = min(limits1[1], limits2[1])

    time_stamps = get_available_frames(start, end, schedule1, schedule2)

    print(format_time_frames(time_stamps))


