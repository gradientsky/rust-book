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

### 3.1 Structs and Methods — DRAFT COMPLETE
- Covers: struct definition (named fields), field init shorthand, mutation (whole-struct mutability), struct update syntax with move semantics, tuple structs (newtype pattern intro), unit structs, methods with `impl` blocks, three method receivers (`&self`/`&mut self`/`self`), methods with extra parameters, associated functions (no `self`), `new` convention, `#[derive(Debug)]` for `{:?}` and `{:#?}`, `Display` trait manual implementation for `{}`, structs and ownership (move vs borrow), capstone `Task` example demonstrating all concepts
- Philosophy: structs are not just data containers — combined with `impl` blocks they form types with clear interfaces; method receiver declares the contract; self-documenting APIs
- All 18 code examples verified to compile and produce documented output (Rust 1.93+, edition 2024); 1 does_not_compile example (E0277) verified with exact error message
- Builds on 2.3 (ownership) and 2.4 (borrowing): method receivers directly map to `&T`, `&mut T`, and owned `T`; struct update syntax demonstrates move semantics; `into_` prefix convention introduced
- `std::fmt` imported for Display — first `use` statement in the book; explained minimally as "bring the formatting module into scope"
- `derive` concept introduced with Debug — explained as "compiler generates the implementation based on your fields"; mentioned other derivable traits (Clone, PartialEq, Default) as preview
- No Rust 2024-specific changes to struct/impl syntax; match ergonomics changes affect destructuring but deferred to 3.2
- `std::fmt::from_fn` (stabilized 1.93) deliberately omitted — too advanced for intro chapter, better suited for Part 4 or Part 7
- **Review items:**
  - Verify the `use std::fmt` introduction doesn't confuse readers — modules/`use` are formally covered in 5.3
  - The `Formatter<'_>` lifetime syntax in Display impl uses `'_` (anonymous lifetime) — verify this is approachable before lifetimes are fully covered; context from 2.4 should be sufficient
  - Struct update syntax example produces a warning about unused `name` field — acceptable for single-file snippet
  - The `into_` prefix naming convention is introduced here — verify it feels natural or needs more explanation
  - Consider whether tuple struct section needs more motivation (newtype pattern is revisited in Part 7)
  - Unit structs are explained briefly — verify the "type-level markers" forward reference to Part 4 feels natural

### 3.2 Enums and Pattern Matching — DRAFT COMPLETE
- Covers: enum definition (simple variants, data-carrying variants, named-field variants), exhaustive `match` with E0004 error, match as expression, wildcard `_` catch-all, or patterns (`|`), `if let` / `if let else`, let chains (Rust 2024 with `&&`), destructuring (enums, structs, tuples, nested), match guards (`if condition`), `..` ignore pattern for structs, `Box<Expr>` for recursive types (brief), `matches!` macro, capstone `Ticket` system example with nested pattern matching and Display impl
- Philosophy: enums model alternatives where strings/integers/booleans fail; exhaustive matching turns runtime bugs into compile-time errors; the type system guarantees every case is handled
- All 16 compilable code examples verified (Rust 1.93+, edition 2024); 1 does_not_compile example (E0004) verified with exact error message
- Builds on 3.1: struct destructuring in match, `Display` impl on enums, `use std::fmt`
- Builds on 2.1: let chains revisited with enum patterns (first introduced in 2.1 with `Result`)
- Introduced `Box<T>` minimally for recursive `Expr` type — explained as "heap-allocated pointer" with forward reference to Part 5
- Introduced `vec![]` for capstone example — used without deep explanation (appeared in 1.2, 2.4)
- Introduced `matches!` macro briefly — explained as "returns true/false for pattern check"
- Introduced `std::mem::discriminant` for catch-all variable binding example
- Rust 2024 features used: let chains (`if let ... && condition`); match ergonomics 2024 changes exist but too advanced for this chapter
- Deliberately omitted: `@` bindings (too advanced, better for Part 7), `ref`/`ref mut` patterns (match ergonomics handles this), range patterns in match (not enum-specific), `#[non_exhaustive]` (library design concept for Part 5), slice patterns (covered in Part 5 with collections)
- **Review items:**
  - The `std::mem::discriminant` example output shows `Discriminant(1)` — verify this is stable output format or consider simplifying to just a debug print
  - The `Box<Expr>` example may be too advanced — it introduces heap allocation before Part 5; current approach: minimal explanation, forward reference
  - Verify the `matches!` macro intro is sufficient — it appears in the capstone without prior dedicated explanation
  - The capstone example uses `vec![]` which hasn't been formally introduced — acceptable given prior appearances
  - Consider whether the `if let else` chain example (Discount) should note that `match` is preferred for exhaustiveness
  - The or-pattern example (`Day::Saturday | Day::Sunday`) could note that `matches!` is even more concise for boolean returns

