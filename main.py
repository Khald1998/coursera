punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as p_f:
    for line in p_f:
        # print(line)
        if line[0] != ';' and line[0] != '\n':
            positive_words.append(line.strip())
# print(positive_words)
positive_words = [word.lower() for word in positive_words]

negative_words = []
with open("negative_words.txt") as n_f:
    for line in n_f:
        # print(line)
        if line[0] != ';' and line[0] != '\n':
            negative_words.append(line.strip())
# print(negative_words)
negative_words = [word.lower() for word in negative_words]


def get_pos(pword):
    count=0
    words=pword.split()
    for word in words:
        word = word.lower()
        word= strip_punctuation(word)
        if word in positive_words:
            count+=1
    return count

def get_neg(nword):
    count=0
    words=nword.split()
    for word in words:
        word = word.lower()
        word= strip_punctuation(word)
        if word in negative_words:
            count+=1
    return count

def strip_punctuation(s):
    for x in s:
        if x in punctuation_chars:
            s = s.replace(x, "")
    return s

outfile = open("resulting_data.csv","w")
outfile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
outfile.write('\n')


fileconnection = open("project_twitter_data.csv", 'r')

lines = fileconnection.readlines()
print(lines)
header = lines[0]
field_names = header.strip().split(',')
print(field_names)
for row in lines[1:]:
    
    vals = row.strip().split(',')
    row_string = '{},{},{},{},{}'.format(vals[1],vals[2],get_pos(vals[0]),get_neg(vals[0]),get_pos(vals[0])-get_neg(vals[0]))
    outfile.write(row_string)
    outfile.write('\n')


outfile.close()
