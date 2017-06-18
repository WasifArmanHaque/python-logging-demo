import sys, logging
import DivideAndConquer as dac

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('test.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

if __name__ == '__main__':
    if len(sys.argv) == 1 or sys.argv[1] == '-se' :
        print('Enter list items, separated by a space: ')
        items = [int(x) for x in raw_input().split()]

        print('Enter key to search for: ')
        key = int(raw_input())

        sas = dac.SearchAndSort(items, key)

        found = sas.binary_search()
        if found:
            print 'Item was found!'
        else:
            print 'Not found.'

        logger.info('Search succesful.')
    elif sys.argv[1] == '-sr':
        print('Enter list items, separated by a space: ')
        items = [int(x) for x in raw_input().split()]

        sas = dac.SearchAndSort(items)
        sas.merge_sort()
        logger.info('Sort succesful.')
    else:
        logger.warning('Not a valid flag.')
