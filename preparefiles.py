#! /usr/bin/env python

import os


def main():
    if not os.path.exists("sentences.csv"):
        os.system("wget http://tatoeba.org/files/downloads/sentences.csv")
    if not os.path.exists("links.csv"):
        os.system("wget http://tatoeba.org/files/downloads/links.csv")

    sentences = {}
    #ghost = {}
    
    senfile = open("sentences.csv")
    while True:
        line = senfile.readline()
        if line == '':
            break
        line = line.strip()
        try:
            id, lang, sen = line.split('\t')
        except ValueError:
            pass # some asshole entered an empty sentence
        sentences[id] = line


    linkfile = open("links.csv")
    while True:
        line = linkfile.readline()
        if line == '':
            break
        line = line.strip()
        main_sentence, translated_sentence = line.split('\t')
        try:
            tr = sentences[translated_sentence]
        except KeyError:
            #ghost[translated_sentence] = 0
            continue # there is a sentence that is linked but doesnt exist
        
        try:
            tr_id, tr_lang, tr_sen = tr.split('\t')[:3]
        except:
            continue
        
        try:
            sentences[main_sentence] += '\t' + tr_lang + ':' + tr_sen
        except KeyError:
            #ghost[main_sentence] = 0
            continue

    #l = []
    #for k in ghost:
    #    l.append(k)
    #l.sort()
    #for i in l:
    #    print i

    outfiles = {}

    try:
        os.mkdir("data/")
    except: pass
    for k in sentences:
        lang = sentences[k].split('\t')[1]
        if not outfiles.has_key(lang):
            outfiles[lang] = file("data/" + lang + ".csv", "w")
        outfiles[lang].write(sentences[k]+'\n')




if __name__ == '__main__':
    main()
