import argparse
import datetime
import os
import time
from temper2 import Temper2


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help='path to log file',
                        default='~/temper.log')
    parser.add_argument('-f', '--freq', type=int,
                        help='frequency of records in seconds',
                        default=30)
    args = parser.parse_args()
    if args.freq <= 0:
        raise ValueError('log frequency must be > 0 seconds')
    log_path = os.path.expanduser(args.path)

    with Temper2() as t, open(log_path, 'a') as f:
        while True:
            int_temp, ext_temp = t.get_temp()
            timestamp = datetime.datetime.utcnow().\
                replace(microsecond=0).isoformat()
            params = {
                'timestamp': timestamp,
                'int_temp': int_temp,
                'ext_temp': ext_temp
            }
            f.write('{timestamp},{int_temp},{ext_temp}\n'.format(**params))
            f.flush()
            time.sleep(args.freq)
