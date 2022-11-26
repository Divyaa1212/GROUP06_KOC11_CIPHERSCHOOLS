def acro(str1):
    ## split the string into substrings 
    phrase_split = str1.split()
    


    acronym = ""

    ## iterate through every substring
    for i in phrase_split:
        acronym = acronym + i[0].upper()

    print("The acronym for your phrase is ",acronym + ".")

#no. strings input from the user

n = int(input("Enter the number of string(s): "))

for i in range(n):
    stri = input("Enter the phrase: ")
    acro(stri)