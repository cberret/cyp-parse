import re

file_to_split = input('What file should be split')

with open(file_to_split,'r') as f:
    ftext = f.read()

messages = re.split('From .*@.* \d{2}:\d{2}:\d{2} \d{4}',ftext)


for message in messages:
    if re.search('Date: .*, (.* \d{2}:\d{2}:\d{2})',message):
        fname = re.search('Date: .*, (.* \d{2}:\d{2}:\d{2})',message).group(1)
        fname = fname.replace(' ','_')
        fname = fname.replace(':','-')
        if re.search('(From: .*Content-Type: text/plain)(.*)',message,flags=re.DOTALL):
            content = re.search('(From: .*Content-Type: text/plain)(.*)',message,flags=re.DOTALL)
            with open(fname+'.txt','w') as foo:
                foo.write(content.group(2))
        else:
            with open(fname+'.txt','w') as foo:
                foo.write(message)
