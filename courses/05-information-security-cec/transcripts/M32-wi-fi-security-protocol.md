# Wi-Fi Security Protocol

**Module 32**  
Duration: 26:30  
Video: https://www.youtube.com/watch?v=vCdk5ufJpPo

Course Coordinator - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala  
Subject Expert - Dr. Yogesh Chaba, Department of Computer Engineering and IT, Guru Jambeshwar University of Science & Technology, Hisar

> Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture (CEC / SWAYAM).

---

**[0:09]** [Music]

**[0:24]** n

**[0:34]** Hello friends I am Professor yogesh Chaba from Department of computer science and engineering Guru jambeshwar

**[0:42]** University of Science and Technology Hisar harana today in this lecture we

**[0:49]** will study about WiFi security protocols first of all please see the contents

**[0:56]** which I shall cover after covering brief give introduction about three basic Wi-Fi security protocols I shall cover

**[1:05]** each one by one first in this series will be wired equivalent privacy

**[1:15]** we followed by WiFi protected access WPA and

**[1:24]** WPA2 in the last I shall compare WPA and WP pa2

**[1:32]** technology the wireless networking is becoming very popular among large number

**[1:38]** of Internet users because of the popularity of the wireless networking

**[1:45]** technology large number of wireless networking products and Protocols are

**[1:52]** available for the home and Business use wireless Transmissions are available

**[2:00]** to authorized users and also to the unauthorized users like

**[2:08]** hackers the i e 802.11 standard offers some level of

**[2:16]** protection this protection known as the wired equivalent privacy W protocol

**[2:24]** defines a set of instructions and rules by which wireless data can be

**[2:32]** transmitted over the air waves with some amount of

**[2:38]** security wired equivalent privacy W protocol is a basic security feature in

**[2:46]** the i e 802.11 standard intended to provide

**[2:54]** confidentiality over a wireless network by encrypting information sent over the

**[3:01]** 3 minutes, 1 second network very soon web got replaced by Wi-Fi protocol access

**[3:08]** WPA due to a flaw in web of getting cracked in a few minutes with the aid of

**[3:16]** automated tools WiFi protected access WPA and

**[3:24]** WPA2 is a wireless security protocol designed to address

**[3:30]** and fix the known security issues in we anyway this was very brief about

**[3:40]** basic security techniques used for wifi now let us see each one by one in

**[3:48]** detail first is wired equivalent privacy web which is a security algorithm for i

**[3:59]** e a 802.11 wireless networks introduced as part of the original

**[4:07]** 802.11 standard ratified in 1997 its intention was to provide data

**[4:17]** confidentiality comparable to that of a traditional wired Network the design

**[4:24]** objectives of web are as per i e 82. 11

**[4:30]** standard which states the following reasonably strong the security afforded

**[4:38]** by the algorithm should rely on the difficulty of discovering the secret key

**[4:45]** through a Brute Force attack this in turn is related to the length of the

**[4:51]** secret key and the frequency of changing Keys self synchronizing web should be self-

**[5:01]** 5 minutes, 1 second synchronizing for each message this property is critical for a data link

**[5:08]** level encryption algorithm where best effort delivery is

**[5:15]** assumed efficient the web algorithm should be efficient and may be implemented in

**[5:24]** either Hardware or software exportable

**[5:31]** every effort should be made to design the web system operation so as to

**[5:38]** maximize the chances of approval by the US government for exporting this

**[5:46]** technology optional the implementation and use of web in I

**[5:55]** 802.11 should be optional from the above objectives it's clear

**[6:03]** that VP was not designed to provide a high military level

**[6:09]** security the intention was to make it hard to break in as opposed to

**[6:17]** impossible to break in now let us move on to the technical details of

**[6:26]** web web security involves two Parts

**[6:34]** authentication and encryption authentication in web involves authenticating a device when it

**[6:43]** first joins the Lan the authentication process in the wireless network using web is to prevent

**[6:52]** devices or stations joining the network unless they know the web

**[7:01]** 7 minutes, 1 second key two methods of authentication can be used with web Open System Authentication

**[7:09]** and shared key authentication in Open System Authentication the W Lan client need not

**[7:19]** provide its credentials to the access point during authentication any client can

**[7:27]** authenticate with the access point and then attempt to associate in fact no

**[7:36]** authentication occurs subsequently VB keys can be used for encrypting data

**[7:45]** frames at this point the client must have the correct

**[7:52]** keys in shared key authentication the web key is used for authentication in a

**[7:59]** for Four Step Challenge response handshake as shown in figure step one

**[8:08]** wireless device sends authentication request to the wireless access point

**[8:15]** step two in response wireless access point sends 128bit random authentication

**[8:23]** Challenge in a clear text to the requesting Wireless

