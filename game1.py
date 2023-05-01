secret_answer = "Amman"
answer = ""
count = 0
limit = 3 
lose = False
while secret_answer != answer and not lose:
    if count < limit:
        answer = input("What is capital of jordan ")
        count+=1
    else:
        lose = True
if lose:
    print('you lose')
else:
     print('you win')
   