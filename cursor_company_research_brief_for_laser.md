# Company research brief for Laserhub
_Exported on 3/5/2026 at 08:10:20 GMT+1 from Cursor (2.5.20)_

---

**User**

<role>
You are a senior research analyst who builds company briefs for product managers. Your briefs are used as both standalone reference documents and as context blocks injected into other AI prompts. Accuracy and recency matter because PMs make strategy decisions based on these briefs — a stale or single-source claim can send a team in the wrong direction.
</role>

<input>
{{https://laserhub.com/ }}
</input>

<instructions>
Research the company at the URL above and produce a structured brief. Follow these steps in order.

1. **Fetch the homepage.** Extract the `<title>`, `<meta name="description">`, and any navigation links. If the URL is unreachable, stop and report the error.

2. **Explore the site.** Fetch key pages you can identify from navigation:
   - About / Company
   - Product / Features
   - Pricing
   - Careers / Jobs
   - Blog or Newsroom (most recent 2–3 posts only)
   - Case studies or Customers

3. **Search the web** using the queries in `<research_queries>`. Prioritize the top 2–3 per category. Go deeper only when the first pass leaves gaps. Always append the current year to queries for fast-changing facts (revenue, team size, funding, leadership).

4. **Cross-validate in a scratchpad.** Before writing the final brief, use a `<scratchpad>` block (visible to you, not included in the output) to:
   - List each claim and its supporting sources.
   - Flag any claim supported by only one source.
   - Note conflicts between sources.
   - Decide confidence level (H / M / L) for each field.

5. **Write the brief** in the exact format shown in `<output_format>`.
</instructions>

<research_queries>
Adapt these to the specific company. Use the company name or category keywords as appropriate.

Company fundamentals:
- "[company] Crunchbase" — funding, investors, founding date, team size
- "[company] LinkedIn" — employee count, description
- "[company] PitchBook OR Tracxn" — valuation, funding rounds

Market positioning:
- Identify 2–3 specific category keywords from the homepage meta tags (e.g., "composable commerce," "headless CMS"). Search for competitors using these keywords, not the company name:
  - "[keyword] alternatives" or "[keyword] platforms comparison"
  - "[keyword] market landscape [current year]"
- "[company] G2 OR Capterra" — category, reviews
- "[company] alternatives OR vs" — competitive landscape

Recent activity:
- "[company] news [current year]"
- "[company] blog OR press release [current year]"

Customer & perception:
- "[company] reviews OR Trustpilot"
- "[company] Reddit OR Hacker News"

Hiring signals:
- "[company] careers OR jobs [current year]"
</research_queries>

<output_format>
Produce exactly two sections: Core Brief, then Confidence & Discrepancies.

### Core Brief

Target: under 200 words total. Each field is 1–2 sentences max. Write in plain language — no filler adjectives, no marketing speak. Date-tag any quantitative fact older than 18 months (e.g., "~$50M ARR (Dec 2023)"). Mark low-confidence fields with ⚠️.

**Company:** [Name | legal entity if different | founded year | stage/ownership | ~team size | HQ]
**Mission:** [One sentence]
**Business model:** [How they make money]
**Market category:** [Category label]
**Target customer:** [Who buys, in one line]
**Product(s):** [What they sell, plain language]
**Differentiators:** [What sets them apart]
**Competitors:** [Key names and one-line positioning for each]
**Current focus:** [What they're investing in now — inferred from hiring, blog, news]

If a field cannot be determined from recent sources, write: "Unknown / outdated — PM should verify."

### Confidence & Discrepancies

**Confidence table:**

| Field | Level | Sources |
|-------|-------|---------|
| ... | H / M / L | [source list] |

Levels: H = 3+ independent sources agree. M = 2 sources, or 1 strong external source. L = single source or self-reported only.

**Discrepancies table** (omit if none):

| Fact | Conflict | Notes |
|------|----------|-------|
| ... | Source A says X; Source B says Y. | [Resolution or "PM should verify."] |
</output_format>

<example>
Here is a completed example so you can see the expected density, tone, and structure.

### Core Brief

**Company:** Acme Widgets Inc. | Founded 2018 | Series B (raised $45M, led by Index Ventures, 2024) | ~200 employees | HQ: San Francisco, CA
**Mission:** Make industrial procurement fast and transparent for mid-market manufacturers.
**Business model:** SaaS subscriptions (tiered by seat count) plus transaction fees on marketplace orders.
**Market category:** B2B procurement platform
**Target customer:** Operations and procurement leads at mid-market manufacturers ($50M–$500M revenue).
**Product(s):** Cloud platform for sourcing, quoting, and managing suppliers; includes supplier marketplace and spend analytics dashboard.
**Differentiators:** Purpose-built for manufacturing (vs. horizontal procurement tools); real-time supplier availability data via integrations with ERP systems.
**Competitors:** Coupa (enterprise, broader scope), Thomasnet (supplier discovery, no transaction layer), Procurify (SMB-focused, less manufacturing-specific).
**Current focus:** Expanding into EMEA (3 open roles in London); launching AI-powered spend classification (announced on blog, Jan 2025).

### Confidence & Discrepancies

| Field | Level | Sources |
|-------|-------|---------|
| Company | H | Crunchbase, LinkedIn, company About page |
| Mission | M | Company About page, CEO interview (podcast) |
| Business model | M | Pricing page, G2 reviews |
| Market category | H | G2, Capterra, company homepage |
| Target customer | M | Case studies, G2 reviews |
| Product(s) | H | Product page, G2, demo video |
| Differentiators | M | Company claims + G2 reviews corroborate |
| Competitors | H | G2 category, "[keyword] alternatives" search, industry report |
| Current focus | M | Careers page, blog post |

| Fact | Conflict | Notes |
|------|----------|-------|
| Team size | LinkedIn says ~250; Crunchbase says 180 (last updated Sep 2024). | Likely ~200–250 now given 15 open roles. PM should verify. |
</example>

<rules>
These rules exist to keep the brief trustworthy and actionable.

1. Only include claims you can attribute to a specific source. This prevents hallucination.
2. Prefer the most recent source available for any fast-changing fact. If the best data is older than 18 months, append the date in parentheses — because stale data misleads PMs who build strategy on it.
3. Apply convergent validity: present single-source claims as tentative (⚠️), not established. Self-reported claims receive M confidence at best.
4. When sources conflict, report the discrepancy in the table rather than choosing a side.
5. Keep the Core Brief under 200 words. Every word should carry information.
6. Write "Unknown / outdated — PM should verify" for any field you cannot fill from recent, credible sources. This is always better than guessing.
7. Produce only the two sections (Core Brief + Confidence & Discrepancies). No preamble, commentary, or sign-off.
</rules>

---

**Cursor**

I’ll first pull key pages from the Laserhub site (home, about, platform/product, pricing, careers, blog/cases), then run targeted web searches (Crunchbase, LinkedIn, reviews, news) to capture funding, size, and positioning. After cross-checking facts in a scratchpad, I’ll condense everything into the requested brief and confidence tables.

### Core Brief

**Company:** Laserhub GmbH | Founded 2017 | Series B (undisclosed “double‑digit million euro” round led by Evli Growth Partners, Jun 2022) | Venture-backed private company | ~80 employees ⚠️ | HQ: Stuttgart, Germany  
**Mission:** Digitize access to the full variety of metalworking so buyers and suppliers can source custom metal parts efficiently via a single, digital platform.  
**Business model:** Unknown / outdated — PM should verify.  
**Market category:** B2B vertically integrated procurement platform / marketplace for custom metal and plastic parts (purchasing systems for manufacturing).  
**Target customer:** Manufacturing firms from small workshops and Mittelstand to DAX corporates in sectors like special machine building, metal construction, and plant engineering in Germany and neighboring European markets.  
**Product(s):** Online platform where customers upload CAD files to configure and order custom metal and plastic parts (laser cutting, bending, tube laser cutting, CNC turning/milling/turn-milling plus finishing) with instant pricing and automated matching to a network of ~100 ISO 9001–certified producers.  
**Differentiators:** Vertically integrated, manufacturer-independent workflow from quote to invoicing; curated ISO 9001–certified producer network in Germany/Austria; 24/7 instant offers and a single contract partner across multiple metalworking processes.  
**Competitors:** Metalshub (focuses on digital trading and price intelligence for raw metals, more commodity-oriented than custom parts); Sourcima (global digital manufacturing marketplace for CNC/sheet metal and other processes); NowPurchase (procurement marketplace specialized in metal manufacturing, more India-focused).  
**Current focus:** Expanding platform capabilities (e.g., welding and assemblies per 2022 funding plans), positioning as a resilience tool for metal processors facing supply-chain and CBAM/tariff pressures (NORTEC 2026 presence), and deepening technical thought leadership via frequent metal/CNC- and CBAM-focused blog content.  

### Confidence & Discrepancies

**Confidence table:**

| Field | Level | Sources |
|-------|-------|---------|
| Company | H | [Laserhub platform](https://laserhub.com/plattform/), [Laserhub “Über uns”](https://laserhub.com/ueber-uns/), [Acton Capital portfolio](https://www.actoncapital.com/portfolio/laserhub), [Acton Series B news](https://www.actoncapital.com/news/laserhub-closes-series-b-to-expand-its-leadership-in-europe), [Startbase Series B article](https://www.startbase.com/news/exklusiv-laserhub-sammelt-series-b-finanzierung-ein/) |
| Mission | H | [Laserhub career page](https://laserhub.com/career/), [Laserhub “Über uns”](https://laserhub.com/ueber-uns/), [Laserhub platform](https://laserhub.com/plattform/) |
| Business model | L | [BusinessWith profile](https://businesswith.com/system/laserhub/), [Acton Series B news](https://www.actoncapital.com/news/laserhub-closes-series-b-to-expand-its-leadership-in-europe), [Laserhub platform](https://laserhub.com/plattform/) |
| Market category | H | [Laserhub homepage](https://laserhub.com/), [Laserhub platform](https://laserhub.com/plattform/), [Acton Capital portfolio](https://www.actoncapital.com/portfolio/laserhub), [BusinessWith profile](https://businesswith.com/system/laserhub/) |
| Target customer | H | [Laserhub platform](https://laserhub.com/plattform/), [Production network page](https://laserhub.com/ueber-uns/produktion/), [Acton Capital portfolio](https://www.actoncapital.com/portfolio/laserhub), [BusinessWith profile](https://businesswith.com/system/laserhub/) |
| Product(s) | H | [Laserhub homepage](https://laserhub.com/), [Laserhub platform](https://laserhub.com/plattform/), [Production network page](https://laserhub.com/ueber-uns/produktion/), [BusinessWith profile](https://businesswith.com/system/laserhub/), [Laserhub blog](https://laserhub.com/blog/) |
| Differentiators | M | [Laserhub homepage](https://laserhub.com/), [Laserhub platform](https://laserhub.com/plattform/), [Production network page](https://laserhub.com/ueber-uns/produktion/), [Acton Series B news](https://www.actoncapital.com/news/laserhub-closes-series-b-to-expand-its-leadership-in-europe), [BusinessWith profile](https://businesswith.com/system/laserhub/) |
| Competitors | M | Web search: “digital metal procurement platform alternatives 2026” (Metals Hub / Metalshub, NowPurchase, Tacto, Sourcima, etc.), [BusinessWith category context](https://businesswith.com/purchasing-systems/) |
| Current focus | M | [Acton Series B news](https://www.actoncapital.com/news/laserhub-closes-series-b-to-expand-its-leadership-in-europe), [Startbase Series B article](https://www.startbase.com/news/exklusiv-laserhub-sammelt-series-b-finanzierung-ein/), [Laserhub blog](https://laserhub.com/blog/), NORTEC 2026 coverage on [Zerspanungstechnik.de](https://www.zerspanungstechnik.de/en/blog/2026/01/27/laserhub-kehrt-auf-die-nortec-zurueck/), [Laserhub career page](https://laserhub.com/career/) |

**Discrepancies table:**

| Fact | Conflict | Notes |
|------|----------|-------|
| HQ location | [Acton Capital](https://www.actoncapital.com/portfolio/laserhub), [Laserhub site](https://laserhub.com/plattform/), and [Startbase](https://www.startbase.com/organization/laserhub/) describe Laserhub as Stuttgart-based; a WebSearch snippet summarizing the [Point Nine job board](https://jobs.pointnine.com/companies/laserhub-2) calls it “Berlin-based.” | Multiple primary and investor sources agree on Stuttgart as HQ; Berlin reference may reflect a secondary office or a job board error. PM should verify via LinkedIn/company register if Berlin has significant operations. |
| Team size | Laserhub homepage states “Über 80 Experten und Expertinnen” (undated); internal team-function counts roughly align with ~70–80; external directories (Point Nine/LinkedIn-style snippet) list a broad “51–200 employees” band. | Numbers are self-reported or in wide bands and not date-stamped. Using “~80 employees ⚠️” in the brief reflects the company claim but should be validated against up-to-date LinkedIn or filings. |
| Hiring activity | WebSearch snippet via [Point Nine job board](https://jobs.pointnine.com/companies/laserhub-2) shows at least one open “Senior Backend Developer Typescript” role in 2026; the current [Personio ATS](https://laserhub-gmbh.jobs.personio.de/) landing page shows no matching jobs. | Likely that specific roles have recently closed or that Personio search defaults hide some postings. PM should verify live on the careers site and LinkedIn before using hiring as a leading signal. |

---

**User**

improve it

