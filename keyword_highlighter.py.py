#Task 1: Keyword Highlighter

#Write a program that searches through reviews list and looks for keywords
#  such as "good", "excellent", "bad", "poor", and "average". 
# We want you to capitalize those keywords then print out each review. 
# Print out each review with the keywords in uppercase so they stand out.


reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
       "The product was average. Nothing extraordinary about it."
    
   ]

#So for the first string in the reviews list, we want it to say: 
# 
# "This product is really GOOD. I'm impressed with its quality."

words_to_upper = ["good", "excellent", "bad", "Poor", "average"]


def highlight_keywords():
    
    for review in reviews:
     
        for word in words_to_upper:
            i = review.find(word)
            
            if i == -1:
                continue
            else:
             
                replace = review.replace(word, word.upper())
        
            print(replace)
        
           
highlight_keywords()    





    # Task 2: Sentiment Tally

# Develop a function that tallies the number of positive and negative words in each review. 
# Use a predefined list of positive and negative words to check against.
# The function should return the count of positive and negative words for each review.
#python 
# positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
# negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]


reviews = [ "This product is really good. I'm impressed with its quality.",
            "The performance of this product is excellent. Highly recommended!", 
            "I had a bad experience with this product. It didn't meet my expectations.",
            "Poor quality product. Wouldn't recommend it to anyone.", 
            "The product was average. Nothing extraordinary about it." ]

words_to_upper = ["good", "excellent", "bad", "Poor", "average"]


def highlight_keywords():
    
    for review in reviews:
     
        for word in words_to_upper:
            i = review.find(word)
            
            if i == -1:
                continue
            else:
             
                replace = review.replace(word, word.upper())
        
            print(replace)
        
           
highlight_keywords()     
