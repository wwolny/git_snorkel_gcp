import os
import pandas as pd
import xml.etree.ElementTree as et
import random
from sklearn.model_selection import train_test_split

df_dict = {}
y_dict = {}
columns = ["text", "who", "dir_name", "relationship"]
arr_conv = [[], [], [], []]
idd= 0
for root, dirs, files in os.walk("/home/wojtek/4Semantics/Tutorials/Snorkel/snorkel-tutorials/spam/pelcra_sp_2/"):
   for dir in dirs:
       for sroot, sdirs, sfiles in os.walk("/home/wojtek/4Semantics/Tutorials/Snorkel/snorkel-tutorials/spam/pelcra_sp_2/"+str(dir)):
            if "header.xml" in sfiles:
                xtree = et.parse("/home/wojtek/4Semantics/Tutorials/Snorkel/snorkel-tutorials/spam/pelcra_sp_2/"+str(dir)+"/header.xml")
                xroot = xtree.getroot()
                # print(xroot[0][2][0][0].text)
                if "rodzinne" in xroot[0][2][0][0].text:
                    arr_conv[3].append(1)
                elif "koleżeńskie" in xroot[0][2][0][0].text or "koleżankami" in xroot[0][2][0][0].text:
                    arr_conv[3].append(0)
                else:
                    break
                arr_conv[2].append(dir)
                ttree = et.parse("/home/wojtek/4Semantics/Tutorials/Snorkel/snorkel-tutorials/spam/pelcra_sp_2/"+str(dir)+"/text_structure.xml")
                troot = ttree.getroot()
                arr_conv[0].append([])
                arr_conv[1].append([])
                for elem in troot[1][1][0]:
                   arr_conv[0][idd].append(elem.text)
                   arr_conv[1][idd].append(elem.attrib.get('who'))
                idd+=1

for iddf in range(len(arr_conv[2])):
    df_dict[arr_conv[2][iddf]] = pd.DataFrame(list(zip(arr_conv[0][iddf], arr_conv[1][iddf])))
    y_dict[arr_conv[2][iddf]] = arr_conv[3][iddf]

# for key in df_dict.keys():
#     print("\n" + "=" * 40)
#     print(key)
#     print("-" * 40)
#     print(df_dict[key])




#    for idf, fname in enumerate(files):
#        xtree = et.parse("/home/wojtek/4Semantics/Tutorials/Snorkel/snorkel-tutorials/spam/pelcra_sp_2/snorkel/"+str(fname))
#        xroot = xtree.getroot()
#        arr_conv[0].append([])
#        arr_conv[1].append([])
#        arr_conv[2].append(fname)
#        for elem in xroot[1][1][0]:
#            arr_conv[0][idf].append(elem.text)
#            arr_conv[1][idf].append(elem.attrib.get('who'))
#
# print(len(arr_conv[0][1]))
# print(len(arr_conv[1][1]))
# for iddf in range(len(arr_conv[2])):
#     df_dict[arr_conv[2][iddf]] = pd.DataFrame(list(zip(arr_conv[0][iddf],arr_conv[1][iddf])))
#
# for key in df_dict.keys():
#     print("\n" + "=" * 40)
#     print(key)
#     print("-" * 40)
#     print(df_dict[key])

#pojedyńczy plik
# xtree = et.parse("/home/wojtek/4Semantics/Tutorials/Snorkel/snorkel-tutorials/spam/pelcra_sp_2/snorkel/text_structure.xml")
# xroot = xtree.getroot()
#
# print(xroot[1][1][0].tag)
# print(xroot.attrib)
#
# text = []
# speaker = []
#
# for elem in xroot[1][1][0]:
#     text.append(elem.text)
#     speaker.append(elem.attrib.get('who'))
#
# df = pd.DataFrame()
# df["who"] = speaker
# df["text"] = text
# print(df.head())

#pojedynczy header
# xtree = et.parse("/home/wojtek/4Semantics/Tutorials/Snorkel/snorkel-tutorials/spam/pelcra_sp_2/720-3-PELCRA_72030100005014/header.xml")
# xroot = xtree.getroot()
#
# print(xroot[1][2].text)

# text = []
# speaker = []
#
# for elem in xroot[1][1][0]:
#     text.append(elem.text)
#     speaker.append(elem.attrib.get('who'))
#
# df = pd.DataFrame()
# df["who"] = speaker
# df["text"] = text
# print(df.head())

# print(len(df_dict))
# print(len(arr_conv[3]))
# X_train = random.choice(list(df_dict.items()), int(len(df_dict)*7/10))
# y_test = {}
# for key in X_train.keys():
#     if not key in df_dict.keys():
#         y_test[key] = df_dict.get(key)
# y_valid = random.choice(list(y_test.items(), int(len(y_test)/2)))
# for key in y_valid.keys():
#     y_test.pop(key)
# X_train, X_test, y_train, y_test = train_test_split(arr_conv, arr_conv[3], test_size=0.33, random_state=42)

ABSTAIN = -1
FRIENDS = 0
FAMILY = 1


from snorkel.labeling import labeling_function

# @labeling_function
# def lf_contains_famliy(x):
#     return