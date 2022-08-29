import sys
sys.stdin = open("input.txt")

T = int(input())
for t in range(1, T+1):
    N, K_min, K_max = map(int,input().split())
    scores = list(map(int,input().split()))
    set_scores = set(scores)
    scores2 = list(set_scores)
    scores2.sort()
    constant = scores2[-1]

    for t2 in range(len(scores2)-1, 0, -1):
        for t1 in range(t2):
            num_c, num_b, num_a = 0, 0, 0
            for elt in scores:
                if elt < scores2[t1]:
                    num_c += 1
                elif scores2[t1] <= elt < scores2[t2]:
                    num_b += 1
                elif elt >= scores2[t2]:
                    num_a += 1
            minimum = min(num_c, num_b, num_a)
            maximum = max(num_c, num_b, num_a)
            if minimum >= K_min and maximum <= K_max:
                if maximum - minimum < constant:
                    constant = maximum - minimum
    if constant < max(scores):
        print(f'#{t} {constant}')
    else:
        print(f'#{t} -1')


    # for t2 in scores:
    #     for t1 in scores:
    #         if t1 < t2:
    #             num_c, num_b, num_a = 0, 0, 0
    #             for elt in scores:
    #                 if elt < t1:
    #                     num_c += 1
    #                 elif t1 <= elt < t2:
    #                     num_b += 1
    #                 elif elt >= t2:
    #                     num_a += 1
    #             minimum = min(num_c, num_b, num_a)
    #             maximum = max(num_c, num_b, num_a)
    #             if minimum >= K_min and maximum <= K_max:
    #                 if maximum - minimum < constant:
    #                     constant = maximum - minimum
    # if constant < max(scores):
    #     print(f'#{t} {constant}')
    # else:
    #     print(f'#{t} -1')




    # if len(lst) != 0 :
    #     minV = max(scores)
    #     for elt in lst:
    #         if max(elt) - min(elt) < minV:
    #             minV = max(elt) - min(elt)
    #     print(f'#{t} {minV}')
    # else:
    #     print(f'#{t} -1')
