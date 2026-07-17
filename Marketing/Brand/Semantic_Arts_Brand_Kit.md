# Semantic Arts — Visual & Brand Style Guide (Reference)

**Version 3.1 — July 2026** · Palette: Option A — Ember & Olive · SA22 Standard Logo Set
**Platform message:** *"One elegant data model can change everything."*

> This is a text reference version of the full Semantic Arts Visual Style Guide, formatted for use as project knowledge. It covers brand colors, logo usage, typography, spacing, UI components, imagery direction, and voice & tone. For the visual/interactive version with rendered components and logo files, see the companion HTML style guide.

---

## 1. Color

### Official SA22 Brand Colors
These two colors are taken directly from the SA22 Standard Logo Set and anchor the entire system.

| Name | Hex | RGB | Usage |
|---|---|---|---|
| **Semantic Blue** (SA22 Primary) | `#005A7D` | 0, 90, 125 | Navigation, logo color version, headings on dark, all primary brand surfaces. The dominant brand color. |
| **Semantic Gray** (SA22 Secondary) | `#808080` | 128, 128, 128 | Hero section backgrounds, section fills, dividers, supporting text. The neutral brand tone. |

### Supporting Palette — Ember & Olive
Confirmed site accent colors, plus two added supporting values for richer layouts.

| Name | Hex | Usage |
|---|---|---|
| Burnt Orange (CTA) | `#C84A2B` | "Get A Quote" and all primary CTA buttons. One per viewport maximum. Never used for decoration. |
| Olive Chartreuse (Active) | `#8C9E38` | Active navigation state, **kicker labels** above section headings, inline emphasis in dark contexts. |
| Link Blue | `#1E70B0` | Body copy hyperlinks. Always underlined. Not for buttons or decorative use. |
| Warm Gold *(Added)* | `#D4A83A` | Stat callouts, achievement badges, pull-quote accents, data visualization highlights. |
| Pale Teal *(Added)* | `#E0EEF2` | Card backgrounds, alternating row fills, quote block backgrounds, light section surfaces. |

### Neutrals

| Name | Hex | Usage |
|---|---|---|
| Near Black | `#2B2B2B` | All headings on white or light surfaces. |
| Charcoal Gray | `#4A4A4A` | Body copy. Comfortable reading contrast without the harshness of pure black. |
| Light Gray | `#CCCCCC` | Horizontal rules, section dividers, table borders, card outlines. |
| White | `#FFFFFF` | Page backgrounds, card interiors, reversed text on dark surfaces. |

### Dark Surface Usage
- **Semantic Blue surface:** navigation bars, footers, dark hero sections, high-impact brand moments. Pair headings in white with an Olive kicker/eyebrow and a small Burnt Orange accent bar.
- **Semantic Gray surface:** hero content panels, interior section backgrounds, image overlays. Pair with an Olive accent bar.

### Accessibility
- Semantic Blue (`#005A7D`) on white: **7.3:1** contrast — well above WCAG AA (4.5:1).
- Semantic Gray (`#808080`) on white: **3.95:1** — use at 18pt+ or bold weight for body text on gray backgrounds, or lighten the background.
- Burnt Orange (`#C84A2B`) on white: **4.6:1** — passes AA at normal text sizes.

---

## 2. Logo — SA22 Standard Logo Set

The Semantic Arts logo combines a distinctive mark (a field of hollow circles growing denser toward the upper right, with a solid Semantic Blue connector form at its center) and the wordmark **"semantic arts"** in bold, lowercase. All logo files are prefixed `SA22` to differentiate them from previous logo versions.

### Three Official Variants

| Variant | When to Use | Notes |
|---|---|---|
| **Color** | White backgrounds | Semantic Blue mark + wordmark on white. The preferred primary usage. |
| **Black** | White, light color, or light image backgrounds | Full black mark and wordmark. Files do not include a background. |
| **White** | Black, dark color, or dark image backgrounds | Mark and wordmark in white. PNG files have transparent backgrounds; a black background is **not** included in the files — you must supply the dark background yourself. |

### File Formats (all three variants)

| Format | Background | Sizes | Use |
|---|---|---|---|
| `.jpg` | White | Small, medium, large, extra-large | Print, PowerPoint, web |
| `.png` | Transparent | Small, medium, large, extra-large | Print, PowerPoint, web |
| `.svg` / `.pdf` | N/A (vector) | Resolution independent | Web (SVG) and print/PowerPoint (PDF) |

