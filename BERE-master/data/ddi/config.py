import logging
import os

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)-8s %(message)s')

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))

SAVE_DIR = 'checkpoint'
RESULT_DIR = 'result'
OUTPUT_DIR = 'output'
DATA_SET = 'ddi'

BAG_MODE = False
LOSS_WEIGHT = None

EMBEDDING_FINE_TUNE = True
BIDIRECTIONAL = True

MAX_LENGTH = 60
TAG_DIM = 50
HIDDEN_DIM = 250

DROP_PROB = 0.5
L2_REG = 0

LEARNING_RATE = 0.0001
BATCH_SIZE = 128
MAX_EPOCHS = 50


def log():
    logging.info('Loading config of {}'.format(ROOT_DIR))

    logging.info('BAG_MODE {}'.format('✔' if BAG_MODE else '×'))
    logging.info('LOSS_WEIGHT: {}'.format(LOSS_WEIGHT))
    logging.info('EMBEDDING_FINE_TUNE {}'.format('✔' if EMBEDDING_FINE_TUNE else '×'))
    logging.info('BIDIRECTIONAL {}'.format('✔' if BIDIRECTIONAL else '×'))

    logging.info('MAX_LENGTH: {}'.format(MAX_LENGTH))
    logging.info('TAG_DIM: {}'.format(TAG_DIM))
    logging.info('HIDDEN_DIM: {}'.format(HIDDEN_DIM))

    logging.info('DROP_PROB: {}'.format(DROP_PROB))
    logging.info('L2_REG: {}'.format(L2_REG))

    logging.info('LEARNING_RATE: {}'.format(LEARNING_RATE))
    logging.info('BATCH_SIZE: {}'.format(BATCH_SIZE))
    logging.info('MAX_EPOCHS: {}'.format(MAX_EPOCHS))
