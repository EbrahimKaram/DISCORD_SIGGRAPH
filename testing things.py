import pickle


if __name__ == '__main__':


    # messages_to_monitor =[870745185364099143,870745192704147507,870745212899717190,870745251017535508] # test


    messages_to_monitor = [871441078459465768, 871441084620890152,
                           871441092992708658, 871441104225046569]  # production


    # message_pickle = 'messages_test.pickle'  # test
    message_pickle = 'messages_production.pickle'  # production
    with open(message_pickle, 'wb') as f:
        pickle.dump(messages_to_monitor, f)

