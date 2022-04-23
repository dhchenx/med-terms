from gensim import corpora, models
import gensim
import pickle
import os
from matplotlib import pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import matplotlib.colors as mcolors
import matplotlib

def show_word_cloud_with_mapping(src_file,mapping_file, num_topics=12,num_words=10,fig_v_num=3,fig_h_num=4,wc_max_words=10,num_pass=10):
    # ============ begin configure ====================
    NUM_TOPICS = num_topics
    NUM_WORDS = num_words
    FIG_V_NUM = fig_v_num
    FIG_H_NUM = fig_h_num
    WC_MAX_WORDS = wc_max_words
    NUM_PASS = num_pass
    # ============ end configure ======================

    current_path = os.path.dirname(os.path.realpath(__file__))

    # load data

    dict_dataset = pickle.load(open(src_file, "rb"))
    # print(dict_dataset)

    dict_en2cn_mapping = pickle.load(open(mapping_file, "rb"))

    # compile sample documents into a list
    # doc_set = [doc_a, doc_b, doc_c, doc_d, doc_e]
    doc_set = []
    for key, value in dict_dataset.items():
        list_new = []
        for w in value.split(","):
            if w in dict_en2cn_mapping.keys():
                list_new.append(dict_en2cn_mapping[w])
            else:
                list_new.append(w)
        doc_set.append(list_new)

    # list for tokenized documents in loop
    texts = []

    # loop through document list
    for tokens in doc_set:
        # clean and tokenize document string

        # stem tokens
        # stemmed_tokens = [p_stemmer.stem(i) for i in tokens]

        # add tokens to list
        texts.append(tokens)

    # turn our tokenized documents into a id <-> term dictionary
    dictionary = corpora.Dictionary(texts)

    # convert tokenized documents into a document-term matrix
    corpus = [dictionary.doc2bow(text) for text in texts]

    # generate LDA model
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=NUM_TOPICS, id2word=dictionary, passes=NUM_PASS)

    # print keywords
    topics = ldamodel.print_topics(num_words=NUM_WORDS, num_topics=NUM_TOPICS)
    for topic in topics:
        print(topic)

    # 1. Wordcloud of Top N words in each topic

    matplotlib.rcParams['font.family'] = 'SimHei'

    cols = [color for name, color in mcolors.XKCD_COLORS.items()]  # more colors: 'mcolors.XKCD_COLORS' TABLEAU_COLORS

    cloud = WordCloud(
        background_color='white',
        width=2500,
        height=1800,
        max_words=WC_MAX_WORDS,
        colormap='tab10',
        color_func=lambda *args, **kwargs: cols[i],
        prefer_horizontal=1.0, font_path=current_path+'/utils/fonts/SimHei.ttf')

    topics = ldamodel.show_topics(formatted=False, num_words=NUM_WORDS, num_topics=NUM_TOPICS)

    print("topic num:", len(topics))

    fig, axes = plt.subplots(FIG_V_NUM, FIG_H_NUM, figsize=(10, 10), sharex=True, sharey=True)

    for i, ax in enumerate(axes.flatten()):
        fig.add_subplot(ax)
        topic_words = dict(topics[i][1])
        cloud.generate_from_frequencies(topic_words, max_font_size=300)
        plt.gca().imshow(cloud)
        plt.gca().set_title('Topic ' + str((i + 1)), fontdict=dict(size=16))
        plt.gca().axis('off')

    plt.subplots_adjust(wspace=0, hspace=0)
    plt.axis('off')
    plt.margins(x=0, y=0)
    plt.tight_layout()
    plt.show()

def show_word_cloud(src_file,num_topics=12,num_words=10,fig_v_num=3,fig_h_num=4,wc_max_words=10,num_pass=10):
    # ============ begin configure ====================
    NUM_TOPICS = num_topics
    NUM_WORDS = num_words
    FIG_V_NUM = fig_v_num
    FIG_H_NUM = fig_h_num
    WC_MAX_WORDS = wc_max_words
    NUM_PASS = num_pass
    # ============ end configure ======================

    current_path = os.path.dirname(os.path.realpath(__file__))

    # load data

    dict_dataset = pickle.load(open(src_file, "rb"))
    # print(dict_dataset)


    # compile sample documents into a list
    # doc_set = [doc_a, doc_b, doc_c, doc_d, doc_e]
    doc_set = []
    for key, value in dict_dataset.items():
        list_new = []
        for w in value.split(","):
            list_new.append(w)
        doc_set.append(list_new)

    # list for tokenized documents in loop
    texts = []

    # loop through document list
    for tokens in doc_set:
        # clean and tokenize document string

        # stem tokens
        # stemmed_tokens = [p_stemmer.stem(i) for i in tokens]

        # add tokens to list
        texts.append(tokens)

    # turn our tokenized documents into a id <-> term dictionary
    dictionary = corpora.Dictionary(texts)

    # convert tokenized documents into a document-term matrix
    corpus = [dictionary.doc2bow(text) for text in texts]

    # generate LDA model
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=NUM_TOPICS, id2word=dictionary, passes=NUM_PASS)

    # print keywords
    topics = ldamodel.print_topics(num_words=NUM_WORDS, num_topics=NUM_TOPICS)
    for topic in topics:
        print(topic)

    # 1. Wordcloud of Top N words in each topic
    from matplotlib import pyplot as plt
    from wordcloud import WordCloud, STOPWORDS
    import matplotlib.colors as mcolors
    import matplotlib
    matplotlib.rcParams['font.family'] = 'SimHei'

    cols = [color for name, color in mcolors.XKCD_COLORS.items()]  # more colors: 'mcolors.XKCD_COLORS' TABLEAU_COLORS

    cloud = WordCloud(
        background_color='white',
        width=2500,
        height=1800,
        max_words=WC_MAX_WORDS,
        colormap='tab10',
        color_func=lambda *args, **kwargs: cols[i],
        prefer_horizontal=1.0, font_path=current_path+'/utils/fonts/SimHei.ttf')

    topics = ldamodel.show_topics(formatted=False, num_words=NUM_WORDS, num_topics=NUM_TOPICS)

    print("topic num:", len(topics))

    fig, axes = plt.subplots(FIG_V_NUM, FIG_H_NUM, figsize=(10, 10), sharex=True, sharey=True)

    for i, ax in enumerate(axes.flatten()):
        fig.add_subplot(ax)
        topic_words = dict(topics[i][1])
        cloud.generate_from_frequencies(topic_words, max_font_size=300)
        plt.gca().imshow(cloud)
        plt.gca().set_title('Topic ' + str((i + 1)), fontdict=dict(size=16))
        plt.gca().axis('off')

    plt.subplots_adjust(wspace=0, hspace=0)
    plt.axis('off')
    plt.margins(x=0, y=0)
    plt.tight_layout()
    plt.show()