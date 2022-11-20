cmake_minimum_required(VERSION 3.23)
project(conan_demo_application CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_executable(conan_demo_application src/main.cpp)
target_link_libraries(conan_demo_application CONAN_PKG::serviceA)


