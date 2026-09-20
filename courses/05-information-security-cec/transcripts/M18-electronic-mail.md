# Electronic Mail

**Module 18**  
Duration: 31:13  
Video: https://www.youtube.com/watch?v=DXGMUDoZZaA

Course Coordinator - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala  
Subject Expert -

> Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture (CEC / SWAYAM).

---

**[0:00]** [Music]

**[0:12]** Hello friends I am Professor yogesh Chaba from Department of computer science and engineering Guru jambeshwar

**[0:20]** University of Science and Technology Hisar harana in this lecture we will

**[0:27]** study about email system first of all please see the contents which I will cover after covering brief introduction

**[0:36]** about email system I shall take up email message format which will be followed by

**[0:44]** message communication protocol SMTP in last message reading protocols

**[0:52]** POP 3 IMAP and mapi will be explained

**[1:00]** email which is short form of electronic mail consist of digital messages which

**[1:07]** are sent and received using the internet it is a method of exchanging digital

**[1:15]** messages from one sender to one or more recipient email operates across the

**[1:25]** internet or other computer networks some early email systems required the author

**[1:34]** and the recipient to both be online at the same time today's email systems are based on

**[1:43]** a store and forward model email servers accept Forward

**[1:51]** deliver and store messages neither the users nor their computers are required

**[1:59]** to be online simultaneously an email system support

**[2:06]** five basic functions let us see one by one composition it refers to the process of

**[2:15]** creating messages and answers although any text editor can be

**[2:22]** used for the body of the message the system itself can provide assistance

**[2:29]** with with addressing and the numerous header Fields attached to each

**[2:36]** message transfer which refers to moving messages from the originator to the

**[2:45]** recipient reporting it has to do with telling the originator what happened to the message

**[2:54]** was it delivered was it rejected or was it lost displaying displaying of incoming

**[3:03]** messages is required so that people can read their email

**[3:11]** disposition which is the final step and concerns what the recipient does with

**[3:17]** the message after receiving it possibilities include throwing it

**[3:24]** away before reading throwing it away after reading

**[3:30]** saving it and few others they normally consist of two

**[3:38]** subsystems the user agents which allow people to compose and read

**[3:45]** email message format and sending is also taken care by user

**[3:52]** agent the user agents are local programs that provide a command based menu based

**[4:01]** 4 minutes, 1 second or graphical method for interacting with the email system protocols which

**[4:09]** supports message formatting are RFC 822 and multi-purpose internet mail

**[4:18]** extensions that is mine which was proposed in RFC

**[4:26]** 1341 for message reading there are three protocols that are POP 3 IMAP and

**[4:36]** mapi second subsystem that is message transfer agents is responsible for

**[4:44]** actual transmission of messages from the source to destination the message transfer agents

**[4:53]** are typical system demons that is processes that run in the background

**[5:01]** 5 minutes, 1 second their job is to move email through the network system protocols that support

**[5:08]** message communication is SMTP that is simple mail transfer

**[5:18]** protocol first we will see message format protocol for email that is

**[5:25]** mine the internet email message format defined by RFC

**[5:32]** 5322 with multimedia content attachments defined in RFC

**[5:39]** 2045 through RFC 2049 collectively called

**[5:46]** multi-purpose internet mail extensions or MIM RFC

**[5:54]** 532 replaced the earlier RFC 282 in 20 8 and RFC

**[6:03]** 282 in 2001 replaced RFC 82 which has been the standard for

**[6:11]** internet email for nearly 20 years internet email messages consist of

**[6:19]** two major sections the message header and the message body the header is

**[6:27]** structured into fields such as from to

**[6:33]** CC subject date and other information

**[6:39]** about the email the body contains the message as unstructured text sometimes

**[6:49]** containing a signature block at the end the header is separated from the

**[6:57]** body by a blank line now first let us see message header of RFC

**[7:04]** 82 and mine messages consist of a primitive

**[7:11]** Envelope as described in RFC 821 with some number of header Fields a

