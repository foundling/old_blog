def human_readable_date(datetime_object):
  import arrow
  ''' takes an arrow.now().datetime object and returns a .humanize() version'''
  return arrow.Arrow.fromdatetime(datetime_object).humanize()
