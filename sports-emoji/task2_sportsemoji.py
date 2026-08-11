# Task 2: Sports Emojis 
# The user types 5 sports keywords separated by commas
# The program changes each keyword into an emoji
# If a keyword is not in my list, a confusion emoji is shown instead
# If there are not 5 keywords, or if a keyword is repeated, an error message is shown
# and the user has to type them again


# Dictionary that matches each keyword to one emoji
emoji_map = {
    "soccer": "⚽",
    "cricket": "🏏",
    "rugby": "🏉",
    "golf": "⛳",
    "volleyball": "🏐",
    "hockey": "🏒",
    "squash": "🎾",
    "bowling": "🎳",
    "table-tennis": "🏓",
    "handball": "🤾",
    "basketball": "🏀",
    "boxing": "🥊"
}

# The emoji used when the keyword is not found in the dictionary
confusion_emoji = "❓"

# This function checks the keywords the user typed
# It returns an error message, or an empty message if everything is fine
def check_keywords(keywords):

    # Check 1: there must be exactly 5 keywords
    if len(keywords) < 5:
        return "Error. Number of keywords is less than 5. Re-enter keywords"

    if len(keywords) > 5:
        return "Error. Number of keywords is more than 5. Re-enter keywords"

    # Check 2: no keyword is allowed to be entered twice
    # I put all the words in lower case first so "Soccer" and "soccer" counts as the same word 
    lower_keywords = []
    for word in keywords:
        lower_keywords.append(word.lower())

    for word in lower_keywords: 
        if lower_keywords.count(word) > 1:
            return "Error. Repeating keywords are not allowed. Re-enter keywords"

    # No problems found
    return ""


# This function changes each keyword into its emoji
def convert_to_emojis(keywords):
    emojis = []

    for word in keywords: 
        word = word.lower()

        if word in emoji_map: 
            emojis.append(emoji_map[word])
        else:
            # the keyword was not in my dictionary
            emojis.append(confusion_emoji)

    return emojis


# Main part of the program 
print("Enter 5 sports keywords separated by commas.")
print("Keywords you can use: Soccer, Cricket, Rugby, Golf, Volleyball,")
print("Hockey, Squash, Bowling, Table-tennis, Handball, Basketball, Boxing")
print()

while True: 
    # Get keywords from the user and split them on the commas
    user_input = input("Input: ")
    keywords = user_input.split(",")

    # strip() removes any spaces the user typed around the commas
    clean_keywords = []
    for word in keywords:
        clean_keywords.append(word.strip())

    # Check the keywords before converting them
    error_message = check_keywords(clean_keywords)

    # If there was a problem, show the message and let the loop ask again
    if error_message != "":
        print(error_message)
    else: 
        # Input was valid, so convert to emojis and stop the loop
        emoji_list = convert_to_emojis(clean_keywords)

        output = ""
        for emoji in emoji_list:
            output = output + emoji + " "

        print("Output:", output.strip())
        break