

def cmd_judge(word,cmd):
    if word.startswith(cmd)==True:
        search_word=word.removeprefix(cmd)
        search_word=search_word.lstrip()
        return search_word


    


    



    