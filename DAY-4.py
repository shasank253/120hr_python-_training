#DAY-4
'''def nearest_smallest_palindrom(n):
    def is_palindrome(p):
       return str(p)==str(p)[::-1]
    while True:
        n+=1
        if is_palindrome(n):
           return n
a=int(input( ))
b=int(input( ))
print(nearest_smallest_palindrom(a))
print(nearest_smallest_palindrom(b))'''



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''def max_visited_speciality(patient_medical_speciality_list,medical_specialist):
    max_visit=0
    P=patient_medical_speciality_list.count('P')
    E=patient_medical_speciality_list.count('E')
    O=patient_medical_speciality_list.count('O')
    if P>E and P>O:
        speciality=medical_speciality['P']
    elif E>O:
        speciality=medical_speciality['E']
    else:
        speciality=medical_speciality['O']
    return speciality
patient_medical_speciality_list=[301,'P',303,'P',302,'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"Ent"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)'''


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''def common(str1, str2):
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")
    common_chars = ""
    for char in str1:
        if char in str2 and char not in common_chars:
            common_chars += char
    if common_chars == " ":
        return -1
    return common_chars
str1 = input(" ")
str2 = input(" ")
print(common(str1, str2))'''



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''class Example:
    def __init__(self,num):
        self.num = num

    def set_num(self, num):
        num=num

    def get_num(self):
        return self.num

obj=Example(10)
print(obj.get_num()) #
obj.set_num(15)
print(obj.get_num())'''


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''class Book:
    def __init__(self):
        self.title=None
my_fav=Book()
my_fav.title="Head First Programming"
your_fav=Book()
your_fav.title="Learn Python the hard way"
my_fav.title="Learning Python"
print("My favorite is", my_fav.title)
print("Your's is", your_fav.title)'''


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''def longest_common(w1, w2):
    table = [[0]*(len(w2)+1) for i in range(len(w1)+1)]
    max_len = 0  
    end_idx = 0  
    for i in range(1, len(w1)+1):
        for j in range(1, len(w2)+1):
            if w1[i - 1] == w2[j-1]:
                table[i][j] = table[i-1][j-1]+1
                if table[i][j]>max_len:
                    max_len = table[i][j]
                    end_idx = i
    start_idx = end_idx - max_len
    return w1[start_idx:end_idx]
a=input()
b=input()
print(longest_common(a,b))  '''



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
''';def count(c, n, sum):
    if (sum == 0):
        return 1
    if (sum < 0):
        return 0
    if (n <= 0):
        return 0
    return count(c,n-1,sum)+count(c,n,sum-c[n-1])
c = [50,25,10,5]
n = len(c)
print(count(c, n, 50))'''




#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''def count_ways(amount, denomination_list):
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    if len(denomination_list) == 0:
        return 0
    return count_ways(amount - denomination_list[0], denomination_list) + count_ways(amount, denomination_list[1:])
amount_1 = 4
denomination_list_1 = [1, 2, 3]
print(count_ways(amount_1, denomination_list_1))
amount_2 = 10
denomination_list_2 = [10, 5, 1]
print(count_ways(amount_2, denomination_list_2))
amount_3 = 50
denomination_list_3 = [50, 25, 10, 5]
print(count_ways(amount_3, denomination_list_3))'''


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
###--QLASt
'''def find_correct(word_dict):
    correct_count = 0
    almost_correct_count = 0
    wrong_count = 0
    
    for word, contestant_spelling in word_dict.items():
        if word == contestant_spelling:
            correct_count += 1
        elif abs(len(word) - len(contestant_spelling)) > 2:
            wrong_count += 1
        else:
            wrong_letters = sum([1 for i in range(len(word)) if word[i] != contestant_spelling[i]])
            if wrong_letters <= 2:
                almost_correct_count += 1
            else:
                wrong_count += 1
    
    return [correct_count, almost_correct_count, wrong_count]
dict1={"THEIR":"THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMLL","WEAR":"WEAR","SAMPLE":"SAMPLE"}
a=find_correct(dict1)
print(a)'''


