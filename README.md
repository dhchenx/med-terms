# Med-Terms

Medical Term Dictionary built from MedDRA

## Installation

```pip
pip install med-terms
```

## Let Codes Speak
Example 1: Build term dicionaries from MedDRA data in English and Chinese versions, and creating term mapping file.
```python
import pickle

from medterms.MedDRA import *

if __name__=="__main__":
    # create the dictionary from the MedDRA knowledge base including Chinese and English versions
    meddra_en_root="input/MedDRA_24.0_English_0"
    meddra_cn_root="input/MedDRA_24_0_Chinese"
    build_en_dict_from_MedDRA(meddra_en_root, save_path="output/en_dict.pickle")
    build_cn_dict_from_MedDRA(meddra_cn_root, save_path="output/cn_dict.pickle")
    # Mapping from english terms to chinese terms according to MedDRA dictionaries
    en_to_cn(src_en_path='input/covid19_en_terms.pickle',  # input
             en_dict_path='output/en_dict.pickle', cn_dict_path='output/cn_dict.pickle',  # input
             target_cn_path='output/covid19_cn_terms.pickle', target_en2cn_path='output/covid19_en2cn_terms.pickle') # output
    # check data files (pickle format)
    print(pickle.load(open('input/covid19_en_terms.pickle', 'rb')))
    print(pickle.load(open('output/covid19_cn_terms.pickle', 'rb')))
    print(pickle.load(open('output/covid19_en2cn_terms.pickle', 'rb')))
```

Example 2: Show word cloud from the entire dictionary or part of the dictionary.

```python
from medterms.wordcloud import *

if __name__=="__main__":
    src_file= "input/covid19_symptoms.pickle"
    mapping_file= "output/covid19_en2cn_terms.pickle"  # Mapping from english to chinese
    # show_word_cloud_with_mapping(src_file,mapping_file)
    show_word_cloud(src_file)
```


## License
The `med-terms` project is provided by [Donghua Chen](https://github.com/dhchenx). 

NOTE: This project does not include MedDRA data due to license issue. 