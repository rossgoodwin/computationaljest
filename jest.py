'''
various routines to parse the annotated infinite jest
'''
import re

PATH_TO_JEST = "infinite_jest_annotated.txt"

def get_all_tags():
    jest = open(PATH_TO_JEST).read()
    p = re.compile(r'</.*?>') # finds the *closing* tags
    all_tags = p.findall(jest)
    all_tags = [x.replace("</", "<") for x in list(set(all_tags))]
    return all_tags
    
def get_all_text_for_tag():
    pass