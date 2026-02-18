---
name: email-content-generator
description: Generate witty, high-energy email drafts (subject + body) tailored to a provided topic, audience, and desired comedic tone. Use for fun announcements, roasts, or lighthearted updates needing structured humor.
---

# Email Content Generator

Keep outputs punchy, respectful, and grounded in the request’s context. Default to friendly workplace-appropriate humor unless told otherwise.

## Required Inputs
- Topic or goal (what the email must accomplish).
- Audience profile (individual vs. team, familiarity level).
- Desired tone or comedic style (snarky, absurd, dry, etc.). Infer if missing.
- Any hard constraints: length, CTA, banned phrases, formatting.

## Drafting Workflow
1. **Clarify intent** – Restate the ask in your head; note any emotional beats (surprise, mock outrage, celebration).
2. **Select humor knobs** – Choose 1–2 devices (hyperbole, callbacks, juxtaposition, mock-seriousness, playful threats). Avoid piling on more than 3.
3. **Outline structure** (Subject → Greeting → Hook → Body → CTA → Sign-off). Ensure each section advances the joke while still achieving the objective.
4. **Write the hook** – Lead with an unexpected image or faux-official statement. Keep it under 25 words.
5. **Body paragraphs** – Use 2–3 short paragraphs. Pattern ideas:
   - Problem setup → ridiculous exaggeration → real ask.
   - “FAQ” mini-list with comedic answers.
   - Mock memo (“Per Section 42.b of Snack Law…”).
6. **CTA + sign-off** – Bring the humor back to the practical request and end with a witty button.
7. **Polish pass** – Read once for comedic timing, once for clarity. Remove inside jokes the audience wouldn’t get.

## Tone Guardrails
- Humor must never punch down. No references to protected classes or sensitive personal info.
- Keep workplace-safe: skip swearing, body humor, or gossip.
- Balance absurdity with clarity so the main ask isn’t lost.

## Subject-Line Patterns
- `🚨 <Over-the-top alert> about <mundane thing>`
- `<Hyperbolic claim> (and also <real reason>)`
- `Re: <serious topic> – jk, it’s about <fun twist>`
Always produce 2–3 optional subject lines unless the user supplies one.

## Output Template
```
Subject Options:
1. ...
2. ...

Email:
Hi <Name or Team>,
<Hook sentence>

<Body paragraph 1>
<Body paragraph 2> (optional)

<CTA sentence>

<Sign-off>,
<Sender>
```
Swap greeting/sign-off to match audience formality.

## Checklist Before Returning
- ✅ Subject line(s) mirror the body tone.
- ✅ CTA is explicit (action + when/where).
- ✅ No conflicting facts with the prompt.
- ✅ Humor device count ≤3 and consistent.
- ✅ Spelling and names double-checked.
