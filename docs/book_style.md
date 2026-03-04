# Book Style Guide

A style guide for the Rust tutorial series, modeled on O'Reilly Media technical
publication conventions. This is a living document — each section is added and
refined iteratively.

---

## 1. Typographic Conventions

This section defines how text is styled throughout the book. Consistent
typography helps readers instantly recognize what kind of information they are
looking at — a new term, a piece of code, a command to type, or a value they
need to substitute.

### 1.1 The Four Canonical Styles

Every O'Reilly technical book uses exactly four font treatments. Our Markdown
source maps them as follows:

| Style | Markdown | Use For | Example |
|---|---|---|---|
| Italic | `_text_` | New terms (first use only), emphasis, URLs, filenames, file extensions, paths | _ownership_, _borrowing_, _src/main.rs_ |
| Monospace | `` `text` `` | Code in running text: variable names, function names, types, keywords, operators, crate names in code context, error messages | `let`, `fn main()`, `Vec<T>`, `Option<T>` |
| Monospace bold | `**`text`**` | Commands or text the reader should type literally | **`cargo run`**, **`rustup update`** |
| Monospace italic | `_`text`_` | Placeholder values the reader must replace with their own | `grep _pattern_ _filename_` |

### 1.2 Rules and Rationale

**Italic for new terms, not bold.** The first time a technical term appears in
the text, set it in italic. All subsequent uses are in roman (normal) text.
This signals "here is a word you should pay attention to" without the visual
heaviness of bold.

> When a value is transferred from one variable to another, we say the first
> variable has _moved_ the value. From this point forward, the original
> variable is uninitialized.

**Bold is reserved.** Do not use bold for general emphasis. In the O'Reilly
house style, bold appears only as monospace bold to indicate literal text the
reader should type. If you need to stress a word, use italic.

**Monospace for all code elements.** Anything that appears in source code or a
terminal gets monospace: keywords (`fn`, `let`, `mut`, `match`), types
(`String`, `Result<T, E>`), trait names (`Display`, `Iterator`), function
calls (`println!()`), environment variables (`RUST_LOG`), and crate names when
used as code identifiers (`serde`, `tokio`).

**Monospace bold for user input.** When showing a command the reader should
execute, use monospace bold. This visually separates "things the computer
prints" from "things you type."

> Open a terminal and run **`cargo new hello_world`** to create a new project.

**Monospace italic for placeholders.** When a code-like value needs to be
replaced by the reader, use monospace italic. Always explain what the
placeholder represents.

> Connect to the database with **`cargo run -- --port _PORT_`**, where _`PORT`_
> is the port number your PostgreSQL instance is listening on.

### 1.3 Rust-Specific Typography

The following conventions apply specifically to Rust content:

| Element | Style | Example |
|---|---|---|
| Keywords | Monospace | `fn`, `let`, `mut`, `impl`, `trait`, `where`, `match`, `if let` |
| Primitive types | Monospace | `i32`, `u8`, `f64`, `bool`, `char`, `str`, `&str` |
| Standard library types | Monospace | `String`, `Vec<T>`, `HashMap<K, V>`, `Option<T>`, `Result<T, E>` |
| Trait names | Monospace | `Clone`, `Debug`, `Display`, `Iterator`, `From<T>` |
| Lifetime annotations | Monospace | `'a`, `'static` |
| Macros | Monospace, include `!` | `println!()`, `vec![]`, `assert_eq!()` |
| Crate names (in prose) | Roman (normal text) | The serde crate provides... |
| Crate names (as code identifiers) | Monospace | Add `serde` to your `Cargo.toml` |
| Compiler errors | Monospace | `error[E0382]: borrow of moved value` |
| File paths | Italic | _src/main.rs_, _Cargo.toml_, _.gitignore_ |
| CLI commands | Monospace bold | **`cargo build --release`** |

### 1.4 Common Mistakes to Avoid

- **Do not bold new terms.** Use italic: _ownership_, not **ownership**.
- **Do not italicize code.** A function name is `calculate_total`, not
  _calculate_total_.
