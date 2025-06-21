# jscontact-json-schema

JSON Schema for JSContact ([RFC 9554](https://datatracker.ietf.org/doc/html/rfc9553)). Schema file is at [`jscontact-schema.json`](jscontact-schema.json).

**Note:** Still under development, use at your own risk!

## Validation Script

Assuming `uv` is installed, you can validate `jscontact-schema.json` itself:

```bash
uv run validate.py --self
```

Or, pass it some JSContact data instead:

```bash
uv run validate.py < my_data.json
```

## License

Distributed under the GNU General Public License, version 3.

See [LICENSE](LICENSE) for more information.
