while True:
    try:
        word= input()
        final_num=""
        for i in word:
            if i != " " and i != ",":
                if i in "oO":
                    final_num+= "0"
                elif i == "l":
                    final_num+= "1"
                else:
                    final_num+= i
        if final_num.isdigit() and int(final_num) <= 2147483647:
            print(int(final_num))
        else:
            print("error")
    except:
        break