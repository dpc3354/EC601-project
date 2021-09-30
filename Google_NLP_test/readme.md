# Google_NLP_API test

## I use the word " Sunyi Feng is the one of the best starcraft player!" to test analyze_sentiment nalyze_text_entities and analyze_text_syntax functions 
### below are the outpust of my program

Text: Yifeng Sun is the one of the best starcraft player!
Sentiment: 0.8999999761581421, 0.8999999761581421
================================================================================
name           : Yifeng Sun
type           : PERSON
salience       : 53.6%
wikipedia_url  : -
mid            : /g/11gb558q0_
================================================================================
name           : one
type           : OTHER
salience       : 29.2%
wikipedia_url  : -
mid            : -
================================================================================
name           : starcraft player
type           : PERSON
salience       : 17.2%
wikipedia_url  : -
mid            : -
================================================================================
name           : one
type           : NUMBER
salience       : 0.0%
wikipedia_url  : -
mid            : -
sentences : 1
tokens    : 11
NOUN      : Yifeng
NOUN      : Sun
VERB      : is
DET       : the
NUM       : one
ADP       : of
DET       : the
ADJ       : best
NOUN      : starcraft
NOUN      : player
PUNCT     : !
================================================================================

## I use the words "StarCraft is a military science fiction media franchise created by Chris Metzen and James Phinney and owned by Blizzard Entertainment. The series, set in the beginning of the 26th century, centers on a galactic struggle for dominance among four species—the adaptable and mobile Terrans, the ever-evolving insectoid Zerg, the powerful and enigmatic Protoss, and the godlike Xel Naga creator race—in a distant part of the Milky Way galaxy known as the Koprulu Sector. The series debuted with the video game StarCraft in 1998. It has grown to include a number of other games as well as eight novelizations, two Amazing Stories articles, a board game, and other licensed merchandise such as collectible statues and toys." to test classify_text function

### the results are below:
category  : /Games/Computer & Video Games/Strategy Games
confidence: 94%
