def solution(s):
    data = s

    num = ["0","1","2","3","4","5",
           "6","7","8","9",]
    
    eng = ["zero","one","two","three","four",
     "five","six","seven","eight","nine"]
    
    for i in range(len(data)):
        for j in range(len(eng)):
            if eng[j][0:2] == data[i:i+2]: 
                data = data.replace(eng[j],num[j])
    answer = print(data)
    return answer

solution("23four5six7")