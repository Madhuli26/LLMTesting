#!/usr/bin/env python3
import os
import argparse
import subprocess
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mock', action='store_true', help='Run tests with mock model responses')
    parser.add_argument('--golens', default='Golens/sample_golens.json')
    parser.add_argument('--report', default='Report/results.json')
    args = parser.parse_args()

    env = os.environ.copy()
    if args.mock:
        env['LLM_TEST_MOCK'] = '1'

    cmd = [sys.executable, 'Evaluations/evaluate.py', '--golens', args.golens, '--report', args.report]
    print('Running:', ' '.join(cmd))
    subprocess.check_call(cmd, env=env)

if __name__ == '__main__':
    main()
