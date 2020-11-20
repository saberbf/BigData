#!/usr/bin/python
 
import sys
import json
 
def main():
 
    oldkey =None 
    old_confirmed_cumulative = 0
    old_deaths_cumulative = 0
    sorted_by_date = dict()
    # loop through each line for stdin
    for line in sys.stdin:
 
        # split line to separate key and value
        key, json_record = line.split("\t", 1)
 
        # parse the incoming json
        data = json.loads(json_record)
        # check if incoming key equals ongoing key
        if oldkey != key:
            writeOutput(sorted_by_date, oldkey)
            old_confirmed_cumulative = 0 
        oldkey = key


        sorted_by_date['fips'] = data['fips']
        # inrement ongoing metrics
        sorted_by_date['date'] = data['date']
        sorted_by_date["confirmed-cumulutive"] = data["confirmed"]
        sorted_by_date["confirmed"] = data["confirmed"] - old_confirmed_cumulative
        old_confirmed_cumulative = data['confirmed']
        # sorted_by_date["deaths-cumulutive"] += data["deaths"]
        

    # emit the final counts
    writeOutput(sorted_by_date, oldkey)
 
 
def writeOutput(sorted_by_date, key):
    if key != None:
        # generate json output
        output_json = json.dumps(sorted_by_date)
 
        # write the key and json to stdout
        print ('{0}\t{1}'.format(key, output_json))
 
 
if __name__ == "__main__":
    main()
