
--- 
title:  LLMs之Agent：Personal_LLM_Agents_Survey的简介、使用方法之详细攻略 
tags: []
categories: [] 

---
LLMs之Agent：Personal_LLM_Agents_Survey的简介、使用方法之详细攻略



>  
 **导读**：该项目包含了针对个人型LLM代理(Personal LLM Agents)的相关论文列表。通过查询相关论文，可以了解这一新兴技术方向的最新研究进展，比如在对话能力、知识表示、隐私保护等方面如何进行优化，从而提升用户体验。通过论文也可以了解这一技术的应用案例、难点以及解决方法。例如如何将LLM代理应用在教育或医疗助手等领域，如何使其对话能力更加逼真自然，或者如何保护用户隐私不被滥用等都是值得关注的问题。 总的来说，此项目给出了一个系统整理的个人LLM代理相关论文列表，从多个角度论述了这个新技术方向的发展现状和未来走势，有助于研究人员和开发者更好地把握趋势并开展工作。 






**目录**











































































## **<strong><strong>Personal_LLM_Agents_Survey的简介**</strong></strong>

个人LLM代理(智能体)被定义为一种特殊类型的基于LLM的代理，它与个人数据、个人设备和个人服务深度集成。它们最好部署到资源受限的移动/边缘设备和/或由轻量级AI模型提供支持。个人LLM代理的主要目的是协助最终用户并增强其能力，帮助他们更专注、更出色地处理有趣和重要的事务。

这份论文清单涵盖了个人LLM代理的几个主要方面，包括能力、效率和安全性。

**<strong>GitHub地址**</strong>：









## **<strong><strong>Personal_LLM_Agents_Survey的使用方法**</strong></strong>

### **1、****个人****LLM****代理的关键能力**

#### **(1)、****任务自动化**

任务自动化是个人LLM代理的核心能力，它决定了代理能够多好地响应用户命令和/或自动执行用户任务。由于UI-based任务自动化代理在这个列表中很受欢迎并与个人设备密切相关，我们专注于这方面。

##### **基于UI的任务自动化代理**



###### LLM-based Approaches
- WebGPT: Browser-assisted question-answering with human feedback. []- Enabling Conversational Interaction with Mobile UI Using Large Language Models. [CHI 2023] []- Language Models can Solve Computer Tasks. [NeurIPS 2023] []- DroidBot-GPT: GPT-powered UI Automation for Android. [] []- Responsible Task Automation: Empowering Large Language Models as Responsible Task Automators.[]- Mind2Web: Towards a Generalist Agent for the Web. arxiv 2023 [][][]- (AutoDroid) Empowering LLM to use Smartphone for Intelligent Task Automation. [] []- You Only Look at Screens: Multimodal Chain-of-Action Agents. ArXiv Preprint [] []- AXNav: Replaying Accessibility Tests from Natural Language. []- Automatic Macro Mining from Interaction Traces at Scale. []- A Zero-Shot Language Agent for Computer Control with Structured Reflection. []- Reinforced UI Instruction Grounding: Towards a Generic UI Task Automation API. []- GPT-4V in Wonderland: Large Multimodal Models for Zero-Shot Smartphone GUI Navigation. [][]- UGIF: UI Grounded Instruction Following. []- Explore, Select, Derive, and Recall: Augmenting LLM with Human-like Memory for Mobile Task Automation. [][]- CogAgent: A Visual Language Model for GUI Agents. [][]- AppAgent: Multimodal Agents as Smartphone Users. [][]
###### Traditional Approaches
- uLink: Enabling User-Defined Deep Linking to App Content. []- SUGILITE: Creating Multimodal Smartphone Automation by Demonstration. [CHI 2017] [][]- Programming IoT devices by demonstration using mobile apps. [IS-EUD 2017]- Kite: Building Conversational Bots from Mobile Apps. [MobiSys 2018]. []- Reinforcement Learning on Web Interfaces using Workflow-Guided Exploration. [ICLR 2018]. [][]- Mapping Natural Language Instructions to Mobile UI Action Sequences. [ACL 2020] [][]- Glider: A Reinforcement Learning Approach to Extract UI Scripts from Websites. [SIGIR 2021] []- UIBert: Learning Generic Multimodal Representations for UI Understanding. [IJCAI-21] []- META-GUI: Towards Multi-modal Conversational Agents on Mobile GUI. [EMNLP 2022][][]- UINav: A maker of UI automation agents. []


