# Email Security Protocols

**Module 19**  
Duration: 31:18  
Video: https://www.youtube.com/watch?v=0PUVjKXOiV8

Course Coordinator - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala  
Subject Expert - Prof Yogesh Chaba, Department of Computer Engineering and IT, Guru Jambeshwar University of Science & Technology, Hisar

> Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture (CEC / SWAYAM).

---

**[0:00]** [Music]

**[0:19]** Hello friends I am Professor yogesh Chaba from Department of computer science and engineering Guru jambeshwar

**[0:27]** University of Science and Technology Hisar harana in this lecture we will

**[0:34]** study about email security protocols first of all please see the contents

**[0:41]** which I shall cover after covering brief introduction about email security I

**[0:48]** shall take up different email security protocols like pretty good privacy pgp

**[0:56]** privacy enhanced mail pem and secure

**[1:02]** multi-purpose internet mail extension s mine in last we will compare all these

**[1:12]** protocols electronic mail most commonly referred to as email since

**[1:19]** 1993 is a method of exchanging digital messages from one sender to one or more

**[1:28]** recipients email operates across the internet or across other computer

**[1:38]** networks email privacy is the broad topic dealing with issues of

**[1:45]** unauthorized assess and inspection of electronic mail this unauthorized assess

**[1:54]** can happen while an email is in transit as well as when it is stored on email

**[2:02]** server or on a user computer email has to go through

**[2:09]** potentially untrusted intermediate servers before reaching its destination

**[2:17]** and there is no way to tell if it was assessed by an unauthorized user or

**[2:26]** not email system is different from a letter sealed in an envelope in which by

**[2:34]** close inspection of the envelope it might be possible to tell if someone

**[2:40]** opened it or not in that sense an email is much like a postcard whose contents

**[2:49]** are visible to everyone who handles it there are certain technical methods that

**[2:57]** make unauthorized assess to email difficult if not

**[3:04]** impossible however since email messages frequently cross Nation boundaries and

**[3:11]** different countries have different rules and regulations so email privacy is a complicated

**[3:20]** issue this problem has stimulated several people and groups to apply the

**[3:27]** cryptographic principles to produce secure email now we will study few

**[3:36]** common widely used email security systems pretty good privacy

**[3:44]** pgp privacy enhanced mail pem and secure

**[3:51]** multi-purpose internet mail extensions s mine first of all let us see pretty good

**[4:00]** privacy pgp short for pretty good privacy is a public key encryption

**[4:08]** program originally written by Phil Zimmerman in

**[4:15]** 1991 over the past few years pgp has got thousands of adherent supporters all

**[4:23]** over the globe and has become a def facto standard for encryption of email

**[4:30]** on the internet released in 1991 pgp is a complete email Security

**[4:40]** package that provides privacy authentication digital

**[4:46]** signatures and compression all in an easy to use

**[4:53]** form furthermore the complete package including all the source code is

**[5:00]** distributed free of charge via the Internet due to its quality zero price

**[5:09]** and easily availability on Unix Linux Windows and Mac operating system

**[5:17]** platforms it is widely used today pgp can be used to send messages

**[5:27]** confidentially for this purpose pgp combines symmetric key encryption and

**[5:34]** public key encryption the message is encrypted using a symmetric encryption

**[5:42]** algorithm which requires a symmetric key each symetric key is used only

**[5:51]** once and is also called a session key the message and its session key are sent

**[6:00]** to the receiver so that they know how to decrypt the message but to protect it

**[6:07]** during transmission it is encrypted with the receiver's public key only the private

**[6:16]** key belonging to the receiver can decrypt the session key pgp supports

**[6:24]** message authentication and integrity checking the letter is used to detect

**[6:31]** whether a message has been altered since it was completed and the former to

**[6:38]** determine whether it was actually sent by the person or entity claimed to be the

**[6:46]** sender because the content is encrypted any changes in the message will result

**[6:54]** in failure of the decryption with the appropriate key

**[7:01]** 7 minutes, 1 second the sender uses pgp to create a digital signature for the message with either

**[7:08]** the RSA or DSA algorithm to do so pgp

