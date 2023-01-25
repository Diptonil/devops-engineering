# Cyclic Redundancy Checks

CRCs find a lot of use over a broad scope in technology, even though they might be somewhat overlooked. They are associated with error correction and detection in data communication. They catch errors that checksums would not be able to catch. It was invented by W. Wesley Peterson in 1961. They ae very versatile and used in packet checking (there are fields allocated in data packets just to make a CRC), hard disk storage, etc. <br />
Apart from all the basic cases mentioned above, CRCs are used to detect very particular and specific errors in transmission as well which few other algorithms can do with such simplicity.


## Working of Modulo Division (not exactly CRC)

- CRCs work by first representing the whole data to be communicated in a large string of binary. When data is encoded into the binary equivalent, we send the data throw a network *along with* a check sequence. This check sequence may vary in size but is actually an identifier for the recieved packet to verify if the data has the same integrity or not after reception.
- The explanation below shows the algorithm that CRC *is based on* but is not actual representation of it since CRC does something different.
- For example, we have a message called "Hi!". This is converted to binary to give us 3 eight bit sequence (1 byte per character): "01001000 01101001 00100001". This results in a plain decimal number. So, this is how we can also convert the message into a decimal.
    - We add 2 bytes of "00000000" to the string as a *check sequence* to the right of the long binary number. This makes the resultant decimal number even larger. Assume that this decimal number is *D*.
    - Consider a number *N* (it is important to choose the perfect number for a particular sequence, which shall be explored in a bit) which we use to compute *D % N* to get a remainder. Let that be *R*. 
    - We could just use the remainder *R* as a check sequence, but we won't do so. This is only done to simplify things a bit further. We find the difference between the number *N* and the remainder *R*. We then add this difference to the *D* to generate a number that leaves no remainder when divided with *N*.
    - The number that gets generated finally is represented into binary and sent over. That has the property that it leaves no remainder with the *N* number. Any alterations that may happen in the recipient side would quickly recognize that the calculations don't really match up if anything goes wrong during transmission (0 is not obtained as a remainder).


## Check Sequence

- One thing that should come to our minds is what if the bits got flipped and there does exist an error in the recieved message. But the bits got flipped in a way such that the resulting number still somehow gets divided without remainders by *N*.
- If we had a flimsy, simple number like 256 as *N*, theer would be many multiples of it for errors to pass through unnoticed. Hence, we must mathematically think of a number fancy and large enough to not suffer from such defects.
- We take into considerations every type of problem that might occur and draw out the ones that are quite common (like 2 bits of the transmitted message being flipped in a row is quite common in the transmission medium). We need a number that can handle the effects that may arise due to these 2 bit flips (which in many complex cases, might end up causing more bits to flip with the rippling effect if there are carries). This is not easy to do, mathematically.
- It is important to know that the rippling error is easy to occur because binary and decimal conversions occur with the number 2 raised to some powers. CRC avoids this mess by doing a trick of replacing that 2 with some arbitrary and unknown 'x'. Representing the binary number as a polynomial is done here, rather than a plain decimal.


## Working (CRC)

- We repeat the whole process that we had described in Module Division, just having everything as polynomials rather than numbers. We have *D*, *N* and all the other variables as polynomials.
- The only small problem that we have here is the fact that once the remainder polynomial is generated, we need to figure out a way to cast it back to binary. This is solved using Finite Fields. 