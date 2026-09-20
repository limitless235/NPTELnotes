# Network Security

**Module 02**  
Duration: 24:29  
Video: https://www.youtube.com/watch?v=kibMPvGrLXw

Course Coordinator - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala  
Subject Expert - Dr Pardeep Bhandari, Doaba College, Jalandhar

> Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture (CEC / SWAYAM).

---

**[0:04]** hello everyone I am pradep bandari from duaba college jander I'm going to present a session on network security

**[0:12]** over the past few years the internet enabled business or E business has drastically improved company's

**[0:20]** efficiency and revenue growth e business applications such as e-commerce Supply Chain management and

**[0:29]** remote assess enable companies to streamline processes lower operating costs and increase customer

**[0:37]** satisfaction such applications require Mission critical networks that accommodate voice video and data traffic

**[0:45]** and these networks must be scalable to support increasing number of users and the need for greater capacity and

**[0:54]** performance however as networks enable more and more applications and are available to more and more users they

**[1:02]** become ever more vulnerable to a wider range of security threats to combat these threats and

**[1:11]** ensure that e business transactions are not compromised network security play a

**[1:17]** major role in today's networks network security deals with securing the information through cryptography and

**[1:26]** network security devices the main goal of net network security confidentiality now confidentiality is

**[1:34]** probably the most common aspect of information security we need to protect our confidential information an

**[1:42]** organization needs to guard against those malicious actions that endanger the confidentiality of its information

**[1:51]** confidentiality not only applies to the storage of the information it also applies to the transmission of information

**[2:00]** when we send a piece of information to be stored in a remote computer or when we retrieve a piece of information from

**[2:09]** a remote computer we need to conceal it during transmission second is integrity

**[2:17]** information needs to be changed constantly in a bank when a customer deposits or withdraws money the balance

**[2:26]** of her account needs to be changed in integrity means that changes need to be done only by authorized entities and

**[2:36]** through authorized mechanisms Integrity violation is not necessarily the result

**[2:43]** of a malicious act and interruption in the system such as a power failure or a power surge may also create unwanted

**[2:52]** changes in some information third is availability the third component of information security

**[3:00]** the information created and stored by an organization needs to be available to authorized entities information is

**[3:09]** useless if it is not available information needs to be constantly changed which means it must be

**[3:16]** accessible to authorized entities the unavailability of information is just as harmful for an organization as the lack

**[3:25]** of confidentiality or Integrity imagine what would happen happen to a bank if the customers could not access their

**[3:33]** accounts for the transaction security attacks now any action that compromises the security of

**[3:40]** information owned by an organization is called security attack two things to be considered separately in context of

**[3:49]** security attacks are threat a potential for violation of security which exists

**[3:57]** when there is a circumstance capability action or event that could breach security and cause harm that is a threat

**[4:05]** is a possible danger that might exploit a vulnerability second is attack an

**[4:12]** assault on system security that derives from an intelligent threat that is an intelligent act that is a deliberate

**[4:21]** attempt to evade Security Services and violate the security policy of a system now security attack attacks can be of

**[4:30]** two types these are passive attacks and active attacks passive attacks passive

**[4:36]** attacks are in nature of if dropping on or monitoring of transmission the goal

**[4:44]** of the opponent is to obtain information that is being transmitted two types of passive attacks are release of message

**[4:53]** contents and traffic analysis release of message contents is easily understood a

**[5:00]** telephone conversation an electronic message and a transferred file may contain sensitive or confidential

**[5:09]** information we would like to prevent an opponent from learning the contents of these

**[5:16]** Transmissions the figure on the screen reveals the concept of if dropping a second type of passive attack

**[5:25]** is traffic analysis suppose that we have had a way of masking the contents of messages or

**[5:33]** other information traffic so that the opponents even if they captured the message could not extract the

**[5:41]** information from the message the common technique for masking contents is encryption if we had encryption