##### **UI自动化的基准测试**
- Mapping natural language commands to web elements. [EMNLP 2018] [][]- UIBert: Learning Generic Multimodal Representations for UI Understanding. [IJCAI-21] []- Mapping Natural Language Instructions to Mobile UI Action Sequences. [ACL 2020] [][]- A Dataset for Interactive Vision Language Navigation with Unknown Command Feasibility. [ECCV 2022][] []- META-GUI: Towards Multi-modal Conversational Agents on Mobile GUI. [EMNLP 2022][][]- UGIF: UI Grounded Instruction Following. []- ASSISTGUI: Task-Oriented Desktop Graphical User Interface Automation. [][]- Mind2Web: Towards a Generalist Agent for the Web. arxiv 2023 [][][]- Android in the Wild: A Large-Scale Dataset for Android Device Control. [][]- Empowering LLM to use Smartphone for Intelligent Task Automation. [] []- World of Bits: An Open-Domain Platform for Web-Based Agents. [ICML 2017] [][]- Reinforcement Learning on Web Interfaces using Workflow-Guided Exploration. [ICLR 2018]. [][]- WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents. [NeurIPS 2022] []- AndroidEnv: A Reinforcement Learning Platform for Android [][]- Mobile-Env: An Evaluation Platform and Benchmark for Interactive Agents in LLM Era. [][]- WebArena: A Realistic Web Environment for Building Autonomous Agents. [][]




#### **(2)、****感知**

理解当前上下文的能力对于个人LLM代理提供个性化、上下文感知的服务至关重要。这包括感知用户活动、心理状态、环境动态等技术。

##### **基于****LLM****的方法**


- “Automated Mobile Sensing Strategies Generation for Human Behaviour Understanding” (Gao et al., 2023, p. 521) - “Cue-CoT: Chain-of-thought Prompting for Responding to In-depth Dialogue Questions with LLMs” (Wang et al., 2023, p. 1) - “Exploring Large Language Models for Human Mobility Prediction under Public Events” (Liang et al., 2023, p. 1) - “Penetrative AI: Making LLMs Comprehend the Physical World” (Xu et al., 2023, p. 1) - “Evaluating Subjective Cognitive Appraisals of Emotions from Large Language Models” (Zhan et al., 2023, p. 1) - “PALR: Personalization Aware LLMs for Recommendation” (Yang et al., 2023, p. 1) - “Sentiment Analysis through LLM Negotiations” (Sun et al., 2023, p. 1) - “Bridging the Information Gap Between Domain-Specific Model and General LLM for Personalized Recommendation” (Zhang et al., 2023, p. 1) - “Conversational Health Agents: A Personalized LLM-Powered Agent Framework” (Abbasian et al., 2023, p. 1) 


##### **传统方法**


