Here's the full path, broken into phases. Each phase has a goal, what you'll actually learn by doing it, and a "you're done when" checkpoint so you know when to move on.

## Phase 0: Setup (half a day)
**Goal:** Environment ready, nothing else.
- Install Python, set up a virtual environment, install pip
- Create a GitHub repo for this project (public, from day one — you're building in public)
- Get an NVD API key (free, just requires email signup) — this is your CVE data source
- Get an API key for Claude or GPT (whichever you have access to) — this is your "generation" model

**Done when:** You can run a basic Python script and it executes without errors. Repo exists on GitHub with a README saying "Security Advisory RAG — work in progress."

---

## Phase 1: Get the raw data (1-2 days)
**Goal:** Pull real CVE data and vendor advisories onto your machine, understand what it looks like.
- Use the NVD API to pull ~50-100 CVEs (pick a theme — e.g. CVEs affecting OpenSSL, or Apache, or something you find interesting)
- Separately, grab 5-10 vendor security advisories (e.g. from Apache's security page, Microsoft's MSRC, Red Hat's advisories) — just copy the text manually if needed, doesn't need to be automated yet
- Save everything as plain text/JSON files locally
- **Just read them.** Notice: CVE descriptions are short (1-3 sentences, structured). Vendor advisories are long (paragraphs, sometimes tables, prose explanations).

**Done when:** You have a folder of CVE data + a folder of advisory text, and you can explain out loud why they look different from each other.

---

## Phase 2: Naive RAG — the "bad" version on purpose (2-3 days)
**Goal:** Build the simplest possible RAG pipeline, badly, so you feel *why* it's bad.
- Chunk everything the same lazy way (fixed-size chunks, no thought)
- Embed the chunks (use a free sentence-transformers model)
- Store in ChromaDB
- Write a basic loop: take a question → embed it → find closest chunks → stuff them into a prompt → ask the LLM to answer
- Ask it questions like "what's the fix for CVE-XXXX" and "which advisories mention OpenSSL"

**Done when:** It technically works but you can point to at least 3 specific wrong or vague answers. Write these down — you'll fix them later and this becomes your "before" evidence.

---

## Phase 3: Build your ground truth (1-2 days)
**Goal:** Create the eval set — the thing that lets you *prove* improvement instead of guessing.
- Manually write 20-30 question/answer pairs where you already know the correct answer from the raw data
- Include some questions that SHOULD be answerable, and a few that should NOT be (data you deliberately didn't include) — these test refusal later
- Save as a simple spreadsheet or JSON: question, correct answer, source document

**Done when:** You have this file, and you could hand it to someone else and they'd understand what "correct" means for each question.

---

## Phase 4: Smarter chunking (2-3 days)
**Goal:** Fix chunking based on document type, not one-size-fits-all.
- For CVE entries (short/structured): treat each CVE as basically one chunk
- For advisories (long/prose): split by section/paragraph, not arbitrary character count
- Re-embed everything with this new chunking
- Re-run your eval set from Phase 3, compare retrieval accuracy vs Phase 2

**Done when:** You have a number — e.g. "Phase 2 retrieval accuracy: 40%, Phase 4: 65%" — written down.

---

## Phase 4B: Semantic Chunking (Embedding Shift Detection)

**Goal:** Replace rule-based splitting with chunk boundaries that are determined by meaning shifts in the text.

Encode every sentence individually using your embedding model
Compute cosine similarity between consecutive sentence embeddings
Wherever the similarity drops sharply (e.g. below a threshold like 0.75), treat that as a chunk boundary — the topic has shifted
Re-embed and re-store the new chunks in ChromaDB
Re-run your Phase 3 eval set and compare against Phase 4A

**Done when:** You can show a side-by-side example where a rule-based chunk split a paragraph mid-topic, but the semantic approach kept it together. Record the new retrieval accuracy number.

---

## Phase 5: Hybrid search (3-4 days)
**Goal:** Add keyword search alongside embedding search.
- Add BM25 (keyword-based search) using a simple library
- Combine BM25 results + vector search results (basic score combination is fine)
- Test specifically on exact-match queries like "CVE-2023-1234" — this is where pure embeddings fail and BM25 saves you
- Re-run your eval set, record the new score

**Done when:** You can show a concrete example question that vector-only search got wrong, and hybrid search got right. This is your money example for interviews.

---

## Phase 6: Reranking (2-3 days)
**Goal:** After retrieving candidates, re-score them with a smarter model before picking the top ones.
- Add a cross-encoder reranker on top of your hybrid results
- Re-run eval, record score again

**Done when:** Another improvement number, e.g. "Phase 5: 70%, Phase 6: 80%."

---

## Phase 6B: Fine-Tuning the Bi-Encoder on Domain Data

**Goal:** Instead of using a generic pretrained embedding model, fine-tune it so it understands CVE and security advisory language specifically.

- Construct training pairs from your Phase 3 eval set: (question, relevant_chunk) = positive pair; (question, irrelevant_chunk) = negative pair
- Use the sentence-transformers library with a MultipleNegativesRankingLoss training setup
- Fine-tune for a small number of epochs on your domain pairs
- Swap the fine-tuned model into your pipeline and re-run your eval set

**Done when:** The fine-tuned model retrieves the correct chunk for at least 3 questions that the generic model consistently got wrong. Record the before/after numbers.

---

## Phase 7: The refusal system (3-5 days — this is the hardest and most important phase)
**Goal:** Make the system say "I don't know" instead of hallucinating when it's not confident.
- Decide on a confidence signal (e.g. how similar/strong the top retrieved chunk is)
- Set a threshold: below it, the system responds "I don't have reliable data on this" instead of generating an answer
- Test against the "should NOT be answerable" questions from Phase 3 — does it correctly refuse?
- Tune the threshold: too strict = refuses things it should know; too loose = still hallucinates

**Done when:** You have a refusal accuracy number (e.g. "correctly refused 8/10 unanswerable questions, incorrectly refused 1/20 answerable ones").

---

## Phase 8: Citations (1-2 days)
**Goal:** Every answer must say which document it came from.
- Attach source metadata to each chunk when you store it
- Make the LLM output cite the CVE ID or advisory name in every answer

**Done when:** You ask a question and the answer includes "(source: CVE-2023-XXXX)" or similar, and it's actually the correct source.

---

## Phase 9: The results table (1 day — do not skip this)
**Goal:** Turn all your numbers into one comparison table.
- Rows: Naive (Phase 2) → Better chunking (Phase 4) → Hybrid (Phase 5) → +Reranking (Phase 6) → +Refusal (Phase 7)
- Columns: retrieval accuracy, answer correctness, refusal accuracy
- Put this table in your README with a short explanation of what each stage fixed and why

**Done when:** The table exists in your GitHub README, with real numbers, not estimates.

---

## Phase 9B: Automated CI/CD Evaluation with Ragas / DeepEval

**Goal:** Stop tracking metrics manually. Build a pipeline that automatically scores your system every time you change it.

- Install ragas or deepeval (pick one — both work similarly)
- Wrap your Phase 3 eval set into the framework's expected format: {question, answer, contexts, ground_truth}
- Configure it to measure at minimum: Faithfulness (does the answer contradict the sources?) and Answer Relevance (does the answer actually address the question?)
- Write a single script (evaluate.py) that runs the full eval suite and outputs a score report
- Optional advanced step: add this as a GitHub Actions workflow so it runs automatically on every git push

**Done when:** Running python evaluate.py produces a JSON/table of Faithfulness and Answer Relevance scores without any manual steps. Scores are committed to the repo alongside the results table.

--- 

## Phase 10: Polish + publish (2-3 days)
**Goal:** Make it presentable.
- Clean up the repo structure
- Write a proper README: what it does, why you made each design decision, the results table, how to run it
- Optional: wrap it in a simple FastAPI endpoint or basic UI so people can actually try it, not just read code

**Done when:** You could send the GitHub link to a senior engineer and they'd understand what you built and why in under 2 minutes of reading.

---

**Total estimate:** 4-5 weeks working consistently, longer if you're doing this alongside your internship. Don't skip phases even when they feel slow — Phase 3 (eval set) and Phase 9 (results table) are the two most people skip, and they're the two that actually make this impressive.

Want me to help you start Phase 1 — picking a CVE theme and figuring out exactly what to pull from the NVD API?