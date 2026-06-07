# AI Agent Skills Candidate Registry

This repository is the candidate registry for SMB-oriented AI.Skills, AI Agents, Agent roles, media-generation providers, and local trial runners.

## Repository Role

This repository is the screening and evidence warehouse. It records source research, license review, smoke queues, smoke results, L2 simulated results, packaging queues, platform acceptance notes, component-only decisions, provider route checks, and local runner configuration.

The stable installable registry is separate:

- Stable registry: `ai-agent-skills-stable-registry`
- Current stable Skill count: 71
- P0 baseline stable Skills: 13
- P1 expanded stable Skills: 42
- P2 Quality Sprint 06 stable Skills: 8
- P3 Quality Sprint 07 stable Skills: 8

## Candidate Inventory

- Candidate/evidence path: `skills/smb-callable-candidate-skills`
- Candidate draft package path: `skills/smb-candidate-draft-l3-skills`
- Local runner path: `platform-runners/deepagents-local-runner`
- Local candidate/evidence Skill artifacts: 89 `SKILL.md` files and 90 `skill.yaml` files, including historical draft packages, nested batch artifacts, and one template.

## Boundary

Candidate admission does not mean stable delivery. DeepAgents smoke, role smoke, provider route checks, and real media sandbox smoke do not by themselves promote a candidate into the stable customer-callable registry.

Promotion into the stable registry happens only after an explicit promotion decision under the active rule: the Skill or Agent must fit the platform base, use the OpenAI-compatible relay/model gateway, serve SMB six-department scenarios, and keep its declared runtime boundaries.

Do not commit `.env`, API keys, real customer files, provider tokens, or real generated media outputs.
