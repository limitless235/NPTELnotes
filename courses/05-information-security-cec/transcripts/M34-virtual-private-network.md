# Virtual Private Network

**Module 34**  
Duration: 29:55  
Video: https://www.youtube.com/watch?v=14DVrUgf2k8

Course Coordinator - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala  
Subject Expert - Prof Yogesh Chaba, Department of Computer Engineering and IT, Guru Jambeshwar University of Science & Technology, Hisar

> Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture (CEC / SWAYAM).

---

**[0:00]** [Music]

**[0:16]** Hello friends I am Professor yogesh Chaba from Department of computer science and engineering Guru jambeshwar

**[0:24]** University of Science and Technology Hisar harana in this lecture we will

**[0:30]** study about virtual private networks first of all please see the contents which I shall cover after covering brief

**[0:39]** introduction about virtual private Network I shall take up its architecture

**[0:45]** which will be followed by features of openvpn in last relationship between

**[0:53]** firewall and VPN will be discussed friends today almost all

**[1:00]** companies have offices and plants scattered over many cities sometimes over multiple countries in the olden

**[1:09]** days it was common for such companies to lease lines from the telephone company

**[1:16]** for connectivity between some or all pairs of locations some companies still

**[1:23]** do this a network built up from company computers and Leed telep phone lines is

**[1:31]** known as a private Network an example of private Network connecting three

**[1:38]** locations is shown in figure private networks work fine and

**[1:45]** are very secure as no traffic can leak out of company location and Intruders

**[1:52]** have to physically wir tap the lines to break in which is not so easy to do

**[2:01]** 2 minutes, 1 second the problem with private networks is that they are very costly when public data networks and later the internet

**[2:10]** appeared many companies wanted to move their data and voice traffic to the

**[2:17]** public network but without giving up the security of the private Network this

**[2:24]** demand soon led to the invention of VPN that is virtual PR private networks

**[2:31]** which are overlay networks on top of public networks but with most of the

**[2:38]** properties of private networks a virtual private Network VPN provides a secure

**[2:46]** connection between a sender and a receiver over a public known secure

**[2:53]** network such as the internet they are known as virtual because they are are

**[3:00]** merely an illusion just as virtual circuits are not real circuits and

**[3:06]** virtual memory is not real memory a VPN is created by establishing

**[3:15]** a virtual Point topoint connection through the use of dedicated connections

**[3:22]** virtual tunnels and traffic encryption on internet as shown in figure a VPN

**[3:30]** connection across the internet is similar to a van link between

**[3:37]** websites from a user perspective the extended network resources are accessed

**[3:44]** in the same way as resources available within the private

**[3:51]** Network vpns allow employees to securely access their company's internet while

**[3:58]** traveling outside the office similarly vpns securely connect geographically

**[4:07]** separated offices of an organization creating one cohesive

**[4:14]** Network VPN technology is also used by individual internet users to secure

**[4:22]** their Wireless transactions to circumvent Geo restrictions and

**[4:28]** censorship and to connect to proxy servers for the purpose of protecting

**[4:36]** personal identity and location now let us see types of

**[4:43]** VPN currently there are three types of vpns while their goal is to use the

**[4:50]** internet as a private Enterprise backbone Network each of them addresses

**[4:57]** the needs of a different interest group in the Enterprise the three types of VPN will

**[5:06]** be explained now first is Access VPN which provide remote user or mobile user

**[5:14]** or tele computer or branch office with reliable access to corporate networks

**[5:22]** second is interet VPN that allow Branch offices to be linked to corporate at

**[5:30]** headquarters in a secure manner third is Extranet vpns that allow customers

**[5:38]** suppliers and partners to assess corporate internet in a secure manner

**[5:46]** now we will see VPN architecture a VPN as shown in figure

**[5:54]** illustrates VPN architecture which consist of four components

**[6:00]** a VPN client a network assess server NES a tunnel terminating device known as VPN

**[6:08]** server and a VPN protocol in this a client is connected to NES through

**[6:16]** public switched telephone network pstn network in a typical assess VPN

**[6:23]** connection a remote user or VPN client initiates a Point to-point protocol PPP

**[6:32]** connection with the isp's NES via the public switch telephone Network

**[6:40]** pstn the NES is owned by the ISP and is usually implemented in the isp's point

