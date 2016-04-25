# This Python file uses the following encoding: utf-8
'''
Created on Apr 24, 2016

@author: nhj
'''
from pypinyin import lazy_pinyin
from os import listdir, rename

def trans_to_pinyin(path):
    files = listdir(path)
    dict = get_new_name_dict(files)
    for file in files:
        rename(path + "\\" + file, path + "\\" + dict[file.decode('GBK')]);
    
def get_new_name_dict(files):
    dict = {}
    for file in files:
        dict[file.decode('GBK')] = process_file(file.decode('GBK')) 
    return dict

def process_file(file_name):
    words = lazy_pinyin(file_name)
    new_words = u""
    for word in words:
        new_words += word.title().replace("Mp3", "mp3")
    return new_words

if __name__ == '__main__':
    trans_to_pinyin("E:\CloudMusic - Copy")
    pass