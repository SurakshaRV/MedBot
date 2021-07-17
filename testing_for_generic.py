from math import log
from textblob import TextBlob
l=[]
words = open("dict.txt").read().split()
wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words))
maxword = max(len(x) for x in words)


def infer_spaces(s):
    """Uses dynamic programming to infer the location of spaces in a string
    without spaces."""

    # Find the best match for the i first characters, assuming cost has
    # been built for the i-1 first characters.
    # Returns a pair (match_cost, match_length).
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)

    # Build the cost array.
    cost = [0]
    for i in range(1,len(s)+1):
        c,k = best_match(i)
        cost.append(c)

    # Backtrack to recover the minimal-cost string.
    out = []
    i = len(s)
    while i>0:
        c,k = best_match(i)
        assert c == cost[i]
        out.append(s[i-k:i])
        i -= k
    return " ".join(reversed(out))

def fn(st):
        flag=0
        with open("F:/upload/uploads/dict.txt") as openfile:
            for line in openfile:
                for part in line.split('\n'):
                    if (st==part or st.lower()==part):
                        flag=1
        return flag

def main(l1):
    l=l1.split()
    #f1=open("test1_corrected.txt",'w')
    output=''
    for i in l:
        if(fn(i)==1):
            #print(i," exists.")
            #f1.write(i+" ")
            output+=i+" "
        else:
            flag2=1
            #print(i," doesnt exists")
            s=infer_spaces(i)
            l=len(s)-len(i)+1
            for j in s.split():
                 if(fn(j)==0):
                     flag2=0
                     break
            if(flag2==1):
                for j in s.split():
                    #print(j," exists")
                    #f1.write(j+" ")
                    output+=j+" "
            if(flag2==0):
                    b=TextBlob(i)
                    str1=b.correct()
                    if(fn(b.correct())==1):
                        #print(b.correct()," exists")
                        #f1.write(str(str1)+" ")
                        output+=str(str1)+" "
            
    return output
if __name__=="__main__":
    i=main('What col thing to say')
