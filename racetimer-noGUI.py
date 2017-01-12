import time
import csv

# Display instructions
print('Press ENTER to begin timing.  Afterwards, press ENTER to record each finisher time.  Press Ctrl+C to quit.')
input()  # press Enter to begin
print('Started')
startTime = time.time()
finishNum = 1
times=[]
finishers=[]

# start tracking
try:
    while True:
        input()
        finishTime = round(time.time()-startTime,3)
        print('Finisher #%s: %s' % (finishNum,finishTime),end='')
        times.append(finishTime)
        finishers.append(finishNum)
        finishNum += 1
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to prevent error from displaying
    print('\nDone. \nWriting to file "results.csv"')
    with open('results.csv','w') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerows(zip(finishers,times))
    
    

    