### 3.3 Null, Errors, and the Type System — DRAFT COMPLETE
- Covers: `Option<T>` (Some/None, unwrap_or, unwrap_or_else, map, and_then, is_some_and, is_none_or), `Result<T, E>` (Ok/Err, unwrap_or, map, map_err), `?` operator (with Result and Option), Option↔Result conversion (ok_or, ok), unwrap/expect guidance, making illegal states unrepresentable (enum replacing boolean flags, newtype wrappers for type safety, validated construction with Result), capstone Score/grade example combining all concepts
- Philosophy: invisible trapdoors (null, exceptions) vs explicit types; if a function can fail its signature must say so; billion-dollar mistake; type system as map of where things can go wrong
- All 19 compilable code examples verified (Rust 1.93+, edition 2024); 1 does_not_compile example (E0369) verified with exact error message
- No Rust 2024-specific changes to Option/Result/`?` operator semantics; `is_none_or` stabilized 1.82, `is_some_and`/`is_ok_and` stabilized 1.70 — all pre-2024 but modern idioms
- Builds on 3.2: bridges from "two enums built into the standard library" closing; uses pattern matching, exhaustive match, if let
- Builds on 3.1: uses struct definition, impl blocks, Display trait, use std::fmt
- Introduced `filter_map` minimally in capstone — explained by context (filter + map on iterators)
- Introduced `.parse::<T>()` turbofish syntax — used throughout, explained as "parse into type T"
- Introduced range patterns in match (`90..=100`) — used in Score::grade, natural extension of match
- Deliberately omitted: custom error types with From impl (Part 5), thiserror/anyhow (Part 5), try blocks (nightly-only), Result::flatten (too advanced for intro), inspect/inspect_err (better for Part 5 error handling chapter)
- **Review items:**
  - The `HOME` env var example in expect section is platform-specific — works on macOS/Linux, not Windows; acceptable for pocket book target audience
  - The `ParseIntError { kind: InvalidDigit }` debug output format may change in future Rust versions — consider whether to use Display format instead
  - The `filter_map` in capstone uses iterator chain (`.iter().filter_map(...).collect()`) — verify this is approachable before iterators are formally covered in Part 4
  - Generics `<T>` are mentioned in Option/Result definitions but explained only as "placeholder for any type" — verify this is sufficient pre-Part 4
  - The newtype section is brief — fuller treatment with `Deref` and trait implementations deferred to Part 7
  - Consider whether the "making illegal states unrepresentable" section needs a note about module privacy for enforcing validated construction (modules covered in 5.3)

### 4.1 Traits — DRAFT COMPLETE
- Covers: trait definition (required methods), implementing traits (`impl Trait for Type`), default methods, traits as parameters (`&impl Trait`), derive macros (Debug, Clone, Copy, PartialEq, Eq, Hash, Default, PartialOrd, Ord), Default trait with struct update syntax, Debug vs Display, From/Into (infallible conversions, `impl Into<String>` parameter pattern), TryFrom/TryInto (fallible conversions with associated Error type), AsRef (cheap reference conversions), implementing multiple traits, operator overloading (Add trait, associated Output type), orphan rule, capstone Celsius/Fahrenheit temperature example
- Philosophy: shared behavior without inheritance — "can-do" relationships instead of "is-a"; traits are flat, composable, and independent
- All 14 code examples verified to compile and produce documented output (Rust 1.93+, edition 2024)
- No Rust 2024-specific changes to core trait syntax; "dyn compatible" replaces "object safe" terminology (1.85+); trait upcasting stable in 1.86 — both deferred to 4.2 (Generics) since dyn Trait is covered there
- Builds on 3.3: closing paragraph bridges to traits; validated construction pattern from 3.3 revisited as TryFrom
- Builds on 3.1: impl blocks, Display trait, use std::fmt — now generalized
- Builds on 2.3: move/copy semantics relevant to derived Copy/Clone
- Introduced associated types minimally (`type Output`, `type Error`) — fuller treatment in 4.2 (Generics)
- Introduced `std::ops::Add` for operator overloading — other operator traits mentioned but not demonstrated
- `AsMut` deliberately omitted — `AsRef` is more common and sufficient for intro; `AsMut` can be covered in Part 5 or Part 7
- **Review items:**
  - Verify the `impl Trait` in parameter position is sufficient intro before full generics in 4.2
  - The associated type explanation ("a type that is part of the trait's contract") is minimal — verify it bridges cleanly to 4.2 where generics vs associated types are contrasted
  - The orphan rule explanation is brief — verify it's sufficient; newtype workaround mentioned but not demonstrated (covered in 3.3 and Part 7)
  - The `content` field warning in example 1 (unused field) is acceptable for snippet
  - Consider whether the `AsRef` example using byte values is too low-level — it demonstrates the concept well but byte arrays may be unfamiliar to beginners
  - The capstone uses `Copy` derive on newtypes — verify readers understand this from 2.3

