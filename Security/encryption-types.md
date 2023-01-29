# Encryption Types

- The process of scrambling data to secure it, hide important things from unauthorized third parties and more is known as encryption. The reverse of the process is decryption. There are primarily two types of encryption. Each type has multiple algorithms under them.
- Key is the entity that is used to encrypt (and decrypt) data.
- The entity generated after applying a key is called a ciphertext.


## Symmetric Encryption

- The process of using the same key to encrypt as well as decrypt is called symmetric encryption.
- Examples include AES, Twofish, Serpent, DES, etc.
- In the early 2000s, a contest was held to generate a very secure algorithm that cannot be brute forced. This was done because DES was brute forced. The winner of the contest was AES.


## Asymmetric Encryption

- Symmetric encryption in itself is pretty great but it is problematic to use them over networks. This is because to make things work, the key also needs to be sent, which is a big problem if someone else is sniffing a network.
- Asymmetric algorithms overcame the problem. Basically the technique here is to use one key to encrypt and another to decrypt.
- Public key is used for encryption. It is called public because there is no issue if others find this out. Because this is only used to encrypt not to decrypt.
- The private key cannot be found out since it is used for decryption.
- Essentially, the two pairs of keys are prime. This is actually quite expensive and not too easy to compute as symmetric techniques.
- For example, we have the RSA (used in SSH, TLS, etc.), ELGhamal, Diffie-Hellman techniques.


## Pros & Cons

- **Symmetric Encryption**
    - Faster than assymetric.
    - Efficient for large data.
    - Transporting the shared key is difficult. This doesn't prevent us from using this concept in networking, though.
- **Asymmetric Encryption** 
    - Public key can be shared. Not the private key. Good for networks.
    - Quite slower than symmetric.
    - Designed for smaller data.


## Use in Networks

We use a combination of both in networking for gaining the best of both worlds. We use assymetric encryption to establish a connection first. Then we use symmetric encryption to pass around messages.