**[5:49]** protection in place an opponent might still be able to observe the pattern of these messages the opponent could

**[5:57]** determine the location and identity of communicating hosts and could observe the frequency and length of messages

**[6:05]** being exchanged the information might be useful in guessing the nature of the communication that was taking place the

**[6:15]** figure on the screen reveals the concept of traffic analysis replay involves the

**[6:22]** passive capture of a data unit and its subsequent retransmission to produce an unauthorized effect as shown on the

**[6:31]** screen modification of messages simply means that some portion of a legitimate message is altered or that messages are

**[6:41]** delayed or reordered to produce an unauthorized effect for example a

**[6:47]** message meaning allow John Smith to read confidential file accounts is modified

**[6:54]** to mean allow Fred Brown to read confidential file

**[7:01]** 7 minutes, 1 second counts the concept is shown on the screen the denial of service prevents or

**[7:08]** inhibits the normal use or management of communication facilities this attack may

**[7:16]** have a specific Target for example an entity May suppress all messages directed to a particular

**[7:25]** destination another form of service denial is the disruption of an entire network either by disabling the network

**[7:35]** or by overloading it with messages so as to degrade performance the concept is shown on the

**[7:44]** screen are three goals of security that is confidentiality integrity and

**[7:51]** availability can be threatened by security attacks we can divide security attacks

**[7:58]** into three groups related to the security goals as well A New Concept snooping is introduced in this

**[8:07]** classification snooping means unauthorized access to or interception

**[8:13]** of data for example a file transferred through the internet may contain confidential information an unauthorized

**[8:22]** entity May intercept the transmission and use the content for her own benefit to prevent grouping the data can be made

**[8:31]** meaningless for the Interceptor by using encryption techniques let us discuss various

**[8:37]** network security service techniques some security services are required to achieve security goals and prevent

**[8:45]** attacks the actual implementation of security goals needs two techniques these techniques are designed

**[8:54]** to protect one or more attacks while maintaining security goals the the first technique is cryptography and second is

**[9:02]** security through specific devices cryptography a word with Greek origin means secret

**[9:09]** writing however we use the term to refer to the science and art of transforming messages to make them secure and immune

**[9:19]** to attacks although in the past cryptography referred only to the encryption and decryption of messages

**[9:26]** using secret keys today is defined Ed as involving three distinct mechanisms

**[9:33]** these are symmetric key cryptography asymmetric key cryptography and hashing let us discuss symmetric key

**[9:41]** cryptography it is also known as traditional Cipher in symmetric key cryptography same key is used for encryption and

**[9:50]** decryption and the key can be used for bidirectional communication the figure on the screen represents the general concept of

**[9:59]** symmetric key cryptography in this model plain text is used as input we convert the plain text

**[10:06]** into Cipher text by using an encryption algorithm and key on the receiver side Cipher text is converted into plain text

**[10:14]** by using decryption algorithm and key in symmetric cryptography sender and receiver share the same secret key

**[10:23]** asymmetric algorithm rely on one key for encryption and a different but Rel Ed key for decryption these algorithms have

**[10:33]** the following important characteristic it is computationally invisible to determine the decryption key given only

**[10:41]** knowledge of the cryptographic algorithm and the encryption key in addition some algorithms such as RSA also exhibit the

**[10:51]** following characteristics either of the two related keys can be used for encryption with the other used for decryption the

**[10:59]** main components of asymmetric key cryptography are as shown on the screen plain text this is the readable message

**[11:08]** or data that is fed into the algorithm as input encryption algorithm performs various

**[11:16]** Transformations on the plain text public and private keys this is a pair of keys that have been selected so that if one

**[11:24]** is used as encryption key the other is used as decryption key the exact Transformations performed by the

**[11:33]** algorithm depend on the public or private key that is provided as input Cipher text this is The Scrambled

**[11:43]** message produced as output it depends on the plain text and the key for a given message two different keys will produce

