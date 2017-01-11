import time

# Display instructions
print('Press ENTER to begin timing.  Afterwards, press ENTER to record each finisher time.  Press Ctrl+C to quit.')
input()  # press Enter to begin
print('Started')
startTime = time.time()
finishNum = 1

# start tracking
try:
    while True:
        input()
        finishTime = round(time.time()-startTime,3)
        print('Finisher #%s: %s' % (finishNum,finishTime),end='')
        finishNum += 1
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to prevent error from displaying
    print('\nDone.')
