def checkPalindrome(strParam):
    var1 =str(strParam)
    orignal = ""

    for char in var1:
        if char.isalnum():
            orignal += char.lower()
        
    if orignal  == orignal[::-1]:
            return "True"
    else:
         return "False"
strParam = "Anne, I vote more cars race Rome-to-Vienna"
print(checkPalindrome(strParam))