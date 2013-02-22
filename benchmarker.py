import sys, string, random, hashlib, multiprocessing
from datetime import datetime

# burn CPU by computing the MD5 of a random string for n seconds
# returns the count of computed hashes into q
def computeRandomHashes(q, secondsToRun = 10):
  startTime = datetime.now()
  elapsedSeconds = 0
  numCalculated = 0
  while elapsedSeconds < secondsToRun:
    randString = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(32)).encode('utf8')
    h = hashlib.md5()
    h.update(randString)
    md5dString = h.hexdigest()
    elapsedSeconds = (datetime.now() - startTime).seconds
    numCalculated += 1
  q.put(numCalculated)

# takes a run
if __name__ == '__main__':
  usage = 'usage: %s [secondsToRun] [requiredBenchmark]'
  if(len(sys.argv) != 3):
    print(usage % sys.argv[0])
    sys.exit(-1)
  secondsToRun = int(sys.argv[1])
  requiredBenchmark = int(sys.argv[2])
  
  resultQueue = multiprocessing.Queue()
  cpuCount = multiprocessing.cpu_count()
  
  processes = [multiprocessing.Process(target = computeRandomHashes, args = (resultQueue, secondsToRun,)) for i in range(cpuCount)]
  
  sumCalculated = 0
  startTime = datetime.now()
  print('Starting %i processes for %i seconds...' % (cpuCount, secondsToRun))
  for p in processes:
    p.start()
  for p in processes:
    p.join()
    sumCalculated += resultQueue.get()
  
  print()
  print('Elapsed time: ' + str(datetime.now() - startTime))
  print('Computed hashes: %i' % sumCalculated)
  print()
  
  if(sumCalculated < requiredBenchmark):
    print('FAILED (required: %i)' % requiredBenchmark)
    sys.exit(-1)
  else:
    print('SUCCESS')
    sys.exit(0)
