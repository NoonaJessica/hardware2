import filefifo

fifo = filefifo.Filefifo('samplecapture03.txt')
count = 0
while True:
    if not fifo.empty():
        value = fifo.get()
        # note: ADC values are always unsigned
        # a negative value is returned by filefifo at the end of file
        if value < 0: # if filefifo reaches end of file get() returns -1
            break

        count += 1
        if count >= 10: # print every 10th sample
            print(value)
            count = 0
