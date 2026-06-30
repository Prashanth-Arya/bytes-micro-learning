# Bytes: Spec-Driven Micro-Learning Engine

An interactive command-line application that ingests dense, unstructured technical documents or academic texts and programmatically chunks them into sequential, high-density micro-learning modules. Built using Python and the modern Google GenAI SDK.

## 🛠️ Technical Architecture
* **Dynamic I/O Pipeline:** Built with an interactive command-line interface that allows users to supply custom topic flags and dynamically stream text files into the processing core.
* **Spec-Driven Validation:** Enforces structural integrity by binding data extractions to strict `pydantic` schemas via the Gemini `response_schema` parameter, guaranteeing deterministic JSON outputs.
* **Context Engineering:** Implements strict system boundaries to govern model persona, control tone, and apply rigid token length constraints (50–70 words per slide layout) without losing engineering depth.

## 📋 How It Works
1. **Ingestion:** Reads raw data streams from user-specified local text files (e.g., lecture notes, textbooks, documentation).
2. **Context Routing:** Evaluates the text against a user-defined topic focus to isolate high-signal data.
3. **Structured Chunking:** Synthesizes the core technical assertions into structured learning slides complete with subheadings, concise content blocks, and standalone core takeaways.

## 🚀 Quick Start

### Prerequisites
* Python 3.10+
* A Gemini API Key from [Google AI Studio](https://aistudio.google.com/)
