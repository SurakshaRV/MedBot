import csv
import random
from fuzzywuzzy import fuzz
flag1=0
def response(question):
    question=question.lower()
    fin=open("F:/upload/uploads/temp_questions.tsv")
    read_tsv=csv.reader(fin,delimiter="\t")
    global flag1
    for row in read_tsv:
        if(row[0].lower().strip("?")==question):
            flag1=1;
            return row[1]
    fin1=open("F:/upload/uploads/temp_questions.tsv")
    read_tsv1=csv.reader(fin1,delimiter="\t")
    if(flag1!=1):
        for row in read_tsv1:
            if(fuzz.token_sort_ratio(row[0],question)>80):
                flag1=2
                return row[1]
        fin2=open("F:/upload/uploads/temp_questions.tsv")
        read_tsv2=csv.reader(fin1,delimiter="\t")
        for row in read_tsv2:
            if(fuzz.token_sort_ratio(row[0],question)>70):
                return row[1]
def main():
    print("medical chat test called")

if __name__=='__main__':
    main()

