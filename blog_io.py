import os

def datesort(filename):
  datestring = filename.strip('.md').split('__')[1]
  datestring = datestring.replace('_','')
  return int(datestring)

if __name__ == '__main__':
  files = [ f for f in os.listdir('static/posts/published') if f.endswith('.md') ]
  print 'files:\n','\n'.join(f for f in files)

  sorted_files = sorted(files,key=datesort)
  print 'files sorted:\n', '\n'.join(f for f in sorted_files)