-  “Afective State Prediction from Smartphone Touch and Sensor Data in the Wild” (Wampfler et al., 2022, p. 1)  -  “Mobile Localization Techniques for Wireless Sensor Networks: Survey and Recommendations” (Oliveira et al., 2023, p. 361)  -  “Are You Killing Time? Predicting Smartphone Users’ Time-killing Moments via Fusion of Smartphone Sensor Data and Screenshots” (Chen et al., 2023, p. 1)  -  “Remote Breathing Rate Tracking in Stationary Position Using the Motion and Acoustic Sensors of Earables” (Ahmed et al., 2023, p. 1)  -  “SAMoSA: Sensing Activities with Motion and Subsampled Audio” (Mollyn et al., 2022, p. 1321)  -  “A Systematic Survey on Android API Usage for Data-Driven Analytics with Smartphones” (Lee et al., 2023, p. 1)  -  “A Multi-Sensor Approach to Automatically Recognize Breaks and Work Activities of Knowledge Workers in Academia” (Di Lascio et al., 2020, p. 781)  -  “Robust Inertial Motion Tracking through Deep Sensor Fusion across Smart Earbuds and Smartphone” (Gong et al., 2021, p. 621)  -  “DancingAnt: Body-empowered Wireless Sensing Utilizing Pervasive Radiations from Powerline” (Cui et al., 2023, p. 873)  -  “DeXAR: Deep Explainable Sensor-Based Activity Recognition in Smart-Home Environments” (Arrotta et al., 2022, p. 11)  -  “MUSE-Fi: Contactless MUti-person SEnsing Exploiting Near-field Wi-Fi Channel Variation” (Hu et al., 2023, p. 1135)  -  “SenCom: Integrated Sensing and Communication with Practical WiFi” (He et al., 2023, p. 903)  -  “SleepMore: Inferring Sleep Duration at Scale via Multi-Device WiFi Sensing” (Zakaria et al., 2022, p. 1931)  -  “COCOA: Cross Modality Contrastive Learning for Sensor Data” (Deldari et al., 2022, p. 1081)  -  “M3Sense: Affect-Agnostic Multitask Representation Learning Using Multimodal Wearable Sensors” (Samyoun et al., 2022, p. 731)  -  “Predicting Subjective Measures of Social Anxiety from Sparsely Collected Mobile Sensor Data” (Rashid et al., 2020, p. 1091)  -  “Attend and Discriminate: Beyond the State-of-the-Art for Human Activity Recognition Using Wearable Sensors” (Abedin et al., 2021, p. 11)  -  “Fall Detection based on Interpretation of Important Features with Wrist-Wearable Sensors” (Kim et al., 2022, p. 1)  -  “PowerPhone: Unleashing the Acoustic Sensing Capability of Smartphones” (Cao et al., 2023, p. 842)  -  “I Spy You: Eavesdropping Continuous Speech on Smartphones via Motion Sensors” (Zhang et al., 2022, p. 1971)  -  “Watching Your Phone’s Back: Gesture Recognition by Sensing Acoustical Structure-borne Propagation” (Wang et al., 2021, p. 821)  -  “Gesture Recognition Method Using Acoustic Sensing on Usual Garment” (Amesaka et al., 2022, p. 411)  - “Complex Daily Activities, Country-Level Diversity, and Smartphone Sensing: A Study in Denmark, Italy, Mongolia, Paraguay, and UK” (Assi et al., 2023, p. 1) - “Generalization and Personalization of Mobile Sensing-Based Mood Inference Models: An Analysis of College Students in Eight Countries” (Meegahapola et al., 2022, p. 1761) - “Detecting Social Contexts from Mobile Sensing Indicators in Virtual Interactions with Socially Anxious Individuals” (Wang et al., 2023, p. 1341) - “Examining the Social Context of Alcohol Drinking in Young Adults with Smartphone Sensing” (Meegahapola et al., 2021, p. 1211) - “Towards Open-Domain Twitter User Profile Inference” (Wen et al., 2023, p. 3172) - “One More Bite? Inferring Food Consumption Level of College Students Using Smartphone Sensing and Self-Reports” (Meegahapola et al., 2021, p. 261) - “FlowSense: Monitoring Airflow in Building Ventilation Systems Using Audio Sensing” (Chhaglani et al., 2022, p. 51) - “MicroCam: Leveraging Smartphone Microscope Camera for Context-Aware Contact Surface Sensing” (Hu et al., 2023, p. 981) -  “A Multi-Sensor Approach to Automatically Recognize Breaks and Work Activities of Knowledge Workers in Academia” (Di Lascio et al., 2020, p. 781)  -  Mobile and Wearable Sensing Frameworks for mHealth Studies and Applications: A Systematic Review” (Kumar et al., 2021, p. 81)  -  “Afective State Prediction from Smartphone Touch and Sensor Data in the Wild” (Wampfler et al., 2022, p. 1)  -  “Are You Killing Time? Predicting Smartphone Users’ Time-killing Moments via Fusion of Smartphone Sensor Data and Screenshots” (Chen et al., 2023, p. 1)  -  “FeverPhone: Accessible Core-Body Temperature Sensing for Fever Monitoring Using Commodity Smartphones” (Breda et al., 2022, p. 31)  -  “Guard Your Heart Silently: Continuous Electrocardiogram Waveform Monitoring with Wrist-Worn Motion Sensor” (Cao et al., 2022, p. 1031)  -  “Listen2Cough: Leveraging End-to-End Deep Learning Cough Detection Model to Enhance Lung Health Assessment Using Passively Sensed Audio” (Xu et al., 2021, p. 431)  -  “HealthWalks: Sensing Fine-grained Individual Health Condition via Mobility Data” (Lin et al., 2020, p. 1381)  -  “Identifying Mobile Sensing Indicators of Stress-Resilience” (Adler et al., 2021, p. 511)  -  “MoodExplorer: Towards Compound Emotion Detection via Smartphone Sensing” (Zhang et al., 2018, p. 1761)  -  “mTeeth: Identifying Brushing Teeth Surfaces Using Wrist-Worn Inertial Sensors” (Akther et al., 2021, p. 531)  -  “Detecting Job Promotion in Information Workers Using Mobile Sensing” (Nepal et al., 2020, p. 1131)  -  “First-Gen Lens: Assessing Mental Health of First-Generation Students across Their First Year at College Using Mobile Sensing” (Wang et al., 2022, p. 951)  -  “Predicting Personality Traits from Physical Activity Intensity” (Gao et al., 2019, p. 1)  -  “Predicting Symptom Trajectories of Schizophrenia using Mobile Sensing” (Wang et al., 2017, p. 1101)  -  “Predictors of Life Satisfaction based on Daily Activities from Mobile Sensor Data” (Yürüten et al., 2014, p. 1)  -  “SmartGPA: How Smartphones Can Assess and Predict Academic Performance of College Students” (Wang et al., 2015, p. 1)  -  “Social Sensing: Assessing Social Functioning of Patients Living with Schizophrenia using Mobile Phone Sensing” (Wang et al., 2020, p. 1)  -  “SmokingOpp: Detecting the Smoking ‘Opportunity’ Context Using Mobile Sensors” (Chatterjee et al., 2020, p. 41)  


