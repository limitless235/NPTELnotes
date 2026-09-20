# Defence to DDoS Attacks

**Module 47**  
Duration: 24:56  
Video: https://www.youtube.com/watch?v=w_XZu6Rc0jM

Course Coordinator - Dr Maninder Singh, Professor and Dean, Academic Affairs, Thapar University, Patiala  
Subject Expert - Dr Abhinav Bhandari, Department of Computer Engineering, Punjabi University, Patiala

> Auto-generated YouTube transcript for personal study. Spoken wording belongs to the original lecture (CEC / SWAYAM).

---

**[0:00]** [Music]

**[0:15]** dear viewers in the previous lecture we have gone through the basics of Doos attacks motivation behind these attacks

**[0:22]** and classification of Dos attacks in today's lecture we will be discussing few aspects of DS attacks that that make

**[0:30]** defending against them difficult after that we will focus on challenges and goals for designing an ideal defense

**[0:37]** solution in the last part of the lecture we will learn some of the tips that can be helpful for preventing the system

**[0:44]** from being attacked by the DS attackers let's begin by learning why dos problem is hard to

**[0:51]** solve dos defense is a challenging issue among the cyber security Community the following characteristics of Dos

**[0:58]** flooding attacks make these attacks very effective for the attacker's purpose and extremely challenging for the defense

**[1:06]** simplified procedures of launching these attacks there are many Doos tools that can be easily downloaded or otherwise

**[1:13]** obtained and set into action they make agent Recruitment and activation automatic and can be used by

**[1:21]** inexperienced users these tools are exceedingly simple and some of them have been around for years still they

**[1:29]** generate effective attacks with little or no tweaking next is traffic variation the similarity of attack traffic to

**[1:37]** legitimate traffics makes separation and filtering extremely hard unlike other security threats that need specially

**[1:44]** crafted packets example intrusions WMS virus flooding attacks need only high traffic volume and can vary packet

**[1:52]** contents and headers value at its will next comes the IP spoofing IP spoofing makes the attack traffic appear as if it

**[2:01]** 2 minutes, 1 second comes from numerous legitimate clients this defeats many resource sharing approaches that identify a client by his

**[2:09]** IP address if IP address were eliminated agents could potentially be distinguished from legitimate clients by

**[2:17]** their aggressive sending patterns and their traffic could be filtered in the presence of Ip spoofing the victim sees a lot of service

**[2:26]** initiation request from numerous seemingly legitimate users while the victim could easily tell those packets apart from ongoing

**[2:35]** Communications with the legitimate users it cannot distinguish new legitimate requests for service from the attack

**[2:42]** ones thus the victim cannot serve any new users during the attack if the attack is long the damage

**[2:50]** to the victim's business is obvious another issue is huge volume of traffic the high volume of attack

**[2:58]** traffic at the victim victim not only overwhelms the targeted resource but makes traffic profiling hard at such

**[3:06]** high packet rates the defense mechanism can do only simple per packet processing the main challenge of Dos defense is to

**[3:13]** discern the legitimate from the attack traffic at higher packet speeds next is several zombies machine

**[3:22]** can be another Factor the strength of adidos attacks lies in numerous agent machines distributed all over the internet with

**[3:31]** so many agents the attacker can take and even the largest networks and he or she can vary his or her attack by deploying

**[3:39]** subsets of agents at time or sending few packets from each agent machine wearing attack strategies defeat many defense

**[3:47]** mechanism that attempt to trace back the attack to its source even the cases when the attacker does not vary the attacking machines the

**[3:56]** mere number of Agents involved makes Trace back and un attractive solution what if we knew the identities of 10,000

**[4:03]** machines that are attacking our Network this would hardly get any closer to stopping the attack the situation would

**[4:11]** clearly be simplified if the attacker were not able to recruit so many agents as discussed the general increase of internet host and more recently the

**[4:20]** higher percentage of novice internet users suggest that pool of potential agents will only increase in

**[4:27]** future furthermore the the distributed internet management model makes it unlikely that any security mechanism will be widely

**[4:36]** deployed thus even if we found ways to secure machines permanently and make them in previous to the attacker

**[4:43]** intrusion attempts it would take many years until these machines would sufficiently deploy to impact the Dos

**[4:51]** threat feak spots in the internet topology the current Internet Hub and spoke topology has a handful of Highly

**[4:59]** connected and very well provisioned spots that relay traffic for rest of the internet these hubs are highly Provisions to handle heavy traffic in