### 4.2 Generics — DRAFT COMPLETE
- Covers: generic functions (single/multiple params), trait bounds (`T: Trait`, `T: Trait1 + Trait2`), `impl Trait` (argument position as sugar, return position for unnameable types), `where` clauses (readability + advanced bounds), generic structs (Pair, KeyValue), generic enums (Tree with Box), `impl Trait` in return position, Rust 2024 RPIT lifetime capture rule, associated types vs type parameters (one-to-one vs one-to-many), trait objects (`dyn Trait`), dyn compatibility rules (with `where Self: Sized` escape hatch), monomorphization and zero-cost abstraction, capstone Measurable example with static + dynamic dispatch
- Philosophy: generics answer "how do you write reusable code without giving up performance and safety?"; Rust answers at compile time via monomorphization; zero-cost = abstraction vanishes in compiled binary
- All 15 compilable code examples verified (Rust 1.93+, edition 2024); 1 does_not_compile example (E0369) verified with exact error message
- Rust 2024 features: RPIT lifetime capture rules (all in-scope lifetimes captured by default); mentioned but not demonstrated: `use<>` precise capturing syntax (too advanced for intro; covered implicitly by the 2024 default behavior)
- Builds on 4.1: `impl Trait` in parameter position from 4.1 now explained as syntactic sugar for generics; associated types (`type Output`, `type Error`) from 4.1 now contrasted with type parameters
- Builds on 3.2: `Box<T>` for recursive types referenced again in generic Tree enum
- Builds on 2.4: borrowing/references used in method signatures; lifetime concept underlies RPIT 2024 rule
- "dyn compatible" terminology used throughout (replaces "object safe" per Rust 1.86+)
- Trait upcasting (1.86) deliberately omitted — too advanced for intro chapter, better for Part 7
- `use<>` precise capturing syntax deliberately omitted from examples — the 2024 default behavior is the simpler and more common case; `use<>` is for edge cases better covered in advanced material
- **Review items:**
  - The `where (T, T): Debug` example is unusual but demonstrates non-parameter bounds; verify it does not confuse beginners
  - The RPIT 2024 lifetime rule section is brief — verify it adequately explains why it matters without overloading; consider if a contrasting "this wouldn't work in 2021" note would help or hurt
  - The associated types example uses `Summarize<Summary = String>` constraint — verify this notation is clear without prior exposure
  - The `Vec<Box<dyn Describe>>` pattern introduces heap allocation with `Box` before Part 5 — context from 3.2 (`Box<Expr>`) should be sufficient
  - The dyn compatibility rules are simplified — full rules include no associated constants, no GATs, etc.; current level of detail is appropriate for intro
  - The `clone_self` example in dyn compatibility generates an unused method warning — acceptable for teaching snippet
  - Consider whether `impl Trait` same-type vs different-type distinction needs a code example showing the difference (currently prose-only)

