from rrb3 import *
rr = RRB3();


while(1):
    while(rr.get_distance() > 10):
        rr.set_motors(1,1,1,0);

    while(rr.get_distance() < 30):
        rr.set_motors(1,1,1,1);