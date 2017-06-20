import logging
import time

with open('logging.yaml') as f:
    conf = yaml.safe_load(f)
    conf.setdefault('version', 1)
    logging.config.dictConfig(conf)
    logger = logging.getLogger('dac_logger')


class SearchAndSort(object):
    """ A Python class with implementing two Divide and Conquer algorithms - Binary Search and Merge Sort """

    def __init__(self, items, key=0):
        """ Initialize Python object

        Keyword arguments:
        items -- the list to operate on
        key -- the item to search for (in case of Binary Search)
        """

        self.items = items
        self.item_length = len(items)
        self.key = key

    def binary_search(self):

        """ Implements the Binary Search algorithm

            Returns:
                A boolean. True if the key was found, False otherwise.
        """

        self.items = self.merge_sort()
        left = 0
        right = self.item_length-1
        while(right >= left):
            midpoint = (left+right) / 2

            if self.items[midpoint] == self.key:
                return True

            if self.items[midpoint] > self.key:
                right = midpoint - 1

            if self.items[midpoint] < self.key:
                left = midpoint + 1
        logger.info('Search completed.')
        return False

    def merge_sort(self):
        """ Implements the Merge Sort algorithm

            Returns:
                A sorted list (items).
        """

        left = 0
        right = self.item_length-1
        midpoint = (left + right) / 2

        if len(self.items) > 1:
            sorted_list = self.merge( self.divide(left, midpoint), self.divide(midpoint+1,right) )
            logger.info('The list has been sorted!')
            print 'Sorted list : ', sorted_list
            return sorted_list
        else:
            logger.warning('Nothing to sort in a list with one item.')
            return self.items

    def divide(self, left, right):
        """ A recurisve helper function for merge sort.

        Args:
            left: the leftmost index of the current split
            right: the rightmost index of the current split
        Returns:
            A merged List after sorting and merging its two subtrees
        """

        if right != left:
            midpoint = (left+right)/2
            return self.merge(self.divide(left, midpoint), self.divide(midpoint+1, right))

        logger.debug('Returning : {}'.format(self.items[left]))
        return [self.items[left]]

    def merge(self, a, b):
        """ Helper function for merging two lists

        Args:
            a: left list
            b: right list
        Returns:
            A merged List after sorting and merging its two subtrees
        """

        merged_list = []
        longer_list = a if len(a) > len(b) else b
        shorter_list = b if len(a) > len(b) else a

        j = k = 0
        while True:
            if j == len(a) or k == len(b):
                break
            if a[j] > b[k]:
                merged_list.append(b[k])
                k += 1
            else:
                merged_list.append(a[j])
                j += 1

        for i in range(len(a)-j):
            merged_list.append(a[j])
            j += 1
        for i in range(len(b)-k):
            merged_list.append(b[k])
            k += 1

        logger.debug('Current State: {} + {} = {}'.format(a,b,merged_list))
        return merged_list