### 4.3 Iterators and Functional Patterns — DRAFT COMPLETE
- Covers: Iterator trait (`next`, `Item`), three iteration modes (iter/iter_mut/into_iter), for-loop desugaring, lazy evaluation, adaptors (map, filter, filter_map, enumerate, zip, take, skip, flatten, flat_map, chain, inspect), consumers (collect, fold, sum, product, count, any, all, find, position, min, max, min_by_key, max_by_key), collecting into Vec/String/HashMap/HashSet/Result, ranges as iterators, std::iter constructors (repeat_n, once, from_fn, successors), implementing Iterator for custom types (Countdown), IntoIterator for custom collections (Playlist), `is_sorted_by_key` (stable 1.82)
- Philosophy: iterators eliminate the trade-off between readable high-level code and fast execution; lazy evaluation enables compiler to fuse pipeline into single loop; zero-cost abstraction applied to data processing
- All 27 code examples verified to compile and produce documented output (Rust 1.93+, edition 2024)
- No Rust 2024-specific changes to core iterator trait; `IntoIterator for Box<[T]>` is edition-gated but not demonstrated (too niche for intro); `gen` keyword reserved in 2024 for future gen blocks (nightly-only); `is_sorted`/`is_sorted_by_key` stable since 1.82; `repeat_n` stable since 1.82
- Builds on 4.2: closing paragraph bridges from generics to iterators; `impl Iterator` return type pattern from 4.2 revisited
- Builds on 4.1: `Iterator` is the key trait; `IntoIterator` and `FromIterator` are standard library traits
- Builds on 3.3: `Option` and `Result` used in `next()`, `find()`, `collect::<Result<Vec<_>,_>>()`; `filter_map` with `.ok()`
- Builds on 2.3/2.4: three iteration modes mirror ownership model (borrow, mutable borrow, owned)
- Introduced `HashMap` minimally for collect examples — used without deep explanation (covered in Part 5)
- Introduced `HashSet` minimally for collect examples — same
- Deliberately omitted: `Iterator::array_chunks` (nightly-only), `Iterator::map_windows` (nightly-only), `gen` blocks (nightly-only), `IntoIterator for Box<[T]>` 2024 behavior change (too niche), `try_fold`/`ControlFlow` (advanced), `Extend` trait (Part 5), `ExactSizeIterator`/`DoubleEndedIterator` (advanced traits better for Part 7), `iter::chain` free function (1.91, not needed when method form exists)
- **Review items:**
  - The `&&n` pattern in `filter` examples may confuse beginners — explained inline but could use more emphasis
  - The `HashMap` output ordering is non-deterministic; capstone sorts keys for deterministic output — verify this doesn't add confusion
  - The `collect::<Result<Vec<_>,_>>` pattern is powerful but dense — verify the explanation is sufficient for readers who haven't seen advanced generics
  - `repeat_n` (1.82) used instead of `repeat().take()` — modern idiom but less commonly seen in older tutorials
  - The `IntoIterator` custom impl delegates to `Vec::into_iter` — simple approach; more complex custom IntoIter structs deferred
  - Consider whether the `inspect` stderr example output is confusing (interleaved output from lazy evaluation)
  - The capstone uses `partial_cmp(&b).unwrap()` for f64 comparison — could note that f64 is `PartialOrd` not `Ord`

### 5.1 Error Handling in Practice — DRAFT COMPLETE
- Covers: `Error` trait (Debug+Display, `source()` for error chains), manual error chain walking, thiserror 2.x (`#[error("...")]` for Display, `#[from]` for From+source, `#[source]` for source-only, `#[error(transparent)]` for delegation), anyhow 1.x (`anyhow::Result<T>`, `.context()`/`.with_context()`, `bail!`/`ensure!`/`anyhow!` macros, `.chain()` for walking), `?` operator `From::from()` conversion mechanism, library vs application error strategy (thiserror for libs, anyhow for apps), unwrap spectrum (`?` > `unwrap_or` > `expect` > `unwrap`), capstone Inventory example with typed errors and `Box<dyn Error>`
- Philosophy: error handling is about communicating what went wrong clearly enough to fix it; typed errors for programmatic consumers, context chains for human readers; two-crate pattern respects both audiences
- All 11 code examples verified to compile and produce documented output (Rust 1.93+, edition 2024)
- thiserror 2.0.18 (latest as of Feb 2026): breaking changes from 1.x include raw identifier format string removal, direct dependency requirement, no_std support; `#[from]` implies `#[source]`
- anyhow 1.0.102 (latest as of Feb 2026): stable 1.x series, no breaking changes; `Context` trait for `.context()`/`.with_context()`
- `core::error::Error` stabilized in Rust 1.81 (Sep 2024) — mentioned conceptually but not demonstrated (no_std is out of scope for this chapter)
- Builds on 3.3: `Result`, `Option`, `?` operator, custom error enums with Display
- Builds on 4.1: `From` trait for error conversion, trait implementation patterns
- Deliberately omitted: `try` blocks (nightly-only), `Error::provide()` (nightly-only), `Error::sources()` iterator (nightly-only), snafu crate (thiserror is the community standard), backtrace capture (nightly `provide()` required), `#[diagnostic::do_not_recommend]` (too advanced)
- **Review items:**
  - The capstone uses `Box<dyn std::error::Error>` instead of `anyhow::Result` to avoid requiring anyhow dependency — verify this substitution is clear enough; noted in prose that anyhow has the same effect
  - thiserror and anyhow are shown with `Cargo.toml` snippets but examples are self-contained (no actual file I/O beyond `read_config` which hits a missing file) — verify all examples work in a single-file context
  - The `#[error(transparent)]` example uses `Box<dyn Error + Send + Sync>` — verify readers understand `Send + Sync` or if this needs a forward reference note to Part 6
  - The "How the Question Mark Converts Errors" section shows `rust,ignore` pseudo-code — verify this is acceptable for non-compilable expansion examples
  - Error message convention (lowercase, no trailing punctuation) is stated but not heavily enforced in all examples — consistent enough for teaching purposes
  - The `HOME` env var in expect example is platform-specific (macOS/Linux) — same caveat as 3.3

