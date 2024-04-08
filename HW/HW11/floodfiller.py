def floodFill(image, sr, sc, color):
    if image is None:
        return []
    
    color1 = image[sr][sc]
    width = len(image)
    height = len(image[0])

    flood(image, sr, sc, color, color1, width, height)
    return image


def flood(image, sr, sc, color2, color1, width, height):
    if sr < 0 or sr >= width:
        return

    if sc < 0 or sc >= height:
        return
    
    if image[sr][sc] == color2:
        return
    
    if image[sr][sc] != color1:
        return
        
    image[sr][sc] = color2

    flood(image, sr+1, sc, color2, color1, width, height)
    flood(image, sr, sc+1, color2, color1, width, height)

    flood(image, sr-1, sc, color2, color1, width, height)
    flood(image, sr, sc-1, color2, color1, width, height)
 
        

# image = [
#     [1,1,1],
#     [1,1,0],
#     [1,0,1]
# ]
# sr = 1
# sc = 1
# color = 2
# tester = floodFill(image, sr, sc, color)
# print(tester)
