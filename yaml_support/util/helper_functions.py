def get_caller_info():
  import inspect
  
  caller_frame = inspect.stack()[1]
  caller_filename_full = caller_frame.filename
  return caller_filename_full