- **Do not use monospace for crate names in prose.** Write "the tokio crate
  provides an async runtime," not "the `tokio` crate provides..." — unless you
  are referring to it as a code identifier (e.g., in a `use` statement or
  `Cargo.toml` dependency).
- **Do not mix emphasis styles.** A word is either italic for emphasis or
  monospace for code. Never both.
- **Do not use bold for emphasis in prose.** Italic is the house style for
  emphasis. Reserve bold exclusively for monospace bold user-typed commands.

### 1.5 Quick-Reference Decision Tree

When deciding how to style a piece of text, follow this order:

1. **Is it something the reader types literally?** → Monospace bold
2. **Is it a placeholder the reader substitutes?** → Monospace italic
3. **Does it appear in source code or terminal output?** → Monospace
4. **Is it a new technical term being introduced?** → Italic (first use only)
5. **Is it a filename, path, URL, or extension?** → Italic
6. **Do you want to emphasize a word?** → Italic
7. **None of the above?** → Roman (normal text)

---

## 2. Headings and Chapter Structure

Headings are the skeleton of the book. They define the table of contents, guide
the reader's navigation, and set expectations for what each section covers.
O'Reilly uses a four-level heading hierarchy with strict rules about
capitalization, sequencing, and what may (and may not) follow a heading.

### 2.1 Heading Hierarchy

O'Reilly's heading levels map to our Markdown source as follows:

| O'Reilly Name | Markdown | Purpose | Example |
|---|---|---|---|
| Chapter title | `#` | Top-level chapter heading | `# Ownership and Borrowing` |
| A-head | `##` | Major section within a chapter | `## The Rules of Ownership` |
| B-head | `###` | Subsection within an A-head | `### Move Semantics` |
| C-head | `####` | Sub-subsection within a B-head | `#### Moves in function calls` |
| D-head | _(run-in, see below)_ | Fine-grained division (rare) | **Partial moves.** The body text continues... |

**Depth guidelines.** Most chapters need only A-heads and B-heads. Use C-heads
sparingly — only when a B-head section genuinely contains multiple distinct
sub-topics. D-heads are exceptional; most O'Reilly books never use them.

**No level skipping.** A B-head (`###`) must be nested inside an A-head (`##`).
You cannot jump from an A-head directly to a C-head. If you find yourself
wanting a C-head without a surrounding B-head, reconsider your outline.

### 2.2 Capitalization Rules

Capitalization depends on heading level:

**A-heads and B-heads: Title Case**

Capitalize the first letter of every word, with these exceptions:

- Articles (`a`, `an`, `the`) are lowercase unless they are the first word.
- Coordinating conjunctions (`and`, `but`, `or`, `nor`, `for`, `yet`, `so`) are
  lowercase unless they are the first word.
- Prepositions of four letters or fewer (`in`, `on`, `at`, `by`, `to`, `for`,
  `from`, `with`, `into`) are lowercase — _unless_ they function as part of a
  phrasal verb. Example: "Set Up Your Environment" ("Up" is part of the verb
  "set up").
- Subordinating conjunctions (`as`, `if`, `so`, `yet`, `once`, `than`, `that`,
  `when`, `while`) are _always_ capitalized, even when four letters or fewer.
- Technical terms that are conventionally lowercase stay lowercase: `rustup`,
  `cargo`, `npm`, `git`.

Hyphenated words: capitalize both parts if the second word is a main content
word ("Big-Endian", "Type-Safe"), but only the first part if the second word is
minor ("Built-in").

**C-heads: Sentence case**

Capitalize only the first word, proper nouns, and the first word after a colon.
Code terms that are conventionally lowercase remain so even after a colon.

> `#### Moves in function calls`
>
> `#### When to use clone: a practical guide`

**D-heads: Sentence case, run-in, with a period**

A D-head is not a standalone heading line. It is bolded text at the start of a
paragraph, ending with a period, followed immediately by the body text:

> **Partial moves.** When a struct has multiple fields, Rust allows you to move
> individual fields out of the struct while leaving the rest in place.

### 2.3 No Inline Formatting in Headings

