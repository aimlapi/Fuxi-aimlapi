# AI/ML API

Connect to the official hosted MCP server at `https://mcp.aimlapi.com/mcp`
using Streamable HTTP. Nothing needs to be installed locally.

## Installation and authentication

This plugin is opt-in. It does not enable tools until you install and configure it.

1. Create an API key at https://aimlapi.com/app/keys.
2. Set `AIMLAPI_API_KEY` in your shell environment before starting FuXi.
   The bundled configuration sends it as `Authorization: Bearer <API key>`.
3. Install with `/plugin install aimlapi@fuxi-plugins`, or use `/plugin > Discover`.

The server also supports OAuth sign-in. To use OAuth instead of this plugin's
Bearer configuration, configure the same endpoint through your client's OAuth
flow without the explicit Authorization header. OAuth sign-in and environment
variable expansion in FuXi still need client-side verification.

## Capabilities and billing

One connector provides access to 10,000+ tools and models, including web search,
crawling, page extraction, document parsing, social media data and SEO data.
Models include chat and reasoning, image, video, music and speech generation,
speech-to-text, OCR and embeddings. Model search allows comparison by price,
speed and context length.

Model lookups and account checks are free. Generation, chat, embeddings and
`tools_run` are paid, billed pay-as-you-go to your AI/ML API account. Review
costs before running tools.

## Security

Use the exact HTTPS endpoint above. Do not send the key to other hosts or follow
cross-host redirects with the Authorization header. The FuXi transport is not
included in this repository, so its redirect handling has not been verified here.

Docs: https://docs.aimlapi.com/quickstart/mcp

Official MCP Registry name: `com.aimlapi/mcp`.
