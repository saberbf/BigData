#!/usr/bin/python

import sys, re
# import simplejson as json
import json

def main():
 
    # loop through each line of stdin
    for line in sys.stdin:
        try:
 
            # parse the incoming json 
            j = json.loads(line.strip())
            # initialize output structure
            output = dict()
 

            # grab an identifier
            output["fips"] = j["fips"]
 
            # and any other useful information from input json
            output["date"] = j["date"]
            output["confirmed"] = j["confirmed"]
            output["deaths"] = j["deaths"]


        except Exception as e:
            sys.stderr.write("unable to read log: %s" % e)
            continue
 
        try:
 
            # generate json output
            output_json = json.dumps(output)
 
            # write the key and json to stdout    
            print ('{0}\t{1}'.format(output["fips"], output_json)) 
 
        except Exception as e:
            sys.stderr.write("unable to write mapper output: %s" % e)
            continue

if __name__ == "__main__":
        main()
