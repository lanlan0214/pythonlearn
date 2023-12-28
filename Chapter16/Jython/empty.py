# 用圖片的
# releases gatech jes (搜尋引擎)
# https://github.com/gatech-csl/jes/releases
# 選這個下載 jes-6.0-windows-java-included.zip
####################################################################### 下面都是用jython寫的
# pickAFile()
# f = pickAFile() 找到一個本機的圖片
# p = makePicture(f) 製作一個圖片
# show(p) 就可以看到圖片
# explore(p) 這是可以看到圖片 然後可以看到x,y值還有RGB 有點像按鍵精靈 可以看到裡面顏色
# getwidth(p) 圖片寬
# getheight(p) 圖片高
# getPixels(p) 這個是裡面全部的RGB 然後返回一個list所以當照片很大張 就會很多...慎用
# getPixel(p,100,100) 可以知道 這格的RGB
# getColor(pixel(p,100,100)) 可以拿到這個顏色 返還一個color object
# getRed(pixel)
# getGreen(pixel)
# getBlue(pixel)
####################################################################### setColor()下面是講解大概順序
# Jython built-in Color Objects
# def change_all_to_red(pic):
#     for p in getPixels(pic):
#         setColor(p, red)
# 這個會把圖片整個變成紅色的
# f = pickAFile()
# p = makePicture(f)
# change_all_to_red(p) 這時候整張圖都會變紅色的
# explore(p)
####################################################################### setRed()
# 因為上面是有把整張圖片都變成紅色的 所以在這樣就可以了
# p = makePicture(f)
# explore(p) 變正常圖片了
# def clearRed(pic):
#     for p in getPixels(pic):
#         setRed(p, 0)
# clearRed(p)
# explore(p) 圖片偏變藍綠的 因為R全部變0 以此類推 getGreen 跟 getBlue也是
####################################################################### makeColor()
# def change_all_to_new_color(pic):
#     new_color = makeColor(100, 50, 125)
#     for p in getPixels(pic):
#         setColor(p, new_color)
# f = pickAFile()
# p = makePicture(f)
# change_all_to_new_color(p)
# explore(p) 這時候整張圖都會變成你設定的那個顏色
####################################################################### 如果忘記有哪些function 可以看視窗上面有個JESfunction那裡面可以看 然後會有解釋
####################################################################### 圖片右上角換成黑色
# def black_top_right_corner(pic):
#     w = getWidth(pic)
#     h = getHeight(pic)
#     for p in getPixels(pic):                    ######### for x in range(w/2, w):         //右邊這個跟左邊一樣 但是程式碼比較好
#         x = getX(p)                             #########   for y in range(h/2):
#         y = getY(p)                             #########       p =getPixel(pic, x, y)
#         if x > (w/2) and y < (h/2):             #########       setColor(p, black)
#             setColor(p, black)               
#      writePictureTo(pic, '路徑\\檔名.png')    
####################################################################### pickFolder()
####################################################################### 要讓圖片變亮
# def brighter(picture):
#     for px in getPixels(picture):
#         r = getRed(px)
#         g = getGreen(px)
#         b = getBlue(px)
#         new_color = makeColor(r*1.3, g*1.3, b*1.3)
#         setColor(px, new_color)

# terminal
# f = pickAFile()
# p = makePicture(f)
# brighter(p)
# explore(p)
####################################################################### 假的夕陽
# def make_sunset(picture):
#     for p in getPixels(picture):
#         b = getBlue(p)
#         g = getGreen(p)
#         setBlue(p, b*0.7)
#         setGreen(p, g*0.7)
####################################################################### 黑變白白變黑有點像X光片圖效果
# def negative(pic):
#     for px in getPixels(pic):
#         r = getRed(px)
#         g = getGreen(px)
#         b = getBlue(px)
#         negColor = makeColor(255 - r, 255 - g, 255 - b)
#         setColor(px, negColor)
####################################################################### 照片換成灰白
# def grayscale(pic):
#     for p in getPixels(pic):
#         x = (getRed(p) + getGreen(p) + getBlue(p)) / 3
#         setColor(p, makeColor(x, x, x))
####################################################################### 拷貝圖然後中間會被分割然後像是倒影的圖片
# def copyHalf(pic):
#     pixels = getPixels(pic)
#     for i in range(0, len(pixels)/2):
#         p1 = pixels[i]
#         c1 = getColor(p1)
#         p2 = pixels[len(pixels) - 1 - i]
#         setColor(p2, c1) #p2顏色換成c1
#     writePictureTo(pic, '路徑')
####################################################################### 拷貝圖然後中間會被分割然後都是正的圖片,只是剩一半
# def copyHalf2(pic):
#     pixels = getPixels(pic)
#     for i in range(0, len(pixels)/2):
#         p1 = pixels[i]
#         c1 = getColor(p1)
#         p2 = pixels[i + len(pixels) /2 ]
#         setColor(p2, c1) #p2顏色換成c1
#     writePictureTo(pic, '路徑')
####################################################################### 找類似的顏色 distance() 這個fun可以看差多少顏色的值
# def blud_panda(pic):
#     for x in range(140, 450):
#         for y in range(35, 320):
#             p = getPixels(pic, x, y)
#             c = getColor(p)
#             if distance(c, white) < 200:
#                 setColor(p, blue)
####################################################################### edge_detection()很像用起來黑白照手的 然後如果想要畫起外框就看一下fill fold
# def edge_detection(source):
#     for px in getPixels(source):
#         x = getX(px)
#         y = getY(px)
#         if y < getHeight(source) - 1 and x < getWidth(source) - 1:
#             sum = getRed(px) + getGreen(px) + getBlue(px)
#             botrt = getPixels(source, x + 1, y + 1)
#             sum2 = getRed(botrt) + getGreen(botrt) + getBlue(botrt)
#             diff = abs(sum2 - sum)
#             newColor = makeColor(diff, diff, diff)
#             setColor = (px, newColor)
#     writePictureTo(source, '路徑')
####################################################################### Chromakey 背景的技術 太空熊貓 算是合成圖 背景+上已知圖
# def chromakey(source, bg):
#     for px in getPixels(source):
#         x = getX(px)
#         y = getY(px)
#         if (getRed(px) + getBlue(px)) < getGreen(px):
#             bgpx = getPixel(bg, x, y)
#             bgcol = getColor(bgpx)
#             setColor(px, bgcol)