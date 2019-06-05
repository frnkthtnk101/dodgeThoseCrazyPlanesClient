##scores stuff

##function to increase score

### function to increase score
def score_flag(y):
    miles=.010203
    #print (y)
    if y <500 and y>=400:
        return miles
    elif y<401.0 and y>=300.0:
        return miles * 1.5
    elif y<300.0 and y>=200.0:
        return miles * 2.0
    elif y < 200.0:
        return miles * 3