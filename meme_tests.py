from MemeEngine.MemeEngine import MemeEngine


# Specify the output file when instantiating the object
test_meme = MemeEngine('./memes/')
print(test_meme.make_meme('_data/photos/dog/xander_1.jpg', 
                          'my amazing and pretty long quote',
                          'me'))
