def rgb_to_hsv(red, green, blue):
    r_norm = red/255
    green_norm = green/255
    blue_norm = blue/255
    C_max = max(r_norm, green_norm, blue_norm)
    C_min = min(r_norm, green_norm, blue_norm)
    delta = C_max - C_min
    hue = 0
    saturation = 0
    lightness = (C_max + C_min)/2
    if (delta != 0):
        if (C_max == r_norm):
            hue = 60 * (((green_norm - blue_norm)/delta) % 6)
        elif (C_max == green_norm):
            hue = 60 * (((blue_norm - r_norm)/delta) + 2)
        elif (C_max == blue_norm):
            hue = 60 * (((r_norm - green_norm)/delta) + 4)
        saturation = delta/(1 - abs(2*lightness - 1))
    return round(hue), round(saturation * 100), round(lightness * 100)
