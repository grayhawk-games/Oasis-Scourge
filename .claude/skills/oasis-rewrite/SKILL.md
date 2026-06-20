---
name: oasis-rewrite
description: Prose and documentation revision skill for the Oasis Scourge project. Use this skill whenever the user asks to review, score, edit, rewrite, improve, or critique any lore document, section, or paragraph in the Oasis Scourge world — including .Rmd files, culture writeups, overviews, land sections, marriage sections, or any world-building prose. Also use when the user asks "what would you change," "is this weak," "score this," "audit this," or "show me a diff." Trigger on any request involving Dusk Reed, Salt-Willow, FogWisps, Deyves, or any named Oasis Scourge culture, region, or faction.
---

## Rule Priority Order

When rules conflict, follow this order:

1. Rmd / file structure preservation
2. Canon preservation
3. User's direct instruction for the current task
4. Cultural voice
5. Clarity
6. Rhythm
7. Sentence-level style rules

## Core Rule

Every sentence must be understandable on first reading. A good sentence says something concrete. It has a subject, a verb, and a clear purpose. It should not sound like notes disguised as prose, a fantasy trailer, or a slogan chain.

## Core Workflow

1. Read the full document before proposing edits.
2. If the full document is not available, state exactly what portion was reviewed and limit all scoring and editing to that portion.
3. Score before editing. Never edit blind.
4. Change one section at a time.
5. Show a proposed diff before applying changes.
6. Stop after showing the diff. Apply the edit only after explicit approval.
7. Do not overwrite the original text unless instructed.

## Rmd Preservation

When editing an Rmd page, preserve the page structure unless the user explicitly asks for structural changes.

Keep the same headers, R code chunks, image paths, gallery structure, recap table structure, and column layout. Do not remove or rename sections unless the user asks.

When asked for a full Rmd rewrite, output a full Rmd file. When asked for a small fix, output only the corrected passage.

## Scoring Before Editing

Before revising a section, score it across these categories:

- Voice fit
- Clarity
- Specificity
- Rhythm
- Cultural distinction
- Canon consistency
- Redundancy control
- Reader interest

Give a short reason for each score. Then identify the highest-value edit target.

## Rating Scale

- Below 70: not usable
- 70–79: useful material, needs heavy revision
- 80–86: structurally usable, sentence-level problems remain
- 87–89: usable, needs only targeted cleanup
- 90+: strong — stop editing unless a specific canon issue remains

## Needs Work Threshold

Any section scoring below 85 overall is flagged as needing work. For each flagged section provide:

1. Why it scored lower
2. The single highest-impact improvement
3. The expected score after that improvement

Do not attempt to fix all flagged sections at once. Address one at a time and wait for approval between each.

When a section has five or more distinct prose problems, offer a full section rewrite rather than targeted patches. Targeted edits on a structurally broken section leave the structure broken.

## Audit Protocol

When asked to audit a page, do not give a vibes score first. Count failures.

Mark sentences that are unclear. Mark sentence fragments. Mark noun chains. Mark fake-poetic lines. Mark abstract slogans. Mark places where a reader would ask "what does that mean?" Mark places where canon is unclear or missing.

Also check for cross-section redundancy: if a custom, institution, or rule is fully described in more than one section of the same document, flag it. The duplicate belongs in the stronger section and should be removed or condensed in the weaker one.

Give the verdict only after counting the problems.

## Revision Philosophy

Use minimal intervention. Preserve the author's structure, cadence, names, cultural logic, sentence order, and implied meaning unless a change directly improves clarity, continuity, voice, specificity, or force.

Do not polish the prose into generic fantasy narration. Do not make the writing smoother if smoothness weakens the document's existing rhythm or cultural edge.

Do not rename cultures, places, factions, offices, gods, kinship terms, social systems, or regional concepts. If something appears inconsistent, flag it as a question instead of silently correcting it.

## Diff Format

For each proposed edit, show:

Original:
[original passage]

Revised:
[revised passage]

Reason:
[one sentence explaining the change: voice, clarity, continuity, specificity, redundancy, rhythm, or canon risk]

Do not bundle unrelated edits. One section means one coherent passage, subsection, or cultural entry.

## Prose Rules

Do not add sentence fragments for rhythm. If fragments already exist, preserve them unless they weaken clarity or clash with the surrounding register.

Avoid list-style description. Do not write "short, wiry, and narrow-handed" when the qualities can be earned through movement, work, tools, clothing, posture, or social behavior.

Avoid stacking more than two adjectives before a noun unless preserving an existing phrase, title, name, or deliberate formal construction.

Do not write sentences built around "X, Y, Z, and A." Do not stack nouns. Do not use list prose.

Important claims need behavioral, historical, environmental, or social context. Do not write "the marsh is dangerous" unless the prose shows why, to whom, and how that danger changes behavior.

Show character, culture, and belief through action, custom, object, speech, gesture, architecture, law, trade, or taboo before naming the trait directly.

Do not explain the theme. If the writing is working, trust the reader.

Do not add warmth, nobility, cruelty, humor, mysticism, or sentiment unless the surrounding document already supports it.

Do not use "shaped by" or "not merely" as filler. Do not write sentences that make an object do something unclear.

Never define a thing by what it is not. "It is not decoration" tells the reader nothing. State what something is and what it does. A negative construction ("it is not X," "this is not merely Y") is never the primary description of an object, custom, or person — only a positive statement earns that position.

