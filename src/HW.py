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