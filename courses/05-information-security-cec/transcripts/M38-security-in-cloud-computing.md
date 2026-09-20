# Security in Cloud Computing

**Module 38**  
Duration: 24:50  
Video: https://www.youtube.com/watch?v=5-6WRtoGJcQ

Course Coordinator - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala  
Subject Expert - Dr Sunil Kumar, Department of Electrical and Computer Engineering, Punjab Agriculture University, Ludhiana

> Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture (CEC / SWAYAM).

---

**[0:00]** [Music]

**[0:20]** Hello friends I welcome you all to the video lecture series of cyber security and information security in this lecture

**[0:28]** we will study about Security in cloud computing first of all please see the contents which I shall

**[0:35]** cover after covering brief introduction about Security in cloud computing I shall take up network security in cloud

**[0:44]** and last I shall take up platform related security so now let us start

**[0:50]** security is an important aspect to be considered in the cloud computing environment cloud computing security

**[0:59]** refers to the C of procedures processes and standards designed to provide information security Assurance in an cloud computing

**[1:07]** environment cloud computing security addresses both physical and logical security issues across all the different

**[1:15]** service models of software platform and infrastructure it also addresses how these services are delivered public

**[1:24]** private or hybrid delivery model Cloud security encompasses a broad broad range of security constraints from

**[1:31]** an end user and Cloud provider's perspective where the end user will primarily will be concerned with the

**[1:39]** provider security policy how and when their data is stored and who has access to that data subsequent sections talk

**[1:48]** about data security virtualization security security issues in software as a service infrastructure as a service

**[1:58]** and platform as a service model Etc security aspects cloud computing places business

**[2:06]** data into the hands of an outside provider and makes Regulatory Compliance inherently riskier and more complex than

**[2:15]** it is when systems are maintained in house loss of direct oversight means that the client company must verify that

**[2:24]** the service provider is working to ensure that data security and integrity are IR cled the following are the

**[2:32]** current security related research areas in cloud computing reliable distributed

**[2:39]** applications based on the internet such as the e-commerce system rely heavily on the trust path among involved

**[2:47]** parties the skyrocketing demand for a new generation of cloud-based consumer

**[2:54]** and business applications is driving the need for the next generation of data centers that must be massively scalable

**[3:02]** efficient agile reliable and secure in order to scale cloud services reliable to millions of service developers and

**[3:12]** billions of end users the Next Generation cloud computing and data center infrastructure will have to

**[3:19]** follow an evolution similar to the one that led to the creation of scalable telecommunication networks in the future

**[3:28]** network-based cloud service providers will leverage virtualization Technologies to be able to allocate just

**[3:36]** the right levels of virtualized compute Network and storage resources to individual applications based on

**[3:44]** realtime business demand while also providing full service level Assurance of availability performance and security

**[3:52]** at a reasonable cost data security due to huge infrastructure cost

**[4:00]** organizations are slowly switching to Cloud technology data are stored in the cloud service provider infrastructure as

**[4:09]** data do not reside in organization territory many complex challenges arise some of the complex data security

**[4:17]** challenges in Cloud include the following cloud service models with multiple tenents sharing the same

**[4:26]** infrastructure data mobility and legal issues relative to such government rules as European Union data privacy

**[4:36]** directive lack of Standards about how cloud service providers securely recycle

**[4:42]** disk space and erase existing data laws of visibility to key security and

**[4:49]** operational intelligence that no longer is available to feed Enterprise it security intelligence and risk

**[4:58]** management a new type of Insider who does not even work for your company but may have control and visibility into

**[5:06]** your data data center security data are stored in outside territory of the user in a location

**[5:13]** called as data center which is unknown to the user as the location of the data center is unknown to the user it becomes

**[5:21]** a virtual data center the backbone of this virtual data center is virtual infrastructure or the virtual machine

**[5:30]** however virtual platforms are dependent on many other often forgotten components of both the physical and virtual data

**[5:38]** centers there are typically seven areas of concern that accompany any major virtual platform implementation or

