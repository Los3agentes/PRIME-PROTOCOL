"""Small, deterministic specimen for testing PRIME COMMUNICATION contract."""
from __future__ import annotations


def normalize_request(request: str) -> dict[str, str]:
    """Return a scoped translation; do not invent user intent or claim verification."""
    text = request.strip()
    if not text:
        raise ValueError('request cannot be blank')
    hints = {'reporte': 'report', 'informe': 'report', 'investigar': 'investigation', 'codigo': 'code', 'código': 'code'}
    tokens = text.lower().split()
    domain = next((hints[t.strip('.,;:')] for t in tokens if t.strip('.,;:') in hints), 'unspecified')
    return {'original': text, 'domain_hint': domain, 'certainty': 'INFERRED', 'scope': 'single_request'}


if __name__ == '__main__':
    import json
    import sys
    print(json.dumps(normalize_request(' '.join(sys.argv[1:])), ensure_ascii=False))