#### **(3)、****记忆**

记忆是个人LLM代理保持关于用户信息的能力，使代理能够提供更定制的服务并根据用户偏好自我演变。

##### **记忆获取**
- “LifeLogging: Personal Big Data” - “Vision-based human activity recognition: a survey” - “Predicting personality from patterns of behavior collected with smartphones” - “Facial Emotion Detection Using Deep Learning” - “Emotion detection of textual data: An interdisciplinary survey” 
##### **记忆管理**


- “Privacystreams: Enabling transparency in personal data processing for mobile apps” - “Tree of Thoughts: Deliberate Problem Solving with Large Language Models” - “Chain-of-Thought Prompting Elicits Reasoning in Large Language Models” - “ReAct: Synergizing Reasoning and Acting in Language Models” - “Generative Agents: Interactive Simulacra of Human Behavior” - “Show Your Work: Scratchpads for Intermediate Computation with Language Models” - “Cognitive Architectures for Language Agents” 


##### **代理自我演化**
- “DreamCoder: growing generalizable, interpretable knowledge with wake–sleep Bayesian program learning” - “Voyager: An Open-Ended Embodied Agent with Large Language Models” - “Language models as zero-shot planners: Extracting actionable knowledge for embodied agents” - “Bootstrap Your Own Skills: Learning to Solve New Tasks with Large Language Model Guidance” - “FireAct: Toward Language Agent Fine-tuning” 




### **2、****LLM****代理的效率**

LLM代理的效率与LLM推理、LLM训练/定制以及内存管理的效率密切相关。

#### **(1)、****高效的****LLM****推理与训练**

LLM推理/训练的效率已经在现有调查中得到全面总结（例如此链接）。因此，在这个列表中，我们省略了这部分内容。

