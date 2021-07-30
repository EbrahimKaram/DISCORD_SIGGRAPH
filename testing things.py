import pickle


if __name__ == '__main__':
    messages_to_monitor = [870745251017535508,870745212899717190,870745192704147507,870744923404656740,870745185364099143]
    message_pickle = 'message.pickle'
    with open(message_pickle, 'wb') as f:
        pickle.dump(messages_to_monitor, f)
