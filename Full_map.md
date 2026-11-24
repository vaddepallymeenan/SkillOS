# Canonical AI/ML Engineer Curriculum (2026)

## Phase 0

### Programming Fundamentals [FOUNDATION]

- Variables, Data Types, Operators
- Conditionals, Loops
- Data Structures
- Functions, Builtin Functions
- Exception Handling
- Object Oriented Programming

### Python for AI/ML [CORE]

- Python Syntax and Idioms
- Virtual Environments and Package Management
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebooks

### Software Engineering Practices [CORE]

- Testing (pytest)
- Linting and Formatting
- Logging
- Configuration Management
- Environment Variables
- Secrets Management

### Version Control [FOUNDATION]

- Git
- GitHub / GitLab
- Branching Strategies
- Pull Requests and Code Review

### Mathematical Foundations [FOUNDATION]

- Linear Algebra
  - Scalars, Vectors, Tensors
  - Matrix and Matrix Operations
  - Eigenvalues and Eigenvectors, Diagonalization
  - Determinants, Inverse of Matrix
  - Singular Value Decomposition
- Calculus
  - Derivatives, Partial Derivatives
  - Chain Rule of Derivation
  - Gradient, Jacobian, Hessian
- Discrete Mathematics

### Statistics and Probability [FOUNDATION]

- Descriptive Statistics
- Probability Basics
- Types of Distributions
- Random Variables, PDFs
- Bayes Theorem
- Inferential Statistics
- Graphs and Charts for Data Analysis

---

## Phase 1

### Data Collection and Sources [FOUNDATION]

- Databases (SQL, NoSQL)
- Internet APIs
- Mobile Apps and IoT Data
- Data Formats (JSON, CSV, Parquet, Excel)

### Data Cleaning and Preprocessing [CORE]

- Data Cleaning Techniques
- Missing Value Handling
- Feature Engineering
- Feature Selection
- Feature Scaling and Normalization
- Dimensionality Reduction

---

## Phase 2 — Classical Machine Learning

### What is Machine Learning [FOUNDATION]

- Types of Machine Learning
  - Supervised Learning
  - Unsupervised Learning
  - Semi-Supervised Learning
  - Self-Supervised Learning
  - Reinforcement Learning

### Supervised Learning [CORE]

- Regression
  - Linear Regression
  - Polynomial Regression
  - Regularization (Lasso, Ridge, ElasticNet)
- Classification
  - Logistic Regression
  - K-Nearest Neighbors
  - Support Vector Machines
  - Decision Trees, Random Forest
  - Gradient Boosting Machines

### Unsupervised Learning [CORE]

- Clustering (Exclusive, Overlapping, Hierarchical, Probabilistic)
- Principal Component Analysis
- Autoencoders (Classical)

### Reinforcement Learning [SPECIALIZED]

- Q-Learning [LEGACY]
- Deep Q-Networks [LEGACY]
- Policy Gradient Methods
- Actor-Critic Methods
- RL from Human Feedback Foundations (bridge to RLHF)

### Model Evaluation [CORE]

- Accuracy, Precision, Recall, F1-Score
- ROC-AUC, Log Loss
- Confusion Matrix
- Train/Test/Validation Split
- K-Fold Cross Validation
- Leave-One-Out Cross Validation (LOOCV)
- Model Selection and Hyperparameter Tuning

### Classical ML Frameworks [CORE]

- Scikit-learn

### Explainable AI [SPECIALIZED]

- Feature Importance
- SHAP, LIME
- Model Interpretability Techniques

---

## Phase 3 — Deep Learning Foundations

### Neural Network Basics [CORE]

- Perceptron, Multi-Layer Perceptrons
- Forward Propagation
- Backpropagation
- Activation Functions
- Loss Functions
- Gradient Descent and Optimizers

### Deep Learning Frameworks [CORE]

- PyTorch
- TensorFlow / Keras [FOUNDATION]

### Convolutional Neural Networks [FOUNDATION]

- Convolution, Padding, Strides, Pooling
- Image Classification
- Image Segmentation
- Image and Video Recognition
- Recommendation Systems (CNN-based)