**[5:46]** migration often these issues are not seen during staging and testing and only appear when the virtual machines take on

**[5:55]** the same amount of load as physical machines the critical points represent two Corner Stones of the data center

**[6:04]** Network and storage lack of performance and availability virtualization moves many

**[6:12]** input output tasks tuned for Hardware to software via the hypervisor the virtualization

**[6:19]** translation layer is responsible for translating the optimized code for the software chip to the physical chip or

**[6:27]** CPU running on the underlying Hardware lack of application awareness one of the limitation of

**[6:35]** hypervisor and kernel based virtualization Solutions is that they only virtualize the operating system OS

**[6:44]** virtualization does not virtualize nor is it even aware of applications that are running on the

**[6:51]** OS even the same applications do not realize that they are using virtual Hardware on top of a

**[6:58]** hypervisor overflowing storage Network although converting physical machines to Virtual machines is an asset

**[7:06]** for building Dynamic data centers hard drives become extremely large flat file

**[7:13]** virtual dis images consequently file storage becomes unmanageable congested

**[7:20]** storage Network due to the portable nature of os virtualization there can be

**[7:26]** Dramatical increase in data traversing the storage Network for the same reason that virtual machine disk files can

**[7:35]** overrun physical storage once these images are made portable it becomes trivial to move these virtual machine

**[7:43]** images across the network from one host to another or from one storage array to another network security cloud is based

**[7:53]** on networking of many things together like the network of infrastructure while the network is the

**[7:59]** backbone of the cloud many challenges are encountered in this network some of the challenges in the existing Cloud

**[8:07]** networks are discussed in the following application performance Cloud tenant should be able to specify

**[8:15]** bandwidth requirements for applications hosted in the cloud ensuring similar performance to the on premise

**[8:24]** deployments many tired applications requires some guaranteed bandwidth between server instances to satisfy user

**[8:32]** transactions within an acceptable time frame and meet predefined service level

**[8:39]** agreements insufficient bandwidth between these servers will impose significant latency on user

**[8:47]** interactions flexible deployment of Appliance flexible deployment of

**[8:54]** appliances Enterprises deploy a wide variety of security applian es in their data centers such as de packet

**[9:04]** inspection or intrusion detection systems and firewalls to protect their applications from attacks these are

**[9:13]** often employed alongside other appliances that perform load balancing caching and application

**[9:20]** acceleration when deployed in the cloud an Enterprise application should continue to be able to flexibly exploit

**[9:28]** the functional ity of these appliances policy enforcement complexities traffic isolation and

**[9:36]** excess control to end users are among the multiple forwarding policies that should be enforced these policies directly impact

**[9:46]** the configuration of each router and switch changing requirements different

**[9:52]** protocols open shortest path first l a link aggregation group Virtual Router

**[10:00]** rency protocol vrrp and different flavors of L2 spanning tree protocols along with

**[10:10]** vendor specific protocols make it extremely challenging to build operate and interconnect a cloud Network at

**[10:18]** scale application rewriting applications should run out of the box as much as possible in

**[10:26]** particular for IP addresses and Network dependent failover mechanisms applications may need to be

**[10:33]** Rewritten or reconfigured before deployment in the cloud to address several Network related

**[10:41]** limitations two key issues are first lack of an broadcast domain abstraction

**[10:47]** in the cloud Network and second Cloud assigned IP addresses for virtual servers location

**[10:56]** dependency Network appliances and servers are typically tied to a statically configured physical Network

**[11:04]** which implicitly creates a location dependent constraint for instance the IP address of a server is typically

**[11:12]** determined based on the ven or the subnet to which it belongs V lens and subnets are based on the physical switch

**[11:20]** Port configuration therefore a virtual machine cannot be easily and smoothly migrated across the network constru

**[11:29]** trained virtual machine migration decreases the level of resource utilization and flexibility besides physical mapping of

**[11:38]** Wheeland or subnet space to the physical ports of a switch often leads to a fragmented IP address

