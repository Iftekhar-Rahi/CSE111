def replace_domain(email, new="sheba.xyz",old="kaaj.com"):
    for i in range (len(email)):
        if email[i::]=="sheba.xyz":
            print(f"Unchanged: {email[0:i]+new}")
        elif email[i::]=="kaaj.com":
            print(f"Changed: {email[0:i]+new}")
replace_domain('alice@kaaj.com', 'sheba.xyz', 'kaaj.com')