from quixstreams import Application

app = Application(
    broker_address="localhost:9092",
    consumer_group="text-splitter",
    auto_offset_reset="earliest",
)

jokes_topic = app.topic(name="jokes", value_deserializer="json")

sdf = app.dataframe(topic=jokes_topic)

# def print_message(message):
#     print(message)
# sdf.update(print_message)
sdf.update(lambda message: print(f"Input message: {message}"))

# transformations
def split_words(message):
    return [{"word": word} for word in message["joke_text"].split()]


sdf = sdf.apply(split_words, expand=True)

sdf["length"] = sdf["word"].apply(lambda word: len(word))

sdf.update(lambda row: print(f"Output: {row}"))

if __name__ == "__main__":
    app.run()