**[11:45]** pool platform related security cloud service providers offer services in various service models like

**[11:54]** s AAS Bas and l a as where the user is offered

**[12:02]** varied Services based on his or her requirements every service model offer brings with it many security related

**[12:10]** challenges like secured Network locality of resources accessing secure data data

**[12:17]** privacy and backup policy security issues in cloud service models cloud computing uses Three Delivery models

**[12:25]** such as s a p AA S and L AAS through which different types of Computing

**[12:34]** Services are provided to the end user these three delivery models provide infrastructure resources application

**[12:41]** platform and software as services to the cloud customer these service models plays a different level of security

**[12:49]** requirements in the cloud environment L is the basis of all cloud services

**[12:57]** with paa s built upon it and s in turn

**[13:03]** built upon it just as capabilities are inherited so are the information security issues and risks there are

**[13:13]** significant trade-offs to each model in terms of integrated features complexity versus extensibility and

**[13:21]** security if the cloud service provider takes care of only the security at the lower part of the security architecture

**[13:29]** the consumers become more responsible for implementing and managing their security capabilities

**[13:37]** saas is a softwar deployed model in which applications are remotely hosted

**[13:44]** by the application or service provider and made available to customers on demand over the Internet the saas model

**[13:54]** offers the customers with significant benefits such as improved op operational efficiency and reduced costs

**[14:03]** saas is rapidly emerging as the dominant delivery model for meeting the needs of Enterprise IT

**[14:11]** services saas is rapidly emerging as the dominant delivery model for meeting the needs of

**[14:20]** Enterprise IT services p is one layer above

**[14:26]** L on the stack and racts a everything up to OS middleware Etc it offers

**[14:34]** developers a service that provides a complete software development life cycle management from planning to design to

**[14:42]** building applications to deployment to testing to maintenance everything else is abstract

**[14:49]** away from the view of the developers software as a service security issues in a traditional on

**[14:58]** premise application deployment model the sensitive data of each Enterprise continue to reside within the Enterprise

**[15:06]** boundary and are subject to its physical logical and personal security and exess control policies

**[15:14]** SAA applications are accessed through the web and so web browser security is very much

**[15:22]** important information security officers will need to consider various methods of securing SA a

**[15:30]** applications web services security extensible markup language encryption

**[15:36]** SSL and available options used in enforcing data protection transmitted over the Internet this involves the use

**[15:45]** of strong encryption techniques for data security and F grained authorization to

**[15:51]** control access to data the pain points of concern in saas are as follows network security in

**[16:01]** 16 minutes, 1 second an saas deployment model sensitive data flow over the network needs to be

**[16:08]** secured in order to prevent leakage of sensitive information this involves the use of strong Network traffic encryption

**[16:16]** techniques such as the SSL and TLS for security resource

**[16:23]** locality in an saas model of a cloud environment the end users use the

**[16:30]** services provided by the cloud providers without knowing exact where the resources for such services are located

**[16:38]** due to the compliance and data privacy rules in various countries locality of data is of utmost importance in much

**[16:47]** Enterprise architecture Cloud standards to achieve interoperability among clouds and to

**[16:55]** increase their stability and security Cloud standard s are needed across organizations for example the current

**[17:03]** storage Services by a cloud provider may be incompatible with those for other providers in order to keep their

**[17:11]** customers Cloud providers May introduce socalled sticky services that create difficulty for the users if they want to

**[17:19]** migrate from one provider to the other data Access Data access issue is mainly

**[17:26]** related to security policies provide to the users while accessing the data the organizations will have their

**[17:34]** own security policies based on which each employee can have access to a particular set of data the security

**[17:41]** policies May entitle some considerations wherein some of the employees are not given access to a certain amount of data

**[17:50]** these security policies must be ader by the cloud to avoid intrusion of data by unauthorized users

**[17:59]** the saas model must be flexible enough to incorporate these specific policies put

**[18:06]** forward by the organization the model must also be able to provide organizational boundary within the cloud because multiple

