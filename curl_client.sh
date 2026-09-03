#!/usr/bin/env sh
# Minimal client for the JSONPlaceholder demo REST API.
#
# Usage:
#   ./curl_client.sh
#
# jq is optional. Without it the raw JSON response is printed instead.

set -eu

BASE_URL="https://jsonplaceholder.typicode.com"
CURL="curl --silent --show-error --fail-with-body --max-time 10 -H Accept:application/json"

# Format with jq when available, otherwise pass the response through untouched.
pretty() {
  if command -v jq >/dev/null 2>&1; then
    jq "$@"
  else
    cat
  fi
}

echo "-- list posts for user 1 --"
# shellcheck disable=SC2086
$CURL "$BASE_URL/posts?userId=1" | pretty -r '.[0:3] | .[] | "  [\(.id)] \(.title)"'

echo
echo "-- fetch post 1 --"
# shellcheck disable=SC2086
$CURL "$BASE_URL/posts/1" | pretty -r '"  title: \(.title)"'

echo
echo "-- fetch a post that does not exist --"
# A 404 is expected here, so ask only for the status code and stay quiet.
status=$(curl --silent --output /dev/null --write-out '%{http_code}' \
  --max-time 10 "$BASE_URL/posts/9999")
echo "  status: $status"

echo
echo "-- create a post --"
# shellcheck disable=SC2086
$CURL -X POST "$BASE_URL/posts" \
  -H "Content-Type: application/json" \
  -d '{"title":"Example title","body":"Example body.","userId":1}' |
  pretty -r '"  server assigned id: \(.id)"'
echo