#### **(2)、****高效的记忆检索与管理**

在这里，我们主要列举与高效内存管理相关的论文，这是LLM代理的重要组成部分。



##### **组织记忆**



(with vector library, vector DB, and others)

**Vector Library**
- RETRO: Improving language models by retrieving from trillions of tokens. [ICML, 2021] []- RETA-LLM: A Retrieval-Augmented Large Language Model Toolkit. [arXiv, 2023] [] []- TRIME: Training Language Models with Memory Augmentation. [EMNLP, 2022] [] []- Enhancing LLM Intelligence with ARM-RAG: Auxiliary Rationale Memory for Retrieval Augmented Generation. [arXiv, 2023] [] []
**Vector Database**
- Survey of Vector Database Management Systems. [arXiv, 2023] []- Vector database management systems: Fundamental concepts, use-cases, and current challenges. [arXiv, 2023] []- A Comprehensive Survey on Vector Database: Storage and Retrieval Technique, Challenge. [arXiv, 2023] []
**Other Forms of Memory**
- Memorizing Transformers. [ICLR, 2022] [] []- RET-LLM: Towards a General Read-Write Memory for Large Language Models. [arXiv, 2023] []


##### **优化记忆的效率**



###### **Searching Design**
- Milvus: A purpose-built vector data management system. [SIGMOD, 2021] [()] []- Analyticdb-v: A hybrid analytical engine towards query fusion for structured and unstructured data. [Proceedings of the VLDB Endowment, Volume 13, Issue 12, pp 3152–3165] []- Hqann: Efficient and robust similarity search for hybrid queries with structured and unstructured constraints. [CIKM, 2022] []- Qdrant []
###### **Searching Execution**
- Faiss:Facebook AI Similarity Search. [] []- Milvus: A purpose-built vector data management system. [SIGMOD, 2021] [] []- Quicker ADC : Unlocking the Hidden Potential of Product Quantization With SIMD. [IEEE Transactions on Pattern Analysis and Machine Intelligence, 2019] [] []
###### **Efficient Indexing**
- LSH: Locality-sensitive hashing scheme based on p-stable distributions. [SCG, 2004] []- Random projection trees and low dimensional manifolds. [STOC, 2008] []- SPANN: Highly-efficient Billion-scale Approximate Nearest Neighborhood Search. [NeurIPS, 2021] [] []- Efficient and Robust Approximate Nearest Neighbor Search Using Hierarchical Navigable Small World Graphs. [IEEE Transactions on Pattern Analysis and Machine Intelligence, VOL. 42, NO. 4, 2020] []- DiskANN: Fast Accurate Billion-point Nearest Neighbor Search on a Single Node. [NeurIPS, 2019] [] []- DiskANN++: Efficient Page-based Search over Isomorphic Mapped Graph Index using Query-sensitivity Entry Vertex. [arXiv, 2023] []- CXL-ANNS: Software-Hardware Collaborative Memory Disaggregation and Computation for Billion-Scale Approximate Nearest Neighbor Search. [USENIX ATC, 2023] []- Co-design Hardware and Algorithm for Vector Search. [SC, 2023] [] []




### **3、****个人****LLM****代理的安全性和隐私**

AI/ML的安全与隐私是一个庞大的领域，涉及大量相关论文。在这里，我们只关注与LLM和LLM代理相关的论文。

#### **(1)、****机密性（用户数据的保密性）**
- THE-X: Privacy-Preserving Transformer Inference with Homomorphic Encryption. [ACL, 2022][]- TextFusion: Privacy-Preserving Pre-trained Model Inference via Token Fusion [EMNLP, 2022] [][]- TextObfuscator: Making Pre-trained Language Model a Privacy Protector via Obfuscating Word Representations. [ACL, 2023] [][]- Adversarial Training for Large Neural Language Models. [arXiv, 2020] [][]


#### **(2)、****完整性（代理行为的完整性）**