**[11:52]** two different Cipher texts decryption algorithm this algorithm accepts the

**[11:58]** cipher for text and the matching key and produces the original plain text hash

**[12:05]** functions a cryptographic hash function takes a message of arbitrary length and

**[12:11]** creates a message digest of fixed length all cryptographic hash functions need to

**[12:19]** create a fixed size digest out of a variable size message creating such a function is best accomplished using

**[12:28]** iteration instead of using a hash function with variable size input a function with fixed size input is

**[12:36]** created and is used as necessary number of times the fixed size input function

**[12:44]** is referred to as a compression function it compresses an nbit string to create

**[12:52]** an M bit string where n is normally greater than M the scheme is referred to

**[12:59]** as has an iterated cryptographic hash function several hash algorithms were designed by Ron rivest these are

**[13:08]** referred to as md2 md4 md5 where MD stands for message digest the last

**[13:15]** version md5 is a strengthened version of md4 that divides the message into blocks

**[13:22]** of 512 bits and creates a 128bit Digest it turns out that a

**[13:30]** message digest of size 128 bits is too small to resist attack the secure hash

**[13:39]** algorithm sha is a standard that was developed by the National Institute of

**[13:45]** Standards and Technology called nist sha has gone through several versions now

**[13:52]** let's discuss the network security through specific network devices when we think about network security we can also

**[14:01]** 14 minutes, 1 second think about the boundary in which our network is established we need to protect our network from external

**[14:09]** attacks and we also need to mind internal suspicious activities we usually deploy security devices as shown

**[14:19]** in the screen to protect our Network border routers as static filtering

**[14:26]** device firewalls in in detection systems idss IPS that is intrusion prevention

**[14:34]** systems border rooters as static filtering devices now routers are the

**[14:41]** traffic cops of the network they direct traffic into out of and within our

**[14:48]** networks as you can observe in the figure the Border router is the last router you control before an untrusted

**[14:56]** Network such as the internet because all of internet traffic goes through this

**[15:03]** router it often functions as in Network's first and last line of defense

**[15:10]** through initial and final filtering we can configure border router as static packet filtering device by

**[15:19]** configuring ACL that is assess control lists we called router as static filtering device because it can inspect

**[15:28]** packets only up to layer three that is Network layer improperly destined traffic might be internal addresses that

**[15:37]** hit your external interface or vice versa and they can be addressed with Ingress and egress

**[15:46]** filtering border routers can also block traffic that is considered high risk

**[15:52]** from entering your network icmp is a favorite of attackers both for denial of

**[15:59]** service attack and Reon insense so blocking this protocol in whole or in part is a common function of

**[16:07]** a border router you may also consider blocking Source rooted packets at the border

**[16:14]** router because they can circumvent defenses the Border router can also Block outof band packets such as syin

**[16:23]** packets on February 9 2000 websites such as Yahoo and CNN were temporarily taken

**[16:30]** off the internet mostly by distributed denial of service Smurf attacks a Smurf

**[16:37]** attack involves sending spoofed icmp Eco request that is pings to the broadcast

**[16:44]** addresses resulting in a response from every host in this case the spoofing

**[16:51]** allowed attackers to direct the large number of responses to a victim Network Ingress and egress filtering would have

**[17:00]** blocked the spoofed traffic and allowed them to weather the distributed denial of service

**[17:08]** stom every Network should have Ingress and ESS filtering at the border router

**[17:15]** to permit only traffic that is destined for the internal Network to enter and traffic that is destined for the

**[17:23]** external network to exit Fireball a fireball is a choke point

**[17:30]** device that has a set of rules specifying what traffic it will allow or deny to pass through it a firewall

**[17:38]** typically picks up where the Border router leaves off and makes a much more thorough pass at filtering traffic

**[17:48]** firewalls can be of three types static stateful and proxy Fireballs although

