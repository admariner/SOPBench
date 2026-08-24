# SOPBench: Evaluating Language Agents at Following Standard Operating Procedures and Constraints


## Overview

<p align="center"><img width="100%" src="assets/overview-v8.png" /></p>

This repository contains the data and code for the paper: "SOPBench: Evaluating Language Agents at Following Standard Operating Procedures and Constraints". This benchmark is used to evaluate Language Agents at Following Standard Operating Procedures and Constraints across seven customer service domains.

## Results

The following table shows model pass rates (%) across seven domains.

| **Model** | **Bank** | **DMV** | **Healthcare** | **Market** | **University** | **Library** | **Hotel** | **Overall** |
|:---------:|:--------:|:-------:|:--------------:|:----------:|:--------------:|:-----------:|:---------:|:-----------:|
| **_Proprietary Reasoning Models_** | | | | | | | | |
| o4-mini-high (FC) | 76.87 | 83.51 | 92.74 | 89.53 | 95.24 | 34.85 | 55.90 | 75.30 |
| GPT-5 (FC) | 71.64 | 84.54 | 76.61 | 69.77 | 88.10 | 66.67 | 67.18 | 72.89 |
| GPT-5-mini (FC) | 58.96 | 82.47 | 92.74 | 75.58 | 95.24 | 34.85 | 69.74 | 72.65 |
| Gemini-2.5-Flash (FC) | 67.91 | 81.44 | 87.90 | 77.91 | 83.33 | 51.52 | 42.56 | 68.07 |
| Gemini-2.5-Pro (FC) † | 69.40 | 76.29 | 79.84 | 56.98 | 90.48 | 51.52 | 52.31 | 64.82 |
| **_Proprietary Non-reasoning Models_** | | | | | | | | |
| GPT-4.1 (FC) | 69.40 | 79.38 | 79.03 | 80.81 | 50.00 | 57.58 | 42.56 | 66.14 |
| GPT-4o (FC) | 58.96 | 80.41 | 73.39 | 61.63 | 66.67 | 60.61 | 39.49 | 60.12 |
| Claude-3-7-Sonnet (FC) | 65.67 | 70.10 | 70.97 | 56.98 | 66.67 | 27.27 | 23.59 | 52.29 |
| GPT-4.1-mini (FC) | 57.46 | 76.29 | 66.13 | 56.40 | 35.71 | 18.18 | 7.18 | 44.70 |
| GPT-4o-mini (FC) | 33.58 | 73.20 | 25.00 | 43.60 | 38.10 | 42.42 | 41.03 | 41.69 |
| Claude-3-5-Sonnet (FC) | 71.90 | 50.43 | 39.23 | 43.32 | 52.27 | 33.33 | 15.82 | 41.35 |
| Gemini-2.0-Flash (FC) | 52.99 | 51.55 | 21.77 | 38.37 | 30.95 | 19.70 | 7.18 | 30.60 |
| **_Open-source Reasoning Models_** | | | | | | | | |
| Qwen3.5-4B (FC, thinking) | 61.19 | 87.63 | 84.68 | 61.63 | 71.43 | 36.36 | 70.77 | 68.67 |
| Deepseek-R1 (ReAct) | 54.48 | 81.44 | 54.03 | 70.41 | 76.19 | 54.55 | 50.77 | 61.10 |
| Gemma-4-E4B-it (FC, thinking) | 58.21 | 63.92 | 77.42 | 38.95 | 66.67 | 22.73 | 60.51 | 55.90 |
| Qwen3.5-2B (FC, thinking) | 35.07 | 49.48 | 62.10 | 43.02 | 71.43 | 27.27 | 47.69 | 46.62 |
| Gemma-4-E2B-it (FC, thinking) | 33.58 | 23.71 | 66.13 | 16.28 | 42.86 | 10.61 | 10.77 | 26.99 |
| **_Open-source Non-reasoning Models_** | | | | | | | | |
| Llama3.1-70B-Instruct (ReAct) | 42.54 | 65.98 | 54.84 | 37.21 | 42.86 | 34.85 | 13.85 | 38.68 |
| Qwen2.5-32B-Instruct (ReAct) | 40.30 | 52.58 | 41.13 | 44.19 | 54.76 | 27.27 | 18.46 | 37.23 |
| Qwen2.5-72B-Instruct (ReAct) | 35.07 | 68.04 | 27.42 | 40.12 | 35.71 | 34.85 | 13.85 | 33.86 |
| Qwen2.5-14B-Instruct (ReAct) | 35.07 | 57.73 | 29.03 | 35.47 | 23.81 | 25.76 | 14.87 | 30.84 |
| Llama3.1-8B-Instruct (ReAct) | 14.93 | 18.56 | 20.16 | 16.28 | 23.81 | 30.30 | 0.00 | 14.58 |
| Qwen2.5-7B-Instruct (ReAct) | 5.22 | 20.62 | 16.94 | 9.30 | 0.00 | 15.15 | 0.51 | 9.04 |