### 5.2 Collections, Strings, and Smart Pointers — DRAFT COMPLETE
- Covers: Vec (creation with vec!/Vec::new/with_capacity/collect, access with []/get/last, modify with push/pop/insert/remove/retain, slices &[T], three iteration modes), HashMap (new/from/collect, get/indexing/contains_key, entry API with or_insert/or_insert_with), HashSet (insert/contains, intersection/union/difference), String vs &str (owned vs borrowed, deref coercion, when to use each, creation/conversion/concatenation/format!, common operations, UTF-8 guarantees), Box (recursive types Expr tree, trait objects Vec<Box<dyn Shape>>), Rc (reference counting, Rc::clone convention, shared ownership in graph-like structures, limitations: not thread-safe, immutable), Arc (thread-safe shared ownership, thread::spawn example), choosing the right pointer (decision table), capstone Library/Document tag system with Vec/HashMap/HashSet/Rc/String/Display
- Philosophy: ownership extends into data structures; collections own their elements; smart pointers extend the ownership model when simple ownership doesn't fit
- All 20 code examples verified to compile and produce documented output (Rust 1.93+, edition 2024)
- No Rust 2024-specific changes to core collection/string/smart pointer types; `IntoIterator for Box<[T]>` is 2024 edition-gated but not demonstrated (too niche); `HashMap::from([...])` stable since 1.56 but modern idiomatic pattern
- Builds on 5.1: bridge from error handling to data structures
- Builds on 4.3: iteration modes (iter/iter_mut/into_iter), collect patterns
- Builds on 4.2: trait objects (dyn Trait), Box<dyn Trait>
- Builds on 2.3/2.4: ownership, borrowing, slices (&[T], &str)
- Introduced `thread::spawn` minimally in Arc example — just enough to demonstrate thread-safe sharing; full concurrency in Part 6
- Deliberately omitted: BTreeMap/BTreeSet (mentioned as alternative), VecDeque/LinkedList (too niche), Cow<str> (advanced), RefCell/Cell (interior mutability pattern, too advanced for intro), Weak<T> (Rc cycles, advanced), LazyCell/LazyLock (better for Part 6/7), slice patterns, Extend trait, drain/retain_mut, Vec::from_raw_parts
- **Review items:**
  - HashMap/HashSet output order is non-deterministic; documented with "(key order may vary)" and sorted outputs where needed
  - The `&&str` type in `indexed: HashMap<usize, &&str>` may confuse beginners — acceptable for showing collect patterns but could use more explanation
  - The capstone uses `Rc` for shared document references in a tag index — verify this feels motivated rather than contrived
  - The `+` operator on strings (moves left, borrows right) asymmetry is mentioned — verify explanation is clear enough
  - UTF-8 byte slicing panic behavior is warned about but no does_not_compile example is shown — deliberate choice to avoid panic output
  - `RefCell` is mentioned as "advanced pattern" but not demonstrated — verify this forward reference feels natural
  - Consider whether `BTreeMap` deserves more than a one-sentence mention
  - The `has_tag` method was removed from capstone to avoid unused warning — verify the HashSet::contains mention in the recap is sufficient

