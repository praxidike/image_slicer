
#from .main import slice
from main import slice, join, join_in_row

im_path01 = '/home/dfki.uni-bremen.de/fstern/Bilder/Messreihe02/VideoPictures/PCWand/00001.jpg'
im_path02 = '/home/dfki.uni-bremen.de/fstern/Bilder/Messreihe02/VideoPictures/PCWand/01000.jpg'
im_path03 = '/home/dfki.uni-bremen.de/fstern/Bilder/Messreihe02/VideoPictures/PCWand/00500.jpg'
im_path04 = '/home/dfki.uni-bremen.de/fstern/Dokumente/motiv-kleines-monster.gif'

a = slice('/home/dfki.uni-bremen.de/fstern/Bilder/Messreihe02/VideoPictures/PCWand/00001.jpg', 1, save=False)
b = slice('/home/dfki.uni-bremen.de/fstern/Bilder/Messreihe02/VideoPictures/PCWand/01000.jpg', 1, save=False)

#print(a)
#print(type(b[0]))
#print(b[0].position)
#b[0].coords=(1920,0)
#im = join((a[0], b[0]))
#im.show()
#im.save('/home/dfki.uni-bremen.de/fstern/Dokumente/test-join.jpg')

im = join_in_row([im_path04, im_path04, im_path04])
im.save('/home/dfki.uni-bremen.de/fstern/Dokumente/test-join.jpg')