**[7:19]** blank line and then the message body each header field logically consist of a

**[7:28]** single line of asky text containing the field name a column and a value for each

**[7:36]** field RFC H2 was designed decades ago and does not clearly distinguish the

**[7:46]** envelope fields from the header Fields the principal header Fields

**[7:53]** related to message transport are listed as shown in figure

**[8:00]** the two field gives the DNS address of the primary recipient having multiple recipients is

**[8:09]** also allowed the CC field gives the address of any secondary

**[8:17]** recipients in terms of delivery there is no distinction between the primary and secondary

**[8:26]** recipients the BCC that is blind carbon copy field is like the CC field except

**[8:34]** that this line is deleted from all the copies sent to the primary and secondary

**[8:43]** recipients the next two field from and sender tell who wrote and sent the

**[8:52]** message respectively these need not be the same a line containing received

**[8:59]** is added by E each message transfer agent along the way this line contains

**[9:07]** the agent's identity the date and time the message was received and other

**[9:16]** information that can be used for finding bugs in the routing system the return

**[9:23]** path field is added by the final message transfer agent to tell how to get back

**[9:31]** to the sender in addition to the fields discussed just now RFC 82 messages may

**[9:41]** also contain a variety of header Fields used by the user agents or human

**[9:49]** recipients the most common ones are listed in figure as shown they are date

**[9:58]** which is used to indicate date and time of the message sent reply two indicates

**[10:07]** email address to which replies should be sent message ID indicates unique number

**[10:16]** for referencing this message later in reply two indicates message ID

**[10:25]** of the message to which this is a reply reference field indicates other relevant

**[10:34]** message IDs keywords indicates user chosen

**[10:40]** keywords and subject field indicates short summary of the message in one line

**[10:50]** display in the early days email consisted exclusive text messages

**[10:56]** written in English and pressed in aski for this environment RFC 82 explained

**[11:06]** did the job completely it specified the headers but

**[11:12]** left the content entirely up to the users nowadays on the worldwide internet

**[11:21]** this approach is no longer adequate because sender want to send audio image

**[11:29]** text video attachment with the mail a solution was proposed in RFC

**[11:38]** 1341 and updated in RFC 20452

**[11:45]** 2049 RFC 2045 to

**[11:50]** 2049 is collectively defined as RFC

**[11:57]** 532 this solution called mine multi-purpose internet mail extensions

**[12:04]** is now widely used mime defines five new

**[12:10]** message headers as shown in figure the first of these is mime version that

**[12:19]** simply tells the user agent receiving the message that it is dealing with a

**[12:26]** MIM message and which version of mime it uses the content description field is an

**[12:35]** asky string telling what is in the message the content ID field identifies

**[12:45]** the content the content transfer encoding tells how the body is wrapped

**[12:53]** for transmission through a network that may object to more characters other than

**[13:01]** 13 minutes, 1 second letters numbers and punctuation marks the last header shown is really

**[13:09]** the most interesting one and that is content type it specifies the type and

**[13:17]** format of the content the type and subtype in this

**[13:23]** field are separated by a slash for example video video/

**[13:31]** MPEG various types and subtypes of content type are shown in figure various

**[13:39]** types are text image audio video

**[13:46]** application message and multi-art after message header it comes

**[13:55]** message body a message body formatted according to the mime

**[14:01]** 14 minutes, 1 second specification is subdivided into parts that are organized as a

**[14:08]** hierarchy as with any hierarchy located at the top is the root body part labeled

**[14:15]** as R some parts contain other parts known as

**[14:22]** descendants this figure has two direct descendant body parts label

**[14:29]** A1 and A2 body part A1 do1 and A1 do2

**[14:38]** that do not contain other body parts are defined as content body parts and body

**[14:47]** part A1 and A2 that do not contain other body parts are defined as multi-art body

**[14:58]** parts contents body part contain the actual content of the message such as the plain

**[15:08]** text version of the message and attachment a HTML page and so on so this

