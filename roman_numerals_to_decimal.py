def solution(rom):
    dec_value = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
    }
    rom_list = [x for x in str(rom)] #SPLIT input number
    dec_list = [dec_value[j] for j in rom_list] #convert to decimal equivalent
    dec_list.append(0) #placeholder
    i = total = 0
    while i < len(dec_list)-1:
        if dec_list[i+1] <= dec_list[i]:
            total += dec_list[i]
        else:
            total += dec_list[i+1] - dec_list[i]
            i += 1
        i += 1
    return total