<sub>Overall is the pass rate over all 830 cases (task-weighted micro average), matching the camera-ready paper. **Newly evaluated (2026-07/08):** Gemini-2.5-Pro via OpenRouter (FC, `max_tokens=512`); and, served locally via vLLM on the same 7-domain protocol, Qwen3.5 (2B/4B) and Gemma-4 (E2B/E4B) in native function calling with thinking enabled (`--enable-auto-tool-choice --tool-call-parser qwen3_xml` / `gemma4`, `max_model_len=32000`). Earlier Qwen3.5 runs without properly enabled thinking were invalidated and replaced; see `docs/SMALL_MODELS.md` for the audit.</sub>
<sub>**†** Gemini-2.5-Pro was run at `max_tokens=512` (matching Gemini-2.5-Flash); at that budget ~38.7% of its assistant turns were truncated by the model's own reasoning tokens, so these scores likely **understate** its true capability.</sub>

### Oracle vs. Full Tool Set

The main table above reports pass rates under the **full** tool set (`--tool_list full`), where the agent must select the correct tools from every tool available in the domain. The table below compares, for the nine models that have complete 7-domain trajectories under **both** settings, the **oracle** tool set (`--tool_list oracle`; only the tools the oracle solution uses for each case) against the **full** tool set. Both rows are scored with the identical `run_evaluation.py` pipeline (`--default_constraint_option full --constraint_descr_format structured`).

| **Model** | **Tools** | **Bank** | **DMV** | **Healthcare** | **Market** | **University** | **Library** | **Hotel** |
|:---------:|:--------:|:--------:|:-------:|:--------------:|:----------:|:--------------:|:-----------:|:---------:|
| GPT-4o (FC) | oracle | 76.87 | 84.54 | 75.81 | 79.07 | 73.81 | 60.61 | 67.18 |
| | full | 58.96 | 80.41 | 73.39 | 61.63 | 66.67 | 60.61 | 39.49 |
| GPT-4o-mini (FC) | oracle | 47.01 | 82.47 | 77.42 | 66.28 | 73.81 | 69.70 | 55.90 |
| | full | 33.58 | 73.20 | 25.00 | 43.60 | 38.10 | 42.42 | 41.03 |
| Claude-3-5-Sonnet (FC) ‡ | oracle | 75.37 | 79.38 | 80.65 | 63.37 | 73.81 | 51.52 | 46.15 |
| | full | 67.16 | 45.36 | 37.90 | 38.95 | 50.00 | 21.21 | 15.38 |
| Gemini-2.0-Flash (FC) | oracle | 71.64 | 74.23 | 61.29 | 63.37 | 69.05 | 63.64 | 21.03 |
| | full | 52.99 | 51.55 | 21.77 | 38.37 | 30.95 | 19.70 | 7.18 |
| Gemini-1.5-Pro (FC) | oracle | 69.40 | 76.29 | 62.90 | 59.30 | 69.05 | 48.48 | 35.90 |
| | full | 48.51 | 56.70 | 16.13 | 30.23 | 61.90 | 16.67 | 11.92 |
| Qwen2.5-32B-Instruct (ReAct) | oracle | 76.87 | 80.41 | 77.42 | 54.07 | 66.67 | 60.61 | 55.38 |
| | full | 40.30 | 52.58 | 41.13 | 44.19 | 54.76 | 27.27 | 18.46 |
| Qwen2.5-14B-Instruct (ReAct) | oracle | 64.93 | 72.16 | 61.29 | 61.63 | 47.62 | 62.12 | 36.92 |
| | full | 35.07 | 57.73 | 29.03 | 35.47 | 23.81 | 25.76 | 14.87 |
| Qwen2.5-7B-Instruct (ReAct) | oracle | 58.21 | 61.86 | 33.06 | 41.86 | 28.57 | 50.00 | 10.26 |
| | full | 5.22 | 20.62 | 16.94 | 9.30 | 0.00 | 15.15 | 0.51 |
| Llama3.1-8B-Instruct (ReAct) | oracle | 41.04 | 59.79 | 43.55 | 22.09 | 42.86 | 50.00 | 3.08 |
| | full | 14.93 | 18.56 | 20.16 | 16.28 | 23.81 | 30.30 | 0.00 |