**[8:31]** device step three the wireless device uses the shared secret key to sign the

**[8:39]** challenge and send them in form of authentication response to the wireless

**[8:46]** access point step four wireless access point decrypts the signed message using the

**[8:55]** shared secret key and verifies the challenge that that it has sent

**[9:01]** 9 minutes, 1 second before if the challenge matches then authentication succeeds otherwise not if

**[9:09]** authentication succeeds then authentication success message is sent

**[9:15]** from access point to wireless device in webbased security

**[9:23]** unfortunately no secret key is exchanged after Authentication the same secret key or shared key is

**[9:33]** used for both authentication and encryption so there is no way to tell

**[9:42]** whether the subsequent message comes from the trusted device or from an

**[9:50]** imposter this kind of authentication is prone to man in the middle

**[9:57]** attack next we shall take up encryption part of web please see figure which shows

**[10:06]** stepbystep implementation of encryption process web uses rc4 stream Cipher to

**[10:16]** encrypt data between access point and wireless

**[10:21]** device web uses 8bit rc4 and operates on

**[10:27]** 8bit values by creating an array with 256 8 bit values for a lookup

**[10:36]** table VB uses CRC for the data integrity and accordingly performs cyclic

**[10:44]** redundancy check operation on the plain text and generates CRC

**[10:51]** value the CRC value is concatenated to the plain text the secret key is Con

**[10:59]** detonated to the initialization Vector i v and fed into the

**[11:07]** rc4 based on the secret key and IV rc4 generates key

**[11:16]** stream the key stream and plain Text Plus CRC message are exod together the

**[11:26]** result is the cipher text the same initialization Vector that was

**[11:33]** used before is prepended in clear text to the resultant Cipher

**[11:41]** text the initialization Vector IV plus Cipher text along with the frame headers

**[11:49]** are then transmitted over the air in this encryption method as we have

**[11:57]** seen some part of the secret key is used with different exposed values and

**[12:05]** attacker can generate the secret part by analyzing some portion of number of bits

**[12:13]** in the first few bytes of the key stream with relatively less

**[12:19]** work another problem with weap is that the secret shared key is concatenated

**[12:27]** with the visible I V value this weakness is known as IV

**[12:35]** weakness in the beginning it was believed that V offers impenetrable

**[12:42]** resistance to the eve droppers and hackers however as wireless networks

**[12:49]** began to grow in popularity many Crypt analyst and researchers discovered flaws in the

**[12:57]** original web design many believe that there was little peer review performed on the web

**[13:08]** protocol many of the web flaws would have been caught in the early design

**[13:14]** phase if its design and implementation specifications had been reviewed

**[13:22]** thoroughly for most of the wireless networking users especially home users

**[13:29]** web is the only choice available until new security mechanisms are added to the

**[13:37]** i e 802.11 standard but as people say something is better than nothing even

**[13:46]** with its known weakness web was still more effective than no security at all

**[13:55]** at least it will provide some security against unauthorized use of wireless

**[14:01]** 14 minutes, 1 second network and eating up the bandwidth there are many solutions available to

**[14:09]** overcome the weakness of web some of them are the bigger size of the

**[14:15]** initialization Vector IV can be chosen the hashed value of IV can be

**[14:23]** prepended or appended to the cipher text instead of the clear

**[14:30]** text instead of using CRC checkm different method can be used for the

**[14:37]** data Integrity verification that is Hash functions change secret key regularly

**[14:46]** dynamically using secure symmetric key distribution

**[14:53]** protocols better key management using security handshake

**[15:00]** protocols new authentication mechanisms using the extensible Authentication Protocol

**[15:09]** EAP in spite of implementation of these improvements there was a flowing in web

**[15:15]** of getting cracked in a few minutes with the aid of automated tools so instead of

**[15:23]** just relying on the web security alone additional measures must be taken to

**[15:30]** provide better security among wireless devices in 2003 the Wi-Fi Alliance

**[15:40]** announced that web had been superseded by WiFi protected access

**[15:48]** WPA in 2004 with a ratification of the full

**[15:55]** 802.11 I standard that is WPA2 the I declared that web has been

**[16:03]** declared obsolete Wi-Fi Alliance also decided to implement I E

**[16:11]** 802.11i standard to overcome the problems in VB i e

**[16:20]** 802.11i was implemented in two steps WiFi protected access WPA and WI Wi-Fi

**[16:29]** protected access 2 that is WPA 2 the Wi-Fi Alliance intended WPA as an

**[16:39]** intermediate measure to take the place of web pending the availability of full

**[16:46]** I E 802.11i standard WPA could be implemented

**[16:55]** through firmware upgrades on wireless network interface cards designed for web

