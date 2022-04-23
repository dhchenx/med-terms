from medterms.wordcloud import *

if __name__=="__main__":
    src_file= "input/covid19_symptoms.pickle"
    mapping_file= "output/covid19_en2cn_terms.pickle"  # Mapping from english to chinese
    # show_word_cloud_with_mapping(src_file,mapping_file)
    show_word_cloud(src_file)