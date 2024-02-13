
import json

headers = []
data = {'node': []}
with open ('SYSNAME_Current.txt') as fh:
  # cleaning empty lines
    lines = filter(None, (line.rstrip() for line in fh))
    for l in lines:
        s = l.split('||')
        if len(headers) == 0:
            headers = s
        else:
            d = {}
            for i, v in enumerate(s):
                try:
                    d[headers[i]] = float(v)
                except ValueError:
                    d[headers[i]] = v
            data['node'].append(d)

# creating json file
out_file = open("out.json", "w")
json.dump(data, out_file, indent = 4, sort_keys = False)
out_file.close()