**[7:15]** computes a hash also known as a message digest from the plain text and then

**[7:23]** creates the digital signature from that hash using the senders private

**[7:31]** key to see how pgp works let us consider the example shown in figure here Alys on

**[7:41]** the left hand side wants to send a signed plan text message P to Bob on

**[7:48]** right hand side of figure in a secure way both Alys and Bob have RSA type of

**[7:58]** private and public key d and e let us assume that each one knows others public

**[8:07]** key Alis starts out by sending message P by invoking the pgp program on her

**[8:16]** computer by first hashing her message P using md5 and then encrypts the

**[8:25]** resulting hash using her private RSA key B A this signed hash of p is

**[8:34]** concatenated with original message P resulting P1 which is transmitted after

**[8:42]** compressing by zip program giving output p1.

**[8:49]** Z on the receiver side Bob receives p1.

**[8:54]** Z message which is given to international data and encryption algorithm idea module for

**[9:04]** decryption when Bob eventually gets the message he can decrypt the hash with

**[9:11]** Ellis public key e and verify that the hash is correct after decompressing it

**[9:19]** Bob separates the plain text from the encrypted hash and decrypts the hash

**[9:25]** using Alis public key if the plain text hash agrees with his

**[9:33]** own md5 computation he knows that P is the correct message and it came from

**[9:41]** ellys after verification of hash function Bob reverses the base 64

**[9:48]** encoding and decrypts the idea key using his private RSA

**[9:56]** key it is worth to note that RSA is only used in two places here to decrypt the

**[10:06]** 128bit md5 hash and to encrypt the

**[10:11]** 128bit idea key although RSA is slow it

**[10:17]** has to encrypt only 256 bits not a large volume of data thus pgp provides

**[10:27]** security compression and a digital signature and does so in a much more efficient

**[10:36]** way pgp supports four RSA key lens it is up to the user to select the one that is

**[10:46]** most appropriate the length are number one casual 384 bits it can be broken

**[10:54]** easily today number two commercial 512 bits it is breakable by three letter

**[11:05]** organization number three military 1024 bits it is not breakable by anyone on

**[11:14]** this Earth number four Ellen 2048 bits

**[11:20]** it is not breakable by anyone on other planets also since RSA is only used for two

**[11:30]** small computations everyone should use Ellen strength Keys all the

**[11:38]** time the format of a classic pgp message is as shown in figure numerous other

**[11:47]** formats are also in use the message has three parts containing the idea key the

**[11:56]** signature and the message respective ly the key part contains the key

**[12:04]** identifier and key itself the signature part contains a

**[12:10]** signature header followed by a time stamp next field is the identifier for

**[12:18]** the senders public key that can be used to decrypt the signature hash and this

**[12:26]** field is followed by type information that identifies the

**[12:32]** algorithms used and the encrypted md5 hash

**[12:40]** itself the message part also contains a header followed by the default file name

**[12:48]** to be used if the receiver writes the file to the disk next field is message

**[12:56]** creation Tim stamp and finally the message itself this was about working of pgp

**[13:06]** algorithm now let us see a product that is open pgp which is being used nowadays based

**[13:16]** on pgp algorithm open pgp is the most widely

**[13:22]** used Email encryption standard in the world today it is defined by the open

**[13:30]** pgp working group of the internet engineering task force

**[13:37]** ietf standard RFC 480 the open pgp Alliance is a growing

**[13:46]** group of companies and other organizations that are implementers of

**[13:52]** the open pgp proposed standard the alliance works to facilitate technical

**[14:02]** interoperability and marketing Synergy between open pgp implementations the open pgp standard

**[14:11]** was originally derived from pretty good privacy pgp protocol RFC 480 document

**[14:22]** contains all the necessary information to develop interoperable applications

**[14:29]** based on the open pgp format it describes the format and methods needed

**[14:37]** to read check generate and write conforming encrypted messages keys and

**[14:47]** signatures in July 1997 pgp incorporation proposed to the ietf that

**[14:56]** there should be a standard called open pgp they gave the ietf permission to use

**[15:04]** the name open pgp to describe this new standard as well as any program that

