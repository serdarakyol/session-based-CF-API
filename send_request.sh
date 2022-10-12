#!/bin/bash
# send request
curl -X 'POST' \
  'http://localhost:1234/api/collaborativefilter' \
  -H 'accept: application/json' \
  -H 'token: serdarakyol55@outlook.com' \
  -H 'Content-Type: application/json' \
  -d '{
  "item": [
    "SGKZB70023"
  ],
  "n_item": 3
}'
