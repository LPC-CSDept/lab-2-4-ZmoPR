def main():

    original_str = 'Python Programming'
    ##################################################
    # Comlete your code here
    ##################################################
    
    original_str = "Python Programming"
    sub2 = original_str[0:6]
    sub1 = original_str[7:18]
    merged_str = sub1 + " " + sub2
    print(sub2)
    print(sub1)
    print(merged_str)
    #########################################
    # Do not delete the return statement
    return sub1, sub2, merged_str


if __name__ == '__main__':
    main()
