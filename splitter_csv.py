import re
import csv

file_to_split = input('What file should be split')

with open(file_to_split,'r') as f:
    ftext = f.read()

messages = re.split('From .*@.* \d{2}:\d{2}:\d{2} \d{4}',ftext)


# create csv filenames to hold output
nodefile='%s_nodes.csv' % (file_to_split[:-4])
edgefile='%s_edges.csv' % (file_to_split[:-4])
#nodefile writer
nf = open(nodefile,'w')
writernf = csv.writer(nf,delimiter=',')
writernf.writerow(['Id','Label','From Author','Date', 'To Author','Subject','In Reply To','Body']) #write headers to be used with gephi
#edgefile writer
ef = open(edgefile,'w')
writeref = csv.writer(ef,delimiter=',')
writeref.writerow(['Source','Target','Type']) #write headers to be used with gephi

all_nodes = []
all_edges = []

for ndx,message in enumerate(messages):
    if re.search('Date: .*, (.* \d{2}:\d{2}:\d{2})',message):
        from_author = re.search('From: (.*)\\n',message).group(1)
        date = re.search('Date: (.*)\\n',message).group(1)
        if re.search('To: (.*)\\n',message):
            to_author = re.search('To: (.*)\\n',message).group(1)
        else:
            to_author = ''
        subject = re.search('Subject: (.*)\\n',message).group(1)
        message_id = re.search('Message-ID: (.*)\\n',message).group(1)
        if re.search('In-Reply-To: (.*)\\n',message):
            in_reply_to = re.search('In-Reply-To: (.*)\\n',message).group(1)
        else:
            in_reply_to = ''

        #fname = fname.replace(' ','_')
        #fname = fname.replace(':','-')

        if re.search('(From: .*Content-Type: text/plain)(.*)',message,flags=re.DOTALL):
            content = re.search('(From: .*Content-Type: text/plain)(.*)',message,flags=re.DOTALL).group(2)
        else:
            content = ''
        
        all_nodes.append([message_id,ndx,from_author,date,to_author,subject,in_reply_to,content])

for ndx,i in enumerate(all_nodes):
    for i2 in all_nodes[ndx+1:]:
        if i[6] == i2[0]:
            all_edges.append([i[0],i2[0],'Directed'])
        elif i2[6] == i[0]: #see if there is an "in reply to" match
            all_edges.append([i2[0],i[0],'Directed'])
        elif i[5] in i2[5]: # if subject i in i2, that means i2 is re: subject1
            all_edges.append([i2[0],i[0],'Directed'])
        elif i2[5] in i[5]: #see if there is a subject-line re: match
            all_edges.append([i[0],i2[0],'Directed'])

for node in all_nodes:
    writernf.writerow(node)

for edge in all_edges:
    writeref.writerow(edge)

'''
            with open(fname+'.txt','w') as foo:
                foo.write(content.group(2))
        else:
            with open(fname+'.txt','w') as foo:
                foo.write(message)
'''
        
nf.close()
ef.close()