**[17:03]** as WPA was an intermediate solution for Hardware that could not support WPA 2 so

**[17:11]** to implement WPA an interim software implementable solution was designed that

**[17:21]** could delay immediate deployment of new hardware to add support vot for WPA or

**[17:30]** WPA 2 some old Wi-Fi access points might need to be replaced or have their

**[17:39]** firmware upgraded WPA which is sometime referred to as draft i e

**[17:48]** 802.11 i standard became available in

**[17:54]** 2003 WPA2 became available in 20 2004

**[18:00]** and is commonly known as full i e

**[18:06]** 802.11i or i e 802.11i 2004

**[18:14]** standard WPA is a wireless security protocol designed to address and fix the

**[18:22]** known security issues in web WPA provides users with a higher

**[18:30]** level of assurance that their data will remain protected by using temporal key

**[18:38]** Integrity protocol tkip for data encryption specifically the temporal key

**[18:47]** Integrity protocol tkip was adopted for

**[18:53]** WPA we used a 40 bit or 100 4bit

**[19:00]** encryption key that must be manually entered on wireless access points and

**[19:07]** devices which does not change but tkip employs a per packet key

**[19:16]** meaning that it dynamically generates a new 128bit key for each packet and thus

**[19:25]** prevents the type of attack that compromise we WPA also includes a message Integrity

**[19:36]** check which is designed to prevent an attacker from altering and resending data

**[19:44]** packets this replaces the cyclic redundancy check CRC that was used by the web standard

**[19:54]** crc's main flaw in web was that it did not provide provide a sufficiently strong data Integrity

**[20:03]** guarantee for the packets it handled well tested message authentication codes existed to solve

**[20:13]** these problems but they required too much computation to be used on Old

**[20:20]** network cables WPA uses a message Integrity

**[20:26]** check algorithm called Michael to verify the Integrity of the

**[20:33]** packets no doubt Michael is much stronger than a CRC but still

**[20:39]** researchers have discovered a flaw in WPA due to reason of limitations of

**[20:47]** Michael to retrieve the key stream from short packets to use for

**[20:54]** reinjection and spoofing in order to solve such problems

**[21:01]** 21 minutes, 1 second in WPA and to completely Implement i e

**[21:07]** 802.11i protocol a new wireless security protocol

**[21:13]** WPA2 is implemented in which only authorized users can access a wireless

**[21:22]** device with features supporting stronger cryptography stronger Authentication

**[21:29]** control key management replay attack protection and data

**[21:37]** Integrity going into technical aspects of WPA 2 instead of

**[21:44]** tkip advanced encryption standard AES is used for encryption purpose that has a

**[21:53]** fixed block size of 128 bits and three different key sizes using three

**[22:03]** different steps of the algorithm in the first iteration a

**[22:10]** 128bit key is used to perform 9 rounds in the second a

**[22:18]** 192bit key performs 11 rounds and in the third iteration a

**[22:27]** 256bit key is used to perform 133 rounds because AES is a substitution

**[22:36]** Cipher So within each round bits are substituted and rearranged and then

**[22:45]** special multiplication is performed based on the new Arrangement the effectiveness of AES

**[22:54]** cannot be disputed as the time needed to break it by using a Brute Force attack

**[23:02]** with a 128bit key length is around 2200

**[23:09]** years now after brief technical details let us compare WPA and WPA 2 there are

**[23:19]** some similarities and differences between WPA and WPA 2

**[23:29]** both the security techniques WPA and WPA 2 uses the

**[23:37]** 802.1x that is EAP framework as part of the infrastructure that ensures Central

**[23:46]** Mutual authentication and dynamic Key Management both offers a pre-shared key

**[23:56]** for using home and small office environments and both are designed to

**[24:03]** secure all versions of 802.11 devices including

**[24:11]** 802.11b 802.11 A and 802.11

**[24:17]** G now coming onto the differences in both techniques WPA2 uses a mix mode

**[24:27]** that supports both WPA and WPA2 enabled

**[24:33]** devices on the same wireless network but WPA supports only

**[24:40]** one however the most significant difference between WPA and WPA2 is that

**[24:49]** WPA2 uses the advanced encryption

**[24:53]** standard AES instead of tki I for data

**[25:01]** 25 minutes, 1 second encryption WPA2 is theoretically not hackable but WPA

**[25:10]** is WPA2 requires more processing power than WP

**[25:18]** a so dear friends today in this lecture we have covered introductory concepts of

**[25:26]** wi-fi security followed by by three basic security techniques VB WPA and WPA

**[25:36]** 2 used for Wi-Fi in last we have also seen comparison of two latest security

**[25:45]** techniques WPA and WPA 2 so this was all

**[25:52]** about WiFi security protocols thank you e

**[25:59]** [Music]