**[5:08]** the first place but if these few spots were taken down by the attacker or heavily congested the internet would

**[5:16]** grind to a halt amassing a large number of agent machines and generating heavy traffic passing through those hotspots

**[5:23]** would have devastating effect on global community so in n sh let's face it a

**[5:32]** flooding based Doos attack seems like a perfect crime in the internet attack tools and agent machines are abundant

**[5:39]** and easily obtainable a sufficient attack volume is likely to bring the strongest victim to its knees and the right mixture of

**[5:47]** attack traffic along with the IP spoofing will defeat attack filtering attempts since numerous business rely

**[5:56]** heavily on the online assess taking that way is show sure to inflict considerable damage to the victim and finally IP spoofing numerous

**[6:05]** agent machines and lack of automated tracing mechanism across the network gruny little to no risk to protect of

**[6:13]** being caught next we will discuss about the challenges of DS

**[6:20]** defense the challenges in designing DS defense system fall roughly into two categories technical challenges and the

**[6:28]** social challenge technical challenges incompasses problems associated with the current Internet Protocol and characteristics of

**[6:36]** Dos threat Social Challenges on the other hand largely pertain to the manner in which a successful technical solution

**[6:45]** will be introduced to the internet users and accepted and widely deployed by these users the main problem that prevails in

**[6:54]** both Technical and social issues is the problem of large scale dos is is a distributed threat that requires a merit

**[7:02]** of overlapping solutions to various aspects of Dos problem which must be spread across the internet because

**[7:09]** attacking machines may be spread all over the Internet clearly attack streams can only be controlled if there is a point of

**[7:18]** Defense between the agents and the victims one approach is to place one defense system close to the victim so

**[7:26]** that it monitors and controls all the incoming TR traffic this approach has many deficiencies the main one being

**[7:34]** that system must be able to efficiently handle and process huge traffic volume the other approach is to divide this

**[7:42]** workload by deploying distributed defense defense system must be then deployed in a widespread manner to

**[7:49]** ensure effective action for any combination of agent and victim machines as WID spread deployment cannot

**[7:58]** be granted the technical challenge lines in designing effective defenses that can provide reasonable performance even if

**[8:05]** they are sparely deployed the social challenge lies in designing an economic model of a defense

**[8:13]** system in a manner that motivates large scale deployment in the internet we will discuss first about the

**[8:21]** technical challenges the distributed nature of DS attacks similarity of the attack packets

**[8:29]** to the legitimate ones and the use of Ip spoofing represents the main technical challenge to the designing effective

**[8:35]** Doos defense system as discussed in the previous section in addition to that advance of Dos defense research has

**[8:43]** historically been hindered by the lack of attack information and absence of standardized evaluation and testing

**[8:51]** approaches the following list summarizes and discusses technical challenges for DS defense

**[8:59]** need for distributed response at many points in the internet there are many possible dos attacks very few of which

**[9:08]** can be handled only by the victim thus it is necessary to have distributed possibly coordinated response

**[9:16]** system it is also crucial that response be deployed at many points in the internet to cover diverse choices of agents and

**[9:25]** victim since the internet is administrated in a distributed manner wide deployment of any defense system or

**[9:33]** even various system that could cooperate cannot be enforced or granted this discourages many

**[9:40]** researchers from even considering distributed Solutions next comes the lack of detailed attack

**[9:48]** information it is widely believed that reporting occurrences of attack damages the business reputation of victim

**[9:56]** Network therefore very limited information exist about various attacks and incidents are reported only to government organizations under

**[10:04]** obligation to keep them secret it is difficult to design a imaginative solution to the problem if

**[10:11]** one cannot become familiar with it note that the attack information should not be confused with the attack tool information which is publicly available

**[10:20]** at many internet sites attack information would include the attack type time and duration of attack number

**[10:28]** of Agents involved if this information is known attempted response and its Effectiveness and damage is

**[10:36]** suffered lack of defense system benchmarks many vendors make bold claims that their solution completely handles

**[10:44]** the deos problem there is currently no standardized approach for testing dos defense system that would enable their

**[10:52]** comparison and characterization this has two detal influences on dos research

**[11:00]** since there is no attack Benchmark defense designers are allowed to present those tests that are most advantageous

**[11:08]** to their system and researchers cannot compare actual performance of their solution to the existing defenses

**[11:17]** instead they can only comment on design issues next comes the difficulty of large scale

**[11:25]** testing Doos defense need to be tested in a realistic enir environment this is currently impossible due to the lack of