**[15:19]** was about message format of emailing system now we will see how these

**[15:27]** messages are transferred or communicated the message transfer system

**[15:35]** is concerned with relaying messages from the originator to the

**[15:43]** recipient the simplest way to do this is to establish a transport connection from

**[15:50]** The Source machine to the destination machine and then just transfer the

**[15:58]** message simple mail transfer protocol SMTP is an internet standard for

**[16:07]** electronic mail transmission first defined by RFC a21 in

**[16:14]** 1982 it was last updated in 2008 with the extended SMTP editions by

**[16:24]** RFC 5321 which is the protocol used

**[16:30]** worldwide today SMTP is a connection oriented text based protocol in which a

**[16:39]** mail sender communicates with a mail receiver by issuing command and

**[16:47]** supplying necessary data over a reliable ordered data stream channel typically at

**[16:55]** TCP connection mail processing model using

**[17:01]** 17 minutes, 1 second SMTP is as shown in figure email is submitted by a male client

**[17:10]** muua that is male user agent to a mail server

**[17:16]** MSA that is mail submission agent using SMTP on TCP Port

**[17:26]** 587 most mailbox provide ERS still allow submission on traditional Port

**[17:36]** 25 from there the MSA delivers the mail to its mail transfer agent

**[17:44]** MTA often these two agents are just different instances of the same software

**[17:52]** launched with different options on the same machine the boundary MTA has to

**[17:59]** locate the target host it uses the domain name system DNS to look up the

**[18:07]** male exchanger record MX for the recipient's domain which is part of the

**[18:15]** email address on the right of at the rate sign the returned MX record contains the

**[18:25]** name of the target host the MTA next connects to the mail

**[18:32]** exchanger MX as an SMTP client once the

**[18:38]** MX accepts the incoming message it hands it to a mail delivery agent

**[18:44]** MDA for local mail delivery an MDA is able to save messages in the relevant

**[18:54]** mailbox format again mail reception can be done

**[19:00]** using many computers or just one an MDA May deliver messages directly

**[19:09]** to storage or forward them over a network using

**[19:15]** SMTP or any other means including the local mail transfer protocol

**[19:26]** lmtp a derivative of of SMTP designed for this

**[19:33]** purpose mail is retrieved by end user applications called email clients using

**[19:43]** IMAP POP 3 or IM AI protocol which we

**[19:49]** will study in next section this was how SMTP transmission takes place now let us

**[19:58]** see SMTP session an SMTP session consist of

**[20:05]** commands originated by an SMTP client that is sender and corresponding

**[20:13]** responses from the SMTP server that is receiver session is opened and session

**[20:21]** parameters are exchanged a session may include zero or more SMTP

**[20:30]** transactions an SMTP transaction consist of three command reply sequences as

**[20:38]** shown in figure maale command to establish the

**[20:45]** return address or return path or bounce address or envelope

**[20:52]** sender this is the address to which bounce messages should be

**[20:59]** send rcpt command to establish a recipient of this

**[21:06]** message this command can be issued multiple times one for each recipient

**[21:14]** these addresses are also part of the envelope data consist of a message

**[21:23]** header and a message body separated by an empty line

**[21:29]** now we shall discuss protocols for reading of emails interactions between email

**[21:38]** servers and clients are governed by email protocols the three most common

**[21:46]** email protocols for interaction or reading emails by user are post office

**[21:54]** protocol version 3 POP 3 inter message access protocol IM map and message

**[22:03]** application programming interface M AI most email software operates under

**[22:12]** one of these protocols now let us see each one by one first we shall take up

**[22:20]** pop three the basic pop three procedure is to retrieve all inbound messages is for

**[22:29]** storage on the client delete them on server and then

**[22:36]** disconnect the user get the email from the isp's message transfer agent

**[22:44]** protocol POP 3 described in RFC 1939 was

**[22:50]** originated with RFC 1081 its current specification is RFC

**[22:59]** 1939 updated with an extension mechanism RFC

**[23:06]** 249 and an authentication mechanism in RFC

