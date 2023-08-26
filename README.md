# Average Word Length

Instructions: Given a sentence as input, calculate and output the average word length of that sentence.
To calculate the average word length, you need to divide the sum of all word lengths by the number of words in the sentence.

Sample Input:
this is some text

Sample Output:
3.5

Explanation: There are 4 words in the given input, with a total of 14 letters, so the average length will be: 14/4 = 3.5

Pseudocode:





            BEGIN
              INPUT sentence "Please input a sentence: "
              DECLARE sentence_length equals to 0
              DECLARE words equals to split sentence
              DECLARE average equals to 0
              
              for i in sentence:
                sentence_length plus one each iteration
              
              average equals to sentence_length divided by words

              PRINT float average

            END