### Recurrent Architectures [FOUNDATION]

- RNN
- LSTM
- GRU
- Sequence-to-Sequence Models
- Use in Time-Series and Sequence Modeling Today

### Generative Adversarial Networks [LEGACY]

- GAN Architecture
- Applications and Limitations

### Classical NLP [LEGACY]

- Tokenization (Classical)
- Stemming
- Lemmatization
- Bag-of-Words, TF-IDF
- Classical Word Embeddings (Word2Vec, GloVe)

### Autoencoders and Representation Learning [FOUNDATION]

- Autoencoder Architectures
- Latent Space Representations

### Graph Neural Networks [SPECIALIZED]

- Graph Representations
- Message Passing
- Applications in Recommendation and Molecules
- Knowledge Graphs

---

## Phase 4 — Attention and Transformers

### Attention Mechanisms [CORE]

- Motivation: Limitations of RNNs
- Self-Attention
- Multi-Head Attention
- Cross-Attention
- FlashAttention [MODERN]

### Transformer Architecture [CORE]

- Encoder-Decoder Structure
- Positional Encoding
- Layer Normalization, Residual Connections
- Encoder-Only Models (BERT-style) [FOUNDATION]
- Decoder-Only Models (GPT-style)
- Encoder-Decoder Models (T5-style) [FOUNDATION]

---

## Phase 5 — LLM Internals

### Tokenization [CORE]

- Byte-Pair Encoding
- SentencePiece
- Vocabulary Size Trade-offs

### Core LLM Mechanics [CORE]

- KV Cache
- KV Cache Optimization [MODERN]
- Prefix Caching [MODERN]
- Rotary Position Embeddings (RoPE)
- Context Windows and Context Length
- Mixture of Experts (MoE)
- Model Scaling Laws

### Decoding Strategies [CORE]

- Greedy Decoding
- Beam Search
- Top-k / Top-p Sampling
- Temperature
- Speculative Decoding [MODERN]
- Speculative Execution [MODERN]

### Model Compression [MODERN]

- Quantization (INT8, INT4, GPTQ, AWQ)
- Pruning
- Distillation
- Safetensors

---

## Phase 6 — Pretrained Models and Ecosystem

### AI Engineer Foundations [FOUNDATION]

- What is an AI Engineer
- AI Engineer vs ML Engineer
- AI vs AGI
- Common Terminology
- Impact on Product Development

### Using Pretrained Models [CORE]

- Benefits and Limitations of Pretrained Models
- Popular Model Providers
  - OpenAI Models
  - Anthropic Claude
  - Google Gemini
  - Mistral AI, Cohere
  - Azure AI, AWS SageMaker
- Model Capabilities, Context Length, Knowledge Cutoffs

### Hugging Face Ecosystem [CORE]

- Hugging Face Hub
- Hugging Face Tasks
- Transformers Library
- Datasets Library
- Evaluate Library
- Accelerate Library
- TRL (Transformer Reinforcement Learning)
- Diffusers
- Transformers.js
- Sentence Transformers
- Finding and Evaluating Open Source Models

### Open Source Local Inference [CORE]

- Ollama
- Ollama Models and SDK
- Open vs Closed Source Model Trade-offs

### Managing Tokens and Cost [CORE]

- Token Counting
- Maximum Tokens
- Pricing Considerations

---

## Phase 7 — Prompt Engineering

### Prompt Engineering Fundamentals [CORE]

- Writing Effective Prompts
- Zero-shot, Few-shot Prompting
- Chain-of-Thought Prompting
- ReAct Prompting
- Structured Outputs [MODERN]
- Prompt Versioning [MODERN]
- Prompt Regression Testing [MODERN]
- A/B Testing Prompts [MODERN]

### Provider Tooling [FOUNDATION]

- OpenAI Playground
- Chat Completions API [LEGACY]
- Responses API [CORE]

---

## Phase 8 — Fine-Tuning and Alignment

### Training Fundamentals [CORE]

- Pretraining vs Fine-tuning
- Supervised Fine-Tuning (SFT)

### Parameter-Efficient Fine-Tuning [CORE]

