import pickle
import os

def build_en_dict_from_MedDRA(medra_en_root_path,save_path="meddra_en_dict.pickle"):

    if not os.path.exists(medra_en_root_path):
        print("Error: Folder Not Found ", medra_en_root_path)
        return

    english_file_paths = [
        f"{medra_en_root_path}/MedAscii/llt.asc",
        f"{medra_en_root_path}/MedAscii/hlgt.asc",
        f"{medra_en_root_path}/MedAscii/pt.asc",
        f"{medra_en_root_path}/MedAscii/soc.asc"
        # "{medra_en_root_path}/MedAscii/meddra_history_english.asc"
    ]

    meddra_en_dict = {}

    def load_en_asc_file(file_path):
        for line in open(file_path, "r", encoding="utf-8"):
            fs = line.strip().split("$")
            # print("id",fs[0],"term",fs[1])
            if fs[0] not in meddra_en_dict.keys():
                meddra_en_dict[fs[0]] = fs[1]

    for fp in english_file_paths:
        load_en_asc_file(fp)

    pickle.dump(meddra_en_dict, open(save_path, "wb"))

def build_cn_dict_from_MedDRA(medra_cn_root_path,save_path="meddra_cn_dict.pickle"):

    if not os.path.exists(medra_cn_root_path):
        print("Error: Folder Not Found ", medra_cn_root_path)
        return

    chinese_file_paths = [
        f"{medra_cn_root_path}/asc-240/llt.asc",
        f"{medra_cn_root_path}/asc-240/hlgt.asc",
        f"{medra_cn_root_path}/asc-240/pt.asc",
        f"{medra_cn_root_path}/asc-240/soc.asc"
        # "{medra_cn_root_path}/MedAscii/meddra_history_chinese.asc"
    ]

    meddra_cn_dict = {}

    def load_cn_asc_file(file_path):
        for line in open(file_path, "r", encoding="utf-8"):
            fs = line.strip().split("$")
            # print("id",fs[0],"term",fs[1])
            if fs[0] not in meddra_cn_dict.keys():
                meddra_cn_dict[fs[0]] = fs[1]

    for fp in chinese_file_paths:
        load_cn_asc_file(fp)

    pickle.dump(meddra_cn_dict, open(save_path, "wb"))

def en_to_cn(src_en_path,en_dict_path,cn_dict_path,target_cn_path,target_en2cn_path):
    # load library
    meddra_en_dict=pickle.load(open(en_dict_path,'rb'))
    meddra_cn_dict=pickle.load(open(cn_dict_path,'rb'))

    dict_symptoms_en = pickle.load(open(src_en_path, "rb"))
    dict_symptoms_cn = {}

    def lookup_dict(dict, value):
        for k in dict.keys():
            if dict[k] == value:
                return k
        return -1

    counter_repeated_term = 0

    dict_en2cn_mapping = {}

    for key in dict_symptoms_en.keys():
        tf_idf = dict_symptoms_en[key]
        term_id = lookup_dict(meddra_en_dict, key)
        if term_id != -1:
            term_cn = meddra_cn_dict[term_id]
            if term_cn in dict_symptoms_cn.keys():
                counter_repeated_term += 1
            dict_symptoms_cn[term_cn] = tf_idf
            dict_en2cn_mapping[key] = term_cn

    dict_symptoms_cn = {k: v for k, v in sorted(dict_symptoms_cn.items(), key=lambda item: item[1], reverse=True)}

    # print(dict_symptoms_cn)
    pickle.dump(dict_symptoms_cn, open(target_cn_path, "wb"))
    pickle.dump(dict_en2cn_mapping, open(target_en2cn_path, "wb"))
