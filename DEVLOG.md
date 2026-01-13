# Development Log - Wimbledon Chatbot

## [2026-01-12]
### Progress
- Successfully generated 'batch_input.json' for all 567 pages of the Compendium.
- Encountered '429 RESOURCE_EXHAUSTED' on the standard Gemini API due to daily free-tier limits.
- Configured Google Cloud Project and enabled Vertex AI API to access higher quotas.
- Prepared the Colab-to-Vertex handshake using 'auth.authenticate_user()'.

### Challenges
- Learned that "Free Tier allows ~100-200 RPD, which 567 pages quickly exceeded.
- Managing Colab Pro on one account and Google Cloud on another required manual credential propogation.
