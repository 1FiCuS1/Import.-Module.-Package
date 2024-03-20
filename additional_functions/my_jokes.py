import pyjokes
def get_jokes():
    joke = pyjokes.get_joke('en', 'all')
    return joke
