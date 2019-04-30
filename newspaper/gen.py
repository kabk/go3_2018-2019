#!/usr/bin/python

import os

tags2files = {}

def tagalytics():
  sorted_t2f = sorted(tags2files.items(), key=lambda kv: len(kv[1]))
  for t in sorted_t2f:
    print(t[0], len(t[1]))

def process_dir(tag, dstr):
  for d, subdirs, files in os.walk('data'):
    for fstr in files:
      if fstr != 'tags.txt':
        if tag in tags2files:
          tags2files[tag].append(dstr + '/' + fstr)
        else:
          tags2files[tag] = [dstr + '/' + fstr]

def process():
  for d, subdirs, files in os.walk('data'):
    #print(d, subdirs, files)
    for subdir in subdirs:
      tf_str = '/'.join([d, subdir, 'tags.txt'])
      #print(tf_str)
      with open(tf_str) as f:
        for tag in f:
          #print(tag.strip())
          process_dir(tag.strip().lower(), '/'.join([d, subdir]))

def gen_html():
  content = ''

  for tag in tags2files:
    for f in tags2files[tag]:
      ext = f.split('.')[1].lower()
      #print(ext)
      if ext == 'jpg' or ext == 'png':
        content += '<img src="' + f + '"/>\n'
      else:
        with open(f, 'r') as txt:
          content += '<p>' + txt.read().strip() + '</p>\n'

  with open('template.html', 'r') as template:
    index_str = template.read().replace('** CONTENT **', content)
    print(index_str)

process()
tagalytics()
#gen_html()
