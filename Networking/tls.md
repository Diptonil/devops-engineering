# Transport Layer Security

Essentially, it is a protocol for securing the communication over the network between the client and the server. It is responsible for the existence of HTTPS.


## Mechanism of HTTPS

- The basic mechanism of HTTPS is similar to HTTP itself. But there are a few differences.
- HTTP works on port 80 while HTTPS works on port 443.
- There occurs a handshake before transfer in HTTPS. This is not the 3 Way Handshake - that happens everywhere TCP is involved. This handshake happens so that both the client and the server agree on a symmetric key for encryption. This encryption happens around layer 7.
- The client would use that key on the request to encrypt it. If there is a man in the middle, they won't be able to figure out the request unless they know the key. So sniffing won't work. And here, the server, since it has a key, would be able to read the request.


## TLS 1.2

It is important to know that the TLS starts acting only after the TCP has been established.
- The first thing that happens here is the client's introduction. It enlists all the encryption techniques that it supports and presents it to the server.
- The server surveys it and sends a certificate, which is a public key of the server. This is a key that the client can support.
- The client takes the key and uses it to generate symmetric key.
- This symmetric key is then encrypted by the client using the certificate that the server had sent before. 
- The encrypted symmetric key is sent off to the server by the client.


## Problem with TLS 1.2

We are encrypting the symmetric key with the certificate and sending it over to the server. If someone manages to get the private key of the server, they can easily decrypt the symmetric key and listen in on the data transfer. <br />
One more defect of it is the number of steps that are executed to do the encryption. There is significant delay and processing involved to go through the whole thing, which is not desired.


## Diffie Hellman

The actual algorithm of Diffie Hellman is very math-intensive which is not needed for us.
- The symmetric key is a derivative that can be obtained by the combination of 3 keys - 2 private (which must not be shared) and 1 public (okay to be shared). The private keys live within the server and the client each.
- If either of the 2 private keys are combined with the public key and sent over, it is okay. That is allowed.
- This is used in TLS 1.3 to circumvent the problems of TLS 1.2.
- There is an ephemeral variant of this algorithm in which the private keys that are generated are not permanent and they keep on changing at each step.


## TLS 1.3

TLS 1.3's best thing is its security and performance. Less steps are required as well.
- The client generates it's private key and the whole system's public key.
- The server generates it's private key.
- It combines them together and sends it to the server (allowed).
- Upon reception, the server has the 3 pieces and can generate the symmetric key for HTTPS transactions. But client doesn't have it yet.
- The server sends over the combination of the public key and its own private key to the client.
- The client also has the 3 pieces now, thereby generating the symmetric key.