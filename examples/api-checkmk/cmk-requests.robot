*** Settings ***
Documentation  Connects to the Checkmk login page and verifies that the page contains "login"
Library    RequestsLibrary
Variables  host.json
Suite Setup   Suite Initialization

# This library was auto-generated from the Checkmk API Swagger YAML with 
# https://marketsquare.github.io/robotframework-openapitools/
Library         CheckmkRESTAPI
...                 source=${API_URL}/openapi-swagger-ui.yaml
...                 origin=${API_URL}
...                 base_path=${EMPTY}

*** Variables ***

${API_URL}  http://127.0.0.1:5000/cmk/check_mk/api/v1
@{API_AUTH_USER}  cmkadmin  cmk
#@{API_AUTH_AUTOMATION}  api  baqNsTDNQaF^Yn8O

*** Test Cases ***

Create Host 1
    [Documentation]  Creates a host in CMK; the metadata are read from dictionaries. 
    ...   Note how the attributes are nested into the payload. 
    &{attributes}=    Create Dictionary   ipaddress=127.0.0.34
    &{payload}=    Create Dictionary    host_name=www.robotmk.org  folder=/  attributes=&{attributes}
    POST On Session  cmk  /domain-types/host_config/collections/all  json=${payload} 

Create Host 2
    [Documentation]  Creates another host in CMK; this time the metadata are read from
    ...   the host.json file. This makes the handling of the nested data much easier.
    ...   Note that "host_config" is the high-level key in the JSON.
    POST On Session  cmk  /domain-types/host_config/collections/all  json=${host_config} 

Create Host 3 With Lib
    Create A Host Group  name=testgroup

*** Keywords ***

Suite Initialization
    &{headers}=    Create Dictionary    Accept=application/json
    Create Session  cmk  url=${API_URL}  auth=${API_AUTH_USER}  headers=&{headers} 
    # Alternatively, connect with an automation user
    #Create Session  cmk  url=${API_URL}  auth=${API_AUTH_AUTOMATION}  headers=&{headers}
    GET On Session    cmk    /domain-types/downtime/collections/all
    &{attributes}=    Create Dictionary   ipaddress=127.0.0.33
    &{payload}=    Create Dictionary    host_name=www.robotmk.org33  folder=/  attributes=&{attributes}
