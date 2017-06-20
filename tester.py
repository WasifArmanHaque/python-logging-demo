import sys, logging, yaml
import logging.config
import divide_and_conquer as dac

with open('logging.yaml') as f:
    conf = yaml.safe_load(f)
    conf.setdefault('version', 1)
    logging.config.dictConfig(conf)
    logger = logging.getLogger('tester_logger')

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
