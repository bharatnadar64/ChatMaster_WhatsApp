import random
import json
import pickle
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import SGD

# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')

lemmatizer = WordNetLemmatizer()

# Load intents data
intents = json.load(open('Dataset/intents2.json'))

words = []
classes = []
documents = []
ignore_letters = ['?', '!', '.', ',']

# Process each sentence in intents
for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# Lemmatize and filter out unwanted characters
words = [lemmatizer.lemmatize(word.lower()) for word in words if word not in ignore_letters and word.isalpha()]
words = sorted(set(words))

# Sort classes
classes = sorted(set(classes))

# Save words and classes to pickle files
pickle.dump(words, open('files/words2.pkl', 'wb'))
pickle.dump(classes, open('files/classes2.pkl', 'wb'))

# Prepare training data
training = []
output_empty = [0] * len(classes)

for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]

    # Create the bag of words for the current sentence
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    # Create the output row (one-hot encoding)
    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])

# Shuffle the training data to avoid any biases
random.shuffle(training)

# Convert training list into a numpy array
training = np.array(training, dtype=object)

# Split data into X (inputs) and Y (outputs)
train_x = np.array(list(training[:, 0]), dtype='float32')  # The input features
train_y = np.array(list(training[:, 1]), dtype='float32')  # The output labels

# Build the model
model = Sequential()
model.add(Dense(400, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(200, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

# Compile the model
sgd = SGD(learning_rate=0.01, weight_decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Train the model
model.fit(train_x, train_y, epochs=200, batch_size=5, verbose=1)

# Save the trained model
model.save('files/chatbot_model2.keras')
print("Done")
