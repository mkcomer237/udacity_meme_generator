"""Manual testing for the meme engine."""


from MemeEngine.MemeEngine import MemeEngine


# Specify the output file when instantiating the object
test_meme = MemeEngine('./memes/')
print(test_meme.make_meme('_data/photos/dog/xander_1.jpg',
                          'my amazing and pretty long quote',
                          'me'))

"""CLI tests.
python3 meme.py -> error missing argument
python3 meme.py '_data/photos/dog/xander_1.jpg' /
    --body 'wow this is a good quote' --author 'me'
    -> correcly adds the body and author to the image
python3 meme.py '_data/photos/dog/xander_1.jpg'
    -> generates a random meme
"""
