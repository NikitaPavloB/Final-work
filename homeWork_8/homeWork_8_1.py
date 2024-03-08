# Для запуска пропишите в консоли:
# python homeWork_8_1.py /path/to/directory --json output.json --csv output.csv --pickle output.pickle


import os
import json
import csv
import pickle
import argparse


def get_dir_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


def traverse_directory(directory):
    results = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            size = os.path.getsize(path)
            results.append({'Path': path, 'Type': 'File', 'Size': size})

        for name in dirs:
            path = os.path.join(root, name)
            size = get_dir_size(path)
            results.append({'Path': path, 'Type': 'Directory', 'Size': size})

    return results


def save_results_to_json(results, filename):
    with open(filename, 'w') as f:
        json.dump(results, f, indent=4)


def save_results_to_csv(results, filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Path', 'Type', 'Size'])
        writer.writeheader()
        writer.writerows(results)


def save_results_to_pickle(results, filename):
    with open(filename, 'wb') as f:
        pickle.dump(results, f)


def main():
    parser = argparse.ArgumentParser(description='Traverse directory and save results in different formats.')
    parser.add_argument('directory', help='Directory to traverse')
    parser.add_argument('--json', help='JSON output filename')
    parser.add_argument('--csv', help='CSV output filename')
    parser.add_argument('--pickle', help='Pickle output filename')
    args = parser.parse_args()

    results = traverse_directory(args.directory)

    if args.json:
        save_results_to_json(results, args.json)
    if args.csv:
        save_results_to_csv(results, args.csv)
    if args.pickle:
        save_results_to_pickle(results, args.pickle)


if __name__ == "__main__":
    main()
