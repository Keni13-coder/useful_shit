from itertools import combinations
def decor(func):
    def wrapper(num):
        rezul = []
        num = str(num)
        hl = [int(v.zfill(len(num)-i)[::-1]) for i,v in enumerate(num)]
        for item in hl:
            rezul.append(func(item))
        return ''.join(rezul)
    return wrapper



@decor
def rim(number: int) -> str:
    number_rim = {'I': 1,'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rez = ''
    summ = 0
    items = reversed(number_rim.items())
    for k,v in items:
        
        if number == v:
            rez += k
            return rez
        
        elif number < v:
            
            if v - number in number_rim.values():

                for kes,vals in reversed(number_rim.items()):
                    sm = v - number
                    # print('зашёл в блок')
                    # print(f'{v}-{number}')
                    if vals == sm and sm != number:
                        # print(v,number)
                        rez += kes + k
                        return rez

        else:
            while summ + v <=number:
                print(f'{v} и {number},{summ=}')
                summ += v
                rez += k
    return rez
                                       
print(rim(743))
# DCCXLIII
# DCCXLIII
# CMLXXVII
# print(328 - 4 in {1:'sdf',2:324}.items())











'''
        if v < number:
            if number % 9 == 0:
                    print(new_rim[i+1],number,v)
            elif number % 4 == 0:
                    print('gfh')
                    
                        new_rim = list(enumerate(number_rim.items()))[::-1]

    for i,(k,v) in new_rim:
        if number - v < 0:
            print(k)
'''


# def test(n):
#     n = str(n)
#     return [int(v.zfill(len(n)-i)[::-1]) for i,v in enumerate(n)]


'4,9,40,90,400,900'

# print(test(494))
# print(900 % 9)