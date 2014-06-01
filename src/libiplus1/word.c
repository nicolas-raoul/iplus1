#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "iplus1.h"
#include "word.h"







int iplus1_word_init(iplus1_word_t* word, char* str)
{
    word->str = strdup(str);
    word->sen_count = 1; // NULL terminated
    word->sentences = NULL;
    
    return IPLUS1_SUCCESS;
}

int iplus1_word_destroy(iplus1_word_t* word)
{
    free(word->str);
    free(word->sentences);
    
    return IPLUS1_SUCCESS;
}

int iplus1_word_add_sentence(iplus1_word_t* word, iplus1_sentence_t* sen)
{
    word->sen_count++;
    
    word->sentences = realloc(word->sentences, word->sen_count*sizeof(iplus1_sentence_t*));
    if (word->sentences == NULL)
        return IPLUS1_FAIL;
    word->sentences[word->sen_count-2] = sen;
    word->sentences[word->sen_count-1] = NULL;
    
    /*int i;
    for(i = 0; word->sentences[i] != NULL; i++) {
        printf("%s: %s\n", word->str, word->sentences[i]->str);
    }*/
    
    return word->sen_count;
}




