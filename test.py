volume1 = 6*8*4.5
volume2 = 3.2*5*7.3
total_volume= volume1+volume2
try:
    assert total_volume==302
    print("OK")
except:
    print("Not OK")