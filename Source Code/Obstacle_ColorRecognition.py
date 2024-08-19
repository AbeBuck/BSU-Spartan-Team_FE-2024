def colorRecognitionThreshold(greenThreshold, redThreshold): 
    if  ( (get_recoColorRGB_more (0, 0, 2)> ()) and  (get_recoColorRGB_more (0, 0, 2)>get_recoColorRGB_more (0, 1, 2))):
        MakerLED_ALLColorLED (0, #0000ff);
        MakerLED_ALLColorLED (2, #0000ff);
    else:
        if  (get_recoColorRGB_more (0, 1, 2)> ()):
            MakerLED_ALLColorLED (0, #ff0000);
            MakerLED_ALLColorLED (2, #ff0000);
        else:
            MakerLED_CloseColorLED (5);

camera_recoColorRGB_more (0, 0, 0, 0, 100, -128, -15, 9, 50, 0, 0, 160, 120);
camera_recoColorRGB_more (0, 0, 1, 0, 100, 22, 127, -50, 127, 0, 0, 160, 120);
data_setvariableto (0, 0);

while True:
        Maker_displayFont (0);
        Maker_displayWordsPos (gPix, 5, 0);
        Maker_displayWordsPos (rPix, 5, 16);

    Maker_displayWordsPos(get_recoColorRGB_more (0, 0, 2), 50, 0);
    Maker_displayWordsPos(get_recoColorRGB_more (0, 1, 2), 50, 16);
    colorRecognitionThreshold(150, 180);
    data_changevariableby(0, 1);
