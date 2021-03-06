import argparse
import json
#import pylab
import matplotlib.pyplot as plt

# Usage
# $ python check_word_frequencies.py --json_file=mapreduceout_wordcount_85917_1.json --loglog

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Project description')
    parser.add_argument('--json_file', help='JSON input file (e.g. mapreduceout_wordcount.json)', default="mapreduceout_wordcount.json")
    parser.add_argument('--loglog', action="store_true", help='Draw loglog rather than linear', default=False)
    args = parser.parse_args()

    # read json lines, sort by frequency
    print args
    lines = open(args.json_file).readlines()
    pairs = [json.loads(s) for s in lines]
    # sort by second item (frequency), reverse so most frequent comes first
    pairs.sort(key=lambda item: item[1], reverse=True)
    print "Most common words:"
    print pairs[:10]

    frequencies = [item[1] for item in pairs]
    if args.loglog:
        plt.loglog(frequencies)
    else:
        plt.plot(frequencies)
    plt.ylabel("Log 10 Frequencies", fontsize=14, fontweight="bold")
    plt.xlabel("Rank", fontsize=14, fontweight="bold")
    plt.grid(True)
    plt.title("Tweet words follow Zipf distribution")
    plt.show()