**[15:12]** supported the standard the ietf accepted the proposal

**[15:18]** and started the open pgp working group open pgp is on the internet

**[15:26]** standards track and is under active development specification of pgp was RFC

**[15:35]** 1991 but the current specification in open pgp is RFC

**[15:42]** 480 in 2007 the successor of RFC

**[15:49]** 24 the standard was extended to support chamelia Cipher by RFC 581 in 2009 and

**[16:00]** encryption based on elliptic curve cryptography as RFC 637 in

**[16:11]** 2012 open pgps encryption can ensure secure delivery of files and messages as

**[16:20]** well as provide verification of who created or sent the message using a

**[16:27]** process called digital signing using open pgp for communication

**[16:35]** requires participation by both the sender and the

**[16:41]** recipient open pgp can also be used to secure sensitive files when they are

**[16:48]** stored in vulnerable places like mobile devices or in the

**[16:56]** cloud so after pgp let us move on to privacy enhanced mail

**[17:04]** pem in contrast to pgp which was initially a oneman show our second email

**[17:12]** security protocol privacy enhanced mail p is an official internet standard and

**[17:21]** described in four rfc's RFC 1421 through rfc4

**[17:30]** 424 it is a 1993 ietf proposal for securing email using public key

**[17:40]** cryptography very roughly PM covers the same teritory as pgp that is privacy and

**[17:49]** authentication for RFC 822 based email systems nevertheless it also has some

**[17:58]** differences from pgp in approach and Technology PM is the outgrowth of work

**[18:06]** by the privacy and security research group psrg of the internet research task force

**[18:17]** irtf messages sent using p are first converted to a canonical form so that

**[18:26]** they all have the same conventions about white space like tabs and

**[18:34]** spaces next a message hash is computed using md2 or

**[18:41]** md5 then the concatenation of the hash and the message is encrypted using d s

**[18:52]** in light of the known weakness of a 56-bit key this choice is certainly

**[18:59]** suspect the encrypted message can then be encoded with base 64 coding and

**[19:08]** transmitted to the recipient as in pgp each message is

**[19:15]** encrypted with a onetime key that is enclosed along with the

**[19:22]** message the key can be protected either with RSA or with tri triple Dees using

**[19:33]** Ed in pem Key Management is more structured as compared to pgp keys are

**[19:42]** certified by x.509 certificates issued by

**[19:48]** CA which are arranged in a rigid hierarchy starting at a single route the

**[19:56]** advantage of this scheme is that certific ific at revocation is possible by having the roote issue crls

**[20:05]** periodically the only problem with p is that nobody ever used it and it has gone

**[20:13]** to that big bit bin in the sky although PM became an ietf proposed standard

**[20:24]** still it was never widely deployed or used the problem was largely

**[20:32]** political who would operate the route and under what conditions there was no

**[20:38]** shortage of candidates but many people were afraid to trust anyone company with

**[20:47]** the security of the whole system the most serious candidate RSA security

**[20:55]** incorporation wanted to charge per certificate issued however some organizations balked

**[21:04]** at this idea in particular the US government is allowed to use all us

**[21:12]** patents for free and companies outside the US had become accustomed to use the

**[21:20]** RSA algorithm for free as the company forget to patent it outside the the

**[21:29]** US no one was ready about suddenly having to pay RSS security

**[21:37]** incorporation for doing something that they had always done for free in the end

**[21:45]** no route could be found and PM collapsed in addition to being an

**[21:52]** obstacle to deployment the single rooted hierarchy was rejected Ed by some

**[22:00]** commentators as an unacceptable imposition of central

**[22:06]** Authority this led Phil Zimmerman to propose the web of trust as the pki

**[22:14]** infrastructure for the encryption program pretty good privacy

**[22:20]** pgp efforts to deploy PM were finally abandoned in response to the need to to

**[22:28]** extend the protocol to support mime this led to the development of the

**[22:35]** protocol mime object Security Services moss and S mime which shares defao

**[22:44]** standard status with pgp this is an ietf standard a result of

**[22:51]** a group working for a long time the basic idea is to have privacy by virtue

**[22:59]** of hierarchial authentication a receiver trusts the message of the sender when it is

