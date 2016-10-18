if __name__ == '__main__':
    #total, x = 0, 1
    #sum_1_8 = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
    #print sum_1_8
    #x = int(raw_input("Enter a number: "))
    total = 0
    x = 1
    while x <= 8:
        if x == 5:
            x += 1
            raw_input('loop_pause')
            continue

        total += x
        x += 1
        #raw_input('pause')
        print total
        print x

print 'final total' + str(total)
print 'final x: {}' .format(x)
