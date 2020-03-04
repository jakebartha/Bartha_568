import sys

# create list that will show up in batch
words = []
words.append(sys.argv[1])
words.append(sys.argv[2])
words.append(sys.argv[3])
# couldn't get ys.argv to work therefore could not run.
# system cant find the batch file can not use commands that internet recommends to search for this batfile.  
for x in words:
    print ('there are' + str(len(x)) + str('this many letters') + str(x))
