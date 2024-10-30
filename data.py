# create an empty list

# empty_list = list()

# print(empty_list)

#create another with 2, 3 ,4

# list_num = list([2,3,4])

# print(list_num)


# # alternative 

# list_num_2= ([5,6,7])

# print(list_num_2)

#access the element within a list
# [] = index operators

# print(list_num_2[0])
# print(list_num_2[1])
# print(list_num_2[2])

#to easily get all elements in the list

# for each_item in list_num:
    
#     print(each_item)



# for each_list_num in range(0,1,2):

#     print(each_list_num)


 

# for seq in range(0,3):
#     print(list_num[seq])
    
    #create a new list
    
# house_items = [2,3,"dog",2,"tv","boys"] 
                   
 #list slicing               
 
#print(house_items[2:6])

#adding a new element to the list

#house_items.append(house_items)

# extending a list

# house_items.extend(list_num)

# print(house_items)

# inserting an item in a specific index

# house_items.insert(0,"pen")

# print(house_items)

# house_items.remove("dog")
# print(house_items)


#returns the index of an element within a list
# print(house_items.index("boys"))

# creating an empty list

# fav_sports = []

#  ask the user their fav sports

# user_input = input("What is your fav sports:")

# add that the user their fav sports

# user_input = input("What team do you support in that sport:")

# add that to the original list

# fav_sports.append(user_input)

# print(fav_sports)


# ways of creating a dic

#my_dict(),{} key:value

# my_dic = {
#     "name":"John", "age": 30, "city": "New york"
# }

# class_records = {
#                 1: {"Sam Tugga","Class 6"},
#                 2:{"Lydia Mansah","Class 6"},
#                 3:{"Hassan Musah","Class 6"},
#                 }
                 
                 
# print(my_dic["age"])

# print(my_dic["city"])

#return all the keys in a dictionary

# print(class_records.keys()) 


# return all the values in a dictionary

# print(class_records.values())


# # insert a new record in the dictionary

# class_records[4] = {"Shadrack", "Class 6"}

# print(class_records)

# # class record.clear()
# print("-----------------------------------------------------------")

# var = class_records.keys()

# for each_item in var:
#     print(class_records[each_item])

# create an empty class register

# class_reg = []

# reg_count = int(input("Enter the number of students to register:"))    

# # 25 participants

# for each_user in range(1,reg_count+1):


# ask for the user full name

#     user_input = input ("Enter your Full name:")

# # store the user name in the class register

#     class_reg.append(user_input)

# # display the class register

# print(class_reg)


# create to add two numbers

# def addition(num1,num2):
    
#     result= num1 + num2
#     return result

# # call the addition function

# add= addition(3, 5)

# print("the sum of adding two numbers:", add)

# print(f"The sum of adding two numbers:{add}")


# create to subtract two numbers

# def subtraction(num1,num2):
    
#     result= num1 - num2
#     return result

# # call the subtract function

# sub = subtraction(10, 5)

# print("the subtracting of two numbers:", sub)

# print(f"The subtracting of two numbers:{sub}")


 #create to max two numbers

# def multiple(num1,num2):
#     user_input1 = int(input("Enter your number here:"))
#     user_input2 = int(input("Enter your number here:"))
#     result= user_input1 * user_input2
#     return result

# # # call the subtract function

# max = multiple(0 , 0)

# print("the multiple of two numbers:", max)
# print(f"The multiple of two numbers:{max}")

# # peformance subtraction

# num1, num2 = user_input()
# sub = subtraction(num1,num2)

# print(f"the subtraction of two numbers")




def cal_commission(sales_amount,commission_rate):

    commission = ((commission_rate /100)*sales_amount)
    return commission
sales_amount= float(input("Enter sales amount here:"))
commission_rate =float(input("Enter commission rate here:"))
final_commission=cal_commission(sales_amount,commission_rate)
print(f"This your discount commission given",final_commission)