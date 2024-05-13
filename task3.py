import logging

# Логирование
logging.basicConfig(filename='my_log_3.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def count_words(text):
    try:
        words = text.split()
        num_words = len(words)
        logging.info(f'Number of words in the text: {num_words}')
        return num_words
    except Exception as e:
        logging.error(f'Error counting words: {e}')

count_words("The sun slowly set behind the mountains, painting the sky in shades of pink and orange.")
count_words("As she walked through the forest, she could hear the gentle rustling of leaves underfoot.")
count_words("The old house was rumored to be haunted, as strange noises were often heard coming from within.")
count_words("After a long day at work, he decided to unwind by taking a stroll along the beach.")
count_words("The city skyline looked breathtaking at night, with the lights twinkling like stars in the darkness.")
count_words("")
count_words(1)
count_words([1, 2, 3, 4, 5])