**File naming convention:** all SA22 logo files begin with `SA22` — e.g. `SA22_color_266.png`, `SA22_black_266.png`, `SA22_white_266.png`.

### Clear Space & Minimum Size
Maintain minimum clear space equal to the cap-height of the letter "s" in "semantic" on all four sides of the logo lockup. Minimum digital render width: **120px**.

### Logo Don'ts
- ✕ Do not use the Color version on orange or colored backgrounds.
- ✕ Do not place the logo on gradients — use the White version on dark fills instead.
- ✕ Do not render the wordmark in gray — use Color, Black, or White version only.
- ✕ Never capitalize the wordmark — it is always lowercase, "semantic arts."

---

## 3. Typography

**Typeface:** Open Sans (weights 300, 400, 600, 700, 800), used throughout — headings, navigation, and body copy share the same typeface at varying weights.

**Unit:** All type sizes below are specified in **points (pt)**, consistent with Semantic Arts' other digital materials.

| Element | Font | Size | Weight | Color / Notes |
|---|---|---|---|---|
| Hero H1 | Open Sans | 36–48pt | 800 ExtraBold | `#2B2B2B` on light · `#fff` on dark |
| Section H2 | Open Sans | 28–34pt | 700 Bold | `#2B2B2B`; followed by `#CCC` horizontal rule |
| Card H3 | Open Sans | 18–22pt | 700 Bold | `#2B2B2B`; line-height 1.3 |
| Lead / Intro | Open Sans | 17–18pt | 300 Light | `#4A4A4A` on white; `rgba(255,255,255,0.78)` on gray |
| Body Copy | Open Sans | 15–16pt | 400 Regular | `#4A4A4A`; line-height 1.7 |
| Nav Links | Open Sans | 14pt | 600 SemiBold | `rgba(255,255,255,0.55)`; active = Olive `#8C9E38` |
| CTA Button | Open Sans | 12–13pt | 700 Bold | All-caps, +5% letter-spacing, white on Burnt Orange |
| **Kicker Label** | Open Sans | **16pt** | **700 Bold** | All-caps, +16–20% tracking; **Olive Chartreuse `#8C9E38`** |
| Caption / Fine | Open Sans | 12pt | 400 Regular | `#888888`; footnotes, image captions |

A "kicker label" is the small, tracked-out, uppercase eyebrow text that sits above a heading (e.g. above the H1 in a hero, or above a card title) — always Olive Chartreuse, always bold, always uppercase.

---

## 4. Spacing System

Base-8 scale for layout spacing (padding, margins, gaps). Expressed in pixels since these are structural/layout dimensions, not typographic sizes. Nav height is ~54px; hero sections run ~300–400px. Body content uses generous line-height (1.7) and ample white space to match the premium, consultancy-level positioning.

| Token | Value |
|---|---|
| xs | 4px |
| sm | 8px |
| md | 16px |
| lg | 24px |
| xl | 40px |
| 2xl | 54px |
| 3xl | 72px |
| 4xl | 96px |

---

## 5. UI Components

All components use Semantic Blue and Semantic Gray as the primary surfaces, with Burnt Orange for CTAs and Olive for active/kicker states. Corner radius is 3–6px — professional, not playful.

### Navigation Bar
- Semantic Blue (`#005A7D`) background, no bottom border rule.
- Logo stacked (mark above wordmark).
- Nav links in `rgba(255,255,255,0.55)`; active link in Olive.
- Right-aligned, filled Burnt Orange CTA button (e.g. "Get A Quote").
- Confirmed site nav pattern: Clients ▾ · Data-Centric ▾ · Services ▾ · Expertise ▾ · Resources ▾ · About Us ▾ · gist · [Get A Quote]

### Buttons
| Style | Fill | Text | Use |
|---|---|---|---|
| `btn-cta` | Burnt Orange | White | Primary call to action |
| `btn-blue` | Semantic Blue | White | Secondary action |
| `btn-outline` | Transparent, Semantic Blue border | Semantic Blue | Tertiary action |
| `btn-gray` | Semantic Gray | White | Low-emphasis action |
| `btn-link` | None (text only, underlined) | Link Blue | Inline text action |

