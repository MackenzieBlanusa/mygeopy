import numbers
#import sys
#sys.path.append('/Users/mackenzie/Documents/Research/PhD/URSSI/mygeopy/mygeopy')
from mygeopy.triangle import hypot

def test_hypot():
    assert hypot(3,4) == 5
    assert hypot(6,8) == 10
    assert hypot(9,12) == 15
    assert hypot(12,16) == 20
