import asyncio
import os
from pathlib import Path

from claude_agent_sdk import query, ClaudeAgentOptions
from dotenv import load_dotenv

repo_root = Path(__file__).resolve().parent
load_dotenv(repo_root / ".env")

os.environ.setdefault("ANTHROPIC_BASE_URL", "http://localhost:4000")
os.environ.setdefault("ANTHROPIC_API_KEY", os.getenv("LITELLM_MASTER_KEY", ""))

async def main():
    async for message in query(
        prompt="get me email content for a mail where I need to fire an employee",
        options=ClaudeAgentOptions(
            model="azure-gpt-4.1",  # must match model_name in config.yaml exactly
            cwd="/Users/sanketh/Work/claude-agent-sdk-openai",
            setting_sources=["user", "project"],  # ← loads skills from filesystem
            allowed_tools=["Read", "Edit", "Bash", "Skill"],
        ),
    ):
        print(message)


if __name__ == "__main__":
    asyncio.run(main())
