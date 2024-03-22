from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.cluster import KMeans

if __name__ == "__main__":
    print("聚类算法 start")

    # 文档集合
    corpus = [
        "I like great basketball game",
        "This video game is the best action game I have ever played",
        "I really really like basketball",
        "How about this movie? Is the plot great?",
        "Do you like RPG game?",
        "You can try this FPS game",
        "The movie is really great, so great! I enjoy the plot",
    ]

    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(corpus)
    # print("all features=", vectorizer.get_feature_names_out())
    # print("all frequency=", vectors)

    tfid_vectorizer = TfidfTransformer()
    tf_idf_res = tfid_vectorizer.fit_transform(vectorizer.fit_transform(corpus))
    tf_idf_arr = tf_idf_res.toarray()
    # print("tfid_arr=", tfid_arr)

    K = 3

    k_means = KMeans(n_clusters=K, n_init=10)
    s = k_means.fit(tf_idf_arr)

    # print("all core=", k_means.cluster_centers_)

    # print("all doc groups=", k_means.labels_)

    res_dic = {}
    for i in range(len(k_means.labels_)):
        label = k_means.labels_[i]
        if label not in res_dic.keys():
            res_dic[label] = []
        res_dic[label].append(corpus[i])
    print("res_dic=", res_dic)