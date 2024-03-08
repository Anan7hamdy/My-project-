# Ahmed Mohamed Ali Yousef 20230033
# Anan Hamdi Ali 20231117
# Ibrahim Hamdy Mohammed 20231002

while True:
    print(' ', '* Binary Calculator *', ' ')
    print('A) Insert New Number')
    print('B) Exit')
    x = input('**Please Enter Your Choice A/B:')
    # set variable x to get the choice the user  selected
    # set variable y to get the operation the user want to do
    # set variable first_bin_num to get the binary number from the user and check it
    if x == 'A':
        first_bin_num = str(input('Enter A Binary Number:'))
        if all(char in '01' for char in str(first_bin_num)):
            print('*Please Select The Operation *')
            print('A) Convert to 1st Complement')
            print('B) Convert to 2nd Complement')
            print('C) Addition')
            print('D) Subtraction')
        else:
            print(' Error "Please Enter A correct Binary Number"')
            continue
        y = input('Please select A/B/C/D:')
        if y == 'A':
            def first_complement():
                num = list(first_bin_num)
                list1 = ''
# set function def(first_complement) to call it when needed
# set variable num to get the number from the user that is wanted to be converted to 1st complement
# convert every 0 to 1 and every 1 to 0
                for i in range(len(num) - 1, -1, -1):
                    if int(num[i]) == 0:
                        list1 = '1' + list1
                    elif int(num[i]) == 1:
                        list1 = '0' + list1
                print('First Complement is:', list1)
            first_complement()
            continue
# get function def(two_compl) to convert the binary number to the 2nd complement
# drop every 0 we get until reach (1) so drop it and convert every 1 to 0 and every 0 to 1
        elif y == 'B':
            def two_compl(list1):
                num = list(first_bin_num)
                list1 = ''
                leng = len(num)
                for i in range(leng - 1, -1, -1):
                    if int(num[i]) == 0:
                        list1 = '1' + list1
                    elif int(num[i]) == 1:
                        list1 = '0' + list1
                lent = len(list1)
                carry = 0
                list2 = (('0' * (lent - 1)) + '1')
                endres = ''
                for i in range(lent - 1, -1, -1):
                    if int(list1[i]) + int(list2[i]) + carry == 0:
                        endres = '0' + endres
                    elif int(list1[i]) + int(list2[i]) + carry == 1:
                        endres = '1' + endres
                        carry = 0
                    elif int(list1[i]) + int(list2[i]) + carry == 2:
                        endres = '0' + endres
                        carry = 1
                if carry == 1:
                    endres = '1' + endres
                print('2nd Complement is:', endres)
            two_compl(1)
            continue
# add(1+1)=0 and carry 1,add(1+1+1)=1 and carry 1
# set list1 and list2 to check first num from the user and get the 2nd num
# set a variable sum as an empty list to get the addition in the end
# set variable leng1 as a length of the list
# set variable second_binary_num to get the number from the user and check it
        elif y == 'C':
            second_bin_num = str(input('Please Enter The Second Binary Number:'))
            if all(char in '01'for char in str(second_bin_num)):
                list2 = list(second_bin_num)
                def add_binary(list1, list2):
                    list1 = list(first_bin_num)
                    list2 = list(second_bin_num)
                    sum = ''
                    leng1 = len(list1)
                    if len(list1) > len(list2):
                        list2 = list('0' * (len(list1) - len(list2))) + (list2)
                        leng1 = len(list1)
                    elif len(list2) > len(list1):
                        list1 = list('0' * (len(list2) - len(list1))) + (list1)
                        leng1 = len(list2)
                    leng = leng1
                    carry = 0
                    for I in range(leng - 1, -1, -1):
                        if int(list1[I]) + int(list2[I]) + carry == 0:
                            sum = '0' + sum
                            carry = 0
                        elif int(list1[I]) + int(list2[I]) + carry == 1:
                            sum = '1' + sum
                            carry = 0
                        elif int(list1[I]) + int(list2[I]) + carry == 2:
                            sum = '0' + sum
                            carry = 1
                        elif int(list1[I]) + int(list2[I]) + carry == 3:
                            sum = '1' + sum
                            carry = 1
                    if carry == 1:
                        sum = '1' + sum
                    print('Result Of Addition is:', sum)
                add_binary(0, 1)
                continue
            else:
                print(' Error "Please Enter A Correct Binary Number"')
                continue
# set the function def bin_sub to call it when needed
# for subtract if the first number bigger then second number:(0-0)=0,(1-0)=1,(1-1)=0.
# if the second number bigger than first:the above and (0-1)=1.we borrow 2 from
# the adjacent and the minus 1.
# set variable second_bin_num2 to get the number from the user and checkit
        elif y =='D':
            second_bin_num2 = str(input('Please Enter The Second Binary Number:'))
            if all(char in '01' for char in str(second_bin_num2)):
                num2 = list(second_bin_num2)
                def bin_sub(list1, list2):
                    list1 = list(first_bin_num)
                    num2 = list(second_bin_num2)
                    list3 = ''
                    leng = len(num2)
                    for i in range(leng - 1, -1, -1):
                        if int(num2[i]) == 0:
                            list3 = '1' + list3
                        elif int(num2[i]) == 1:
                            list3 = '0' + list3
                    # we get the first complement for the second number
                    leng = len(list3)
                    carry = 0
                    list4 = (('0' * (leng - 1)) + '1')
                    endres = ''
                    for i in range(leng - 1, -1, -1):
                        if int(list4[i]) + int(list3[i]) + carry == 0:
                            endres = '0' + endres
                            carry = 0
                        elif int(list4[i]) + int(list3[i]) + carry == 1:
                            endres = '1' + endres
                            carry = 0
                        elif int(list4[i]) + int(list3[i]) + carry == 2:
                            endres = '0' + endres
                            carry = 1
                    if carry == 1:
                        endres = '1' + endres
                        # we get the second complement
                    leng1 = len(list1)
                    if len(list1) > len(endres):
                        list2 = list('0' * (len(list1) - len(endres))) + (endres)
                        leng1 = len(list1)
                    elif len(endres) > len(list1):
                        list1 = list('0' * (len(endres) - len(list1))) + (list1)
                        leng1 = len(endres)
                    leng = leng1
                    sub = ''
                    leng1 = len(list1)
                    carry = 0
                    for I in range(leng - 1, -1, -1):
                        if int(endres[I]) + int(list1[I]) + carry == 0:
                            sub = '0' + sub
                            carry = 0
                        elif int(endres[I]) + int(list1[I]) + carry == 1:
                            sub = '1' + sub
                            carry = 0
                        elif int(endres[I]) + int(list1[I]) + carry == 2:
                            sub = '0' + sub
                            carry = 1
                        elif int(endres[I]) + int(list1[I]) + carry == 3:
                            sub = '1' + sub
                            carry = 1
                    print("Result Of Subtraction  is " + sub)
                bin_sub(1, 2)
                continue
            else:
                print(' Error "Please Enter A Correct Binary Number"')
                continue
# else here if the user entered another option except (A,B,C,D).
        else:
            print('Error" Please Select A Valid Choice" ')
            continue
    elif x == 'B':
        print('Exiting program')
        exit()
# if  here if the user entered another option expect(A,B).
    if x != 'A' and 'B':
        print('Error" Please Select A Valid Choice" ')
        continue
    exit()
                           #***Test***#
# fixed number =1101,first_complement(fixed number),output=0010
# two_compl(fixed number),output=0011
#  fixed number 2 = 0111,add_binary(fixed number,fixed number 2),output=10100
# bin_sub(fixed number ,fixed number 2), output=0110
