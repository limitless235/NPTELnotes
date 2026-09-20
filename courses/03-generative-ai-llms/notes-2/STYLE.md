# notes-2 writing rules

Read the **full transcript** at the given path. Write **one markdown file** at the given output path. Do not commit. Do not edit other files.

## Grounding

- Cover **every topic, example, formula, comparison, and lab step the lecture actually teaches**. Do not skip sections because they feel basic.
- Do **not** add later-week topics (RAG, ethics, LoRA, etc.) unless this transcript teaches them.
- **Correct ASR errors** (gshian→Gaussian, barnoli→Bernoulli, autoenccoder→autoencoder, adversial→adversarial, rack→RAG, base theorem→Bayes, diss→disease, unit→U-Net, multimodel→multimodal, …) using standard ML names, while keeping the lecture’s examples (age/height/weight, cat/dog, digit 7, malignancy images, etc.).
- Reconstruct math the instructor stated; do not dump a textbook chapter they never walked through.

## Shape (match L00/L01)

Start with:

```
# Lxx: Title from the lecture

**Video:** [Lec xx](https://www.youtube.com/watch?v=ID) · duration
```

Then: learning objectives (3–6 bullets), then sections in **lecture order**, then **Key takeaways**.

Use:

- `###` / `##` headings
- Markdown tables
- Display math with `$$` and inline `$...$`
- At least one ` ```mermaid ` diagram when the lecture has an architecture, process, or taxonomy (required for theory lectures; for Colab/lab lectures include a flowchart of the exercise)
- Numbered lab steps for practicals: dataset, splits, architecture, activations, losses, optimizers, metrics, plots, what to observe
- A short “what this lecture is *not*” only if needed to avoid mixing with another video

## Length

- Theory lecture (~30–50 min): typically 180–400 lines. Short theory (~10–20 min): 100–180 lines.
- Practical: 150–350 lines with concrete steps from the transcript (library names, dataset names, layer counts, if spoken).

## Tone

Concise study notes like `courses/03-generative-ai-llms/notes/vol-01.md` and the gold files `notes-2/L00-course-intro.md`, `notes-2/L01-introduction-to-generative-ai.md`. No filler, no “as an AI”, no copying the garbled caption paragraph.

End the file with `---`.
