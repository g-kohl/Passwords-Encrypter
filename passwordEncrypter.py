import pandas as pd
table = pd.read_excel("passwords.xlsx")
print(table)

publickey = input("Write the name of the service (just letters): ")
privatekey = input("Write the password you want to encrypt (just letters): ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
prime2 = 1
ctrl = 0
ctrl2 = 0
ctrl3 = 0
line = 0
lastletter = ""

while table.loc[line, "services"] != publickey:
    line += 1
table.loc[line, "passwords"] = ""

while ctrl < len(publickey):
    letter = publickey[ctrl]
    while ctrl2 < len(alphabet):
        if letter == alphabet[ctrl2]:
            prime2 = prime2 * prime[ctrl2]
        ctrl2 += 1
    ctrl2 = 0
    ctrl += 1
ctrl = 0

strprime = str(prime2)

while ctrl < len(privatekey):
    letter = privatekey[ctrl]
    while ctrl2 < len(alphabet):
        if letter == alphabet[ctrl2]:
            if len(strprime) <= ctrl3:
                ctrl3 = 0
            if ctrl2 + int(strprime[ctrl3]) > 25:
                letterposition = ctrl2 + int(strprime[ctrl3]) - 26
                lastletter = table.loc[line, "passwords"]
                table.loc[line, "passwords"] = lastletter + alphabet[letterposition]
            else:
                letterposition = ctrl2 + int(strprime[ctrl3])
                lastletter = table.loc[line, "passwords"]
                table.loc[line, "passwords"] = lastletter + alphabet[letterposition]
        ctrl2 += 1
    ctrl2 = 0
    ctrl += 1
    ctrl3 += 1
ctrl = 0

table.to_excel("passwords.xlsx", index=False)
print(table)
