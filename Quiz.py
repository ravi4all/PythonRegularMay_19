file = open('questions.txt')
data = file.readlines()
#print(data)

options = [['Modi','Rahul','Arvind','Yogi'],['Meerut','Delhi','Pune','Mumbai'],
           ['Dhoni','Kohli','Rohit','Sachin'],['CSK','RCB','MI','SRH']]

answers = ['modi','delhi','kohli','mi']
counter = 0
for i in range(len(data)):
    print(data[i])
    for option in options[i]:
        print(option)
    ans = input("Enter your ans : ").lower()
    if ans == answers[i]:
        counter += 1
    print("--------------------")
print("Final Result :",counter,"out of",len(answers))
file.close()
