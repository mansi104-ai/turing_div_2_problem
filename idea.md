# idea.md

## Title: Huffman Pixels — The Compression Tree

### Origin
This problem was inspired by a real challenge faced during our **medical imaging deep learning project** for **meningioma detection and classification**.  
We worked with MRI scans of **512×512 resolution** and around **10,000 images**. Feeding these raw images directly into the GPU caused frequent **out-of-memory errors** due to massive uncompressed pixel data.

During optimization discussions, we explored encoding pixel frequencies using a **Huffman-like compression** to minimize redundant intensity storage. Although this method wasn’t ultimately used in our training pipeline, it sparked the idea for a **tree-based compression algorithmic problem**.

---

### Problem Development
We wanted a problem that combined:
- **Huffman Tree principles**,  
- **Tree structure constraints**, and  
- **Real-world compression relevance**.

Early variants either resembled existing Huffman problems or introduced unnecessary balancing logic. The final formulation added a **depth-difference constraint** during merging — mimicking GPU parallelization limits — making the problem both unique and non-trivial.

---

### Why It’s Unique
- Adds a **depth constraint** to classical Huffman merging.  
- Inspired by real GPU memory constraints in medical imaging.  
- Not searchable or similar to any known problem.  
- Balances algorithmic design with real-world motivation.

---

### Summary
This problem bridges **AI-based compression insights** with **competitive programming**. It tests **priority queues, greedy merging, and tree balancing**, making it suitable for **Codeforces Div2 C / Div1 A** level.

Even though the original idea wasn’t deployed in our medical model, it evolved into a creative and original programming challenge that captures the essence of solving real AI infrastructure issues through algorithmic thinking.
