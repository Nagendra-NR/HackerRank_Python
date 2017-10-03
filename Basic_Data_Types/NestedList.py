if __name__ == '__main__':
    students_data = []
    
    name_list = []
    score_list = []
    
    heighest_score = 0
    previous_heighest = 0
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_list.append(name)
        score_list.append(score)
        List1 = [name, score]
        students_data.append(List1)
        
    #print("student_data : ", students_data)
    
    #sort and reverse the score list
    score_list.sort()
    score_list.reverse()
    
    #Remove all lowest score items
    lowest_score = score_list.pop()
    while lowest_score in score_list :
        score_list.remove(lowest_score)
    
    #Now, the last element will be the second lowest score
    second_lowest_score = score_list.pop()   
    #print ("second_lowest_score : ", second_lowest_score)
    
    final_list = []
    
    for sublist in students_data :
        #print("",sublist[0],":", sublist[1])
        if(sublist[1] == second_lowest_score):
            #print("found : ", sublist[0])
            final_list.append(sublist[0])
     
    final_list.sort()
    
    for student in final_list :
        print(student)
