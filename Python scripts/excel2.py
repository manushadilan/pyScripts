import openpyxl
import re

# Illegal character remover
ILLEGAL_CHARACTERS_RE = re.compile(r'[\000-\010]|[\013-\014]|[\016-\037]|[\x00-\x1f\x7f-\x9f]|[\uffff]')
def illegal_char_remover(data):
    """Remove ILLEGAL CHARACTER."""
    if isinstance(data, str):
        return ILLEGAL_CHARACTERS_RE.sub("", data)
    else:
        return data


# Open a blank workbook to populate.
wb = openpyxl.Workbook()
sheet = wb.active

log1=[]
log2=[]

# Loop through the text files.
with open ('SYSNAME_Current.txt') as fh:
    # cleaning empty lines
    lines = filter(None, (line.rstrip() for line in fh))
    i=0
    for l in lines:
        row = l.split('||')
        for j in range(len(row)):       
            log1.append(illegal_char_remover(row[j]))
        log2.append(log1)
        log1=[]

for i in log2:  
    sheet.append(i)  

# Write spreadsheet file
wb.save('text_to_spreadsheet.xlsx')




