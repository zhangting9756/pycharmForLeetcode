# -*- coding: UTF-8 -*-
"""俊龙华为机试题"""
def junlong():
    InputString = input()
    InputString = InputString.lower()
    WordDict = {}
    for i in InputString:
        if i in WordDict:
            WordDict[i] += 1
        else:
            WordDict[i] = 1
    Result = []
    while sum(list(WordDict.values())) > 0:
        if "x" in WordDict and WordDict["x"] > 0:
            for i in range(WordDict["x"]):
                WordDict["s"] -= 1
                WordDict["i"] -= 1
                WordDict["x"] -= 1
                Result.append(6)
        if "z" in WordDict and WordDict["z"] > 0:
            for i in range(WordDict["z"]):
                WordDict["z"] -= 1
                WordDict["e"] -= 1
                WordDict["r"] -= 1
                WordDict["o"] -= 1
                Result.append(0)
        if "w" in WordDict and WordDict["w"] > 0:
            for i in range(WordDict["w"]):
                WordDict["t"] -= 1
                WordDict["w"] -= 1
                WordDict["o"] -= 1
                Result.append(2)
        if "u" in WordDict and WordDict["u"] > 0:
            for i in range(WordDict["u"]):
                WordDict["f"] -= 1
                WordDict["o"] -= 1
                WordDict["u"] -= 1
                WordDict["r"] -= 1
                Result.append(4)
        if "r" in WordDict and WordDict["r"] > 0:
            for i in range(WordDict["r"]):
                WordDict["t"] -= 1
                WordDict["h"] -= 1
                WordDict["r"] -= 1
                WordDict["e"] -= 2
                Result.append(3)
        if "o" in WordDict and WordDict["o"] > 0:
            for i in range(WordDict["o"]):
                WordDict["o"] -= 1
                WordDict["n"] -= 1
                WordDict["e"] -= 1
                Result.append(1)
        if "f" in WordDict and WordDict["f"] > 0:
            for i in range(WordDict["f"]):
                WordDict["f"] -= 1
                WordDict["i"] -= 1
                WordDict["v"] -= 1
                WordDict["e"] -= 1
                Result.append(5)
        if "s" in WordDict and WordDict["s"] > 0:
            for i in range(WordDict["s"]):
                WordDict["s"] -= 1
                WordDict["v"] -= 1
                WordDict["n"] -= 1
                WordDict["e"] -= 2
                Result.append(7)
        if "t" in WordDict and WordDict["t"] > 0:
            for i in range(WordDict["t"]):
                WordDict["e"] -= 1
                WordDict["i"] -= 1
                WordDict["g"] -= 1
                WordDict["h"] -= 1
                WordDict["t"] -= 1
                Result.append(8)
        if "i" in WordDict and WordDict["i"] > 0:
            for i in range(WordDict["i"]):
                WordDict["n"] -= 2
                WordDict["i"] -= 1
                WordDict["e"] -= 1
                Result.append(9)
    Result.sort()
    Result_string = ""
    for i in Result:
        Result_string += str(i)
    print(Result_string)
def zhangtingzidan(inputScore):
    input_length = len(input_score)
    input_sorted = sorted(enumerate(input_score), key=lambda x: x[1])

    flag = [False] * input_length
    result = [3] * input_length

    index_list = []
    for index, value in input_sorted:
        temp_flag = True
        for item in index_list:
            if (abs(index - item) == 1) & \
                    (input_score[index] != input_score[item]):
                temp_flag = False
            if 0 == index:
                if input_score[index] > input_score[index + 1]:
                    temp_flag = False
            elif (input_length - 1) == index:
                if input_score[index] > input_score[index - 1]:
                    temp_flag = False
            else:
                if input_score[index] > input_score[index - 1] | input_score[index] > input_score[index + 1]:
                    temp_flag = False

        if (temp_flag):
            result[index] = 1
            flag[index] = True
            index_list.append(index)

    for index, value in input_sorted:
        if True == flag[index]:
            continue
        for item in index_list:
            if abs(index - item) == 1:
                result[index] = 2

    print(sum(result))

def caixiaomiandan(n,a):
    arr = []
    for i in range(n):
        arr.append(a[i])
    dict1 = {}
    for item in arr:
        data1 = item.split('.')[0]
        data2 = item.split('.')[1]
        if data1 in dict1.keys():
            dict2 = dict1[data1]
            if data2 in dict2.keys():
                dict2[data2] += 1
            elif int(data2) < int(list(dict2)[0]):
                dict2 = {data2: 1}
        else:
            dict1[data1] = {data2: 1}
    count = 0
    for k, v in dict1.items():
        count += list(v.values())[0]
    print(count)
if __name__ == '__main__':
    input_score = [1,2,3]
    #input_score = list(map(int, input().split(",")))

    input_length = len(input_score)
    input_sorted = sorted(enumerate(input_score), key=lambda x: x[1])

    flag = [False]*input_length
    result = [3]*input_length

    index_list = []
    for index,value in input_sorted:
        temp_flag = True
        for item in index_list:
            if (abs(index-item) == 1) & \
                (input_score[index] != input_score[item]) :
                temp_flag = False
            if 0 == index:
                if input_score[index] > input_score[index+1]:
                    temp_flag = False
            elif (input_length-1) == index:
                if input_score[index] > input_score[index-1]:
                    temp_flag = False
            else:
                if input_score[index] > input_score[index-1] | input_score[index] > input_score[index+1]:
                    temp_flag = False

        if(temp_flag):
            result[index] = 1
            flag[index] = True
            index_list.append(index)

    for index,value in input_sorted:
        if True == flag[index]:
            continue
        for item in index_list:
            if abs(index-item) == 1:
                result[index] = 2

    print(sum(result))