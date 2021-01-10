# YouTube-Checker-to-Feedbro
Converts YouTube Checker JSON exports to Feedbro OPML subscriptions and JSON rules.

## Usage
```
python3 YouTube-Checker-to-Feedbro.py YouTube-Checker-Export.json
```

This will generate two files. `Feedbro-YouTube-Checker-Subscriptions.xml` with your subscriptions and `Feedbro-YouTube-Checker-Subscriptions-Rules.json` with the rules (although rules are not actually converted currently – the script just assumes that you don’t want case-sensitive comparisons and have fixed strings only). 

Importing the subscriptions or rules doesn’t overwrite previous subscriptions or rules (unless the rare case happens where we roll a number between 1 and 9999999999999 that is already in use by one of your own rules).
