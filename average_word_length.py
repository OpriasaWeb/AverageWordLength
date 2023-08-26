# BEGIN
#   INPUT sentence "Please input a sentence: "
#   DECLARE sentence_length equals to 0
#   DECLARE words equals to split sentence
#   DECLARE average equals to 0
  
#   for i in sentence:
#     sentence_length plus one each iteration
  
#   average equals to sentence_length divided by words

#   PRINT float average

# END

sentence = input("Please input a sentence: ")
sentence_length = 0
words = sentence.split()
average = 0

for i in sentence:
  if i != " ":
    sentence_length = sentence_length + 1
    
average = sentence_length / len(words)

print(float(average))
  