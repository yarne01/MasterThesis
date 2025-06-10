#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "helib" for configuration "RelWithDebInfo"
set_property(TARGET helib APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(helib PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/libhelib.so.2.2.0"
  IMPORTED_SONAME_RELWITHDEBINFO "libhelib.so.2.2.0"
  )

list(APPEND _IMPORT_CHECK_TARGETS helib )
list(APPEND _IMPORT_CHECK_FILES_FOR_helib "${_IMPORT_PREFIX}/lib/libhelib.so.2.2.0" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