**[6:48]** of presence po after the user has been authenticated by the appropriate

**[6:56]** authentication method the NES directs the packet to the IP tunnel that

**[7:03]** connects both the NES and the VPN server the VPN server May reside in the

**[7:11]** isp's poop or at the corporate site depending on the VPN model that is

**[7:20]** implemented the VPN server recovers the packet from the tunnel unwraps it and

**[7:28]** delivers it to the corporate Network there are two basic categories

**[7:37]** of VPN tunneling protocols which are used to establish vpns these are Layer

**[7:45]** Two and layer three tunneling protocols Layer Two category contains pointto

**[7:52]** Point tunneling protocol pptp Layer Two forwarding protocol l2f and layer 2

**[8:00]** tunneling protocol l2tp whereas in layer three tunneling

**[8:06]** protocol we have IP security suit IP SEC

**[8:12]** when both pptp and l2f were submitted to the ietf it was decided to combine the

**[8:22]** features of both protocols into a common tunneling protocol which is now L2

**[8:30]** TP now first we shall see details of layer 2 protocol Layer Two protocols

**[8:39]** operate at the data link layer or Layer Two of OSI reference model they use the

**[8:47]** security provided by Point to-point protocol PPP authentication is performed

**[8:54]** using existing PPP authentication protocols namely password Authentication

**[9:02]** Protocol papap and challenge handshake Authentication Protocol chap no specific

**[9:11]** provision is made for data encryption which may be performed by the user prior

**[9:17]** to requesting VPN service the joural structure of the tunnel creation process

**[9:25]** for layer 2 tunneling protocols is shown in figure a client initiates a PPP

**[9:33]** Connection by dialing up the NES which is typically implemented in the isp's

**[9:40]** PO the client then answers and then perform The Logical control protocol LCP

**[9:48]** negotiation to establish the PPP authenticated connection once the PPP connection is

**[9:58]** established the NES uses either PPP or chap to authenticate the client using

**[10:06]** PPP authentication request client in response reply with PPP authentication

**[10:15]** reply message if the authentication is successful the NES attempts to open a

**[10:22]** PPP connection to the VPN server using openvpn request

**[10:29]** the VPN server will authenticate the NES using p or chap protocol by giving open

**[10:39]** VPN reply and thus PPP authentication is

**[10:46]** successful the client and the VPN server will then use the network control

**[10:52]** protocol NCP to negotiate the network layer protocol this compan completes the

**[10:59]** tunneling process and thus VPN is established between client and corporate

**[11:08]** server so this was how layer 2 protocol work now let us see first type of layer

**[11:15]** two protocol that is point too protocol pptp pptp is a protocol developed by

**[11:25]** Microsoft and a group of network equipment vendors including Ascend communication and 3om

**[11:34]** as an extension of PPP it handles only Point topoint connections and it does

**[11:41]** not support point to multi-point Connections in pptp the NES that allows

**[11:48]** the remote user to initiate a VPN call at ISP is known as the pptp assess

**[11:57]** concentrator p EAC and the VPN server at ISP is known

**[12:04]** as the pptp network server pns figure illustrates the components of

**[12:13]** a pptp based VPN pptp does not provide packet by packet encryption instead it

**[12:21]** relies on ppp's Native encryption capability in pep and chap

**[12:30]** figure shown illustrates the pptp packet format the PPP payload consist of the

**[12:38]** data and its original Ip and TCP header a pptp packet consisting of PPP payload

**[12:48]** and PPP header is encapsulated in generic routing

**[12:55]** encapsulation gr header which is then carried over IP IP header is inserted on

**[13:04]** top of gr header now next type of layer two protocol is Layer Two forwarding

**[13:13]** l2f l2f is a proprietary protocol that was developed by Cisco Systems it is

**[13:21]** protocol independent and can run over x.25 frame relay and ATM networks it

**[13:32]** supports private IP ipx and apple talk and uses UDP for internet

**[13:41]** tunneling l2f defines many connections within a tunnel allowing a tunnel to

**[13:49]** support many connections figure illustrates the components of an l2f

**[13:56]** based VPN in l2f the VPN server is known as home

**[14:04]** Gateway rest all components like Nas at ISP IP tunnel and others are same as in

**[14:13]** journal architecture of any layer 2 protocol l2f uses PPP for dialup user