**[23:13]** 1734 pop three begins when the user starts the mail reader the mail reader

**[23:21]** calls up the ISP and establishes a TCP connection with the message trans

**[23:28]** transer agent at Port 110 once the connection has been

**[23:35]** established the pop three protocol goes through three states in sequence first

**[23:44]** authorization second transaction third update the authorization State deals with having

**[23:53]** the user log in the transaction State deals with the user collecting the

**[24:00]** emails and marking them for deletion from the mail box the update State

**[24:08]** actually causes the emails to be deleted this Behavior can be observed by

**[24:17]** typing something like tnet mail. isp.com Port

**[24:26]** 110 here mail. isp.com represents the DNS name of isp's mail

**[24:36]** server tnet establishes a TCP connection to Port

**[24:43]** 110 on which the pop three server listens upon accepting the TCP

**[24:51]** connection the server sends an asky message announcing that it is present

**[24:59]** present client starts authorization state by sending over its username and

**[25:07]** password after a successful login the client can then send over the list

**[25:14]** command which causes the server to list the contents of the mailbox one message

**[25:21]** per line giving the length of that message the list is terminated by a

**[25:30]** period Then the client can retrieve messages using the RR command and mark them for deletion

**[25:40]** with D E when all messages have been retrieved and possibly marked for

**[25:48]** deletion the client gives the quit command to terminate the transaction

**[25:54]** State and enter the update state when the server has deleted all the

**[26:01]** 26 minutes, 1 second messages it sends a reply and breaks the TCP

**[26:06]** connection now after po3 let us see IM

**[26:13]** map for a user with an email account which is always assessed from one PC pop

**[26:22]** three works fine and is widely used due to its simply it and

**[26:30]** robustness but this is always not the case many time user want to assess email

**[26:39]** from some other computer also which is not possible in pop three this

**[26:46]** disadvantage gave rise to an alternative delivery protocol IMAP that is internet

**[26:55]** message assess protocol Define find in RFC

**[27:02]** 2060 the current version IMAP version 4 is defined by RFC

**[27:10]** 3501 IMAP is a newer protocol and oriented towards a connection mode of

**[27:19]** operation the standard IM procedure is to leave messages on the server instead

**[27:27]** of keeping copies so email is only accessible when

**[27:36]** online IMAP does not exclude keeping copies on the client but in an inversion

**[27:44]** of the way POP 3 works it's the servers copies that are considered the real

**[27:53]** ones that offers an important security benefit as you won't lose your email if for some

**[28:02]** reason client computers storage media fails an IMAP server typically listens

**[28:11]** on well-known Port 143 IMAP provides extensive mechanisms

**[28:19]** for reading messages or even parts of the messages with large audio and video

**[28:29]** attachments since the working assumption is that messages will not be transferred

**[28:36]** to the users's computer for permanent storage IMAP provides mechanisms for

**[28:44]** creating destroying and manipulating multiple mailboxes on the

**[28:52]** server in this way a user can maintain a mailbox for each

**[28:59]** correspondent and move messages there from the inbox after they have been

**[29:08]** read after IMAP it is now turn for last email reading protocol that is

**[29:17]** mapi the message application programming interface M

**[29:24]** AI is a proprietary email protocol of Microsoft that can be used by Outlook a

**[29:34]** Microsoft email client software to communicate with Microsoft Exchange

**[29:42]** which is its email server software it provides somewhat more

**[29:49]** functionality than an IMAP protocol unfortunately as a proprietary protocol

**[29:57]** it works only for Microsoft Outlook Exchange

**[30:05]** interactions so friends this was about email system used in Internet

**[30:13]** nowadays in this lecture first we covered introduction of email system

**[30:20]** which was followed by email message format and message transmission protocol

**[30:30]** SMTP in last message reading protocols

**[30:35]** POP 3 IMAP and mapi were explained thank

**[30:42]** you

**[30:44]** [Music]

**[30:58]** n

**[30:59]** [Music]