##### **Adversarial Attacks**
- Certifying LLM Safety against Adversarial Prompting. [arXiv, 2023] [][]- On evaluating adversarial robustness of large vision-language models. [arXiv, 2023] [][]- Jailbroken: How does llm safety training fail? [arXiv, 2023] []- On the adversarial robustness of multi-modal foundation models. [arXiv, 2023] []- Misusing Tools in Large Language Models With Visual Adversarial Examples. [arXiv, 2023] []- Jailbreak in pieces: Compositional Adversarial Attacks on Multi-Modal Language Models. [arXiv, 2023] []
##### **Backdoor Attacks**
- Backdoor attacks for in-context learning with language models. [arXiv, 2023] []- Prompt as Triggers for Backdoor Attack: Examining the Vulnerability in Language Models. [arXiv, 2023] []- PoisonPrompt: Backdoor Attack on Prompt-based Large Language Models. [arXiv, 2023] [][]- Defending against backdoor attacks in natural language generation. [arXiv, 2021] [][]
##### **Prompt Injection Attacks**
- Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection. [arXiv, 2023] []- Ignore Previous Prompt: Attack Techniques For Language Models. [arXiv, 2022] [][]- Prompt Injection attack against LLM-integrated Applications. [arXiv, 2023] [][]- Jailbreaking Black Box Large Language Models in Twenty Queries. [arXiv, 2023] [][]- Extracting Training Data from Large Language Models. [arXiv, 2020] []- SmoothLLM: Defending Large Language Models Against Jailbreaking Attacks. [arXiv, 2023] [][]




#### **(3)、****可靠性（代理决策的可靠性）**

##### **Problems**
- Survey of Hallucination in Natural Language Generation. [ACM Computing Surveys 2023] []- A Survey of Hallucination in Large Foundation Models. [arXiv, 2023] []- DERA: Enhancing Large Language Model Completions with Dialog-Enabled Resolving Agents. [arXiv, 2023] []- Cumulative Reasoning with Large Language Models. [arXiv, 2023] []- Learning From Mistakes Makes LLM Better Reasoner. [arXiv, 2023] []- Large Language Models can Learn Rules. [arXiv, 2023] []
##### **Improvement**
- PromptSource: An Integrated Development Environment and Repository for Natural Language Prompts. [ACL 2022] []- Super-NaturalInstructions: Generalization via Declarative Instructions on 1600+ NLP Tasks. [EMNLP 2022] []- Finetuned Language Models are Zero-Shot Learners. [ICLR 2022] []- SELFCHECKGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models. [EMNLP 2023] []- Large Language Models Can Self-Improve. [arXiv, 2022] []- Self-Refine: Iterative Refinement with Self-Feedback. [arXiv, 2023] []- Teaching Large Language Models to Self-Debug. [arXiv, 2023] []- Prompt-Guided Retrieval Augmentation for Non-Knowledge-Intensive Tasks. [ACL 2023] []- Chain-of-Note: Enhancing Robustness in Retrieval-Augmented Language Models. [arXiv, 2023] []- Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection. [arXiv, 2023] []- Self-Knowledge Guided Retrieval Augmentation for Large Language Models. [Findings of EMNLP, 2023] []
##### **Inspection**
- CGMH: Constrained Sentence Generation by Metropolis-Hastings Sampling. [AAAI 2019] []- Gradient-Based Constrained Sampling from Language Models. [EMNLP 2022] []- Large Language Models are Better Reasoners with Self-Verification. [Findings of EMNLP 2023] []- Explainability for Large Language Models: A Survey. [arXiv, 2023] []- Self-Consistency Improves Chain of Thought Reasoning in Language Models. [ICLR, 2023] []- Enhancing Chain-of-Thoughts Prompting with Iterative Bootstrapping in Large Language Models. [arXiv, 2023] []- Mutual Information Alleviates Hallucinations in Abstractive Summarization. [EMNLP, 2023] []- Overthinking the Truth: Understanding how Language Models Process False Demonstrations. [arXiv, 2023] []- Inference-Time Intervention: Eliciting Truthful Answers from a Language Model. [NeurIPS, 2023] []





