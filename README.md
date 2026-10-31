<div align="center">

# api-examples

**Working API calls in three languages — the same request, in curl, Python stdlib, and Node fetch.**

[![deps](https://img.shields.io/badge/dependencies-none-lightgrey?style=flat-square)](#quick-start)
[![license](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)

</div>

## About

Documentation snippets rot because they are never run. Each directory
here holds the same calls written three ways, and every one of them is a
complete script — copy it out and it runs. Nothing imports a client library, so
the example shows the actual wire format rather than what an SDK makes of it.

## Quick start

```bash
git clone https://github.com/lxcadoza993/api-examples
cd api-examples
sh curl/create.sh     # or python3 python/create.py / node js/create.js
```

## Configuration

| Key | Description |
| --- | --- |
| `curl/` | shell examples, no jq required |
| `python/` | standard library only — `urllib`, no requests |
| `js/` | Node 18+ built-in `fetch`, no npm install |
## Roadmap

- [ ] Go and Rust variants
- [ ] A script that asserts all three produce identical output
- [ ] Error-handling examples per language

## Contributing

Issues and pull requests are welcome. Please keep changes small and focused,
and add a test for any behaviour change — every repository here ships with a
runnable test suite and no third-party dependencies, so CI is just
`python3 -m unittest` / `bash test_*.sh`.

## License

[MIT](LICENSE)
