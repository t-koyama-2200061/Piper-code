#!/bin/bash

echo $1
echo $2

c='{ "date": { "S": "202301071220" }, "key": { "S": "'$1'" }, "humit": { "N": "'$2'" } }'
aws dynamodb put-item --table-name 2200061-handson-test --item "$c"
