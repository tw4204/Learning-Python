import logging
logging.basicConfig(filename='chap11.log',level=logging.DEBUG, # minimum level capture in the file
format='[%(asctime)s] %(levelname)s:%(message)s',
datefmt='%m/%d/%Y %I:%M:%S %p')
mylist = [1, 2, 3]
logging.info('Starting to process `mylist`...')
for position in range(4):
    try:
        logging.debug('Value at position {} is {}'.format(position, mylist[position]))
    except IndexError:
        logging.exception('Faulty position: {}'.format(position))
        logging.info('Done parsing `mylist`.')