<sub>Oracle pass rates are ≥ full in nearly every cell, and the gap widens for smaller models (e.g. Qwen2.5-7B rises from single digits to 30–60), reflecting that restricting the agent to the oracle-used tools removes the tool-selection burden present in the full setting.</sub>
<sub>**‡** The Claude-3-5-Sonnet full-tool row here is recomputed from the current trajectory files and differs slightly from the main-table row above (recorded from an earlier generation); the other eight models match the main table cell-for-cell.</sub>

## Getting Started

### Installation

```bash
# Clone the repository
# Create and activate conda environment
conda create -n agent python=3.10
conda activate agent

# Install dependencies
pip install -r requirements.txt
```

### Configuration

#### API Keys Setup

Create a `.env` file in the root directory with your API keys:

```bash
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
GEMINI_API_KEY=your_gemini_api_key
FIREWORKS_API_KEY=your_fireworks_api_key
```

#### Supported Language Models

The framework supports a wide range of language models through unified interfaces for both multi-turn inference and function calling:

##### API-based Models

- **OpenAI Models**
  - GPT-5 Series: `gpt-5`, `gpt-5-mini`
  - GPT-4o Series: `gpt-4o`, `gpt-4o-mini`, `gpt-4.1`
  - "o" Series: `o1`, `o3`, `o3-mini`, `o4-mini`
- **Anthropic Models**
  - Claude 3.5: `claude-3-5-sonnet-20241022`, `claude-3-5-haiku-20241022`
  - Claude 3.7: `claude-3-7-sonnet-20250219`, `claude-3-7-sonnet-20250219-thinking`
- **Google Gemini Models**
  - Gemini 1.5: `gemini-1.5-flash`, `gemini-1.5-pro`
  - Gemini 2.0: `gemini-2.0-flash-001`, `gemini-2.0-flash`, `gemini-2.0-flash-thinking-exp`
  - Gemini 2.5: `gemini-2.5-pro-preview-03-25`, `gemini-2.5-flash-preview-04-17`
- **Fireworks Models**
  - Various models hosted on the Fireworks AI platform

##### Local Inference
- **OSS Models via vLLM**: Run open-source models locally with vLLM for efficient inference

All models use a unified format for multi-turn inference and function calling, with backend-specific implementations that convert responses to a standardized format compatible with OpenAI's API.

##### Adding Custom Models

You can add or customize supported models by modifying the model lists in `swarm/constants.py`.

## Usage

#### Key Parameters

The following command line arguments control the simulation and evaluation:

| Parameter | Description | Options |
|-----------|-------------|---------|
| `--domain` | Test domain | bank, online_market, dmv, healthcare, library, hotel, university |
| `--user_model` | Model for user agent | Any supported model name, "human" for interactive mode, or None (default) |
| `--assistant_model` | Model for assistant agent | Any supported model name |
| `--env_mode` | Environment mode | "prompt" (without code constraint checking), "program" (with code constraint checking) |
| `--tool_list` | Available tools | "full" (all tools), "oracle" (only the oracle-used tools for each case) |
| `--tool_call_mode` | Tool call mode | "fc" (function calling), "react", "act-only" |

