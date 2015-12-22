#!/usr/bin/env python
#
# Copyright (C) 2014  Google Inc.
#
# This file is part of YouCompleteMe.
#
# YouCompleteMe is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# YouCompleteMe is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with YouCompleteMe.  If not, see <http://www.gnu.org/licenses/>.

import os
import ycm_core

# These are the compilation flags that will be used in case there's no
# compilation database set (by default, one is not set).
# CHANGE THIS LIST OF FLAGS. YES, THIS IS THE DROID YOU HAVE BEEN LOOKING FOR.
flags = [
#'-x',
#'c++',
#'-arch',
#'x86_64',
#'-fmessage-length=0',
#'-fdiagnostics-show-note-include-stack',
#'-fmacro-backtrace-limit=0',
#'-std=gnu++11',
#'-stdlib=libc++',
#'-fmodules',
#'-gmodules',
#'-fmodules-cache-path=/Users/user/Library/Developer/Xcode/DerivedData/ModuleCache',
#'-fmodules-prune-interval=86400',
#'-fmodules-prune-after=345600',
#'-fbuild-session-file=/Users/user/Library/Developer/Xcode/DerivedData/ModuleCache/Session.modulevalidation',
#'-fmodules-validate-once-per-build-session',
#'-fpascal-strings',
#'-O0',
#'-fno-common',
#'-DDEBUG=1',
#'-isysroot',
#'/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.11.sdk',
#'-fasm-blocks',
#'-fstrict-aliasing',
#'-mmacosx-version-min=10.10',
#'-g',
#'-fvisibility-inlines-hidden',
#'-iquote',
#'/Users/user/Library/Developer/Xcode/DerivedData/testCommandLine-eflwuvhcrseihabrcfasikkzhrfy/Build/Intermediates/testCommandLine.build/Debug/testCommandLine.build/testCommandLine-generated-files.hmap',
#'-I/Users/user/Library/Developer/Xcode/DerivedData/testCommandLine-eflwuvhcrseihabrcfasikkzhrfy/Build/Intermediates/testCommandLine.build/Debug/testCommandLine.build/testCommandLine-own-target-headers.hmap',
#'-I/Users/user/Library/Developer/Xcode/DerivedData/testCommandLine-eflwuvhcrseihabrcfasikkzhrfy/Build/Intermediates/testCommandLine.build/Debug/testCommandLine.build/testCommandLine-all-target-headers.hmap',
#'-iquote',
#'/Users/user/Library/Developer/Xcode/DerivedData/testCommandLine-eflwuvhcrseihabrcfasikkzhrfy/Build/Intermediates/testCommandLine.build/Debug/testCommandLine.build/testCommandLine-project-headers.hmap',
#'-I/Users/user/Library/Developer/Xcode/DerivedData/testCommandLine-eflwuvhcrseihabrcfasikkzhrfy/Build/Products/Debug/include',
#'-I/Users/user/Library/Developer/Xcode/DerivedData/testCommandLine-eflwuvhcrseihabrcfasikkzhrfy/Build/Intermediates/testCommandLine.build/Debug/testCommandLine.build/DerivedSources/x86_64',
#'-I/Users/user/Library/Developer/Xcode/DerivedData/testCommandLine-eflwuvhcrseihabrcfasikkzhrfy/Build/Intermediates/testCommandLine.build/Debug/testCommandLine.build/DerivedSources',
##'-I/Users/user/testDir/cppCommandLineTest/testCommandLine/testCommandLine',
#'-F/Users/user/Library/Developer/Xcode/DerivedData/testCommandLine-eflwuvhcrseihabrcfasikkzhrfy/Build/Products/Debug',
'-x',
'c++',
'-arch',
'x86_64',
'-fmessage-length=0',
'-fdiagnostics-show-note-include-stack',
'-fmacro-backtrace-limit=0',
'-std=gnu++11',
'-stdlib=libc++',
'-fmodules',
'-gmodules',
'-fmodules-cache-path=/Users/user/Library/Developer/Xcode/DerivedData/ModuleCache',
'-fmodules-prune-interval=86400',
'-fmodules-prune-after=345600',
'-fbuild-session-file=/Users/user/Library/Developer/Xcode/DerivedData/ModuleCache/Session.modulevalidation',
'-fmodules-validate-once-per-build-session',
'-Wnon-modular-include-in-framework-module',
'-Werror=non-modular-include-in-framework-module',
'-Wno-trigraphs',
'-fpascal-strings',
'-O0',
'-fno-common',
'-Wno-missing-field-initializers',
'-Wno-missing-prototypes',
'-Werror=return-type',
'-Wunreachable-code',
'-Werror=deprecated-objc-isa-usage',
'-Werror=objc-root-class',
'-Wno-non-virtual-dtor',
'-Wno-overloaded-virtual',
'-Wno-exit-time-destructors',
'-Wno-missing-braces',
'-Wparentheses',
'-Wswitch',
'-Wunused-function',
'-Wno-unused-label',
'-Wno-unused-parameter',
'-Wunused-variable',
'-Wunused-value',
'-Wempty-body',
'-Wconditional-uninitialized',
'-Wno-unknown-pragmas',
'-Wno-shadow',
'-Wno-four-char-constants',
'-Wno-conversion',
'-Wconstant-conversion',
'-Wint-conversion',
'-Wbool-conversion',
'-Wenum-conversion',
'-Wshorten-64-to-32',
'-Wno-newline-eof',
'-Wno-c++11-extensions',
'-DDEBUG=1',
'-isysroot',
'/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.11.sdk',
'-fasm-blocks',
'-fstrict-aliasing',
'-Wdeprecated-declarations',
'-Winvalid-offsetof',
'-mmacosx-version-min=10.10',
'-g',
'-fvisibility-inlines-hidden',
'-Wno-sign-conversion',
'-iquote',
'/Users/user/Library/Developer/Xcode/DerivedData/testCommandLine-eflwuvhcrseihabrcfasikkzhrfy/Build/Intermediates/testCommandLine.build/Debug/testCommandLine.build/testCommandLine-generated-files.hmap',
'-I/Users/user/Library/Developer/Xcode/DerivedData/testCommandLine-eflwuvhcrseihabrcfasikkzhrfy/Build/Intermediates/testCommandLine.build/Debug/testCommandLine.build/testCommandLine-own-target-headers.hmap',
'-I/Users/user/Library/Developer/Xcode/DerivedData/testCommandLine-eflwuvhcrseihabrcfasikkzhrfy/Build/Intermediates/testCommandLine.build/Debug/testCommandLine.build/testCommandLine-all-target-headers.hmap',
'-iquote',
'/Users/user/Library/Developer/Xcode/DerivedData/testCommandLine-eflwuvhcrseihabrcfasikkzhrfy/Build/Intermediates/testCommandLine.build/Debug/testCommandLine.build/testCommandLine-project-headers.hmap',
'-I/Users/user/Library/Developer/Xcode/DerivedData/testCommandLine-eflwuvhcrseihabrcfasikkzhrfy/Build/Products/Debug/include',
'-I/Users/user/Library/Developer/Xcode/DerivedData/testCommandLine-eflwuvhcrseihabrcfasikkzhrfy/Build/Intermediates/testCommandLine.build/Debug/testCommandLine.build/DerivedSources/x86_64',
'-I/Users/user/Library/Developer/Xcode/DerivedData/testCommandLine-eflwuvhcrseihabrcfasikkzhrfy/Build/Intermediates/testCommandLine.build/Debug/testCommandLine.build/DerivedSources',
'-F/Users/user/Library/Developer/Xcode/DerivedData/testCommandLine-eflwuvhcrseihabrcfasikkzhrfy/Build/Products/Debug',
]


