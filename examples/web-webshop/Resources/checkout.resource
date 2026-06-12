*** Settings ***
Library           Browser    run_on_failure=Take A Screenshot
Resource          common.resource

*** Keywords ***
Checkout
    Click          data-test=proceed-1
    Click          data-test=proceed-2
    Fill Billing Address
    Execute Payment
    



Fill Billing Address
    Fill Text   data-test=street   29 Clerkenwell Rd
    Fill Text   data-test=city     Islington
    Fill Text   data-test=state    London
    Fill Text   data-test=postal_code      EC1M 5TA
    Fill Text   data-test=house_number      23
    Select Options By   id=country   value     GB
    common.Take A Screenshot  app-address
    Click          data-test=proceed-3
     


Checkout Page Should Be Visible
    Get Title    ==    Checkout
    Page Should Contain    Order summary


Execute Payment 
    [Arguments]  
    # SLeep  200
    Select Options By  data-test=payment-method  value  bank-transfer
    Fill text  data-test=bank_name  Test Bank
    Fill text  data-test=account_name  ${USER_NAME}
    Fill text  data-test=account_number  876587645234239423
    Click  data-test=finish
    Get Text  data-test=payment-success-message  ==  Payment was successful  msg=Payment confirmation message not found or incorrect!
    common.Take A Screenshot
