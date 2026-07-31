cmake_minimum_required(VERSION 3.20)

project(StoreBackend)

set(CMAKE_CXX_STANDARD 17)

add_executable(server

backend/main.cpp
backend/database.cpp
backend/auth.cpp
)