# Set this to the absolute path to the folder (NOT the file!) containing the
# compile_commands.json file to use that instead of 'flags'. See here for
# more details: http://clang.llvm.org/docs/JSONCompilationDatabase.html
#
# Most projects will NOT need to set this to anything; you can just change the
# 'flags' list of compilation flags.
compilation_database_folder = ''

if os.path.exists( compilation_database_folder ):
  database = ycm_core.CompilationDatabase( compilation_database_folder )
else:
  database = None

SOURCE_EXTENSIONS = [ '.cpp', '.cxx', '.cc', '.c', '.m', '.mm' ]

def DirectoryOfThisScript():
  return os.path.dirname( os.path.abspath( __file__ ) )


def MakeRelativePathsInFlagsAbsolute( flags, working_directory ):
  if not working_directory:
    return list( flags )
  new_flags = []
  make_next_absolute = False
  path_flags = [ '-isystem', '-I', '-iquote', '--sysroot=' ]
  for flag in flags:
    new_flag = flag

    if make_next_absolute:
      make_next_absolute = False
      if not flag.startswith( '/' ):
        new_flag = os.path.join( working_directory, flag )

    for path_flag in path_flags:
      if flag == path_flag:
        make_next_absolute = True
        break

      if flag.startswith( path_flag ):
        path = flag[ len( path_flag ): ]
        new_flag = path_flag + os.path.join( working_directory, path )
        break

    if new_flag:
      new_flags.append( new_flag )
  return new_flags


def IsHeaderFile( filename ):
  extension = os.path.splitext( filename )[ 1 ]
  return extension in [ '.h', '.hxx', '.hpp', '.hh' ]


def GetCompilationInfoForFile( filename ):
  # The compilation_commands.json file generated by CMake does not have entries
  # for header files. So we do our best by asking the db for flags for a
  # corresponding source file, if any. If one exists, the flags for that file
  # should be good enough.
  if IsHeaderFile( filename ):
    basename = os.path.splitext( filename )[ 0 ]
    for extension in SOURCE_EXTENSIONS:
      replacement_file = basename + extension
      if os.path.exists( replacement_file ):
        compilation_info = database.GetCompilationInfoForFile(
          replacement_file )
        if compilation_info.compiler_flags_:
          return compilation_info
    return None
  return database.GetCompilationInfoForFile( filename )


# This is the entry point; this function is called by ycmd to produce flags for
# a file.
def FlagsForFile( filename, **kwargs ):
  if database:
    # Bear in mind that compilation_info.compiler_flags_ does NOT return a
    # python list, but a "list-like" StringVec object
    compilation_info = GetCompilationInfoForFile( filename )
    if not compilation_info:
      return None

    final_flags = MakeRelativePathsInFlagsAbsolute(
      compilation_info.compiler_flags_,
      compilation_info.compiler_working_dir_ )
  else:
    relative_to = DirectoryOfThisScript()
    final_flags = MakeRelativePathsInFlagsAbsolute( flags, relative_to )

  return {
    'flags': final_flags,
    'do_cache': True
  }

