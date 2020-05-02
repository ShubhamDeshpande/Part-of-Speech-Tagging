import nltk
test = "And now, for something completely different.".split(" ")
print nltk.pos_tag(test)
fread = open("corpus.txt")
input = fread.read()


sentence = input.split("\n")
correct = 0
incorrect = 0
for k in range(0, len(sentence)-1):
    #print sentence[k]
    parts = sentence[k].split(" ")
    new_sent = []
    new_sent_format = ""
    new_tag = []

    for i in range(0, len(parts)-1):
        #print parts[i].split("_")[0]
        #print parts[i].split("_")[1]
        word = parts[i].split("_")[0]
        tag = parts[i].split("_")[1]
        new_sent += [word]
        new_sent_format += (word+" ")
        new_tag += [tag]
    print new_sent_format
    result = nltk.pos_tag(new_sent)
    print result
    for i in range(0, len(result)-1):
        if(result[i][1]== new_tag[i]):
            #print "true"
            correct+=1
        else:
            #print "false"
            incorrect+=1

            #
    accuracy = correct/float(correct+incorrect)
    print ("accuracy is " + str(accuracy))
    #print "."
    #print "."
    #print "."

print "total correct tagging: " + str(correct)
print "total incorrect tagging " + str(incorrect)
print "final accuracy is "+ str(accuracy)
fread.close()

