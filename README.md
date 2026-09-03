# api-examples

The same small REST workflow, implemented three times: **Python**, **Node**, and
**POSIX shell**. Each client lists posts for a user, fetches one by id, handles a
missing resource, and creates a record.

All three run against [JSONPlaceholder](https://jsonplaceholder.typicode.com), a
public demo API with no authentication — clone and run, no key required.

## Why three languages

Most quickstarts pick one language and leave everyone else translating. These
three cover the usual first questions: the ergonomic library case (`requests`),
the zero-dependency runtime case (Node's built-in `fetch`), and the "just show me
the HTTP" case (`curl`). Output is deliberately identical across all three, so you
can diff behaviour rather than syntax.

## Running them

**Python** (3.8+):

```sh
pip install -r requirements.txt
python python_client.py
```

**Node** (18+, for global `fetch` and `AbortSignal.timeout`):

```sh
node node_client.mjs
```

**Shell** (`curl` required, `jq` optional — without it you get raw JSON):

```sh
chmod +x curl_client.sh
./curl_client.sh
```

## What each one demonstrates

| Behaviour | Why it is here |
|---|---|
| `GET /posts?userId=1` | Query parameters, encoded rather than concatenated |
| `GET /posts/1` | Reading a single resource |
| `GET /posts/9999` | A 404 treated as an expected result, not an exception |
| `POST /posts` | JSON request body with the right `Content-Type` |

Every client sets an explicit timeout and checks the status code before parsing —
the two lines most examples skip and production needs most.

## Adapting these

Change `BASE_URL` to your own service. If it needs authentication, add the header
where each client builds its request — the session in Python, the `request()`
helper in Node, the `CURL` variable in the shell script. Do not commit the token.

## License

MIT — see [LICENSE](LICENSE).
