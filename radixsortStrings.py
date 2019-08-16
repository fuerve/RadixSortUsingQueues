from myqueue import Queue
from orderedDictionary import OrderedDictionary
import string

def testSorted(mylist):
    if (len(mylist) < 2):
        return
    for i in range (len(mylist) - 1):
        assert(mylist[i] <= mylist[i+1])

def setupAuxQueuesDictionary():
    ''' Function to set up an OrderedDictionary that has 27 queues corresponding
    to ' ' and 26 alphabets added in correct order
    '''

    auxQueueDictionary = OrderedDictionary(Queue()*27)
    
    # auxQueueDictionary.__setitem__(" ",0)
    # for char in string.ascii_lowercase:
    #     auxQueueDictionary.__setitem__(char,0)

def updateQueue(mainQ, auxQ):
    ''' Function to add all the elements of auxQ queue to mainQ
    '''
    for item in auxQ:
        mainQ.update(item)

def charAt(s,i):
    ''' Function to return the character at index i of string s, it should
    return ' ' if no character at index i
    '''
    if (i >= len(s)):
        return ' '
    else:
        return s[i]        

def radixSortStrings(listOfStrings):
    ''' Function to sort the items in the listOfStrings using a radixsort algorithm
    '''
    # Create the mainqueue and enqueue the items from the listOfStrings
    mainqueue = Queue()
    for item in listOfStrings:
        mainqueue.enqueue(item)

    # Calculate the max length so that we know how many iterations we need to do
    maxLength = 0
    auxQ = Queue()
    for item in range(len(mainqueue)):
        temp = mainqueue.dequeue() 
        length = len(temp)
        auxQ.enqueue(temp)
        if length > maxLength:
            maxLength = length
    updateQueue(mainqueue,auxQ)

    # Initialize an ordered dictionary auxQueuesDictionary that holds 27 auxiliary queues for 27 characters
    # as keys: ' ' and 26 lower case letters. Make sure the keys are added in
    # alphabetical order so that when we iterate over the dictinary, keys are
    # retrieved in alphbetical order.
    setupAuxQueuesDictionary()
    auxQueueDictionary.__setitem__(" ",0)
    for char in string.ascii_lowercase:
        auxQueueDictionary.__setitem__(char,0)

    #Set up a for loop that sorts the items from the mainqueue based on
    # characters at index maxLength, then the characters at index maxLength-1,
    # maxLength-2, ...index 0. Every time using the auxiliary queues to do the sorting
    
    for strng in mainqueue:
        for index in range(maxLength-1,0,-1):
            char = charAt(strng,index)
            auxQueueDictionary.__setitem__(char,strng)

    for item in auxQueueDictionary
        temp = auxQueueDictionary.pop()
        mainqueue.enqueue(temp)

    sortedList = []
    # mainQueue should be sorted.
    # dequeue the items of the mainqueue into a list and return it
    for item in range(len(mainqueue)):
        temp = mainqueue.dequeue()
        sortedList.append(temp) 
    return sortedList
      
def main():
    print("Sorting lists of strings using radix sort using queues\n")

    lol = [['cat','hat','CAR','barn','farm','bat'],
           ['cat', 'hat','Cat','car','BARN', 'bat','one', 'ZOO','cow'],
           ["Initialize ","a","Dictionary","that holds","the","queues","corresponding to","the","individual","letters"],
            ["Iron Man", "Captain America", "Black Widow", "Hulk", "Thor",
             "Clint Barton","Loki"]]
             
    for lyst in lol:
        print("Before sorting: ")
        print(lyst)
        sortedlist = radixSortStrings(lyst)
        testSorted(sortedlist)
        print("After sorting: ")
        print(sortedlist, "\n")

if (__name__ == "__main__"):
    main()
    