**[14:23]** authentication unlike pptp l2f defines its own encapsulation header which is

**[14:31]** not dependent on IP and gr this capability permits l2f to work in

**[14:39]** different types of network figure illustrates the format of an l2f packet

**[14:47]** the slip or PPP payload is encapsulated in an l2f packet with an l2f header and

**[14:55]** an optional l2f checkm as the trailer next type of layer two protocol

**[15:04]** which we will take up is Layer Two tunneling protocol l2tp as stated earlier l2tp combines the

**[15:14]** features of pptp and l2f unlike pptp which runs over TCP l2tp

**[15:22]** runs over UDP and does not use gr because many fireworks s do not

**[15:30]** support gr l2tp is more firewall friendly than

**[15:36]** pptp figure illustrates the components of an l2tp based VPN in l2tp the nas is

**[15:46]** known as the l2tp asss concentrator LA and the VPN server is known as the

**[15:54]** l2tp network server LNS rest all components are same as in

**[16:02]** journal architecture of any layer 2 protocol l2tp uses PPP dialup links and

**[16:11]** as a result also uses PPP and chap for authentication however it allows the use

**[16:20]** of radius for user authentication l2tp permits multiple tunnels to be created between the same

**[16:29]** pair of end points allowing the user to create different tunnels with different

**[16:36]** qualities of service between the same end points figure shows the format of an

**[16:45]** l2tp packet as l2tp support UDP so there

**[16:51]** is UDP header after PPP header after UDP there is a IP header l 2tp is supported

**[17:01]** 17 minutes, 1 second by many vendors and is expected to be the pre-dominant protocol once it becomes a

**[17:09]** standard l2tp relies on IPC to perform data

**[17:15]** encryption if l2tp discovers that IPC is not supported at the remote end it uses

**[17:24]** the less secure PPP encryption after discussing Layer Two protocols let

**[17:31]** us move on to layer three tunneling protocols that is IP SEC IP SEC was

**[17:39]** originally designed to add security to the TCP IP IPC provides packet level

**[17:48]** authentication integrity and confidentiality by adding two security

**[17:55]** headers the authentication header ah which provides header integrity and

**[18:02]** authentication without confidentiality and the encapsulating security payload ESP which

**[18:11]** provides Integrity authentication and confidentiality to

**[18:19]** payload ESP permits packet by packet encryption and uses a standard-based

**[18:26]** encryption key management protocol thus IPC VPN can be created

**[18:34]** with either ah or ES or both ah does not

**[18:41]** provide data encryption and is useful in those environments where only authentication is

**[18:50]** required more importantly since authentication is not regulated ah is

**[18:57]** the preferred method for vpns ah also has a lower processing

**[19:05]** overhead than ESP however when data encryption is desired ESP is

**[19:13]** used on comparison of layer 2 and layer three tunneling protocol it is found

**[19:21]** that ipx supports only IP however pptp l2f and

**[19:29]** l2tp can support known IP traffic such as ipx and apple

**[19:37]** talk unlike IPC Layer Two tunneling protocols support individual dialup

**[19:45]** assess because they use PPP user authentication which permits seamless

**[19:53]** dialup connections through isps IP SE is designed for security

**[20:01]** 20 minutes, 1 second protection between routers and firewalls but it does not provides user

**[20:09]** authentication so these were Layer Two and layer three tunneling protocols

**[20:16]** there are few other VPN products that neither supports IPC nor l2tp one such

**[20:25]** product is openvpn this which is a fairly new opsource technology that uses the open

**[20:34]** SSL library and SSL version 3 or TLS

**[20:41]** version 1 protocols along with an mlgm of other Technologies to provide a

**[20:50]** strong and reliable VPN solution openvpn neither supports layer

**[20:57]** 2 nor layer three tunneling protocols openvpn support SSL and as such is not

**[21:06]** compatible with IPC l2tp or pptp one of its major strength is that

**[21:15]** it is highly configurable and although it runs best on a UDP Port it can be set

**[21:23]** to run on any port including TCP Port 440

**[21:29]** three another advantage of openvpn is that the open SSL Library used to

**[21:36]** provide encryption supports a number of cryptographic algorithms like AES

**[21:44]** Blowfish 3des cast 128 chamelia and many more with openvpn

