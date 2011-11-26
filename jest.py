'''
various routines to parse the annotated infinite jest
'''
import re
import pdb

PATH_TO_JEST = "infinite_jest_annotated.txt"

def get_all_tags():
    jest = open(PATH_TO_JEST).read()
    p = re.compile(r'</.*?>') # finds the *closing* tags
    all_tags = p.findall(jest)
    all_tags = [x.replace("</", "<") for x in list(set(all_tags))]
    return all_tags
    
def get_tags_in_text(text):
    p = re.compile(r'<.*?>') # finds the *closing* tags
    all_tags = p.findall(text)
    tags = [x for x in list(set(all_tags))]
    # which are close tags?
    return all_tags
    

def is_close_tag(tag):
    return tag.startswith("</")
    
    
def get_all_text_for_tag():
    pass
    
def get_jest():
    return open(PATH_TO_JEST).readlines()
    
def get_tags_for_segments():
    '''
    return a tuple of segments and their tags; the tags will be removed
    from the text of the segments
    '''
    # the way to do this is a forward pass through the whole text
    # keeping track of open tags
    open_tags, tags_for_segments = [], []
    segments = get_segments()
    tags_opened_d = {}
    for i, segment in enumerate(segments):
        print "on segment %s. open tags: %s" % (i, open_tags)
        #pdb.set_trace()
        tags_in_segment = get_tags_in_text("\n ".join(segment))
        tags_closed_in_segment = [t for t in tags_in_segment if is_close_tag(t)]
        tags_opened_in_segment = [t for t in tags_in_segment if not is_close_tag(t)]
        
        # keep a record of when we opened each tag
        for new_tag in tags_opened_in_segment:
            # don't overwrite tags
            if not new_tag in tags_opened_d:
                tags_opened_d[new_tag] = i
            if new_tag in open_tags:
                pdb.set_trace()
                
        # take the already open tags, and anything opened in this segment
        tags_in_segment = open_tags + tags_opened_in_segment
        tags_for_segments.append(list(tags_in_segment))
        
        open_tags = tags_in_segment
        
        #
        # now remove tags from open_tags that were closed in this segment
        for tag in tags_closed_in_segment:
            try:
                cur_tag = tag.replace("</", "<")
                open_tags.remove(cur_tag)
                if cur_tag not in open_tags and cur_tag in tags_opened_d.keys():
                    # remove it from the dictionary
                    tags_opened_d.pop(cur_tag)
            except:
                print "whoops."
                pdb.set_trace()
    
    return (tags_for_segments, segments, tags_opened_d)
       
def get_segments():
    segments = []
    cur_segment = []
    JEST = get_jest()
    for line in JEST:
        if line == "\n": 
            # blank line; this is a segment
            segments.append(cur_segment)
            cur_segment = []
        else:
            cur_segment.append(line)
    return segments