def turn(temperatures):
    M = []
    m = []
    dic_tem = {}
    for temp in temperatures:
        M.append(temp[0])
        m.append(temp[1])
    dic_tem['maximum'] = M
    dic_tem['minimum'] = m
    return dic_tem
    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    temperatures = [
        [9, 3],
        [9, 0],
        [11, -3],
        [11, 1],
        [8, -3],
        [7, -3],
        [-4, -12]
    ]
    print(turn(temperatures)) 
    # {
    #     'maximum': [9, 9, 11, 11, 8, 7, -4], 
    #     'minimum': [3, 0, -3, 1, -3, -3, -12]
    # }
