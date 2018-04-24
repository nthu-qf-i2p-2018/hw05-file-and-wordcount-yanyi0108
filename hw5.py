
# coding: utf-8

# In[2]:


import string
import csv

def main(filename):
    lines = open("i_have_a_dream.txt").readlines()
    all_words = []

    for line in lines:
        line=line.strip()
        words=line.split()

        for word in words:
            word=word.strip(string.punctuation)
            if word != '':
                all_words.append(word)
    from collections import Counter
    word_counter = Counter(all_words)
    
    with open('word_count.csv','w',newline='') as csv_file:
        writer = csv.writer(csv_file)
       
        writer.writerow(['word', 'count'])   #命名他的表頭

        writer.writerows(word_counter.most_common()) #將內容列入

    # dump to a json file named "wordcount.json"

    import json
    json.dump(word_counter.most_common(),open('word_count.json','w'))

    # BONUS: dump to a pickle file named "wordcount.pkl"
    # hint: dump the Counter object directly

    import pickle
    pickle.dump(word_counter.most_common(),open('word_count.pkl','wb'))
    
    
    
if __name__ == '__main__':
    main("i_have_a_dream.txt")    