O'Reilly headings must not contain inline code font, bold, or italic formatting.
If a heading refers to a code element, spell it out in plain text:

| Wrong | Right |
|---|---|
| `## The \`Option<T>\` Type` | `## The Option Type` |
| `## Using \`match\` Expressions` | `## Using Match Expressions` |
| `### The \`impl\` Block` | `### The Impl Block` |

In the body text immediately following the heading, you can (and should) use the
proper monospace styling when you refer to the same element.

### 2.4 Chapter Opening Pattern

Every chapter must begin with one or more introductory paragraphs before the
first A-head. These paragraphs orient the reader: what the chapter covers, why
it matters, and how it connects to earlier material.

**Correct:**

```markdown
# Error Handling

Rust's approach to errors is unlike most languages you may have used. Rather
than exceptions, Rust uses the type system to make error conditions explicit.
This chapter introduces the two main error types — recoverable and
unrecoverable — and shows how to handle each one idiomatically.

## Unrecoverable Errors with panic!

When something goes catastrophically wrong...
```

**Wrong — heading immediately after heading:**

```markdown
# Error Handling

## Unrecoverable Errors with panic!

When something goes catastrophically wrong...
```

This rule applies at every level: an A-head must have body text before its first
B-head, and a B-head must have body text before its first C-head.

### 2.5 Chapter Closing Pattern

O'Reilly does not mandate a specific closing structure, but the following
pattern works well for tutorial-style content:

1. End the final technical section naturally.
2. Add a brief closing paragraph (under the last A-head, or as a standalone
   paragraph after it) that recaps the key ideas and bridges to the next
   chapter.

> You now know how ownership, borrowing, and lifetimes work together to
> guarantee memory safety at compile time. In the next chapter, we will put
> these concepts to work by building a small command-line tool that reads and
> transforms files.

A formal "Summary" A-head is optional. If used, it must be followed by body
text — the same anti-stacking rule applies.

### 2.6 The Anti-Stacking Rule

This is the single most important structural rule in O'Reilly style:

> **A heading must always be immediately followed by body text.**

Nothing else may appear between a heading and its first paragraph:

| After a heading... | Allowed? |
|---|---|
| Body paragraph | Yes |
| Another heading (any level) | No — add introductory text first |
| An admonition (Note, Tip, Warning) | No — add introductory text first |
| A code block | No — add a lead-in sentence first |
| A figure or table | No — add an in-text reference first |
| A sidebar | No — add introductory text first |

Similarly, do not stack two admonitions back-to-back, or place a sidebar
immediately after an admonition. Interleave body text between block-level
elements.

### 2.7 Section Numbering

**Headings are not numbered.** O'Reilly books do not use "1.1", "1.2.3"-style
numbering on section headings. Sections are identified by title alone.

**Chapters are numbered** in the final rendered book, but this numbering is
generated automatically by the production toolchain. In our Markdown source, do
not manually type chapter numbers.

> Write `# Ownership and Borrowing`, not `# Chapter 3: Ownership and Borrowing`.

Figures, tables, and examples _are_ numbered using a chapter-sequence format
(e.g., Figure 3-1, Table 5-2). This is covered in a later section of this
guide.

### 2.8 Heading Phrasing Guidelines

- **Be substantive.** Every heading should make sense in isolation when read in a
  table of contents. Avoid vague titles like "Introduction" or "Background" for
  A-heads — prefer descriptive titles like "Why Ownership Matters."
- **Prefer noun or gerund phrases.** "Error Handling", "Setting Up the
  Environment", "The Request Lifecycle." Questions and imperatives are acceptable
  in tutorial-style chapters: "How Does the Borrow Checker Work?"
- **Do not duplicate parent headings.** A B-head under "## Error Handling" should
  not be titled "### Error Handling Details." Differentiate clearly.
- **Keep headings concise.** There is no official character limit, but headings
  that exceed one line in the rendered book will wrap awkwardly. Aim for under
  eight words.
- **Expand acronyms** unless universally known to the target audience. Use the
  expanded form in the body text on first mention, not in the heading itself.
