# BitTorrent

It is an application based on the P2P architecture to make the distribution and sharing of files easier and faster. Here, there is no system of an absolute centralized server. The peers give out the data that constitutes the file being shared. This also makes the system robust as if a peer goes down, transaction can still be processed, unlike a centralized server.


## How Is High Speed Achieved?

- Traditionally, no matter how high the download speed of a client is, extremely fast downloads aren't what generally happen. This is because for a regular internet connection, the downlink speed is always greater than the uplink speed (like a 100 mbps download and 60 mbps upload). This applies for servers as well, due to which they cannot serve the files that effectively and fast. <br />
With BitTorrent, the files are constituted by peers themselves. So, the uplink of many peers make for a very high amount of data that can flow in, which matches a client's download speed. This is why BitTorrent is so fast (as can be practically observed).
- Distributing a large file in smaller chunks boosts concurrency.
- Due to the multiplicity of the peers, even a large number of downloader of the same resource would not suffer from slow speed. That scenario can be handled pretty well.
- If users want to download a file, they'd sniff around their networks for any peers to have any pieces of that file. After that, the users can download different pieces from different peers at the same time.


## The Peer-to-Peer Variation

The standard P2P model is used here, with just a slight variation. A *central entity* is used along with the peers in a network. This is not responsible for storing the file data but only stores metadata. Peers cannot be identified without the metadata. So this central entity should, ideally, never go down.


## Terminologies

1. **Pieces & Blocks**: Every file is shared in the BitTorrent network by first breaking it up into pieces. Pieces are further divided into blocks. In one transfer, a piece is served by a peer completely, with blocks being transferred atomically. If any block is missing from the data housed by the peer, that piece won't be served.
1. **Peer Set**: Each peer maintains a set of peers to whom they can send pieces. This is the peer set. It is not compulsory that a peer has to send pieces to *all* the members of a peer set at all times.
1. **Active Peer Set**: A subset of the peer set to which data would be sent across.
1. **Seeder & Leecher**: A peer may be a leecher or a seeder. When peers downloads, it becomes a leecher. When peer uploads, it becomes a seeder. Large number of seeders lead to higher download speed support since we can pull from multiple seeders quickly. There are no incentives a peer may have to join a torrent and become a seeder (this is a point of difference from a typical blockchain architecture since there is no scope of incentives).


## The Torrent File

Every torrent is associated with a `.torrent` file, which contains information and metadata about the file that the user wants to download. Every torrent would have its own unique torrent file. Without that, the download cannot happen. <br />
The lifecycle of a torrent is as such:
- A seeder is seeding the file in a network.
- So long we have at least one seeder, the file can be derived. If there are no seeders, the torrent is dead.
- Once a file is downloaded completely, the peer has two choices: either discard the torrent file and finish the process or hold on to it and become a seeder of that torrent.


## Contents of the Torrent File

It is a static file that contains metadata. It is a simple key-value pair file that has these five fields below as the key and their corresponding value:
- `announce`: The announce URL of the *tracker*. This is critical. The tracker is the *central entity* which keeps track of which peer has what piece of a file in a torrent network.
- `created by`: The name of the creater and version of the creation.
- `creation date`
- `encoding`: Encoding of strings as part of the 'info' dictionary.
- `comment`: Some additional comment by the author or associated with the content.
- `info`: A dictionary that describes file of the torrent. A torrent might be a single-file or a multi-file (sometimes we download a whole directory) torrent. They have three common properties:
    - `length`: File size in bytes. Each file in a multi-file directory of a torrent has one.
    - `name`: Name of file/ directory of the torrent.
    - `md5sum`: md5 (somewhat liek a checksum) of the file. Each file in a sulti-file directory of a torrent has one.
    - `path`: List of string representing the path of a file. This is only available for multi-file torrents. The way it gets stored, however, is somewhat different. For example, a relative path of `a/b/c.txt` gets represented as a dictionary of `[a, b, c.txt]`. This is done because separators (like slash, backslash, etc.) are always different for different operating systems. Torrent doesn't take that risk to ust adhere to one OS specs.
    - `piece length`: This is a very critical bit of information. We need some mechanism to know how much exactly a piece is worth before being capable of identifying the source from which we should be acquiring the piece from.
    - `pieces`: 20 byte SHA1 hash value, concatenated. This means that the torrent file stores the hash values of all the pieces of data that exist. This is the most critical data we store in a torrent file. All 20 byte SHA1 hashes are concatenated into one long string.


## Bencoding

The torrent file doesn't store its information in the traditional JSON format. It is Bencoded (pronounced as Bee-encoded).To extract all te information, we would need a particular decoder through which the data passes and gets decoded to give the torrent info. After that, the torrent metadata can be processed. <br />
Review the `bencoding.md` file for the specification and internal working of it.


## Architecture

We hae seen the overview of the components that make up the entire system. We dive deep into the mechanisms in `architecture.md`.


## Applications

- BitTorrent was used to power the transfer of huge softwares, movies, games, etc.
- It was initially used largely to download Linux distros.
- Sending security patches to users.
- Facebook used these to power their massive deployments.