**[18:15]** organizations will be deploying their business processes within a single Cloud environment data

**[18:22]** breaches since data from various users and business organizations lie together in a cloud environment breaching into

**[18:31]** the cloud environment will potentially attack the data of all the users thus the cloud becomes a high value Target

**[18:41]** backup the saas vendor needs to ensure that all sensitive Enterprise data are

**[18:48]** regularly backed up to facilitate quick recovery in case of disasters also the use of strong encryption schemes to

**[18:56]** protect the backup data is recommended to prevent accidental leakage of sensitive information in the case of

**[19:03]** cloud vendors such as Amazon the data at RIS in est3 are not encrypted by default

**[19:11]** the users need to separately encrypt their data and backups so that it cannot be acccessed or tampered with by

**[19:19]** unauthorized parties platform as a service security issues

**[19:27]** paas Pro provides a ready to use platform including OS that runs on vendor provided

**[19:34]** infrastructure as the infrastructure is of the cloud service provider various security challenges of the focused

**[19:41]** architecture are caused mainly by the spread of the user objects over the hosts of the cloud stringently allowing

**[19:50]** excess of objects to the resources and defending the objects against malicious or corrupt providers reasonably reduce

**[19:58]** possible risks network access and service measurement bring together concerns about secure Communications and excess

**[20:08]** control well-known practices object scale enforcement of authorization and

**[20:14]** undeniable traceability methods May alleviate the concerns apart from the aform problems

**[20:22]** user privacy must be protected in a public share Cloud therefore prop most solutions must be privacy aware service

**[20:32]** continuity is another concern for many Enterprises that consider Cloud adoption accordingly fall tolerant reliable

**[20:41]** systems are required infrastructure as a service security issues cloud computing

**[20:48]** makes a lot of promises in the areas of increased flexibility and Agility potential cost savings and

**[20:56]** competition advantages for for developers so that they can stand up and infrastructure quickly and efficiently to enable them to develop the software

**[21:05]** to drive business success there are a lot of problems that cloud especially private Cloud solves but it is not that

**[21:14]** much good is solving problems related to security however in a private Cloud environment some of the traditional

**[21:23]** problems faced are as follows hypervisor security in private Cloud most or all of the services will

**[21:32]** run in a virtualized environment and the security model used by the hypervisor cannot be taken for granted a need to

**[21:41]** evaluate the security models and the development of hypervisors becomes

**[21:48]** necessary multi- tency although all the tenants in the multi- tency environment will be from

**[21:56]** the same company not all rents may be comfortable sharing infrastructure with other users within the same company

**[22:04]** identity management and access control in our traditional data center we were comfortable with the small handful of

**[22:12]** authentication repositories we had to work with active directory being one of the most popular but with private Cloud

**[22:21]** handling authentication and authorization for the cloud infrastructure handling denance and handling delegation of administration of

**[22:30]** various aspects of the cloud fabric are the major task to be addressed network security in private Cloud we are likely

**[22:39]** to have many components of a service communicate with each other over virtual network channels only accessing the traffic employing

**[22:49]** some powerful access controls for physical networks and control quality of service which is a key issue in the

**[22:56]** availability aspect of the confidentiality integrity and availability security model are major

**[23:05]** concerns combining the three types of clouds public Cloud private cloud and hybrid Cloud together with the three

**[23:14]** Service delivery models we get a complete picture of a cloud computing environment interl by connectivity

**[23:22]** devices coupled with information security components virtualized physical sources

**[23:29]** virtualized infrastructure virtualized middleware platforms and business related applications are being provided

**[23:37]** as Computing Services in the cloud cloud providers and Cloud consumers must be able to maintain and

**[23:46]** establish Computing security at all levels of interfaces in the cloud computing architecture so friends this was all

**[23:55]** about Security in cloud computing hope the concepts explained in this lecture were understandable and helpful hope to

**[24:03]** see you in next lecture till then goodbye thank you

**[24:08]** [Music]

**[24:46]** [Music]
