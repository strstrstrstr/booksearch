from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

df1=pd.read_csv(r'C:\booksearch2\booksearch\booksearch\pybo\df_all_file.csv',encoding='utf-8')
list_book = list(df1['bookname'].values)

count_vect = CountVectorizer(min_df=0, ngram_range=(1,2))
genre_mat = count_vect.fit_transform(df1['tag_list'])
genre_sim = cosine_similarity(genre_mat, genre_mat)

def find_sim_book(title_name):
    movie_index = df1[df1['bookname']==title_name].index.values[0]
    d = pd.DataFrame(genre_sim[movie_index])
    s = d.sort_values(0,ascending=False)
    result = list(s.index)[5:40]
    book=[]
    for temp in result:
        book.append(list_book[temp])
    book1 = list(set(book))
    count=0
    bookres=[]
    while len(bookres)!=5:
        count=count+1
        if title_name == book1[count]:
            continue
        bookres.append(book1[count])
    # print(bookres)
    return bookres