**[11:33]** large scale test beds safe ways to perform live distributed experiments across the internet or detailed and

**[11:40]** realistic simulation tools that can support several thousands of nodes Claim about defense system

**[11:48]** performance are thus made based on small scale experiments or simulations are not

**[11:55]** credible some test bits are in use right now by DS resers example Planet lab and IMU

**[12:03]** lab now we will discuss about the Social Challenges many dos defense systems require certain deployment patterns to

**[12:12]** be effective those patterns fall into several category complete deployment a

**[12:20]** given system is deployed at each host router or network in the internet next is continuous deployment a given system

**[12:29]** is deployed at host or routers that are directly connected next is large scale widespread deployment the majority of

**[12:38]** hosts in the internet deploy a given System complete deployment at specified points in the

**[12:46]** internet there is a set of carefully selected deployment points All Points must deploy the proposed defense to

**[12:53]** achieve the desired security modification of widely deployed internet protocols such as tcpip or

**[13:03]** HTTP next we will discuss that what are the goals necessary to have a strong and effective defense

**[13:11]** system following are some of Doos defense goals which Doos defense strategies strive to

**[13:19]** achieve first is Effectiveness a good Dos defense should actually defend it should provide either

**[13:28]** effective prent prevention that really makes attacks impossible or effective reaction ensuring that dos effect goes

**[13:37]** away in the case of reactive mechanism the response should be sufficiently quick and automated to ensure that the

**[13:44]** target does not suffer seriously from the attack next goal should be completeness a good Dos defense should

**[13:53]** handle all possible attacks if that degree of perfection is impossible it should at least handle a large number of

**[14:02]** them a mechanism that is capable of handling an attack based on TCP sin flooding but cannot offer any assistance

**[14:10]** if a ping flood arrives is clearly less valuable than a defense that can handle both styles of

**[14:18]** attack thus a preventive measures like TCP sin cookies helps but is not

**[14:25]** sufficient unless coupled with other defense mechanisms completeness is also required in detection and reaction if our detection

**[14:35]** mechanism does not recognize a particular pattern of incoming packet as an attack pre assumably it will not work

**[14:42]** invoke any response and attack will succeed while completeness is an obvious goal it is extremely hard to

**[14:51]** achieve since attackers are likely to develop new types of attacks specially designed to bypass existing defense

**[14:59]** moreover flash events discussed need clear-cut distinctions from dos attacks next is minimum collateral

**[15:09]** damage as discussed above the core goal of Doos defense is not to stop dos attack packets but to ensure that

**[15:17]** legitimate users can continue to perform their normal activities despite the presence of Dos attack clearly a good

**[15:25]** defense mechanism must achieve it some legitimate traffic may be flowing from sides that are also sending attack

**[15:33]** traffic other legitimate traffic is destined for nodes on same network as the target node there may be a

**[15:41]** legitimate traffic that is neither coming from an attack machine nor being delivered to the targets network but perhaps shares some portion of its path

**[15:50]** through the internet with some of the attack traffic and some of the legitimate traffic meares other characteristics

**[15:58]** with the track traffic such as application protocol or destination Port potentially making it difficult to

**[16:05]** distinguish between them none of these legitimate traffic categories should be distributed by the

**[16:12]** Dos defense mechanism however dos defense mechanisms are not able to characterize dos traffic accurately and

**[16:21]** drop a part of legitimate traffic also this dropping of legitimate traffic is called coal literal damage

**[16:30]** since dos attackers often strive to conceal their tra traffic in the legitimate traffic stream it is common

**[16:38]** for legitimate traffic to closely resemble the attack packets so the problem of collateral damond is real and

**[16:46]** serious especially in case of flash events protecting legitimate traffic that is minimizing collateral

**[16:54]** damage is very important next comes the low Falls positive rates defense mechanism should Target only

**[17:02]** true dos attacks preventive mechanism should not have the effect of hurting other forms of net

**[17:09]** traffic reactive mechanism should be activated only when a Doos attack is actually

**[17:16]** underway a detection scheme can falsely detect an attack in a situation when no attack was actually

**[17:23]** happening this is called false positive these false positive CA collateral damage as they trigger the

**[17:31]** filtering mechanism when there is actually no attack moreover reactive mechanisms are likely to incure some

**[17:39]** cost the cost is in terms of extra CPU Cycles memory and delay caused on processing of all

**[17:47]** packets low deployment and operational cost dos defense are meant to allow systems to continue operations during DS