**[23:06]** accompanied by a certificate from his trusted Authority these authoritative

**[23:14]** certificates are distributed from a group called internet policy

**[23:20]** registration Authority IP and policy certificate Authority PCA

**[23:29]** these trusted Authority actually certifies the public key sent by senders

**[23:37]** now after PM let us see third email security algorithm that is secure

**[23:45]** multi-purpose internet mail extensions s mine ietf next venture into email

**[23:54]** security known as secure multi-purpose internet mail extension s mine is

**[24:02]** described in RFC 2632 through

**[24:09]** 2643 as we know internet email messages consist of two parts the header and the

**[24:17]** body the header forms a collection of field or value pairs structured to

**[24:25]** provide information essential for the transmission of the message the structure of these headers can be found

**[24:34]** in RFC 822 the body is normally unstructured

**[24:41]** unless the email is in mind format mime defines how the body of an email message

**[24:50]** is structured the MIM format permits email

**[24:56]** to include enhance Ed text Graphics audio and more in a standardized manner

**[25:05]** via MIM compliant male systems however mime itself does not provide any

**[25:13]** Security Services the purpose of s mime is to Define such

**[25:20]** services like PM it provides authentication data Integrity secrecy

**[25:27]** and known reputation it also is quite flexible supporting a variety of cryptographic

**[25:37]** algorithms not surprisingly given the name s mime integrates with mime all

**[25:44]** kind of messages to be protected secure multi-purpose internet

**[25:51]** mail extensions is a protocol that adds digital signatures and an encryption to

**[25:59]** internet mime messages a variety of new mime headers are defined for example for holding

**[26:09]** digital signatures ietf definitely learn something from the PM

**[26:18]** experience s mime does not have a rigid certificate hierarchy beginning at a

**[26:25]** single route instead user can have multiple trust anchors as long as

**[26:33]** certificate can be traced back to some trust anchor the user believes in it is

**[26:41]** considered valid SM mime uses the standard algorithms and

**[26:50]** protocols now in last let us see comparison of email security protocols

**[26:58]** we have studied three email security protocols first was pgp that is pretty

**[27:06]** good privacy second was privacy enhanced mail pem and third was s

**[27:16]** mime as already discussed P could not gain popularity due to its shortcomings

**[27:24]** so it got collapsed pgp and S MIM which was adopted as an internet standard are

**[27:33]** two official email security systems which are currently National Institute

**[27:40]** of Standards and Technology nist specified standards both are considered to be

**[27:47]** secure male transmission techniques there has been a great deal of confusion in public and even within

**[27:57]** the IET F about the status of S M and

**[28:03]** pgp let us compare s MIM version 3 and open pgp protocol which are widely used

**[28:13]** nowadays please see the figure although they offer similar services to the users

**[28:20]** the two protocols have many differences s mine supports binary

**[28:26]** format whereas as open pgp supports pkcs7 mime format further and more

**[28:36]** important to corporate users they have different formats for their

**[28:42]** certificates as you can see s mime supports binary certificate based on

**[28:49]** x.509 version 3 whereas open pgp supports previous pgp based bind

**[28:59]** certificates this means that user of one protocol cannot communicate with the

**[29:05]** user of other and also they cannot share authentication

**[29:13]** certificates s mime supports Dey Helman with DSS or RSA but open pgp supports

**[29:22]** elgl with DSS signature algorithm both both the protocol supports S1 hash

**[29:32]** algorithm s mime supports CMS format of mime encapsulation of signed data but

**[29:41]** open pgp supports asy the difference between the two protocols is similar to the differences

**[29:51]** between giif and JPEG file they both do basically the same thing for end users

**[29:59]** but their formats are very different so friends this was about protocols for

**[30:08]** email Security in this lecture after covering brief introduction about email

**[30:15]** security we discussed different email security protocols like pretty good

**[30:23]** privacy pgp privacy enhanced mail p and secure multi-purpose internet mail

**[30:33]** extension s mine in last we also compared to most commonly used protocols

**[30:41]** s MIM version 3 and open pgp thank you

**[30:50]** [Music]

**[31:11]** [Music]