### 5.3 Modules and Project Structure — DRAFT COMPLETE
- Covers: `mod`/`use`/`pub`, visibility spectrum (private default, `pub(crate)`, `pub(super)`, `pub`), struct field visibility with invariant protection, re-exports (`pub use`), grouped imports (`use std::io::{self, Write}`), `as` renaming, file layout (named-file convention: `network.rs` + `network/` directory), library vs binary crates (`lib.rs`/`main.rs`), lib+bin pattern, multiple binaries (`src/bin/`), Cargo.toml in depth (package metadata, edition/rust-version, dependencies/dev-dependencies/build-dependencies, `[lints]` section with priority, resolver v3 MSRV-aware), workspaces (members, `workspace.dependencies` with `workspace = true`, `workspace.lints`, 2024 `default-features` hard error), evaluating third-party crates (docs.rs, crates.io, lib.rs, ecosystem defaults table), capstone KeyValueStore example with modules/visibility/re-exports
- Philosophy: modules define boundaries, not just organize files; every `pub` is a promise; private by default forces deliberate API design; visibility enforced by compiler, not convention
- All 8 compilable code examples verified (Rust 1.93+, edition 2024); 5 `rust,ignore` multi-file examples (cannot compile in single-file context)
- No Rust 2024-specific changes to core module/path/visibility system; edition-relevant: resolver v3 default, `default-features` rejection in workspace inheritance, `gen` reserved keyword (not demonstrated but relevant context)
- Builds on 5.2: bridge from "data structures" to "how to organize code"
- Builds on 3.1: struct methods, impl blocks
- Builds on 4.3: iterator patterns in capstone (collect, map, sort)
- Introduced `use std::io::{self, Write}` — `self` import pattern explained
- Introduced `writeln!` macro briefly — used without deep explanation (I/O traits)
- `[lints]` section: stable since Rust 1.74, not 2024-specific but modern and relevant
- `workspace.dependencies` and `workspace.lints`: stable since 1.64 and 1.74 respectively
- Deliberately omitted: `pub(in path)` (rarely used, mentioned in visibility table only conceptually), `extern crate` (obsolete since 2018 edition), `#[path]` attribute for custom module paths (rare), conditional compilation (`#[cfg]`, better for advanced chapter), `build.rs` build scripts (too advanced), `[features]` in Cargo.toml (better for library authoring guide), `Cargo.lock` detailed mechanics, `cargo publish` workflow
- **Review items:**
  - The `is_even` dead_code warning in example 1 is acceptable for teaching private items
  - The `email` field unused warning in the User struct example is acceptable — demonstrates field-level visibility
  - The FmtResult/IoResult renaming example generates unused import warnings — acceptable for teaching `as` syntax
  - The HashSet output order in example 4 is non-deterministic — output may vary
  - The multi-file examples use `rust,ignore` since they cannot be verified in single-file context — file layout descriptions substitute for compilation proof
  - The crate evaluation table lists ecosystem defaults — verify these are still accurate (serde, thiserror, anyhow, reqwest, axum, clap, tokio, tracing)
  - Consider whether `pub(super)` deserves a code example or if the visibility table is sufficient
  - The `mod.rs` vs named-file convention is explained — old convention mentioned briefly for codebase literacy
  - The capstone sorts HashMap keys for deterministic output — same pattern as 5.2

### Part 5 — NEXT UP
- 5.4 Testing as a First-Class Citizen: unit/integration/doc tests, cargo test
- Bridge from 5.3: "you can organize code with modules; next, how Rust builds testing into the language"

## Rust 2024 Features Tracker (for future chapters)

- Async closures (`async || {}`) + `AsyncFn`/`AsyncFnMut`/`AsyncFnOnce` traits — stabilized Rust 1.85.0, all editions — cover in Part 6 (Concurrency)
- `use<>` precise capturing syntax — stabilized Rust 1.82.0 (bare fns), Rust 1.88.0 (trait return position) — advanced usage, cover in Part 7 or appendix if needed

## General Notes

- All code must target `edition = "2024"` (Rust 1.85+)
- Follow O'Reilly style guide in docs/book_style.md strictly
- Philosophy first, then syntax — every chapter opens with WHY
- Show behavior first, name it second
- No "we'll cover this later" — if it appears, explain enough to use NOW
- Reserved keyword `gen` in 2024 — warn readers if relevant
- Let chains stabilized in Rust 1.88.0 (June 2025), edition-gated to 2024
- Range types gained `Copy` in Rust 2024 edition (via `IntoIterator` instead of `Iterator`) — note when relevant