#### Data Preparation

The framework comes with pre-generated task data in the `data` folder.

To generate new data (note that generating each task using GPT-4o costs approximately $0.015 USD):

```bash
python run_datagen.py
```

The code will run data generation and verification (format verification and constraint verification). If failed, it will start re-generation. The whole process is fully automated.

#### Running Simulations

```bash
python run_simulation.py \
  --domain [domain] \
  --user_model [user_model] \
  --assistant_model [assistant_model] \
  --env_mode [env_mode] \
  --tool_list [tool_list] \
  --tool_call_mode [tool_call_mode]
```

#### Running Evaluations

```bash
python run_evaluation.py \
  --domain [domain] \
  --user_model [user_model] \
  --assistant_model [assistant_model] \
  --tool_list [tool_list] \
  --tool_call_mode [tool_call_mode]
```

#### Reviewing Agent Trajectories

To view agent trajectories and evaluation results:

```bash
python run_checking.py \
  --output_dir [output_dir] \
  --domain [domain] \
  --assistant_model [assistant_model] \
  --tool_call_mode [tool_call_mode] \
  --default_constraint_option [default_constraint_option] \
  --constraint_descr_format [constraint_descr_format] \
  --tool_list [tool_list]
```

Over 24,000 agent trajectories are provided in the `output/` directory for reference.

## Project Structure

```
SOPBench/
├── swarm/                  # Framework code for agent interaction
│   ├── core.py             # Core agent and swarm classes
│   ├── llm_handler.py      # Unified LLM backend handler
│   ├── types.py            # Type definitions
│   ├── util.py             # Utility functions
│   ├── claude.py           # Claude-specific utilities
│   ├── gemini.py           # Gemini-specific utilities
│   └── constants.py        # Project constants and configurations
├── env/                    # Environment for different domains
│   ├── dependencies.py     # Core program code for constraint checking
│   ├── helpers.py          # Helper functions for environment
│   ├── dep_eval.py         # Evaluation utilities
│   ├── ablation.py         # Layered harness ablation switches (hints/verdicts/order)
│   └── domains/            # Domain implementations (bank, dmv, healthcare, hotel, library, online_market, university)
├── data/                   # Task data for simulation and evaluation
├── scripts/                # Shell scripts for simulation and evaluation
├── analysis/               # SOP action-graph statistics and analysis utilities
├── output/                 # All simulation and evaluation results
│   ├── <domain>/           # Main results (paper main table): bank, dmv, healthcare, hotel, library, online_market, university
│   ├── abl2_{oracle,hints,order,verdicts}/  # Layered harness ablation runs (paper Section 4.2)
│   ├── abl_{hints,order,verdicts}/          # Earlier ablation runs (GPT-5-mini rows; retained for audit)
│   ├── qwen_nothink/       # Qwen3.5 no-thinking runs (ablation no-thinking column)
│   └── think_fc1024/       # Small-model thinking-FC runs (ablation thinking column)
├── docs/                   # Experiment documentation and review records
│   ├── ABLATION.md         # Layered harness ablation: design, runs, and findings
│   ├── SMALL_MODELS.md     # Small-model FC/ReAct/thinking audit and rerun matrix
│   └── ablation_prompt_examples/  # Verbatim prompt examples for each ablation setting
├── latex/                  # Camera-ready paper source
├── latex_submission/       # Submitted (pre-camera-ready) paper source, frozen
├── archive/                # Deprecated data, superseded runs, and unadopted experiments (e.g. PVA)
├── run_datagen.py          # Task generation script
├── run_simulation.py       # Simulation script
├── run_evaluation.py       # Evaluation script
├── run_checking.py         # Validation script
└── run_operation.py        # Operations script
```

## License

- **Code**: released under the [MIT License](LICENSE).
- **Data**: the benchmark data (the `data/` directory, domain environment specifications, and any released agent trajectories) is released under the [CC BY 4.0 License](DATA_LICENSE). Please cite the SOPBench paper when using the data.