- PEFT
- LoRA
- QLoRA
- Adapters, Prefix Tuning [FOUNDATION]

### Alignment Techniques [CORE]

- Reinforcement Learning from Human Feedback (RLHF)
- Direct Preference Optimization (DPO)
- Reward Modeling

### Fine-Tuning in Practice [CORE]

- OpenAI Fine-Tuning API
- Dataset Preparation for Fine-Tuning
- Dataset Curation [MODERN]
- Synthetic Data Generation [MODERN]
- Unsloth [MODERN]
- Axolotl [MODERN]
- Evaluating Fine-Tuned Models

---

## Phase 9 — LLM Inference and Serving

### Inference Fundamentals [CORE]

- Inference vs Training
- Latency, Throughput, Cost Trade-offs
- Batching Strategies
- Continuous Batching
- GPU Memory Optimization

### Inference Engines [MODERN]

- vLLM
- TensorRT-LLM
- SGLang
- PagedAttention

---

## Phase 10 — Embeddings and Vector Databases

### Embeddings [CORE]

- What are Embeddings
- Use Cases: Semantic Search, Recommendation, Anomaly Detection, Classification
- OpenAI Embeddings API
- Open Source Embedding Models
- Vector Compression [MODERN]

### Vector Databases [CORE]

- Purpose and Functionality
- Indexing Embeddings (HNSW, IVF)
- Similarity Search
- Popular Vector Databases
  - Chroma, Pinecone
  - Weaviate, FAISS
  - LanceDB, Qdrant
  - Supabase, MongoDB Atlas

---

## Phase 11 — Retrieval-Augmented Generation (RAG)

### RAG Fundamentals [CORE]

- RAG Use Cases
- RAG vs Fine-tuning
- Chunking Strategies
- Document Parsing [MODERN]
- Embedding and Indexing
- Retrieval Process
- Generation with Retrieved Context

### Implementing RAG [CORE]

- Using SDKs Directly
- LangChain
- LlamaIndex
- OpenAI Assistants API [LEGACY]

### Advanced Retrieval [MODERN]

- Hybrid Search
- BM25
- Reranking
- ColBERT and Late Interaction Retrieval
- Metadata Filtering
- Query Rewriting
- Contextual Retrieval
- Parent-Child Retrieval
- Graph RAG
- Agentic RAG
- Multimodal RAG

### RAG Evaluation [MODERN]

- Retrieval Metrics (Precision@k, Recall@k, MRR)
- Faithfulness and Groundedness Evaluation
- Ragas
- RAG-specific Evaluation Frameworks

---

## Phase 12 — AI Agents

### Agent Fundamentals [CORE]

- Agents as a RAG Alternative / Extension
- Agent Use Cases
- Manual Agent Implementation
- Tool Calling
- OpenAI Functions / Tools
- OpenAI Assistants API [LEGACY]

### Agent Frameworks [CORE]

- LangGraph
- DSPy [MODERN]
- PydanticAI [MODERN]
- AutoGen [MODERN]
- CrewAI [SPECIALIZED]
- Building AI Agents End-to-End

### Agent Capabilities [MODERN]

- Planning
- Reflection
- Memory Systems
- Semantic Memory
- Long-Term Memory
- Routing
- Workflow Orchestration
- Human-in-the-Loop

### Multi-Agent Systems [MODERN]

- Multi-Agent Architectures
- Agent Communication and Orchestration
- Model Context Protocol (MCP)
- Agent-to-Agent Protocol (A2A)

---

## Phase 13 — Multimodal AI

### Multimodal Fundamentals [FOUNDATION]

- Multimodal Use Cases
- Image Understanding
- Image Generation
- Video Understanding
- Video Generation [MODERN]
- Audio Processing
- Text-to-Speech
- Speech-to-Text
- Speech Agents [MODERN]

### Vision Language Models [MODERN]

- VLM Architectures
- OCR
- Document AI
- Multimodal RAG

### Multimodal Tooling [FOUNDATION]

- OpenAI Vision API
- DALL-E API
- Whisper API
- Hugging Face Multimodal Models
- LangChain / LlamaIndex for Multimodal Apps

