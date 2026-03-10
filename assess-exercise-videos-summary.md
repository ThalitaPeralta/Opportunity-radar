# Should We Build: Exercise Demonstration Videos

**Request:** Add a feature that shows how to do each exercise in the form of a video.
**Stakeholder:** Alex, Product Operations Lead
**Full assessment:** [assess-exercise-videos-full.md](assess-exercise-videos-full.md)

---

## Relevance of Criteria

| Criteria | Relevance | Why |
|----------|-----------|-----|
| User/Customer Value | 🔴 Low | Experts already know the exercises — edge cases only |
| Business Impact | 🟡 Medium | High content cost, unclear revenue upside |
| Strategic Alignment | 🟢 High | Risks diluting the expert-first positioning |
| Goal Contribution | 🟡 Medium | No known OKR this directly moves |
| Market & Competitive | 🟢 High | Table stakes for general apps; not a differentiator for expert apps |
| Risk & Urgency | 🔴 Low | No urgency; minor content quality risk only |
| Long-term Vision | 🟢 High | Creates content debt unless tied to a bigger vision (e.g., AI form analysis) |
| Segmentation | 🟡 Medium | Only serves edge cases within the expert segment |
| Feasibility | 🔴 Low | Tech is easy; content pipeline is the real constraint |
| Resources & Effort | 🟢 High | Significant opportunity cost regardless of approach |

**Focus on:** Strategic Alignment, Market & Competitive, Long-term Vision, Resources & Effort

---

## Pro: Reasons to Build

### User Experience Completeness
- Covers edge cases where even experts encounter unfamiliar accessory or rehab movements
- Reduces friction of leaving the app to search YouTube mid-workout

### Retention & Perceived Value
- Adds content richness that could reduce churn from users who find the app "too bare bones"
- Low-effort version (YouTube embeds) is cheap to ship and closes a gap vs. general apps

### Market Expansion Bridge
- If strategy shifts to capture intermediate users, videos are already in place
- Could serve as early infrastructure if AI form analysis becomes a future direction

---

## Con: Reasons Not to Build

### Strategic Misalignment
- Expert users chose this app because it doesn't treat them like beginners
- Adding tutorial videos signals the wrong positioning — risks drift toward Fitbod/JEFIT territory
- A crowded, undifferentiated space where the app currently has an advantage by not playing

### Wrong Problem for This Audience
- The expert use case is tracking and progression — not learning exercises
- The users who most need video are not the users this app is for
- Solving for the edge case at the cost of the core use case

### Cost Doesn't Match Value
- Content is the hard part: hundreds of videos needed for meaningful coverage
- Ongoing maintenance — videos go stale, need re-recording
- Every sprint here is not spent on analytics, program builder, or performance tools

### No Competitive Upside
- General apps have already won the video library battle
- Matching them doesn't differentiate — it just makes the app look more like them

---

## The Decision Hinges On

| Question | If Yes → Build | If No → Don't Build |
|----------|----------------|---------------------|
| Are we planning to expand to intermediate/beginner users? | ✅ | ❌ |
| Do expert users frequently encounter unfamiliar exercises in the app? | ✅ | ❌ |
| Is there a cheap/existing content licensing path available? | ✅ Consider | ❌ |
| Is AI-powered form analysis part of the long-term vision? | ✅ As foundation | ❌ |

---

## My Read

**Build it if:** The strategy is expanding beyond experts to intermediate users, or there's a clear path toward AI-powered form analysis where video infrastructure becomes a foundation — not a destination.

**Don't build it if:** The app's identity is expert-first and the goal is to deepen that moat. The opportunity cost is too high and the feature solves a problem your core users don't really have.

**The honest middle ground:** If something must ship, embed curated YouTube links with zero maintenance cost — it covers the edge cases without creating a content pipeline. But treat it as convenience, not a feature. Spend real engineering cycles on what experts actually care about: deeper analytics, progressive overload automation, or program comparison tools.
