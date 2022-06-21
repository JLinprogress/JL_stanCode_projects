"""
File: best_photoshop_award.py
Name: Jerry Lee
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage
THRESHOLD = 1.2
BLACK = 140


def main():
    """
    創作理念：從小就嚮往在大公司上班，既然要進就要進最屌的FAANG，先用這張圖讓自己看一下以後在公司門前拍照是什麼樣子，
    藉此督促期許自己勇敢追夢，並相信自己一定可以做到的。(((o(*ﾟ▽ﾟ*)o)))
    """
    jl = SimpleImage('image_contest/JL.jpg') # 1108 x 1478
    jl.show()
    bg = SimpleImage('image_contest/amazon.jpg')
    bg.make_as_big_as(jl)
    new_img = combine(jl, bg)
    new_img.show()


def combine(jl, bg):
    for x in range(jl.width):
        for y in range(jl.height):
            jl_pixel = jl.get_pixel(x, y)
            avg = (jl_pixel.red + jl_pixel.green + jl_pixel.blue)//3
            total = jl_pixel.red + jl_pixel.green + jl_pixel.blue
            if jl_pixel.green > avg*THRESHOLD and total > BLACK:
                bg_pixel = bg.get_pixel(x, y)
                jl_pixel.red = bg_pixel.red
                jl_pixel.green = bg_pixel.green
                jl_pixel.blue = bg_pixel.blue
    return jl


if __name__ == '__main__':
    main()
