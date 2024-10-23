""" Task 3: Review Summary

Implement a script that takes the first 30 characters of a review and appends
 "…" to create a summary. 
 
 Ensure that the summary does not cut off in the middle of a word.

Example: "This product is really good. I'm...", """

reviews = [ "This product is really good. I'm impressed with its quality.",
            "The performance of this product is excellent. Highly recommended!", 
            "I had a bad experience with this product. It didn't meet my expectations.",
            "Poor quality product. Wouldn't recommend it to anyone.", 
            "The product was average. Nothing extraordinary about it." ]

def summarize_review(string, index):
    

    if index >= len(string):
        return string

    for i in range(index, len(string)):
        if string[i].isspace():
            return string[:i]

    return string

for review in reviews:


    string = review
    index = 29

    result = summarize_review(string, index)
    print(result)  # Output: "This is a" 
