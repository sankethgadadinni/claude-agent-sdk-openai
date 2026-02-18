# Claude Agent SDK + LiteLLM Bridge

This repo shows how to run the Claude Agent SDK against Azure OpenAI (and optionally Gemini) adapters that are fronted by a single LiteLLM proxy. The SDK talks to LiteLLM through Anthropic-compatible environment variables, while LiteLLM fans requests out to whichever backend models you configure.

## Repo Layout
- `agent.py` – minimal Claude Agent SDK script that streams tool responses.
- `config.yaml` – LiteLLM config targeting Azure OpenAI deployments.
- `config_with_gemini.yaml` – alternative config that swaps Azure for Gemini models.
- `req.txt` – Python dependencies (`claude-agent-sdk`, `litellm[proxy]`).
- `.env.example` – template for the environment variables `config.yaml` expects.

## Prerequisites
1. Python 3.10+ and `pip`.
2. Azure OpenAI resource with deployments that match the model strings you want (example: deployment name `gpt-4.1` so `model: azure/gpt-4.1`).
3. Optional: Google AI Studio (Gemini) API key — only needed when you launch `config.yaml`, just make sure `GEMINI_API_KEY` is set.

## Installation
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Environment Variables
Copy `.env.example` to `.env`, fill in the secrets, then load it before running LiteLLM (the CLI depends on the shell environment):

```bash
cp .env.example .env
# edit .env with your preferred method, then:
source .env
```

| Variable | Required | Used By | Description |
| --- | --- | --- | --- |
| `LITELLM_MASTER_KEY` | ✅ | LiteLLM + Agent | Shared secret; LiteLLM checks it for every request and the agent reuses it as `ANTHROPIC_API_KEY`. |
| `AZURE_API_BASE` | ✅ | LiteLLM | Your Azure OpenAI endpoint (`https://<resource>.openai.azure.com`). |
| `AZURE_API_KEY` | ✅ | LiteLLM | Azure OpenAI API key with access to the deployments referenced in `config.yaml`. |
| `GEMINI_API_KEY` | optional | LiteLLM | Only needed if you swap to `config.yaml`. |
| `ANTHROPIC_BASE_URL` | ✅ | Agent | Should point to the LiteLLM proxy (defaults to `http://localhost:4000`). |
| `ANTHROPIC_API_KEY` | ✅ | Agent | Must match `LITELLM_MASTER_KEY` so the SDK can authenticate with LiteLLM. |

> Tip: add `set -a; source .env; set +a` to export everything in one command when using `zsh`/`bash`.

The Python demo script calls `python-dotenv` to load `.env` automatically, so you can run `python agent.py` without sourcing. Keep sourcing for any shell processes (like `litellm` or `curl`) that need the same variables.

## Configure LiteLLM
- Update the `model` fields inside `config.yaml` so they reference your actual Azure deployment names (`azure/<deployment>`). The `model_name` values (`azure-gpt-4.1`, `claude-sonnet-4-6`, etc.) are the identifiers the agent script will request.
- The `claude-*` aliases exist because the Claude Agent SDK hardcodes those names when spawning sub-agents; mapping them to Azure or Gemini deployments keeps everything compatible.
- `litellm_settings.master_key` now pulls from `LITELLM_MASTER_KEY`, so no secrets live in the repo.

If you want to target Gemini, run LiteLLM with `config.yaml` instead; just make sure `GEMINI_API_KEY` is set.

## Run LiteLLM
```bash
source .env
pkill -f litellm || true    # stop any previous proxy
litellm --config config.yaml
```

LiteLLM listens on `localhost:4000` by default. You can sanity-check it with:

```bash
curl -H "Authorization: Bearer $LITELLM_MASTER_KEY" \
     http://127.0.0.1:4000/v1/models
```

## Run the Claude Agent SDK Demo
In a second terminal (with the same `.env` sourced):

```bash
python agent.py
```

The script streams the agent’s tool output for the sample prompt. Edit `agent.py` to change the prompt, model (`ClaudeAgentOptions.model` must match a `model_name` from the LiteLLM config), or tool permissions.

## Switching Between Azure and Gemini
- Azure only: keep using `config.yaml`.
- Gemini: start LiteLLM with `litellm --config config.yaml` after exporting `GEMINI_API_KEY`.
- Mixed: adjust the `claude-*` aliases to point to whichever backend tier (fast vs. powerful) you want; both configs already show safe defaults.

## Troubleshooting
- `401 Unauthorized`: confirm the shell running LiteLLM has `LITELLM_MASTER_KEY` exported and matches the agent’s `ANTHROPIC_API_KEY`.
- `404 The model does not exist`: double-check that the `model_name` requested by the agent exactly matches the entry in `config.yaml` and that its `model` field references a real deployment.
- Requests hanging: ensure no other service is bound to port `4000` and rerun `pkill -f litellm`.
