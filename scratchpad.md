# Scratchpad

Working notes and action items for the next iteration.

---

## Part 1: First Contact

### 1.1 Your First Rust Program — DRAFT COMPLETE
- Covers: philosophy (safety + speed), rustup install, `cargo new`, Cargo.toml anatomy, `fn main`, `println!` with `{}`, `{variable}`, `{:?}`, `{:#?}`
- Edition 2024 context: `cargo new` defaults to edition 2024 since Rust 1.85.0 (Feb 2025)
- Current stable Rust: 1.93.1 (Feb 2026)
- **Review items:**
  - Verify tone is accessible to true beginners (no assumed systems programming background)
  - Consider adding a "what you'll need" prereqs note (terminal, text editor)
  - The `version = 1.85` float example is slightly misleading (Rust versions aren't floats) — consider changing to a more natural float example

### 1.2 The Compiler Is Your Ally — DRAFT COMPLETE
- Covers: error anatomy (E0382, E0308, unused variable warning), `cargo check` as fast feedback, `cargo clippy` with needless_range_loop and bool_comparison examples, `cargo fmt` with before/after, quality baseline workflow
- Philosophy: compiler as code reviewer, not gatekeeper; trust it instead of fighting it
- Rust 2024 note: `cargo fmt` auto-applies 2024 style edition (17 formatting fixes) when edition = "2024"
- Clippy and rustfmt are bundled in the default rustup profile — no extra install needed
- **Review items:**
  - Verify E0382 error output matches current compiler (Rust 1.93+) — minor formatting may differ
  - The "version = 1.85" example from 1.1 is referenced indirectly via minimum Rust version — keep consistent
  - Consider whether the clippy `needless_range_loop` example is too advanced for Ch 1 (uses `vec!` macro not yet explained) — current approach: show it, trust the reader to follow the intent
  - The chapter intentionally teases ownership ("you do not need to understand ownership yet") — verify this forward reference feels natural, not frustrating

## Part 2: Thinking in Values

### 2.1 Variables, Expressions, and Control Flow — DRAFT COMPLETE
- Covers: immutability by default (philosophy), `let`/`mut`, shadowing (including type changes), scalar types (integers/floats/bool/char), type inference defaults (i32, f64), type annotations, constants (`const`), expression-oriented design (if/blocks as expressions), control flow (if/else, loop with break-value, while, for with ranges), loop labels, tuples and arrays at a glance, `if let` intro, let chains (Rust 2024)
- Philosophy: immutability is a feature not a limitation; expressions produce values everywhere
- Rust 2024 features: let chains in `if` and `while` conditions (stabilized in Rust 1.88.0, edition-gated to 2024)
- All 26 code examples verified to compile and produce documented output (Rust 1.93+)
- Introduced `if let` and `Result` just enough for let chains — explained self-contained, no forward references
- **Review items:**
  - Verify the `if let` / `Result` mini-intro is sufficient for beginners who haven't seen enums yet — it needs to "just work" without deeper understanding
  - The compound types section (tuples, arrays) is brief by design — consider if `Vec<T>` forward reference ("covered in a later part") is acceptable or needs rewording
  - Integer overflow behavior (debug panic vs release wrap) was deliberately omitted to avoid overload — may add as a tip/note in review pass
  - Consider adding a note about `usize` being required for array indexing — currently mentioned but could be demonstrated
  - The `while let` chain example uses array indexing (`values[index]`) which is less idiomatic than iterator-based approaches — acceptable here since iterators aren't introduced yet

### 2.2 Functions and Closures — DRAFT COMPLETE
- Covers: function definitions (params, return types), implicit last-expression return, early return with `return`, expression-oriented function bodies, closures (syntax, type inference, capture by reference/mutable reference), Fn/FnMut/FnOnce trait hierarchy (conceptual), higher-order functions (`impl Fn` in argument position), passing named functions, choosing the right trait bound, returning closures (`impl Fn` in return position), function factories, `move` keyword (intro only)
- Philosophy: functions as primary abstraction unit; expression-oriented design makes bodies concise; closures "close over" environment
- All 14 code examples verified to compile and produce documented output (Rust 1.93+, edition 2024)
- Introduced `Option` just enough for early return example — self-contained, no forward reference
- Introduced `&str` as "read-only view of text" — enough to use, details deferred to borrowing chapter
- Introduced `'static` lifetime annotation briefly for string literals — minimal explanation, no deep dive
- Deliberately omitted: async closures (too advanced, covered in Part 6), `Box<dyn Fn>` (needs heap/trait objects from Part 4), full `move` semantics (needs ownership from 2.3)
- **Review items:**
  - The `apply_to_each` example uses a fixed-size `[i32; 3]` return — slightly artificial; acceptable since `Vec` hasn't been introduced
  - The `&'static str` in `classify` and `make_greeter` is explained minimally — verify this doesn't confuse readers who haven't seen lifetimes
  - `String::from("hello")` appears in the `FnOnce` example — briefly demonstrates owned strings; may need forward-ref check against 2.3
  - The `move` keyword is introduced with a light touch ("forces ownership") — full explanation deferred to 2.3 (ownership)
  - Consider whether the Fn trait hierarchy section is too abstract for beginners — it's conceptual and short, but could be trimmed further

### 2.3 Ownership — DRAFT COMPLETE
- Covers: three rules of ownership, stack vs heap mental model (with ASCII diagram), move semantics (assignment, function calls, return values), E0382 error example, Copy types (full list), Clone (explicit deep copy), Drop trait and RAII, drop order (reverse declaration order with Noisy struct demo), early drop with `std::mem::drop` (including its trivial implementation), comprehensive "ownership in action" capstone example
- Philosophy: ownership as the third path between GC and manual memory — compiler checks, zero runtime cost; ownership is not a restriction but a system that eliminates bugs
- All 12 code examples verified to compile and produce documented output (Rust 1.93+, edition 2024)
- No Rust 2024-specific changes to ownership model itself; tail expression temporary scope change (RFC 3606) is relevant to Drop order but too advanced for this chapter — covered implicitly by teaching correct patterns
- Builds on 2.2: functions transfer/return ownership, `move` keyword from 2.2 gets context here
- Introduced `struct` and `impl Drop` minimally for the drop order example — self-contained, no forward reference needed
- **Review items:**
  - The `move` keyword from 2.2 is not explicitly re-explained here — verify the 2.2→2.3 connection is clear enough; consider adding a brief callback
  - The ASCII diagrams (stack/heap, double-pointer) are important for understanding — verify they render well in target format
  - The `Noisy` struct example introduces `struct`, `impl`, and trait implementation before Part 3 — minimal and self-contained, but verify it doesn't confuse readers
  - Consider adding a note about `String::from` vs string literals — currently shown but not explicitly contrasted (`&str` vs `String` distinction)
  - The "Why This Matters" section lists data races as prevented by ownership — technically ownership + borrowing together; verify this claim is precise enough
  - No mention of partial moves — deliberately omitted for simplicity; will be relevant in Part 3 (structs)

### 2.4 Borrowing and References — DRAFT COMPLETE
- Covers: shared references (`&T`), mutable references (`&mut T`), the many-readers-or-one-writer rule, Non-Lexical Lifetimes (NLL), borrow checker error anatomy (E0596, E0499, E0502, E0106), string slices (`&str` vs `&String`), array/vector slices (`&[T]`), dangling references, lifetime annotations (`'a`), lifetime elision, practical patterns (separate reads/writes, index-based mutation, narrow scopes)
- Philosophy: borrowing is what makes ownership practical — use without owning; borrow checker is a tool, not an obstacle
- All 14 compilable code examples verified (Rust 1.93+, edition 2024); 5 does_not_compile examples verified with exact error messages
- No Rust 2024-specific changes to core borrowing/reference mechanics; NLL has been stable since Rust 2018 edition; match ergonomics 2024 changes exist but are too advanced for this chapter
- Builds on 2.3: opens with the ownership-only pain point (tuple return pattern), introduces `&` as the solution
- Introduced `vec![]` macro minimally for borrow checker examples — used without explanation, context makes intent clear
- Introduced `iter().max().unwrap()` and `*` dereference briefly in practical patterns — minimal, self-contained
- **Review items:**
  - Verify the `vec![]` usage doesn't confuse readers who haven't formally seen it (it appeared in 1.2 clippy example)
  - The `first_word` function uses `s.bytes().enumerate()` and byte literal `b' '` — verify this is approachable for beginners
  - The lifetime annotation section uses `longer` function — classic example, but verify the nested scope example doesn't feel contrived
  - The `*scores.iter().max().unwrap()` pattern in "Separate Your Reads and Writes" may be too dense — consider if it needs more explanation
  - No mention of reborrowing — deliberately omitted for simplicity
  - No mention of `Deref` coercion beyond the `&String` → `&str` auto-conversion — details deferred to Part 4 (Traits)
  - Consider whether the "Working With the Borrow Checker" section should come before or after the dangling references section

### Part 3 — NEXT UP
- 3.1 Structs and Methods: build on ownership + borrowing; `&self`, `&mut self`, `self` method receivers map directly to the borrowing concepts from 2.4
- The chapter closer in 2.4 bridges to structs: "choosing when methods should read, modify, or consume the values they operate on"

## Rust 2024 Features Tracker (for future chapters)

- Async closures (`async || {}`) + `AsyncFn`/`AsyncFnMut`/`AsyncFnOnce` traits — stabilized Rust 1.85.0, all editions — cover in Part 6 (Concurrency)
- RPIT lifetime capture rules changed in 2024 edition (all lifetimes captured by default) — cover in Part 4 (Generics)
- `use<>` precise capturing syntax — stabilized Rust 1.82.0 (bare fns), Rust 1.88.0 (trait return position) — cover in Part 4 (Generics)

## General Notes

- All code must target `edition = "2024"` (Rust 1.85+)
- Follow O'Reilly style guide in docs/book_style.md strictly
- Philosophy first, then syntax — every chapter opens with WHY
- Show behavior first, name it second
- No "we'll cover this later" — if it appears, explain enough to use NOW
- Reserved keyword `gen` in 2024 — warn readers if relevant
- Let chains stabilized in Rust 1.88.0 (June 2025), edition-gated to 2024
- Range types gained `Copy` in Rust 2024 edition (via `IntoIterator` instead of `Iterator`) — note when relevant
