#!/usr/bin/env python
 
# Anwesh Kumar Sahoo | Poster for 'The Garden Tantra' in GIMP Python
 
from gimpfu import *
 
def poster(file1, file2, file3, file4, text, text2, fontsize, fontsize2, font, colorBack, colorFore):
 
        # make a new image. Size A4.
        imgW, imgH = 2480, 3508
        img = gimp.Image(imgW, imgH, RGB)
        gimp.message("created a new image")

        pdb.gimp_context_set_background(colorBack)
        pdb.gimp_context_set_foreground(colorFore)

        gimp.message("created colors")

        # make a background layer
        background = gimp.Layer(img, "background", imgW, imgH, RGB_IMAGE, 100, NORMAL_MODE)
        background.fill(BACKGROUND_FILL)
        img.add_layer(background, 1)
        gimp.message("created background")

        
        # make a new text layer for book name
        textLayer = pdb.gimp_text_fontname(img, None, imgW/2, imgH/2, text, 10, True, fontsize, PIXELS, font)
        textLayer.translate(-textLayer.width + textLayer.width/2 + textLayer.width/6, -textLayer.height/2)
        gimp.message("created text")

        # seting the text color (using the user-defined colorFore parameter)
        # also adding leading of -150 and setting justification to right
        pdb.gimp_text_layer_set_color(textLayer, colorFore) #adding chosen color to the text
        pdb.gimp_text_layer_set_line_spacing(textLayer, -150) #adding text leading value of -150 to reduce extra spacing between every word in the line
        pdb.gimp_text_layer_set_justification(textLayer, 1) #justify right with value 1


        # make image layer 1
        image1 = pdb.file_png_load(file1, file1)
        pdb.gimp_image_scale(image1, imgW * 2, imgH)
        pdb.gimp_edit_copy(image1.layers[0])
        imageLayer1 = gimp.Layer(img, "image 1", imgW * 2, imgH, RGBA_IMAGE, 100, NORMAL_MODE)
        img.add_layer(imageLayer1,1)
        floatingLayer = pdb.gimp_edit_paste(imageLayer1, True)
        pdb.gimp_floating_sel_anchor(floatingLayer)
        imageLayer1.translate(imgW - imageLayer1.width + 1100, 0)

        # make image layer 2
        image2 = pdb.file_png_load(file2, file2)
        pdb.gimp_image_scale(image2, imgW * 2, imgH * 11/10)
        pdb.gimp_edit_copy(image2.layers[0])
        imageLayer2 = gimp.Layer(img, "image 2", imgW * 2, imgH * 11/10, RGBA_IMAGE, 100, NORMAL_MODE)
        img.add_layer(imageLayer2,1)
        floatingLayer = pdb.gimp_edit_paste(imageLayer2, True)
        pdb.gimp_floating_sel_anchor(floatingLayer)
        imageLayer2.translate(imgW - imageLayer2.width + imgW/3, imgH/10 - imgH/8)

        # make image layer 3
        image3 = pdb.file_png_load(file3, file3)
        pdb.gimp_image_scale(image3, imgW * 11/10, imgH * 1/3 * 14/10)
        pdb.gimp_edit_copy(image3.layers[0])
        imageLayer3 = gimp.Layer(img, "image 3", imgW * 11/10 * 11/10, imgH * 1/3 * 14/10 * 11/10, RGBA_IMAGE, 100, NORMAL_MODE)
        img.add_layer(imageLayer3,1)
        floatingLayer = pdb.gimp_edit_paste(imageLayer3, True)
        pdb.gimp_floating_sel_anchor(floatingLayer)
        imageLayer3.translate(imgW - imageLayer3.width + imgW/10, imgH/10 - imgH/4)

        # make image layer 4
        image4 = pdb.file_png_load(file4, file4)
        pdb.gimp_image_scale(image4, imgW * 21/10, imgH * 11/10)
        pdb.gimp_edit_copy(image4.layers[0])
        imageLayer4 = gimp.Layer(img, "image 4", imgW * 21/10, imgH * 11/10, RGBA_IMAGE, 100, NORMAL_MODE)
        img.add_layer(imageLayer4,1)
        floatingLayer = pdb.gimp_edit_paste(imageLayer4, True)
        pdb.gimp_floating_sel_anchor(floatingLayer)
        imageLayer4.translate(imgW - imageLayer4.width + imageLayer4.width/8, imgH/8 - imgH/10 - imgH/16 + imgH/30) 

        # make a new text layer for the copyright
        textLayer2 = pdb.gimp_text_fontname(img, None, imgW/2, imgH/2, text2, 10, True, fontsize2, PIXELS, font)
        textLayer2.translate(-textLayer2.width/2, textLayer2.height * 4)
        gimp.message("created copyright")
        
        # textLayer2 will be used as its shadow layer, hence set to black
        pdb.gimp_text_layer_set_color(textLayer2, "#000000")

        # duplicate textLayer2 to create a highlight
        highlightLayer = textLayer2.copy()
        highlightLayer.name = "Copyright Highlight"
        img.add_layer(highlightLayer)

        # offsetting the highlight layer
        pdb.gimp_layer_translate(highlightLayer, -1, 0)

        # setting the color of the highlight layer to white
        pdb.gimp_text_layer_set_color(highlightLayer, (255, 255, 255))

        # adjusting the opacity of the highlight layer to 100, no transparency
        pdb.gimp_layer_set_opacity(highlightLayer, 100)

        
        # create a new image window
        gimp.Display(img)
        # show the new image window
        gimp.displays_flush()



register(
              "python_fu_poster",
              "Anwesh Sahoo Poster",
              "Create a new image for Garden Tantra with 4 images",
              "ST",
              "Copyright@ST",
              "2023",
              "Anwesh Sahoo Poster",
              "", # Create a new image, don't work on an existing one
              [
                  (PF_FILE, "file1", "Choose Image 1", ""),
                  (PF_FILE, "file2", "Choose Image 2", ""),
                  (PF_FILE, "file3", "Choose Image 3", ""),
                  (PF_FILE, "file4", "Choose Image 4", ""),
                  (PF_STRING, "text", "Choose Title", "The\nGarden\nTantra"),
                  (PF_STRING, "text2", "Choose Copyright", "Embrace Its Wisdom"),
                  (PF_SPINNER, "fontsize", "Font Size Title", 300, (300, 300, 360)),
                  (PF_SPINNER, "fontsize2", "Font Size Copyright", 160, (160, 160, 220)),
                  (PF_FONT, "font", "Font Type", "Black Knife Demo"),
                  (PF_COLOR, "colorBack", "Background Color", (255, 255, 255)),
                  (PF_COLOR, "colorFore", "Foreground Color", (2, 2, 180)),
                  
              ],
              [],
              poster,
              menu="<Image>/File/Create/Assign2"
)
 
main()
 

