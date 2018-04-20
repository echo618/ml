def input_YM(str_ym, end_ym):
    YM_list = []
    str_year = int(str_ym[:4])
    str_month = int(str_ym[4:])
    end_year = int(end_ym[:4])
    end_month = int(end_ym[4:])
    curr_year = str_year
    while True:
        curr_month = str_month
        while True:
            YM_list.append(str(curr_year) + str(curr_month).rjust(2, '0'))
            if curr_year == end_year and curr_month == end_month:
                break
            curr_month += 1
            if curr_month > 12:
                curr_month = 1
                curr_year += 1
        break

    #        for m in range(1,12):
    #            if m<10 :
    #                set_ym=str(i)+"0"+str(m)
    #            else:
    #                set_ym=str(i)+str(m)
    #            if int(set_ym) >= int(str_ym) and int(set_ym) <= int(end_ym):
    #                YM_list.append(set_ym)
    return YM_list


#a = input_YM('201512', '201612')
#print(a)

# output
# [201512,201601,201602,201603,201604,201605,201607,201608,201609,201610,201611,201612]

