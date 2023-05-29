from textblob import TextBlob


# Function to perform sentiment analysis
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"


# Main program loop
def main():
    while True:
        text = input("Enter some text (or 'q' to quit): ")

        if text.lower() == "q":
            print("Goodbye!")
            break

        sentiment = analyze_sentiment(text)
        print("Sentiment:", sentiment)


# Run the program
if __name__ == "__main__":
    main()
