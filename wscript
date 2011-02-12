# shamelessly lifted from the factorial example in node-ffi

import Options
from os import unlink, symlink, popen
from os.path import exists 
from logging import fatal

srcdir = '.'
blddir = 'build'

def set_options(opt):
  opt.tool_options('compiler_cxx')

def configure(conf):
  conf.check_tool('compiler_cxx')
  conf.env.append_value('LINKFLAGS', ['-lgmp']);

def build(bld):
  obj = bld.new_task_gen('cxx', 'shlib')
  obj.target = 'bignum'
  obj.source = 'bignum.cc'

def shutdown():
  if exists("build/default/libbignum.dylib") and not exists("libbignum.dylib"):
    symlink("build/default/libbignum.dylib", "libbignum.dylib")
  if exists("build/default/libbignum.so") and not exists("libbignum.so"):
    symlink("build/default/libbignum.so", "libbignum.so")
