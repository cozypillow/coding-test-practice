
palindrome=[]
T=int(input())
for _ in range(T):
    words=[]
    tf=False
    k=int(input())
    for i in range (k):
        words.append(input())
    for j in range (len(words)):
        words_except_word=words[:j]+words[j+1:]
        for word_2 in words_except_word:
            if (words[j]+word_2)==((words[j]+word_2)[::-1]):
                palindrome.append(words[j]+word_2)
                tf=True
    if tf is False:
        palindrome.append("0")            
for i in palindrome:
    print(i)