---

## Phase 14 — AI Safety, Security, and Evaluation

### AI Safety and Ethics [CORE]

- AI Safety Issues Overview
- Bias and Fairness
- Security and Privacy Concerns
- Safety Best Practices
- Know Your Customers / Use Cases
- Constraining Inputs and Outputs
- OpenAI Moderation API
- Adding End-User IDs in Prompts

### AI Security [MODERN]

- Prompt Injection (Direct and Indirect)
- Jailbreaks
- Adversarial Testing
- Model Stealing
- Data Poisoning
- Prompt Leakage
- PII Protection
- Secret Management for AI Systems
- Supply-Chain Security
- Guardrails

### AI Evaluation [MODERN]

- Evaluation Frameworks and Benchmarks
- HELM
- OpenAI Evals
- DeepEval
- LangSmith Evaluation
- Hallucination Evaluation
- LLM-as-Judge
- Human Evaluation Pipelines

---

## Phase 15 — Backend Engineering for AI Systems

### Backend Fundamentals [CORE]

- REST APIs
- FastAPI
- Async Python
- Authentication and Authorization
- API Versioning
- Rate Limiting

### Real-Time and Background Processing [MODERN]

- WebSockets
- Server-Sent Events (SSE)
- Background Jobs
- Celery
- Task Queues

### Data and Messaging Infrastructure [CORE]

- PostgreSQL
- Redis
- Message Queues

---

## Phase 16 — Data Engineering for ML/AI

### Data Pipelines [CORE]

- Data Ingestion Architecture
- Data Lakes and Warehouses
- Airflow
- Spark
- Kafka
- Flink [FOUNDATION]

### Modern Data Stack [MODERN]

- Delta Lake
- Apache Iceberg
- dbt
- DuckDB
- Data Quality
- Schema Evolution

---

## Phase 17 — MLOps Foundations

### MLOps Principles [CORE]

- MLOps vs DevOps
- Version Control for ML Assets

### MLOps Components [CORE]

- CI/CD for ML
- Orchestration
- Experiment Tracking and Model Registry
  - MLflow
  - Weights & Biases
- Data Lineage and Feature Stores
- Feature Stores in Depth
- Model Training and Serving Pipelines
- Infrastructure as Code

### Model Serving Frameworks [CORE]

- BentoML
- KServe

---

## Phase 18 — LLMOps and Observability

### LLMOps [MODERN]

- Prompt Versioning and Management
- Model Routing
- Response Caching
- Semantic Caching

### AI Observability [MODERN]

- Tracing
- LangSmith
- OpenTelemetry
- Phoenix (Arize)
- Weights & Biases Weave
- Production Dashboards
- Production Metrics

---

## Phase 19 — System Design for AI Systems

### Scalable AI Systems [MODERN]

- Caching Strategies
- Queues and Event-Driven Architecture
- Microservices for AI
- Distributed Systems Basics
- Designing for High Availability

---

## Phase 20 — Cloud and Deployment

### Cloud Computing [CORE]

- AWS / Azure / GCP
- Cloud-native ML Services

### Containerization and Orchestration [CORE]

- Docker
- Kubernetes

### Production Deployment [CORE]

- Nginx, Reverse Proxy
- Gunicorn / Uvicorn
- HTTPS
- Load Balancing
- Autoscaling
- CDN Basics

### CI/CD and Monitoring [CORE]

- CI/CD Pipelines for AI Systems
- Production Monitoring
- Alerting and Incident Response

### Cost Optimization [MODERN]

- Token Optimization
- Model Routing for Cost
- Semantic Caching for Cost
- Batching for Cost
- Quantization Trade-offs
- Inference Cost Estimation

---

## Phase 21 — Development Tooling

### AI-Assisted Development [FOUNDATION]

- AI Code Editors
- Code Completion Tools

---

## Phase 22 — Capstone Production Projects

### Capstone Projects [CORE]

- Classical ML Project
- Computer Vision Project
- NLP Project
- RAG System
- AI Agent
- Multimodal Application
- Full-Stack AI SaaS
- End-to-End MLOps Deployment
- Production Monitoring Implementation