**[17:56]** firewalls aren't perfect effect they do block what we tell them to block and allow what we tell them to allow as

**[18:05]** previously discussed router can be used as static packet filter or as static

**[18:13]** firewall but we need specialized firewalls to implement as stateful and

**[18:20]** proxy firewalls unlike static packet filtering devices stateful firewalls

**[18:27]** keep track of Connections in a state table and are the most common type of

**[18:34]** firewalls a stateful firewall blocks traffic that is not in its table of

**[18:40]** established connections the firewall rule base determines the source and destination IP and port numbers

**[18:49]** permitted to establish connections by rejecting non-established non-permitted

**[18:56]** connections a stateful fireball helps to block reconnaissance packets as well as those that may gain more extensive

**[19:05]** unauthorized assess to protected resources proxy firewalls are the most advanced and least common type of

**[19:14]** firewalls proxy firewalls are also stateful in that they block any

**[19:21]** non-established non-permitted connections as with stateful firewalls the firewall rule base determines the

**[19:30]** source and destination IP and port numbers that are permitted to establish connections proxy firewalls offer a high

**[19:39]** level of security because internal and external hosts never communicate directly rather the fireball acts as an

**[19:49]** intermediary between hosts proxy firewalls examine the entire packet to ensure compliance with the protocol that

**[19:58]** is in indicated by the destination port number ensuring that only protocol compliant traffic passes through the

**[20:06]** fire wall helps defense in depth by diminishing the possibility of malicious traffic entering or exiting from your

**[20:15]** network proxy firewalls diminishes the possibility of malicious traffic entering or exiting your network by

**[20:23]** ensuring that only protocol compliant traffic passes through if intrusion detection systems now an IDs is like a

**[20:32]** security alarm system for your network that is used to detect an alert on malicious

**[20:40]** events the system might comprise many different IDs sensors placed at strategic points in your network in

**[20:49]** general IDs sensors watch for predefined signatures of malicious events and they

**[20:56]** might perform statistical and anomal nor analysis when IDs sensors detect suspicious events they can Alert in

**[21:05]** several different ways including email paging or simply logging the

**[21:12]** occurrence a network IDs could identify and alert on the following first is DNS Zone transfer

**[21:20]** request from unauthorized host uni code attacks directed at a web server buffer overflow attack

**[21:29]** V propagation Etc intrusion prevention systems now an IPS is a system that

**[21:39]** automatically detects and prevents Network and hosts attacks in contrast to

**[21:46]** a traditional IDs which focuses on notifying the administrator of anomalies

**[21:52]** and IPS strives to automatically defend the target without administrators direct

**[21:59]** involvement protection may involve using signature-based or behavioral techniques to identify an attack and then blocking

**[22:09]** the malicious traffic or system call before it causes harm in this respect an

**[22:16]** IBS combines the functionality of a firewall and IDs to offer a solution

**[22:23]** that automatically blocks offending actions as soon as it detects and attack frequently we get caught up in the

**[22:32]** technical aspect of network security without considering its non-technical elements tasks such as optimizing the

**[22:41]** firewall rule base examining Network traffic for suspicious patterns and locking down the configuration of

**[22:49]** systems are certainly important to network security what we often forget is the human end of

**[22:57]** things such as has policies and awareness that go along with the Technical Solutions policy determines what

**[23:06]** security measures your organization should Implement as a result the security policy guides your decisions

**[23:15]** when implementing security of the network an effective defense and depth infrastructure requires a comprehensive

**[23:23]** and realistic security policy Hallmarks of good security policy

**[23:30]** include Authority who is responsible scope who it affects expiration when it

**[23:38]** ends specificity what is required and Clarity can everyone understand it so in

**[23:46]** this session we have discussed what is network security security issues and basic network security techniques I hope

**[23:56]** you have enjoyed the session thank you so much much

**[24:01]** 24 minutes, 1 second [Music]

**[24:20]** [Music]
