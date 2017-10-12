if __name__ == '__main__':
   
    # Read the input
    Mlen = int(raw_input())
    M_str = raw_input().split()
    Nlen = int(raw_input())
    N_str = raw_input().split()
    
    #Convert the String arry to set
    M_list = list(map(int,M_str))
    M_Set = set(M_list)    
    N_list = list(map(int,N_str))
    N_Set = set(N_list)
    
    # M_Set : 2 4 5 9     N_Set : 2 4 11 12    
 
    #Elements exists only in M
    M_diff_set = M_Set.difference(N_Set) # 9, 5
    
    #Elements exists only in N
    N_diff_set = N_Set.difference(M_Set) #11 12
    
    Symetric_difference_set = M_diff_set.union(N_diff_set)
    Symetric_difference_list = list(Symetric_difference_set)
    Symetric_difference_list.sort()
    for i in Symetric_difference_list:
        print i