**[21:54]** we can tunnel any IP sub Network or virtual ethernet adapter over a single

**[22:01]** 22 minutes, 1 second UDP or TCP Port configure a scalable load balanced VPN server using one or

**[22:10]** more machines which can handle thousands of dynamic connections from incoming VPN

**[22:19]** clients use all of the encryption authentication and certification

**[22:25]** features of the open SS SL library to protect any private Network traffic on

**[22:34]** internet use any Cipher key size or hmac digest for datagram integrity checking

**[22:43]** supported by the open SSL Library choose between static key based conventional

**[22:52]** encryption or certificate based public key encryption

**[22:59]** use static pre-shared keys or tls-based dynamic key

**[23:07]** exchange use realtime adaptive link compression and traffic shaping to

**[23:14]** manage link bandwidth utilization tunnel networks whose public

**[23:21]** end points are Dynamic such as DHCP or dialing clients

**[23:29]** tunnel networks through connection oriented State full firewalls without

**[23:35]** having to use explicit firewall rules tunnel networks over net create secure

**[23:45]** ethernet Bridges using virtual tap devices and control openvpn using a GUI

**[23:56]** on Windows or Mac operating system compared to pptp and l2tp or IP

**[24:06]** secc openvpn can be bit fidly to setup when

**[24:12]** using generic openvpn software in particular it is necessary to not only

**[24:19]** download and install the client but also to download and set up additional

**[24:26]** configuration files many VPN providers get around this configuration Problem by supplying

**[24:35]** customized VPN clients so friends we have studied many

**[24:42]** types of VPN in this lecture now let us Summarize each one by

**[24:49]** one pptp is very insecure and should therefore be avoided while its ease of

**[24:57]** setup and attractive crossplatform compatibility l2tp or IP SEC has the

**[25:06]** same advantage and is much more secure l2tp or IP SEC is a good VPN solution

**[25:16]** for non critical use however for a quick VPN setup without the need to install

**[25:24]** extra software it remains useful particularly for mobile devices where

**[25:32]** openvpn support remains somewhat patchy openvpn is easily the best

**[25:42]** allround VPN solution despite needing thirdparty software on all platforms it

**[25:50]** is reliable fast and most importantly secure although it usually needs a bit

**[25:58]** more settings than the other protocols so basically wherever possible

**[26:05]** we should always choose open VPN if we need a quick and simple solution such as

**[26:13]** for protecting our phone from casual criminals or when connecting to public

**[26:19]** Wi-Fi hotspot then l2tp or IPC will probably do but given the increase using

**[26:29]** availability of openvpn apps for mobile devices especially Android we still

**[26:36]** should prefer to use openvpn so far in this lecture we have

**[26:43]** been studying about VPN actually firewalls and VPN go hand in hand vpns

**[26:52]** open secure Tunnels for communication whereas firewalls sit at strategic

**[26:59]** locations on the network and block certain type of traffic many firewall

**[27:06]** products provide encrypted firewall to firewall tunnels firewall control assess

**[27:13]** to corporate network resources and establish trust between the user and the

**[27:20]** network consider the network configuration in figure shown the firewall at each Network controls access

**[27:29]** to resources in the network however the data transmitted between the two sides

**[27:36]** is still vulnerable to attack as it traverses the internet for this purpose

**[27:44]** vpns are created to provide privacy between two sites as there is usually no

**[27:52]** trust between the two sides in this way a combination of fireballs and a VPN

**[28:01]** 28 minutes, 1 second establishes trust and provides privacy between the two sides this approach

**[28:09]** provides more security than using either fir walls at both sides or a VPN between

**[28:18]** the two sides figure shows a VPN tunnel between two firewalls in the past

**[28:26]** firewall products provided only firewall Security Service however many new

**[28:34]** firewall products now support VPN functionality as stated earlier both

**[28:41]** firewall functionality and VPN functionality are needed to establish

**[28:49]** effective security control so friends this was about

**[28:55]** virtual private Network in this lecture we studied introduction

**[29:02]** about VPN which was followed by two architectures of VPN that is layer 2 and

**[29:11]** layer three then we discussed other VPN product which was based on

**[29:19]** SSL in the end relationship between firewall and VPN was discussed thank you

**[29:28]** e

**[29:29]** [Music]

**[29:48]** [Music]
