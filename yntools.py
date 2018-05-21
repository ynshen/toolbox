def progressBar(pct):
    import sys
    sys.stdout.write('\r')
    # the exact output you're looking for:
    bar_num = int(round(pct * 20))
    sys.stdout.write("[%-20s] %d%%" % ('='*bar_num, pct*100))
    sys.stdout.flush()


def histogram_log():
    pass
