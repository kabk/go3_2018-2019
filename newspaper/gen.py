#!/usr/bin/python

import os

tags2files = {}

def tagalytics():
  sorted_t2f = sorted(tags2files.items(), key=lambda kv: len(kv[1]))
  for t in sorted_t2f:
    print(t[0], len(t[1]))

def process_tag(tag, dstr, fstr):
  if tag in tags2files:
    tags2files[tag].append(dstr + '/' + fstr)
  else:
    tags2files[tag] = [dstr + '/' + fstr]

def process():
  for d, subdirs, files in os.walk('data'):
    # print(d, subdirs, files)
    if len(files) > 0:
      for f in files:
        tag = d.split('/')[-1]
        process_tag(tag, d, f)

def gen_images(content):
  sorted_t2f = sorted(tags2files.items(), key=lambda kv: len(kv[1]))
  for i, (k, v) in enumerate(sorted_t2f):
    data_str = 'data-rank=' + str(i) + ' data-tag=' + k
    content += '<p class="tag"' + data_str + '>' + k.strip() + '</p>\n'
    for f in v:
      ext = f.split('.')[-1].lower()
      if ext == 'jpg' or ext == 'png' or ext == 'jpeg' or ext == 'gif':
        content += '<img src="' + f + '" ' + data_str + '>\n'
      else:
        with open(f, 'r') as txt:
          content += '<p ' + data_str + '>' + txt.read().strip() + '</p>\n'
  return content

def gen_html(content):
  with open('template.html', 'r') as template:
    index_str = template.read().replace('** CONTENT **', content)
    print(index_str)

process()
#tagalytics()
content = ''
content = gen_images(content)
gen_html(content)