Corner radius 3px throughout. There's also a confirmed inline "LINK" pattern (bold, uppercase, Olive Chartreuse, no underline) used next to client/case-study names — see Bullet List pattern below.

### Content Card
Structure: thin Semantic Blue top bar → body padding → **kicker** (Olive, e.g. "Case Study") → title (bold, dark) → body text → "Read More →" link in Link Blue.

### Pull Quote / Testimonial
Left border in Semantic Blue, Pale Teal background, italic light-weight quote text, with an all-caps attribution line in light gray below (e.g. "Chief Data Officer — Fortune 100 Financial Services").

### Stat Callouts
Warm Gold themed pills: large bold number (e.g. "10×", "25+", "100%") over a small label (e.g. "Faster initiatives"). Background is Warm Gold at 13% opacity with a matching border.

### Bullet List Pattern (Clients / Case Studies)
Confirmed site pattern: **Bold client name**, comma, descriptor, space, linked "LINK" in Link Blue. Standard bullet, no custom styling.

Example:
> **Amgen**, Data-Centric Architecture: LINK
> **Broadridge**, Legacy Understanding: LINK
> **Dun & Bradstreet**, Identity Resolution: LINK

---

## 6. Imagery / Visual Language

The confirmed hero imagery direction: a professional interacting with a glowing, holographic data-visualization — blue-tinted, futuristic, expert-centered.

**Use:**
- **Holographic / Data Interfaces** — blue-tinted, luminous data visualizations and knowledge graph representations.
- **Expert in Context** — professional engaging with technology, from behind or side-profile, conveying agency and mastery. Not posed.
- **Structured Architecture** — clean interconnected systems; order emerging from complexity. Reinforces "one elegant model" messaging.
- **Icon style** — line icons, 1.5–2px stroke, geometric and precise, in Semantic Blue or Olive. Avoid rounded "friendly" icon sets.

**Avoid:**
- Generic stock imagery — handshakes, lightbulbs, puzzle pieces, cheerful team photos. CDOs recognize and dismiss obvious stock imagery.
- Warm color casts — photography should trend cool (blue tones) to align with Semantic Blue and Semantic Gray. Warm-tinted photos feel off-brand.

---

## 7. Voice & Tone

From the True North Strategy: Semantic Arts speaks to CDOs who are frustrated that data initiatives are fragmented and reactive — "pushing a boulder uphill." The voice names that struggle with empathy, then offers the proven path out of it.

### Write Like This
- **Specific and empathetic:** "We know how overwhelming it can be to give your heart and soul to transforming data — and still feel like you're pushing a boulder uphill."
- **Bold and clear:** "One elegant data model can change everything."
- **Concrete outcomes:** "All new information-intensive initiatives — 10× easier."
- **Name the culprit directly:** "Application-centric thinking, pushed by self-serving vendors."
- **Lead with the promises:** "No Contract Bloat. No Change Orders. No Platform Lock-in."
- **Frame clients as heroes:** CDOs become "Data Masters."

### Avoid This
- Buzzword pile-up: "Leverage synergistic data ecosystems for transformational outcomes."
- Vague benefit claims: "We help you make better decisions with your data."
- Vendor bragging: "Industry-leading, best-in-class, cutting-edge."
- Passive or hedging language: "We can help you potentially improve data access."
- Consumer or startup tone: casual, emoji-heavy, hype-driven.
- Lock-in language: anything that implies dependency or long-term commitment.

### Four Voice Pillars
1. **Authoritative** — 100% specialized in data-centric transformation. Own that positioning. Speak with earned expertise — never arrogance, never hedging.
2. **Empathetic** — Name the CDO's frustration: fragmented initiatives, putting out fires, throwing good money after bad. Then offer the way through.
3. **Principled** — The three promises aren't fine print — they're brand identity: No Contract Bloat. No Change Orders. No Lock-in. Front and center.
4. **Clear** — Simplicity is literally the product. If a sentence needs a second read, rewrite it. The brand should embody what it sells.

---

*Semantic Arts Visual Style Guide · SA22 Standard · Version 3.1 — July 2026 · Palette: Option A — Ember & Olive*
*Semantic Blue `#005A7D` · Semantic Gray `#808080` · Burnt Orange `#C84A2B` · Olive Chartreuse `#8C9E38`*
*"One elegant data model can change everything."*
