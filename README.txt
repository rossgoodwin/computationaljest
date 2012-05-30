Infinite Jest narrative corpus, version 1, 2012
---
This is the text of Infinite Jest (David Foster Wallace, 1996) manually annotated (by me) with narrative tags. Each tag "<NARRATIVE-NAME>" corresponds to a narrative. I initially attempted to tag many sub-narratives; e.g., "PGOAT", "HAL" and many other individual characters. This is complex to do correctly, and I'm only a single annotator, so ***I advise only using the <EHDRH>,<AFR> and <ETA> narratives; these are relatively well-defined and hence reliable***. It would be very useful to acquire an additional set of annotations for these tags to assess agreement, and I encourage anyone interested on working on this to contact me. For curious parties, I describe the main narratives below.

AFR -- This is the tale of the wheelchair assassins, a Qu\`{e}b\`{e}cois terrorist group, and their attempts to seize an original copy of a dangerous film.
 Focalizer: Marathe.
 
EHDRH -- The Ennet House Drug Recovery House (sic). This narrative concerns the going-ons at a drug recovery house. 
 Focalizer: Don Gately.
 
ETA -- This narrative follows the students and faculty at the Enfield Tennis Academy. 
  Focalizer: Hal.
  
Text that covers the going-ons of the AFR, especially involving Marathe, I thus tagged as <AFR>; I considered text that describes events relevant to the Ennett drug recovery house <EHDRH> and events involving the Ennett tennis academy as <ETA>. I break down statistics regarding the proportion of the whole these sub-narratives comprise in the paper (below). 

The <INC> narrative is also reasonably clear-cut; any text that deals with any of the Incandenza family members (Hal, Himself, The Moms, etc.) or PGOAT meets this criteria.

The task in the paper was to assign *passages*, which are clearly defined in Infinite Jest by breaks (these are sort of like mini-chapters) to the narratives to which they belong (if any). There are 183 such passages. I've included extracted passages (one per file) in the "narratives_segment.zip" folder. I've also included these by narrative; so the sub-directory "AFR", for example, includes the passages in which an <AFR> tag spans any text. Finally, I've included a directory filled with the named entities I extracted from each passage using the NLTK toolkit (I didn't do anything fancy; just off-the-shelf NER): these files can be found in the "NEs.zip" file. 

Some (mostly undocumented) code is provided for parsing this file in jest.py.

Citation
---
Byron C. Wallace. Multiple Narrative Disentanglement: Unraveling Infinite Jest. In Proc. of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT), 2012.

Contact
---
byron.wallace@gmail.com