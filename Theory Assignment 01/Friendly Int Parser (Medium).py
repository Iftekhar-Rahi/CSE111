while True:
    try:
        all_num="0123456789 ,oOl"
        num = "0123456789"
        final_num = ""
        flag=False
        word = input()
        if word==" ":
            flag=True
        else:
            for i in word:
                if i in all_num:
                    if i in num:
                        final_num += i
                    elif i == "o" or i == "O":
                        final_num += "0"
                    elif i == " " or i == ",":
                        pass
                    elif i == "l":
                        final_num += "1"
                else:
                    flag=True
            if int(final_num)>2147483647:
                flag=True
            if flag==True:
                print("error")
            else:
                print(int(final_num))
    except:
        break