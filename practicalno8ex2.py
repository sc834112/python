# Text Moderation Filter

feedback = input("Enter your feedback: ")

# Target words to be filtered
target_words = ["bad", "hate", "stupid"]

# Replace target words with ****
for word in target_words:
    feedback = feedback.replace(word, "****")
    feedback = feedback.replace(word.capitalize(), "****")
    feedback = feedback.replace(word.upper(), "****")

print("Filtered Feedback:", feedback)