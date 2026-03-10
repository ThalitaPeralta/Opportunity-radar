# Assessment: Exercise Demonstration Videos

**Request:** Add a feature that shows how to do each exercise in the form of a video (exercise form/technique demonstration videos).
**Stakeholder:** Alex, Product Operations Lead
**Date:** 2026-03-09
**Context:** Gym tracking app built specifically for expert-level athletes/lifters.

---

## 1. User/Customer Value
*How much value does this generate for the user?*

The app is built for **experts** — users who already know how to squat, deadlift, and bench press. Demonstration videos are primarily a beginner/intermediate learning tool. For an expert audience, a generic "how to do a squat" video generates negligible value and may feel condescending. The real edge case where value exists: experts occasionally explore unfamiliar accessory or rehabilitation movements where a reference video could help. But this is the exception, not the rule for this segment.

**Confidence:** 🟡 Assumed — Based on what expert user behavior typically looks like; no app-specific usage data available.

**What would change this:** Evidence that expert users frequently encounter unfamiliar exercises within the app, or user research showing experts want video as a form-check reference rather than instruction.

---

## 2. Business Impact
*What is the financial impact?*

Video content carries high hosting and delivery costs (CDN, storage, encoding). If self-produced, add production costs. If licensed, add recurring fees. Revenue upside is unclear — experts likely chose this app because of its expert focus, not because it has video tutorials. It's unlikely to drive new paid conversions. It could marginally improve retention if users feel the app is more complete, but that's a weak effect for this audience.

**Confidence:** 🟡 Assumed — No pricing or conversion data available; cost estimates are based on industry norms.

**What would change this:** Data showing trial-to-paid conversion correlates with content richness, or a licensing deal that makes video cheap to add.

---

## 3. Strategic Alignment
*Does this align with company/product plans?*

This is the most critical criterion. A gym tracking app for experts has a clear identity: serious tracking, performance data, progressive overload, analytics. Adding instructional video pulls the product toward general fitness app positioning (Fitbod, Jefit, Apple Fitness+), risking **dilution of the expert identity**. If the strategy is to own the expert segment, this is a misalignment. If the strategy is to expand to intermediate users, it could serve as a bridge — but that would require revisiting the expert-first positioning as well.

**Confidence:** 🟡 Assumed — Strategy inferred from "expert app" description; actual roadmap not available.

**What would change this:** A stated strategic intent to expand beyond experts, or a roadmap commitment to content as differentiation.

---

## 4. Goal Contribution
*Does this help us focus on the right goals?*

Without knowing the actual OKRs, the typical expert fitness app goals are: retention, workout frequency, PRs logged, and paid conversion. Instructional video does not obviously move any of these for an expert user. It adds surface area without addressing the core loop — log workout, track progress, hit PRs. It could distract the team from features that actually move retention (e.g., better analytics, coach integration, program builder).

**Confidence:** 🔴 Blind — No access to actual OKRs or goal metrics for this product.

**What would change this:** If a current OKR is explicitly "increase session depth" or "expand content catalog," video becomes more relevant.

---

## 5. Market & Competitive Landscape
*Is this important for competitive advantage?*

Nearly every general fitness app has exercise videos — Fitbod, Hevy, Strong, JEFIT all include them. For general apps, it's table stakes. **For an expert app, not having videos can be a feature, not a bug** — it signals "we don't waste your time with basics." Competitors targeting the expert segment (Boostcamp, GZCLP-style trackers) largely don't emphasize instructional video. Adding it doesn't differentiate; it makes the app look more generic.

**Confidence:** 🟢 Evidence-Based — Competitor feature sets are publicly observable.

**What would change this:** A competitor in the expert space successfully using high-quality biomechanics or technique video as a differentiator.

---

## 6. Risk & Urgency
*Are there risks or urgencies requiring quick action?*

No urgency signals. No compliance, legal, or security risk. One minor content risk: third-party or user-submitted videos with incorrect form could lead to injury — carrying reputational risk in a fitness context. Neither this nor any other risk factor is urgent here.

**Confidence:** 🟡 Assumed — No known urgent triggers; risk assessment is precautionary.

**What would change this:** A contractual commitment to a content partner, or a competitor announcement forcing a response.

---

## 7. Long-term Vision
*Does this comply with where we're heading?*

If the long-term vision is to be the definitive platform for serious athletes, instructional video ages poorly — it becomes a content maintenance burden (videos go stale, technique evolves). It also creates a content moat problem requiring hundreds of videos for meaningful coverage. Alternatively, if the vision moves toward AI-powered form analysis, video infrastructure *could* be a stepping stone — but that's a different product direction than static tutorial videos.

**Confidence:** 🟡 Assumed — Vision inferred; no roadmap document available.

**What would change this:** A product vision pointing toward AI coaching, form analysis, or expert content as a long-term moat.

---

## 8. Segmentation
*Who benefits, and how many?*

Within an expert user base, video beneficiaries are narrow: users exploring new accessory movements, users returning from injury with modified exercises, or users coaching others through the app. This is a minority use case. The majority of expert users logging their 5th year of compound lifts will never watch a squat tutorial. The feature serves the edges of the expert segment and the whole of the beginner segment — but beginners aren't the target.

**Confidence:** 🟡 Assumed — Behavioral segmentation inferred from expert user archetype; no usage data.

**What would change this:** User research showing a meaningful percentage of expert users encounter unfamiliar exercises regularly (e.g., coach-assigned movements).

---

## 9. Feasibility
*Can we actually build this?*

Video playback in a mobile app is technically straightforward. The real challenge is **content**: sourcing, producing, or licensing high-quality videos for hundreds of exercises. Options range from embedding YouTube links (low effort, low control) to licensed libraries (moderate cost, good coverage) to self-production (high cost, full control). The build itself is not the constraint — the content pipeline is.

**Confidence:** 🟢 Evidence-Based — Video playback and content sourcing are well-understood problems in the industry.

**What would change this:** An existing content provider relationship that makes licensing trivial.

---

## 10. Resources & Effort
*How much will this take?*

Minimum viable (YouTube embeds): low dev effort (~1–2 weeks), low cost, external dependency risk. Licensed content library: moderate dev + recurring licensing + curation. Self-produced: high production cost, significant ongoing maintenance. The opportunity cost is significant regardless — every sprint spent here is not spent on analytics, progressive overload automation, or performance tools that move the needle for expert users.

**Confidence:** 🟡 Assumed — Effort estimates based on industry norms; actual team velocity unknown.

**What would change this:** An existing content partnership or team member with video production capacity already available.

---

## Confidence Overview

| Criteria | Confidence |
|----------|------------|
| User/Customer Value | 🟡 Assumed |
| Business Impact | 🟡 Assumed |
| Strategic Alignment | 🟡 Assumed |
| Goal Contribution | 🔴 Blind |
| Market & Competitive | 🟢 Evidence-Based |
| Risk & Urgency | 🟡 Assumed |
| Long-term Vision | 🟡 Assumed |
| Segmentation | 🟡 Assumed |
| Feasibility | 🟢 Evidence-Based |
| Resources & Effort | 🟡 Assumed |

**Evidence-Based:** 2 | **Committed:** 0 | **Assumed:** 7 | **Blind:** 1
