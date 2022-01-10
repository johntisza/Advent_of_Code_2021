from collections import Counter

num_dict = {
    '0':"a,b,c,d,e,g",
    '1':"a,b",
    '2':"a,c,d,f,g",
    '3':"a,b,c,d,f",
    '4':"a,b,e,f",
    '5':"b,c,d,e,f",
    '6':"b,c,d,e,f,g",
    '7':"a,b,d",
    '8':"a,b,c,d,e,f,g",
    '9':"a,b,c,d,e,f"
}

# dict_length = []
# for v in num_dict.values():
#     dict_length.append(v)


total_nums = 0

with open('day8.txt', 'r') as f:
    
    for line in f:
        current_num = ''
        input = line.strip().split(' | ')[0]
        output = line.strip().split(' | ')[1]
        output = output.split(' ')
        for scramble in output:
            sort_scramble = sorted(scramble)
            sort_scramble = ",".join(sort_scramble)
            for key,value in num_dict.items():
                print(key, value, sort_scramble, current_num)
                if sort_scramble == value:
                    current_num += key
        print(current_num)
        # total_nums += current_num

print(total_nums)
