# Architecture

## Pieces

- The original file shared in the network is split into equal sized pieces of 256 kB to 1 mB. 
- The SHA1 hash of each piece is added in the `.torrent` file under the pieces attribute. Piece is fetched by its SHA-1 from the torrent file.
- Pieces can be exchanged by peers internally. 