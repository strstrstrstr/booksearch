from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df1=pd.read_csv('df_all_file.csv',encoding='utf-8')


count_vect = CountVectorizer(min_df=0, ngram_range=(1,2))
genre_mat = count_vect.fit_transform(df_all['tag_list'])
genre_sim = cosine_similarity(genre_mat, genre_mat)