## Required Sentence Test

Before finalizing any output, reread every paragraph and ask:

- Does each sentence mean something clear?
- Does each sentence have a subject and verb?
- Does the sentence explain a real relationship, action, custom, or consequence?
- Would a reader understand what is happening without already knowing the canon?
- Is the sentence trying to sound deep instead of saying something useful?
- Does the sentence hide a list inside commas?
- Does the sentence introduce a reference that is not explained?

If a sentence fails any of these, rewrite it.

## Bad and Better Examples

**Clothing**
Bad: Their clothing is made for roots, skiffs, nets, and sudden movement.
Better: Deyves wear close-fitted clothing so roots and nets do not catch them.

**Color**
Bad: Most clothing is dark green, brown, gray, or mud-red, because bright color makes a traveler easy to see in the mangrove channels.
Better: Most clothing stays dark, with subtle variation, because color carries far through the mangrove channels.

**Ornaments**
Bad: Bone charms, shell knots, teeth, and red cords are worn in ways outsiders often mistake for decoration.
Better: A Deyve may wear a bone charm at the throat. It is not decoration. It tells the household what was survived, owed, or warned against.

**Tools**
Bad: The knife is work tool and warning both.
Better: A Deyve keeps a knife close because the same blade may cut rope, clean fish, or warn a stranger to step back.

**Abstract slogan chain**
Bad: Patience became a weapon. Debt became a hook. Hospitality became a public claim.
Better: Deyves often wait before answering an insult. They remember who needed help, who gave it, and what was owed afterward. Even hospitality can create obligation if the household chooses to make it one.

**Physical description**
Too flat: Deyves are short and wiry.
Too fake: Deyves are short and wiry, built close to the ground the way a folk is when the ground has spent generations trying to swallow them.
Better: Deyves tend to be short and wiry, with the balance of folk who spend their lives stepping from plank to root to skiff without trusting any surface for long.

**Water and danger**
Bad: They watch still water because stillness may hide sickness, depth, or hunger.
Better: They watch still water because bad pools often look harmless at first. A pool without insects, ripples, or feeding fish may be poisoned, too deep to cross, or hiding something beneath the surface.

## Documentation Rules

Documentation may be clearer and more direct than fiction prose, but it should still preserve cultural voice.

Do not turn documentation into bullet-heavy encyclopedia prose unless the surrounding document already uses that format.

Do not use filler phrases, generic fantasy abstractions, or inflated summary language.

Prefer concrete social consequences: who does what, who benefits, who suffers, who refuses, who remembers, who pays, who leaves, who returns.

## Voice Rules

Match the register of the surrounding document.

Dusk Reed prose is spare and weighted. Do not add warmth, softness, communal affection, or comic movement unless already present in the source.

Salt-Willow prose has more movement, social texture, and humor. Do not flatten it into grim Dusk Reed severity.

Never make one culture sound like the other.

If a passage mixes cultural registers, identify the conflict before rewriting.

## Cultural Register Controls

For Dusk Reed:
- Keep sentences controlled and heavy.
- Prefer pressure, endurance, silence, debt, possession, survival, and consequence.
- Do not romanticize them. Do not soften domination into misunderstanding.
- Deyves are not generic swamp villains. They are households, children, elders, workers, fishers, poisoners, boat-menders, spouses, singers, and storytellers. Show ordinary life under pressure.
- Mention Salt-Willow only when the comparison is historically or geographically necessary. Deyves must stand on their own first.

For Salt-Willow:
- Preserve motion, improvisation, oral memory, neighborly friction, humor, and marsh practicality.
- Do not make them quaint. Do not make them purely innocent.
- Let humor come from behavior, not jokes pasted onto the prose.

## Project Vocabulary

Use "folk" not "people" throughout all Oasis Scourge documents. "People" is generic. "Folk" is the established register of the project and should appear wherever a generic term for persons is needed.

## Geography Check

Before writing any directional origin reference — "driven from the east," "came from the north," "displaced from further west" — verify the direction against the established canon map. Placing an origin in a direction that puts it off the map or into open sea is a canon error. Flag the geography as a question rather than inventing a direction.

## Anti-AI Style Rules

Do not use: "deeply rooted," "rich tapestry," "complex relationship," "harsh but beautiful," "proud people," "ancient traditions," "a land of contrasts," "shaped by," "not merely."

Do not summarize what the reader can infer.

Do not conclude sections with moral lessons.

Do not add dramatic final sentences unless the existing document is already building toward one.

Do not increase lyricism just because the subject is cultural, religious, tragic, or old.

## Final Check Danger Signs

Before finishing any rewrite, check for:

- A sentence that is only a noun phrase
- A sentence with four or more objects in a row
- A sentence that has rhythm but no clear meaning
- A sentence using "weapon," "hook," "claim," "shadow," or "memory" as a shortcut instead of explaining the actual custom
- A sentence that sounds like a trailer line
- A sentence that makes the reader ask why something is true
- A paragraph that lists facts but does not connect them
- A section that explains politics but forgets household life
- A section that explains culture but forgets geography
- A Deyve passage that could be copied into any generic swamp villain culture

If any of these appear, revise before output.

## Approval Rule

After showing the score and proposed diff, stop. Wait for approval before applying the edit.
