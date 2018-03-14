import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw            


def round_corners_one_image(original_image, image_apple):
    """ Rounds the corner of a PIL.Image
    
    original_image must be a PIL.Image
    Returns a new PIL.Image with rounded corners, where
    0 < percent_of_side < 1
    is the corner radius as a portion of the shorter dimension of original_image
    """

    width, height = image_apple.size
    original_image=original_image.resize((width, height))
    
    rounded_mask = PIL.Image.new('RGBA', (width, height))
     
    rounded_mask.paste(image_apple, (0,0))

    result = PIL.Image.new('RGBA', image_apple.size, (0,0,0,0))
    result.paste(original_image, (0,0), mask=rounded_mask)
    return result
    

def combine(directory=None):
    """ Saves a modfied version of each image in directory.
    
    Uses current directory if no directory is specified. 
    Places images in subdirectory 'modified', creating it if it does not exist.
    New image files are of type PNG and have transparent rounded corners.
    """
    
    if directory == None:
        directory = os.getcwd() 
        
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'promotions')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    absolute_filename = os.path.join(directory, 'apple.PNG')
    image_apple = PIL.Image.open(absolute_filename)
    
    absolute_filename = os.path.join(directory, 'incinerator-smokestack.jpg')
    image_smoke = PIL.Image.open(absolute_filename)
    
    new_image = round_corners_one_image(image_smoke,image_apple) 
        
    # Save the altered image, suing PNG to rroundaletain transparency
    new_image_filename = os.path.join(new_directory, 'apple.png')
    new_image.save(new_image_filename)    

    absolute_filename = os.path.join(directory, 'apple.PNG')
    image_apple = PIL.Image.open(absolute_filename)
    
    absolute_filename = os.path.join(directory, 'smokesquare.jpg')
    image_smoke = PIL.Image.open(absolute_filename)
    
    new_image = round_corners_one_image(image_smoke,image_apple) 
        
    new_image_filename = os.path.join(new_directory, 'applesquare.png')
    new_image.save(new_image_filename)    
    
    absolute_filename = os.path.join(directory, 'smokeportrait.jpg')
    image_smoke = PIL.Image.open(absolute_filename)
    
    new_image = round_corners_one_image(image_smoke,image_apple) 
        
    new_image_filename = os.path.join(new_directory, 'apple portrait.png')
    new_image.save(new_image_filename)    
    
    absolute_filename = os.path.join(directory, 'smokelandscape.jpeg')
    image_smoke = PIL.Image.open(absolute_filename)
    
    new_image = round_corners_one_image(image_smoke,image_apple) 
        
    new_image_filename = os.path.join(new_directory, 'applelandscape.png')
    new_image.save(new_image_filename)  
    