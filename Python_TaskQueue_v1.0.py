import queue
import time


startTime = time.time()
def getTimeSinceStart():
    return round(time.time() - startTime, 2)


# definition of our tasks
def drinkBeer(id, target):
    time.sleep(0.3)
    time = getTimeSinceStart()
    print(f"{time} (ID {id}) {target}: burp")


def smokeCigarette(id, target):
    time.sleep(0.3)
    time = getTimeSinceStart()
    print('{time} (ID {id}) {target}: puff')


def goToToilet(id, target):
    time.sleep(0.3)
    print('{time} (ID {id}) {target}: {result}'.format(time = getTimeSinceStart(), id = id, target = target, result = 'wizz'))

# link task names to functions and rate limiting information
taskConfig = dict(
    drinkBeer = dict(
        func = drinkBeer,
        rateLimit = 5 # how often may this task be executed per second
    ),
    smokeCigarette = dict(
        func = smokeCigarette,
        rateLimit = 3 # how often may this task be executed per second
    ),
    goToToilet = dict(
        func = goToToilet,
        rateLimit = 2 # how often may this task be executed per second
    ),
)

# fill queue with jobs that should be done to a target
jobs = queue.Queue()
jobs.put(( 1, 'dave', 'drinkBeer'))
jobs.put(( 2, 'dave', 'smokeCigarette'))
jobs.put(( 3, 'dave', 'drinkBeer'))
jobs.put(( 4, 'dave', 'goToToilet'))
jobs.put(( 5, 'dave', 'drinkBeer'))
jobs.put(( 6, 'cris', 'smokeCigarette'))
jobs.put(( 7, 'cris', 'drinkBeer'))
jobs.put(( 8, 'cris', 'drinkBeer'))
jobs.put(( 9, 'cris', 'goToToilet'))
jobs.put((10, 'cris', 'smokeCigarette'))
jobs.put((11, 'andi', 'drinkBeer'))
jobs.put((12, 'andi', 'smokeCigarette'))
jobs.put((13, 'andi', 'drinkBeer'))
jobs.put((14, 'andi', 'goToToilet'))
jobs.put((15, 'andi', 'drinkBeer'))
jobs.put((16, 'nick', 'smokeCigarette'))
jobs.put((17, 'nick', 'drinkBeer'))
jobs.put((18, 'nick', 'drinkBeer'))
jobs.put((19, 'nick', 'goToToilet'))
jobs.put((20, 'nick', 'smokeCigarette'))
jobs.put((21, 'phil', 'drinkBeer'))
jobs.put((22, 'phil', 'smokeCigarette'))
jobs.put((23, 'phil', 'drinkBeer'))
jobs.put((24, 'phil', 'goToToilet'))
jobs.put((25, 'phil', 'drinkBeer'))
jobs.put((26, 'maxi', 'smokeCigarette'))
jobs.put((27, 'maxi', 'drinkBeer'))
jobs.put((28, 'maxi', 'drinkBeer'))
jobs.put((29, 'maxi', 'goToToilet'))
jobs.put((30, 'maxi', 'smokeCigarette'))

####################################################################
#################### START ASSIGNMENT BELOW ########################
####################################################################

# execute the jobs
while not jobs.empty():
    job = jobs.get()
    jobID = job[0]
    jobTarget = job[1]
    jobTaskName = job[2]
    taskFunction = taskConfig[jobTaskName]['func']
    taskFunction(jobID, jobTarget)

print('done')
