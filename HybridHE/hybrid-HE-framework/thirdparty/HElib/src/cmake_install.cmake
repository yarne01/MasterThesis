# Install script for directory: /home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/src

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "RelWithDebInfo")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xlibx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libhelib.so.2.2.0" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libhelib.so.2.2.0")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libhelib.so.2.2.0"
         RPATH "$ORIGIN/:/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/NTL/usr/local/lib:/usr/local/lib")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/lib/libhelib.so.2.2.0")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libhelib.so.2.2.0" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libhelib.so.2.2.0")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libhelib.so.2.2.0"
         OLD_RPATH "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/NTL/usr/local/lib:/usr/local/lib:::::::::"
         NEW_RPATH "$ORIGIN/:/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/NTL/usr/local/lib:/usr/local/lib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libhelib.so.2.2.0")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xlibx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libhelib.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libhelib.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libhelib.so"
         RPATH "$ORIGIN/:/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/NTL/usr/local/lib:/usr/local/lib")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/lib/libhelib.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libhelib.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libhelib.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libhelib.so"
         OLD_RPATH "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/NTL/usr/local/lib:/usr/local/lib:::::::::"
         NEW_RPATH "$ORIGIN/:/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/NTL/usr/local/lib:/usr/local/lib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libhelib.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xlibx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/helib" TYPE FILE FILES
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/helib.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/apiAttributes.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/ArgMap.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/binaryArith.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/binaryCompare.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/bluestein.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/ClonedPtr.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/CModulus.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/CtPtrs.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/Ctxt.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/debugging.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/DoubleCRT.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/EncryptedArray.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/EvalMap.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/Context.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/FHE.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/keys.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/keySwitching.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/log.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/hypercube.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/IndexMap.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/IndexSet.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/intraSlot.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/JsonWrapper.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/matching.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/matmul.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/Matrix.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/multicore.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/norms.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/NumbTh.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/PAlgebra.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/partialMatch.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/permutations.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/polyEval.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/PolyMod.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/PolyModRing.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/powerful.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/primeChain.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/PtrMatrix.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/PtrVector.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/Ptxt.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/query.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/randomMatrices.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/range.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/recryption.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/replicate.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/sample.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/scheme.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/set.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/SumRegister.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/tableLookup.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/timing.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/zzX.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/assertions.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/exceptions.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/PGFFT.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/fhe_stats.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/zeroValue.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/include/helib/EncodedPtxt.h"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/src/helib/version.h"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xlibx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/cmake/helib/helibTargets.cmake")
    file(DIFFERENT EXPORT_FILE_CHANGED FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/cmake/helib/helibTargets.cmake"
         "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/src/CMakeFiles/Export/share/cmake/helib/helibTargets.cmake")
    if(EXPORT_FILE_CHANGED)
      file(GLOB OLD_CONFIG_FILES "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/cmake/helib/helibTargets-*.cmake")
      if(OLD_CONFIG_FILES)
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/share/cmake/helib/helibTargets.cmake\" will be replaced.  Removing files [${OLD_CONFIG_FILES}].")
        file(REMOVE ${OLD_CONFIG_FILES})
      endif()
    endif()
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/cmake/helib" TYPE FILE FILES "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/src/CMakeFiles/Export/share/cmake/helib/helibTargets.cmake")
  if("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Rr][Ee][Ll][Ww][Ii][Tt][Hh][Dd][Ee][Bb][Ii][Nn][Ff][Oo])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/cmake/helib" TYPE FILE FILES "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/src/CMakeFiles/Export/share/cmake/helib/helibTargets-relwithdebinfo.cmake")
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/cmake/helib" TYPE FILE FILES
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/src/helibConfig.cmake"
    "/home/yarne/masterThesis2/test/hybrid-HE-framework/thirdparty/HElib/src/helibConfigVersion.cmake"
    )
endif()

