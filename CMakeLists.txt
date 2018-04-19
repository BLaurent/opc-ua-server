cmake_minimum_required(VERSION 2.8)
SET(IMAGE_PATH ${CMAKE_CURRENT_SOURCE_DIR})
SET(IMAGE_TAG "blaurent/opcua-server")
SET(IMAGE_CONTAINER_NAME opcua-server)
SET(TAG_RELEASE "blaurent/opcua-server")
SET(no_proxy *.grc-apps.svc.ice.ge.com,predix.io,gecis.io,lattice.dev,*.dev,3.*,192.*,127.*,localhost,0.0.0.*)
SET(build_args --build-arg "http_proxy=$ENV{http_proxy}" --build-arg "https_proxy=$ENV{https_proxy}" --build-arg "no_proxy=$ENV{no_proxy}" )

add_custom_target(build
  COMMAND docker build ${build_args} --tag=${IMAGE_TAG} .
  WORKING_DIRECTORY ${IMAGE_PATH})

add_custom_target(run
  COMMAND python app.py
  WORKING_DIRECTORY ${IMAGE_PATH})

add_custom_target(up
  COMMAND docker-compose up -d
  WORKING_DIRECTORY ${IMAGE_PATH})
