import re

# To get a probability on which response to give
def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing',], required_words=['how', 'you'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Our hours are \nMon - Fri: 9am - 9pm \nSaturday: 9am - 10pm \nSunday: Closed', ['what', 'hours', 'are', 'you', 'open'], required_words=['open'])
    response('Our Price for 1 lane is $22 per hour.', ['how', 'much', 'cost'], required_words=['cost'])
    response('We have 5 different weights for our Bowling Balls: \n8lb \n9lb \n10lb \n11lb \n12lb', ['how', 'much', 'does', 'weigh'], required_words=['weigh'])
    response('We have Party Deals! You can make a reservation to get an extra lane at no cost!', ['do', 'you', 'do', 'parties'], required_words=['parties'])
    response('We have a bar and grill for food! See our Menu for the options!', ['do', 'you', 'have', 'food', 'there'], required_words=['food'])
    response('Our Address is: [Example Address Here!]', ['what', 'is', 'the', 'bowling', 'alley', 'address'], required_words=['address'])
    response('Our Number to call is: [Example Phone Number Here!]', ['what', 'is', 'the', 'phone', 'number'], required_words=['number'])
    response('We aren\'t currently hosting any events right now.', ['what', 'events', 'are', 'there'], required_words=['events'])
    # Responses -------------------------------------------------------------------------------------------------------

    best_match = max(highest_prob_list, key=highest_prob_list.get)

    return 'I don\'t understand' if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

