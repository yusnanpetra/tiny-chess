# tiny-chess

A chess engine that fits in 4 KB of Python (`main.py` = 3,824 bytes), written for the
tiny-chess-01 AI-agent bounty.

## Features
- Full legal move generation: castling, en passant, promotion
- Iterative-deepening alpha-beta search with move ordering (PV + captures first)
- Piece-square tables for positional evaluation
- Communicates with a small HTTP game server (`POST /game`, `POST /move`) via
  `MAKEFUN_ENV_URL`

## Run
```bash
MAKEFUN_ENV_URL=http://127.0.0.1:8090 python3 main.py
```

## License
MIT — see [LICENSE](LICENSE).
