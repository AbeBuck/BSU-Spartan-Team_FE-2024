import image, sensor, time
from micropython import const
from pupremote import PUPRemoteSensor, OPENMV

camera = PUPRemoteSensor(power = True)
camera.add_channel('blob', to_hub_fmt = 'hhhhhh')

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 500)
sensor.set_vflip(True)
sensor.set_hmirror(True)
clock = time.clock()

_GREEN = const((0, 100, -128, -10, 20, 127))
_RED = const((0, 100, 7, 127, -10, 127))
# format: (Lmin, Lmax, Amin, Amax, Bmin, Bmax)

while True:
    img = sensor.snapshot()

    gBlobs = img.find_blobs([_GREEN], roi = [0, 0, 320, 240], pixels_threshold = 150)
    gBlob, gPix, gCx, gCy = None, 0, 0, 0

    for g in gBlobs:
        if ((g.h() > g.w() or (g.y() + g.h()) == 240) and g.pixels() > gPix and g.density() > 0.6):
            gPix = g.pixels()
            gBlob = g

    if (gBlob != None):
        gDen = gBlob.density()
        gCx = gBlob.cx()
        gCy = gBlob.cy()
        img.draw_rectangle(gBlob.rect(), (238, 39, 55), 2)

    rBlobs = img.find_blobs([_RED], roi = [80, 0, 160, 240], pixels_threshold = 250)
    rBlob, rPix, rCx, rCy = None, 0, 0, 0

    for r in rBlobs:
        if (r.pixels() > rPix):
            rPix = r.pixels()
            rBlob = r

    img.draw_rectangle([80, 0, 160, 240], thickness = 2)

    if (rBlob != None):
        rCx = rBlob.cx()
        rCy = rBlob.cy()
        img.draw_rectangle(rBlob.rect(), color = (68, 214, 44), thickness = 2)

    camera.update_channel('blob', gCx, gCy, gPix, rCx, rCy, rPix)
    camera.process()