**[17:56]** attacks the cost associated with the defense system must be common straight with Benefits provided by it for

**[18:04]** commercial Solutions there is an obvious economic cost of buying the hardware and software required to run it usually

**[18:12]** there are also significant system administration cost with setting up new security equipment or

**[18:20]** software depending upon the character of dedos defense mechanism it may require frequent ongoing

**[18:27]** Administration for example example a mechanism based on detecting signatures of particular attacks will need to

**[18:34]** receive update as new attacks are characterized requiring either manual or automated actions other operational cost

**[18:43]** relate to overheads imposed by the defense system A system that performs stateful

**[18:50]** inspection of all incoming packets May delay each packet for example or a system that throttles data streams from

**[18:59]** suspicious sources may slow down any legitimate interactions with those sources unless such cost are extremely

**[19:07]** low or extremely rare paid they must be balanced against benefits of achieving some degrees of protection against dos

**[19:17]** attacks how we can defend against these attacks our next part of discussion will focus on the

**[19:25]** defense Doos defense modules are shown in the Fig figure generally there are four broad

**[19:32]** categories of defense against dos attacks first is attack prevention second is attack detection

**[19:40]** third is attack Source identification and fourth is attack reaction attack preventions aims to stop

**[19:49]** attacks before they can reach their target it refers to the filtering spoof packets close to or at the attack

**[19:57]** sources which is one of the most effective defense approaches for dos attacks that use poofed

**[20:05]** traffic attack detection aims to detect dos attacks when they occur attack detection is an important

**[20:12]** procedures to direct any further action it is the process of detecting the attack based on the traffic feature

**[20:21]** distribution signature based detection techniques are not applied for dos defense due to everchanging nature of signature of

**[20:30]** attacks anomaly based detection techniques are suitable for for this purpose next is attack Source

**[20:38]** identification which aims to locate the attack sources regardless of whether the source address field in which packet

**[20:45]** contains enormous information it is a crucial steps to minimize the attack damage and provide

**[20:53]** prevention to the potential attackers next comes the attack reactions with which aims to eliminate

**[21:00]** or curtail the effects of an attack it is the final step in defending against dos attacks and therefore determines the

**[21:08]** overall performance of the defense mechanism the challenge of the attack reaction is however to filter and attack traffic without disturbing the

**[21:16]** legitimate traffic in the last part of the discussion we will learn some of the important tips which helps us to protect

**[21:25]** our system from being attacked by dos first is Implement router filters this will lessen your exposures to certain

**[21:34]** denial of service attacks additionally it will Aid in preventing users on your network from effectively launching

**[21:42]** certain denial of service attacks second if they are available for your system install patches to guard against TCP sin

**[21:51]** flooding this will substantially reduce your exposure to those attacks but may not eliminate the risk entirely

**[22:00]** third is disable any unused or unneeded Network Services this can limit the ability of an intruder to take advantage

**[22:08]** of those services to execute a denial of service attack next is enable quota systems on

**[22:15]** your operating system if they are available for example if your operating system supports dis quotas enable them

**[22:23]** for all accounts especially accounts that operate Network Services in addition if your operating system

**[22:30]** support partitions or volume consider partitioning your file system so as to separate critical functions from other

**[22:39]** activities next is observe your system performance and establish baselines for ordinary

**[22:47]** activity next use the baselines to cause unusual levels of disk activity CPU uses

**[22:54]** or network traffic next routinely examine your physical security with respect to your

**[23:02]** current needs consider servers routers un attending terminals network access points wiring closets environmental

**[23:11]** systems such as air and power and other components of your system next use trip wire or similar

**[23:19]** tool to detect changes in the configuration information or other files next invest in redundant and fall

**[23:28]** TN Network configurations establish and maintain regular backup schedules and policies

**[23:35]** particularly for important configuration information next establish and maintain

**[23:42]** appropriate password policies especially assessed to highly privileged account such as Unix rout or Microsoft Windows

**[23:52]** administration at last I would like to conclude that DS attacks is a devastating attack among the cyber community and the defense to this attack

**[24:01]** 24 minutes, 1 second is eluded so far though there are many academic and Commercial Solutions present in the

**[24:08]** market in this lecture we have discussed some of the factors that made dos attack problem harder to solve we have also

**[24:15]** learned some of the key challenges and goals for designing an ideal defense solution some tips to manage your system against these attacks are also

**[24:24]** highlighted thank you all

**[24:27]** [Music]

**[24:48]** [Music]
