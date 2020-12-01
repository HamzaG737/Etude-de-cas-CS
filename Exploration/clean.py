### Define cleaning function 
import re 
dict_sub = {
    "\n": " ",
    "\x89Û_": "",  # Special characters
    "\x89ÛÒ": "",
    "\x89ÛÓ": "",
    "\x89ÛÏWhen": "When",
    "\x89ÛÏ": "",
    "\x89Û÷": "",
    "\x89Ûª": "",
    "\x89Û\x9d": "",
    "å_": "",
    "\x89Û¢": "",
    "\x89Û¢åÊ": "",
    "åÊ": "",
    "åÈ": "",
    "Ì©": "e",
    "å¨": "",
    "&gt;": ">",  # Character entity references
    "&lt;": "<",
    "&amp;": "&",
    "http\S+|www.\S+": "",
    "@[A-Za-z0-9]+":""
}
dict_replace = {"...": " ... ", "'": " ' "}


def clean(tweet):
    #tweet=p.clean(tweet)
    for key, val in dict_sub.items():
        tweet = re.sub(r"{}".format(key), val, tweet)
    for key, val in dict_replace.items():
        tweet = tweet.replace(r"{}".format(key), val).strip()

    # Punctuations at the start or end of words
    for punctuation in "@!?()[]*%":
        tweet = tweet.replace(punctuation, " {} ".format(punctuation)).strip()
    
    tweet=tweet.replace('#','')
    if "http" not in tweet:
        tweet = tweet.replace(":", " : ").strip()
        tweet = tweet.replace(".", " . ").strip()
    return tweet