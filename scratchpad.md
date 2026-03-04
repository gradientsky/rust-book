# Scratchpad

Working notes and action items for the next iteration.

---

## Part 1: First Contact

### 1.1 Your First Rust Program — ITERATED
- Covers: philosophy (safety + speed), rustup install, `cargo new`, Cargo.toml anatomy, `fn main`, `println!` with `{}`, `{variable}`, `{:?}`, `{:#?}`
- Edition 2024 context: `cargo new` defaults to edition 2024 since Rust 1.85.0 (Feb 2025)
- Current stable Rust: 1.93.1 (Feb 2026)
- All 5 code examples verified to compile and produce documented output (Rust 1.93+, edition 2024)
- **Review items:**
  - ~~Verify tone is accessible to true beginners (no assumed systems programming background)~~ — RESOLVED: rewrote opening three paragraphs to eliminate systems programming jargon; replaced "garbage collector" with "the language sometimes pauses to reclaim memory you are no longer using"; replaced "dangling pointers, data races, use-after-free, buffer overflows" with accessible descriptions ("crashes from accessing freed memory, data corruption from unsynchronized access, resource leaks from forgotten cleanup"); framed the trade-off through concrete language comparisons (Python/JS vs C/C++)
  - ~~Consider adding a "what you'll need" prereqs note (terminal, text editor)~~ — DEFERRED: the chapter already instructs "Open a terminal and run" which implicitly requires a terminal; adding a formal prereqs box risks making the opening feel bureaucratic for a pocket book
  - ~~The `version = 1.85` float example is slightly misleading~~ — RESOLVED: replaced with `mass_kg = 72.5`, a naturally floating-point value
  - ~~Style compliance: first-mention styling for rustup and Cargo~~ — RESOLVED: _rustup_ italic on first mention (line 30), _Cargo_ italic on first mention (line 31, moved from line 64), "crates" introduced with inline gloss ("projects (_crates_, in Rust terminology)") on first use

### 1.2 The Compiler Is Your Ally — ITERATED
- Covers: error anatomy (E0382, E0308, unused variable warning), `cargo check` as fast feedback, `cargo clippy` with needless_range_loop and bool_comparison examples, `cargo fmt` with before/after, quality baseline workflow
- Philosophy: compiler as code reviewer, not gatekeeper; trust it instead of fighting it
- Rust 2024 note: `cargo fmt` auto-applies 2024 style edition (17 formatting fixes) when edition = "2024"
- Clippy and rustfmt are bundled in the default rustup profile — no extra install needed
- All 7 code examples verified (Rust 1.93.1, edition 2024); 2 does_not_compile examples (E0382, E0308) verified with exact error output
- **Review items:**
  - ~~Verify E0382 error output matches current compiler (Rust 1.93+)~~ — RESOLVED: updated E0382 output (column 4:15→4:16, 10→8 carets, added `help: consider cloning` suggestion); added point 6 to error anatomy list explaining compiler fix suggestions; replaced vague forward-reference with inline explanation of move semantics ("ownership transfers from greeting to other, and greeting becomes invalid")
  - ~~The "version = 1.85" example from 1.1~~ — RESOLVED: 1.1 float example changed to `mass_kg = 72.5`; no cross-reference needed
  - ~~Consider whether the clippy `needless_range_loop` example is too advanced for Ch 1 (uses `vec!` macro not yet explained)~~ — RESOLVED: changed `vec!["Alice", "Bob", "Charlie"]` to array literal `["Alice", "Bob", "Charlie"]`; eliminates unexplained `vec!` macro and avoids `useless_vec` clippy lint that would fire on Rust 1.93+; updated clippy output to match current format (diff-style suggestion, `is only used to` wording)
  - ~~The chapter intentionally teases ownership ("you do not need to understand ownership yet") — verify this forward reference feels natural, not frustrating~~ — RESOLVED: replaced with inline explanation: "String is a piece of text that lives on the heap. When you write `let other = greeting`, the value moves — ownership transfers from greeting to other, and greeting becomes invalid"; defers full picture to ownership chapter but explains enough to understand the error NOW
  - Updated E0308 output: column 6:27→6:25, added `note: function defined here` section showing function signature; updated prose to mention this feature
  - Updated unused variable warning: note now shows `(part of #[warn(unused)])` matching Rust 1.93.1
  - Updated clippy bool_comparison output: added `= note: #[warn(clippy::bool_comparison)]` line matching Rust 1.93.1

## Part 2: Thinking in Values

### 2.1 Variables, Expressions, and Control Flow — ITERATED
- Covers: immutability by default (philosophy), `let`/`mut`, shadowing (including type changes), scalar types (integers/floats/bool/char), type inference defaults (i32, f64), type annotations, constants (`const`), statics (`static` vs `const`, when to use each, **mutable globals with `AtomicU32` example**), expression-oriented design (if/blocks as expressions), control flow (if/else, loop with break-value, while, for with ranges), loop labels, tuples and arrays at a glance, **`Vec<T>` mini-intro with `vec!` macro**, **`usize` array indexing demonstration**, `if let` intro, let chains (Rust 2024)
- Philosophy: immutability is a feature not a limitation; expressions produce values everywhere; mutable global state is deliberately hard because it causes data races
- Rust 2024 features: let chains in `if` and `while` conditions (stabilized in Rust 1.88.0, edition-gated to 2024); `static mut` references disallowed in 2024 (not demonstrated — too advanced, covered in 7.3)
- All 31 code examples verified to compile and produce documented output (Rust 1.93+, edition 2024); 1 `does_not_compile` example (E0384 immutable reassignment)
- ~~Immutable reassignment example was missing `does_not_compile` annotation~~ — FIXED
- ~~Outline specifies "Constants and statics" but `static` was missing~~ — FIXED: added Statics section with `static` vs `const` comparison table, when to use each, and mutable globals forward-reference
- Introduced `if let` and `Result` just enough for let chains — explained self-contained, no forward references
- ~~`LazyLock` (Rust 1.80+) for runtime-initialized statics deliberately omitted — too advanced for this chapter, better covered in Part 5/6~~ — RESOLVED: added "Lazy Initialization" B-head after mutable globals section; introduces `LazyLock` with `DEFAULT_PORTS` `Vec<u16>` example (computed once on first access); explains why `vec![]` cannot be used in plain `static`; briefly notes closure syntax with forward ref to 2.2; mentions thread-safety and replaces `lazy_static`/`once_cell` crates; code verified zero-warning Rust 1.93.1
- **Review items:**
  - Verify the `if let` / `Result` mini-intro is sufficient for beginners who haven't seen enums yet — it needs to "just work" without deeper understanding
  - ~~The compound types section (tuples, arrays) is brief by design — consider if `Vec<T>` forward reference ("covered in a later part") is acceptable or needs rewording~~ — RESOLVED: replaced forward reference with inline `vec!` macro example showing `push`; explains enough to use NOW without deep dive; full Vec coverage remains in 5.2
  - ~~Integer overflow behavior (debug panic vs release wrap) was deliberately omitted to avoid overload~~ — RESOLVED: added "What happens when integers overflow" C-head subsection after integer types; covers debug panic vs release wrap, method families table (checked/saturating/wrapping/strict), two verified code examples; `strict_add` (Rust 1.91+) included in table
  - ~~Consider adding a note about `usize` being required for array indexing — currently mentioned but could be demonstrated~~ — RESOLVED: added "Array indexing requires usize" C-head subsection after Vec intro; demonstrates `usize` index with days array; explains compiler error for wrong integer type; notes platform portability rationale
  - The `while let` chain example uses array indexing (`values[index]`) which is less idiomatic than iterator-based approaches — acceptable here since iterators aren't introduced yet
  - ~~The statics section mentions `Mutex`/`Atomic` types for mutable globals but does not demonstrate them — deliberate forward-reference to Part 5/6~~ — RESOLVED: replaced forward reference with `AtomicU32` static counter example; shows `fetch_add`/`load` with `Ordering::Relaxed`; explains enough to understand the pattern without requiring concurrency knowledge; removes "you will learn in Part 5/6" phrasing

### 2.2 Functions and Closures — ITERATED
- Covers: function definitions (params, return types), implicit last-expression return, early return with `return`, expression-oriented function bodies, closures (syntax, type inference, capture by reference/mutable reference), Fn/FnMut/FnOnce trait hierarchy (conceptual), higher-order functions (`impl Fn` in argument position), passing named functions, choosing the right trait bound, returning closures (`impl Fn` in return position), function factories, `move` keyword (intro only)
- Philosophy: functions as primary abstraction unit; expression-oriented design makes bodies concise; closures "close over" environment
- All 14 code examples verified to compile and produce documented output (Rust 1.93+, edition 2024)
- Introduced `Option` just enough for early return example — self-contained, no forward reference
- Introduced `&str` as "read-only view of text" — enough to use, details deferred to borrowing chapter
- Introduced `'static` lifetime annotation briefly for string literals — minimal explanation, no deep dive
- Deliberately omitted: async closures (too advanced, covered in Part 6), `Box<dyn Fn>` (needs heap/trait objects from Part 4), full `move` semantics (needs ownership from 2.3)
- **Review items:**
  - ~~The `apply_to_each` example uses a fixed-size `[i32; 3]` return — slightly artificial~~ — RESOLVED: replaced hardcoded `[i32; 3]` return with proper slice iteration using `for &v in values`; function now accepts any-length `&[i32]` and prints `v -> f(v)` per element; avoids panic on short slices, consistent with capstone `convert_temps` pattern; zero Clippy warnings; output verified Rust 1.93.1
  - The `&'static str` in `classify` and `make_greeter` is explained minimally — verify this doesn't confuse readers who haven't seen lifetimes
  - ~~`run_once`/`run_repeatedly` example had misleading comment claiming `move` closure "can only run once" — actually `move || println!("{message}")` implements `Fn` since `println!` only borrows; `run_repeatedly` used trivial non-capturing closure that didn't demonstrate `FnMut`~~ — RESOLVED: rewrote example to use genuine `FnMut` closure (mutates `count`); fixed `move` explanation to accurately describe ownership transfer without conflating it with consumption; added "why not always use FnOnce?" closing note; verified output matches
  - The `move` keyword is introduced with a light touch ("forces ownership") — full explanation deferred to 2.3 (ownership)
  - The Fn trait hierarchy section is conceptual and short — appropriate level of abstraction for pre-generics introduction
  - Clippy flags `first_positive` as `manual_find` — intentional: the example teaches early returns, iterators not introduced until Part 4

### 2.3 Ownership — ITERATED
- Covers: three rules of ownership, stack vs heap mental model (with ASCII diagram), **`String::from` vs string literal explanation** (D-head: `&str` as baked-in reference, `String` as owned heap text, why String demonstrates ownership), move semantics (assignment, function calls, return values, **closures with `move`**), E0382 error example, Copy types (full list), Clone (explicit deep copy), Drop trait and RAII, drop order (reverse declaration order with Noisy struct demo), early drop with `std::mem::drop` (including its trivial implementation), comprehensive "ownership in action" capstone example
- Philosophy: ownership as the third path between GC and manual memory — compiler checks, zero runtime cost; ownership is not a restriction but a system that eliminates bugs
- All 14 code examples verified zero-warning (Rust 1.93.1, edition 2024)
- No Rust 2024-specific changes to ownership model itself; tail expression temporary scope change (RFC 3606) is relevant to Drop order but too advanced for this chapter — covered implicitly by teaching correct patterns
- Builds on 2.2: functions transfer/return ownership, `move` keyword from 2.2 gets context here
- Introduced `struct` and `impl Drop` minimally for the drop order example — self-contained, no forward reference needed
- **Updated E0382 error output** to Rust 1.93.1: column 5:22→5:21, added `help: consider cloning the value if the performance cost is acceptable` suggestion, added inline note connecting suggestion to Clone section
- **Review items:**
  - ~~The `move` keyword from 2.2 is not explicitly re-explained here~~ — RESOLVED: added "Moves into closures" C-head subsection after "Moves and Return Values"; shows `move` closure taking ownership of `String` (greet example), `make_greeter(String) -> impl Fn()` function factory (closure outliving scope); 2 verified code examples; fulfills the promise made in 2.2 ("you will see why in the next chapter on ownership")
  - The ASCII diagrams (stack/heap, double-pointer) are important for understanding — verify they render well in target format
  - The `Noisy` struct example introduces `struct`, `impl`, and trait implementation before Part 3 — minimal and self-contained, but verify it doesn't confuse readers
  - ~~Consider adding a note about `String::from` vs string literals — currently shown but not explicitly contrasted (`&str` vs `String` distinction)~~ — RESOLVED: added D-head "Why we keep writing String::from" after stack/heap section; explains `"hello"` as `&str` baked into binary (reference, not owned), `String::from` as owned heap-allocated text; explains why `String` demonstrates ownership while literals are `Copy`; forward-references 2.4 for full `String` vs `&str` treatment
  - ~~The "Why This Matters" section lists data races as prevented by ownership — technically ownership + borrowing together; verify this claim is precise enough~~ — RESOLVED: refined bullet to "Ownership ensures that a value has exactly one owner at a time. Combined with the borrowing rules you will learn next, this guarantee extends to concurrent programs — the same system that prevents use-after-free also prevents data races"
  - No mention of partial moves — deliberately omitted for simplicity; will be relevant in Part 3 (structs)

### 2.4 Borrowing and References — ITERATED
- Covers: shared references (`&T`), mutable references (`&mut T`), the many-readers-or-one-writer rule, Non-Lexical Lifetimes (NLL), borrow checker error anatomy (E0596, E0499, E0502, E0106), string slices (`&str` vs `&String`), array/vector slices (`&[T]`), dangling references, lifetime annotations (`'a`), **lifetime violation example (E0597 does_not_compile — result used after shorter-lived borrow dropped)**, lifetime elision, practical patterns (separate reads/writes, index-based mutation, narrow scopes)
- Philosophy: borrowing is what makes ownership practical — use without owning; borrow checker is a tool, not an obstacle
- All 14 compilable code examples verified (Rust 1.93+, edition 2024); 6 does_not_compile examples verified with exact error messages (added E0597 lifetime violation)
- No Rust 2024-specific changes to core borrowing/reference mechanics; NLL has been stable since Rust 2018 edition; match ergonomics 2024 changes exist but are too advanced for this chapter
- Builds on 2.3: opens with the ownership-only pain point (tuple return pattern), introduces `&` as the solution
- Introduced `vec![]` macro minimally for borrow checker examples — used without explanation, context makes intent clear
- Practical patterns use only concepts from Parts 1–2 (indexing, loops, Copy types); no forward references to iterators or `unwrap`
- **Updated E0596 error output** to Rust 1.93.1: added `help: consider changing this to be a mutable reference` suggestion with `&mut String` fix; added prose noting compiler suggests the fix
- **Updated E0106 error output** to Rust 1.93.1: added `help: instead, you are more likely to want to return an owned value` suggestion showing `&String` → `String` fix; updated prose to reference compiler suggestion
- **Added E0597 lifetime violation example**: shows `result` used outside inner scope after `s2` dropped; demonstrates that lifetime annotations let the compiler catch dangling references at compile time; completes the "show, then break" teaching pattern for lifetimes
- **Heading case fix**: `Working With the Borrow Checker` → `Working with the Borrow Checker` (preposition lowercase per O'Reilly style)
- **Review items:**
  - ~~Verify the `vec![]` usage doesn't confuse readers who haven't formally seen it (it appeared in 1.2 clippy example)~~ — ACCEPTED: `vec![]` was introduced in 2.1 with a mini-intro; context is clear in all uses
  - ~~The `first_word` function uses `s.bytes().enumerate()` and byte literal `b' '` — verify this is approachable for beginners~~ — RESOLVED: replaced with `find(' ')` + `if let Some(space)` pattern; avoids byte-level operations, uses only concepts from 2.1 (`if let`) and intuitive `find` method; added explanatory paragraph about `find` returning `Option`
  - ~~The lifetime annotation section uses `longer` function — classic example, but verify the nested scope example doesn't feel contrived~~ — RESOLVED: added does_not_compile example showing what happens when result escapes the inner scope; the working example shows success, the failing example shows the compiler catching the bug; "show then break" pattern makes lifetimes concrete
  - ~~The `*scores.iter().max().unwrap()` pattern in "Separate Your Reads and Writes" may be too dense — consider if it needs more explanation~~ — RESOLVED: replaced with explicit index-based loop (`for i in 1..scores.len()`) using only Copy semantics and comparison; avoids iterators (Part 4), `unwrap` (Part 3), and dereference; added explanatory paragraph about why index-based reads avoid borrow conflicts
  - No mention of reborrowing — deliberately omitted for simplicity
  - No mention of `Deref` coercion beyond the `&String` → `&str` auto-conversion — details deferred to Part 4 (Traits)
  - ~~Consider whether the "Working With the Borrow Checker" section should come before or after the dangling references section~~ — ACCEPTED: current placement (after lifetimes, before capstone) works well; readers have seen all the rules and error types before getting practical advice

### 3.1 Structs and Methods — ITERATED
- Covers: struct definition (named fields), field init shorthand, mutation (whole-struct mutability), struct update syntax with move semantics, tuple structs (newtype pattern intro), unit structs, methods with `impl` blocks, three method receivers (`&self`/`&mut self`/`self`), methods with extra parameters, associated functions (no `self`), `new` convention, `#[derive(Debug)]` for `{:?}` and `{:#?}`, `Display` trait manual implementation for `{}`, structs and ownership (move vs borrow), capstone `Task` example demonstrating all concepts
- Philosophy: structs are not just data containers — combined with `impl` blocks they form types with clear interfaces; method receiver declares the contract; self-documenting APIs
- All 18 code examples verified zero-warning (Rust 1.93.1, edition 2024); 1 does_not_compile example (E0277) verified with exact error output matching Rust 1.93.1
- Builds on 2.3 (ownership) and 2.4 (borrowing): method receivers directly map to `&T`, `&mut T`, and owned `T`; struct update syntax demonstrates move semantics; `into_` prefix convention introduced
- `std::fmt` imported for Display — first `use` statement in the book; explained minimally as "bring the formatting module into scope"
- `derive` concept introduced with Debug — explained as "compiler generates the implementation based on your fields"; mentioned other derivable traits (Clone, PartialEq, Default) as preview
- No Rust 2024-specific changes to struct/impl syntax; match ergonomics changes affect destructuring but deferred to 3.2
- ~~`std::fmt::from_fn` (stabilized 1.93) deliberately omitted — too advanced for intro chapter, better suited for Part 4 or Part 7~~ — RESOLVED: added to 4.1 Traits under "Formatting: Debug and Display" section
- **Review items:**
  - ~~Verify the `use std::fmt` introduction doesn't confuse readers — modules/`use` are formally covered in 5.3~~ — ACCEPTED: the `use std::fmt;` line is explained as "bring the formatting module into scope"; formal module system in 5.3 adds depth but this is sufficient for use NOW
  - ~~The `Formatter<'_>` lifetime syntax in Display impl uses `'_` (anonymous lifetime) — verify this is approachable before lifetimes are fully covered~~ — ACCEPTED: `'_` is an anonymous lifetime readers don't need to understand; context from 2.4 (lifetime annotations) is sufficient; the Display signature is treated as a recipe pattern
  - ~~Struct update syntax example produces a warning about unused `name` field~~ — RESOLVED: changed println to display `user2.name`, showing the move landed correctly (Alice's name now appears in user2); zero warnings
  - ~~The `into_` prefix naming convention is introduced here — verify it feels natural or needs more explanation~~ — ACCEPTED: introduced naturally in capstone Task example; explained as "a Rust convention for methods that take ownership"; fuller treatment in Part 7
  - ~~Consider whether tuple struct section needs more motivation (newtype pattern is revisited in Part 7)~~ — ACCEPTED: the Meters/Color examples are self-motivating; "you cannot accidentally add meters to seconds" is clear motivation; Part 7 adds depth
  - ~~Unit structs are explained briefly — verify the "type-level markers" forward reference to Part 4 feels natural~~ — ACCEPTED: the sentence "you will see them used with traits" is a natural bridge; the concept is self-contained enough to understand without traits
  - **Fixed unused variable warnings** in opening example (user_active/user2_active): added active field to println output
  - **Fixed unused `active` field warning** in mutation example: added active to println output
  - **Fixed dead_code warnings** in Debug example: added direct `coordinates` println using `p.x`/`p.y` alongside Debug output; contrasts derived Debug with manual field access
  - **Fixed dead_code warnings** in ownership move example: replaced `#[derive(Debug)]` with direct field access in `apply_config`; more instructive for ownership section
  - **Updated E0277 error output** to match Rust 1.93.1 format (added `---- required by this formatting parameter` annotation)

### 3.2 Enums and Pattern Matching — ITERATED
- Covers: enum definition (simple variants, data-carrying variants, named-field variants), exhaustive `match` with E0004 error, match as expression, wildcard `_` catch-all, or patterns (`|`), **`matches!` macro** (introduced with or-patterns as idiomatic boolean pattern check), `if let`, **"When to Prefer Match Over If Let"** (Discount example with exhaustiveness note), `let`-`else` (guard clauses, divergent else block, happy-path-flat idiom, when-to-use-each guide), let chains (Rust 2024 with `&&`), destructuring (enums, structs, tuples, nested), match guards (`if condition`), `..` ignore pattern for structs, `Box<Expr>` for recursive types (brief), capstone `Ticket` system example with nested pattern matching and Display impl
- Philosophy: enums model alternatives where strings/integers/booleans fail; exhaustive matching turns runtime bugs into compile-time errors; the type system guarantees every case is handled
- All 20 compilable code examples verified zero-warning (Rust 1.93.1, edition 2024); 1 does_not_compile example (E0004) verified with exact error message; 2 `rust,ignore` comparison snippets
- **Fixed dead_code/unused warnings** in 10 examples: Direction (iterate all), Coin (use all variants), Season (iterate all), HttpStatus (iterate all), Command catch-all (handle all data-bearing variants, `_` for unit variants), Day/or-patterns (iterate full week), Notification/if-let (unit variant for non-extracted data), Config/`..` pattern (read remaining fields in separate function), Role/Request (use Admin variant), capstone Ticket (use Medium/High Priority variants)
- **Updated E0004 error output** to Rust 1.93.1: added `note: Coin defined here` section showing enum definition with `------- not covered` annotation, `= note: the matched value is of type &Coin`, and `help: ensure that all possible cases are being handled` suggestion with `&Coin::Quarter => todo!()` fix; updated prose to reference `todo!()` suggestion
- **Replaced `std::mem::discriminant` example** with simpler catch-all pattern: Command enum with data-bearing variants handled explicitly, `_` catching unit variants; removes confusing `Discriminant(1)` output
- **Added `matches!` macro** as dedicated subsection after or-patterns (was only in capstone before); explains `matches!` as idiomatic boolean pattern check; Day weekend example with full week iteration
- **Added exhaustiveness note** to If Let with Else section: renamed to "When to Prefer Match Over If Let"; added explicit note that `match` catches new variants at compile time while `if let` chains silently fall through
- `let`-`else` stabilized in Rust 1.65.0 — not 2024-specific but essential production pattern; introduced between `if let` and let chains as the natural progression (if let → let-else → let chains)
- Builds on 3.1: struct destructuring in match, `Display` impl on enums, `use std::fmt`
- Builds on 2.1: let chains revisited with enum patterns (first introduced in 2.1 with `Result`)
- Introduced `Box<T>` minimally for recursive `Expr` type — explained as "heap-allocated pointer" with forward reference to Part 5
- Introduced `vec![]` for capstone example — used without deep explanation (appeared in 2.1, 2.4)
- Rust 2024 features used: let chains (`if let ... && condition`); match ergonomics 2024 changes exist but too advanced for this chapter
- Deliberately omitted: `@` bindings (too advanced, better for Part 7), `ref`/`ref mut` patterns (match ergonomics handles this), range patterns in match (not enum-specific), `#[non_exhaustive]` (library design concept for Part 5), slice patterns (covered in Part 5 with collections), `std::mem::discriminant` (too obscure for beginners)
- **Review items:**
  - ~~The `std::mem::discriminant` example output shows `Discriminant(1)` — verify this is stable output format or consider simplifying~~ — RESOLVED: replaced with simpler catch-all using `_`; removed `std::mem::discriminant` entirely
  - The `Box<Expr>` example may be too advanced — it introduces heap allocation before Part 5; current approach: minimal explanation, forward reference — ACCEPTED: `Box` is explained as "heap-allocated pointer" with forward reference; the recursive type example is a natural fit for nested destructuring
  - ~~Verify the `matches!` macro intro is sufficient — it appears in the capstone without prior dedicated explanation~~ — RESOLVED: added dedicated `matches!` subsection after or-patterns with Day weekend example; capstone now has prior explanation
  - The capstone example uses `vec![]` which hasn't been formally introduced — ACCEPTED: `vec![]` was introduced in 2.1; context is clear
  - ~~Consider whether the `if let else` chain example (Discount) should note that `match` is preferred for exhaustiveness~~ — RESOLVED: renamed section to "When to Prefer Match Over If Let"; added explicit note about exhaustiveness checking vs silent fall-through
  - ~~The or-pattern example (`Day::Saturday | Day::Sunday`) could note that `matches!` is even more concise for boolean returns~~ — RESOLVED: added `matches!` subsection immediately following or-patterns

### 3.3 Null, Errors, and the Type System — ITERATED
- Covers: `Option<T>` (Some/None, unwrap_or, unwrap_or_else, map, and_then, is_some_and, is_none_or), `Result<T, E>` (Ok/Err, unwrap_or, map, map_err), `?` operator (with Result and Option), Option↔Result conversion (ok_or, ok), unwrap/expect guidance, making illegal states unrepresentable (enum replacing boolean flags, newtype wrappers for type safety, validated construction with Result, **module privacy for invariant enforcement**), capstone Score/grade example combining all concepts
- Philosophy: invisible trapdoors (null, exceptions) vs explicit types; if a function can fail its signature must say so; billion-dollar mistake; type system as map of where things can go wrong
- All 20 compilable code examples verified zero-warning (Rust 1.93.1, edition 2024); 1 does_not_compile example (E0369) verified with exact error message; 1 `rust,ignore` snippet (fragile boolean Connection, illustrative only); 1 `rust,ignore` module privacy example (compilable but marked ignore for consistency with module pattern)
- No Rust 2024-specific changes to Option/Result/`?` operator semantics; `is_none_or` stabilized 1.82, `is_some_and`/`is_ok_and` stabilized 1.70 — all pre-2024 but modern idioms
- Builds on 3.2: bridges from "two enums built into the standard library" closing; uses pattern matching, exhaustive match, if let
- Builds on 3.1: uses struct definition, impl blocks, Display trait, use std::fmt
- Introduced `filter_map` minimally in capstone — explained by context (filter + map on iterators)
- Introduced `.parse::<T>()` turbofish syntax — used throughout, explained as "parse into type T"
- Introduced range patterns in match (`90..=100`) — used in Score::grade, natural extension of match
- Deliberately omitted: custom error types with From impl (Part 5), thiserror/anyhow (Part 5), try blocks (nightly-only), `Result::flatten` (stabilized 1.89 — consider adding to 3.3 or 5.1 in future iteration), inspect/inspect_err (better for Part 5 error handling chapter)
- **Updated E0369 error output** to Rust 1.93.1: fixed column 3:33→3:31, added `note: Option<i32> does not implement Add<{integer}>` help line
- **Fixed dead_code warnings**: Connection enum example now uses both `Disconnected` and `Connected` variants (two connections shown); Percentage example now destructures `PercentageError::OutOfRange(n)` in match arms instead of using `{:?}` debug format; fragile boolean Connection struct marked `rust,ignore` (illustrative non-compilable snippet)
- **Review items:**
  - The `HOME` env var example in expect section is platform-specific — works on macOS/Linux, not Windows; acceptable for pocket book target audience
  - The `ParseIntError { kind: InvalidDigit }` debug output format may change in future Rust versions — consider whether to use Display format instead
  - The `filter_map` in capstone uses iterator chain (`.iter().filter_map(...).collect()`) — verify this is approachable before iterators are formally covered in Part 4
  - Generics `<T>` are mentioned in Option/Result definitions but explained only as "placeholder for any type" — verify this is sufficient pre-Part 4
  - The newtype section is brief — fuller treatment with `Deref` and trait implementations deferred to Part 7
  - ~~Consider whether the "making illegal states unrepresentable" section needs a note about module privacy for enforcing validated construction (modules covered in 5.3)~~ — RESOLVED: added "Why the field is not public" C-head subsection after Percentage example; explains module-boundary privacy, shows `mod percentage` wrapper with pub struct + private field + validating constructor, verified output; forward-references Part 5 for full module system

### 4.1 Traits — ITERATED
- Covers: trait definition (required methods), implementing traits (`impl Trait for Type`), default methods, traits as parameters (`&impl Trait`), derive macros (Debug, Clone, Copy, PartialEq, Eq, Hash, Default, PartialOrd, Ord), Default trait with struct update syntax, Debug vs Display, **`fmt::from_fn` (Rust 1.93: ad-hoc Display/Debug from closure, lazy evaluation, reusable `join` formatter returning `impl Display`)**, From/Into (infallible conversions, `impl Into<String>` parameter pattern), TryFrom/TryInto (fallible conversions with associated Error type, **`Display` impl for error type**), AsRef (cheap reference conversions), implementing multiple traits, **supertraits (`trait Foo: Bar + Baz`, Loggable:Display example, prerequisite traits, bridges to Error:Debug+Display in 5.1)**, operator overloading (Add trait, associated Output type), orphan rule, capstone Celsius/Fahrenheit temperature example
- Philosophy: shared behavior without inheritance — "can-do" relationships instead of "is-a"; traits are flat, composable, and independent
- All 17 code examples verified zero-warning (Rust 1.93.1, edition 2024); 1 `rust,ignore` example (Storable multiple supertraits, non-compilable snippet)
- No Rust 2024-specific changes to core trait syntax; "dyn compatible" replaces "object safe" terminology (1.85+); trait upcasting stable in 1.86 — both deferred to 4.2 (Generics) since dyn Trait is covered there
- Builds on 3.3: closing paragraph bridges to traits; validated construction pattern from 3.3 revisited as TryFrom
- Builds on 3.1: impl blocks, Display trait, use std::fmt — now generalized
- Builds on 2.3: move/copy semantics relevant to derived Copy/Clone
- Introduced associated types minimally (`type Output`, `type Error`) — fuller treatment in 4.2 (Generics)
- Introduced `std::ops::Add` for operator overloading — other operator traits mentioned but not demonstrated
- `AsMut` deliberately omitted — `AsRef` is more common and sufficient for intro; `AsMut` can be covered in Part 5 or Part 7
- ~~`fmt::from_fn` (Rust 1.93) — previously noted as "deliberately omitted from 3.1, better suited for Part 4 or Part 7"~~ — RESOLVED: added "Ad-hoc formatting with from_fn" C-head subsection under "Formatting: Debug and Display"; philosophy-first explanation of when newtype Display is overkill; first example shows closure-based binary formatting and comma-separated list; second example shows reusable `join` function returning `impl fmt::Display + 'a` with lifetime, `move` closure, `write_str` for separator; both examples zero-warning Rust 1.93.1
- ~~Supertraits not covered~~ — RESOLVED: added "Supertraits" A-head section between "Implementing Multiple Traits" and "Traits for Operators"; introduces `trait Loggable: fmt::Display` syntax, shows `Event` struct implementing both Display (supertrait) and Loggable, `rust,ignore` snippet for multiple supertraits (`trait Storable: Display + Debug + Clone`), explains derive table entries (Copy:Clone, Eq:PartialEq, Ord:Eq+PartialOrd) as supertrait relationships, forward-references `Error: Debug + Display` from 5.1; added to key points summary
- **Review items:**
  - ~~The `content` field warning in example 1 (unused field) is acceptable for snippet~~ — RESOLVED: removed `content` field from `Article` struct; example now zero-warning
  - ~~Default methods example has unused `title` field~~ — RESOLVED: removed `title` field from `Article` struct; only `author` needed for `summarize_author`
  - ~~Default values example has unused `verbose` field~~ — RESOLVED: added `println!("verbose: {}", custom.verbose)` to use the field; zero-warning
  - ~~Debug formatting example has unused `Active` variant and unread `reason` field~~ — RESOLVED: added `label()` method that destructures all variants including `reason` field; both variants used in `main`; zero-warning
  - ~~Display formatting example has unused `Active` variant~~ — RESOLVED: both variants now constructed and printed in `main`; zero-warning
  - ~~TryFrom example has unread `value` and `OutOfRange(i32)` fields~~ — RESOLVED: added `Display` impl for `PercentageError` that destructures `OutOfRange(v)`; `main` uses `match` to access `p.value` and `{e}` (Display); zero-warning
  - ~~C-head "Using Into in Function Parameters" capitalization~~ — RESOLVED: changed to sentence case "Using Into in function parameters"
  - Verify the `impl Trait` in parameter position is sufficient intro before full generics in 4.2 — ACCEPTED: the chapter explicitly says "You will explore the full generics syntax in the next chapter"
  - The associated type explanation ("a type that is part of the trait's contract") is minimal — ACCEPTED: bridges cleanly to 4.2 where generics vs associated types are contrasted
  - The orphan rule explanation is brief — ACCEPTED: sufficient for intro; newtype workaround mentioned but not demonstrated (covered in 3.3 and Part 7)
  - Consider whether the `AsRef` example using byte values is too low-level — ACCEPTED: demonstrates the concept well with concrete observable output; byte arrays are familiar enough after 2.1
  - The capstone uses `Copy` derive on newtypes — ACCEPTED: `Copy` was introduced in 2.3 and in the derive table earlier in this chapter

### 4.2 Generics — ITERATED
- Covers: generic functions (single/multiple params), trait bounds (`T: Trait`, `T: Trait1 + Trait2`), `impl Trait` (argument position as sugar, return position for unnameable types, **same-type vs different-type code example**: `show_any`/`show_pair`), `where` clauses (readability + advanced bounds), generic structs (Pair, KeyValue), generic enums (Tree with Box), `impl Trait` in return position, Rust 2024 RPIT lifetime capture rule, associated types vs type parameters (one-to-one vs one-to-many), trait objects (`dyn Trait`), dyn compatibility rules (with `where Self: Sized` escape hatch), monomorphization and zero-cost abstraction, capstone Measurable example with static + dynamic dispatch
- Philosophy: generics answer "how do you write reusable code without giving up performance and safety?"; Rust answers at compile time via monomorphization; zero-cost = abstraction vanishes in compiled binary
- All 15 compilable code examples verified zero-warning (Rust 1.93.1, edition 2024); 1 does_not_compile example (E0369) verified with exact error message
- Rust 2024 features: RPIT lifetime capture rules (all in-scope lifetimes captured by default); mentioned but not demonstrated: `use<>` precise capturing syntax (too advanced for intro; covered implicitly by the 2024 default behavior)
- Builds on 4.1: `impl Trait` in parameter position from 4.1 now explained as syntactic sugar for generics; associated types (`type Output`, `type Error`) from 4.1 now contrasted with type parameters
- Builds on 3.2: `Box<T>` for recursive types referenced again in generic Tree enum
- Builds on 2.4: borrowing/references used in method signatures; lifetime concept underlies RPIT 2024 rule
- "dyn compatible" terminology used throughout (replaces "object safe" per Rust 1.86+)
- Trait upcasting (1.86) deliberately omitted — too advanced for intro chapter, better for Part 7
- `use<>` precise capturing syntax deliberately omitted from examples — the 2024 default behavior is the simpler and more common case; `use<>` is for edge cases better covered in advanced material
- **Updated E0369 error output** to Rust 1.93.1: column 2:11→2:10
- **Fixed `clone_self` dead_code warning**: added `#[derive(Clone)]` to Circle, added `clone_self()` call on concrete type in main; demonstrates that excluded methods work on concrete types but not through `dyn Describe`; zero warnings
- **Review items:**
  - The `where (T, T): Debug` example is unusual but demonstrates non-parameter bounds; verify it does not confuse beginners
  - The RPIT 2024 lifetime rule section is brief — verify it adequately explains why it matters without overloading; consider if a contrasting "this wouldn't work in 2021" note would help or hurt
  - The associated types example uses `Summarize<Summary = String>` constraint — verify this notation is clear without prior exposure
  - The `Vec<Box<dyn Describe>>` pattern introduces heap allocation with `Box` before Part 5 — context from 3.2 (`Box<Expr>`) should be sufficient
  - The dyn compatibility rules are simplified — full rules include no associated constants, no GATs, etc.; current level of detail is appropriate for intro
  - ~~The `clone_self` example in dyn compatibility generates an unused method warning — acceptable for teaching snippet~~ — RESOLVED: added `#[derive(Clone)]` to Circle and `clone_self()` call in main; demonstrates excluded methods work on concrete types; zero warnings
  - ~~Consider whether `impl Trait` same-type vs different-type distinction needs a code example showing the difference (currently prose-only)~~ — RESOLVED: added `show_any`/`show_pair` code example demonstrating independent type params (`impl Display, impl Display`) vs shared type param (`<T: Display>`); verified compiles with correct output; commented-out `show_pair(42, "hello")` produces `error[E0308]: expected integer, found &str`

### 4.3 Iterators and Functional Patterns — ITERATED
- Covers: Iterator trait (`next`, `Item`), three iteration modes (iter/iter_mut/into_iter), for-loop desugaring, lazy evaluation, adaptors (map, filter, filter_map, enumerate, zip, take, skip, flatten, flat_map, chain, inspect), consumers (collect, fold, sum, product, count, any, all, find, position, min, max, min_by_key, max_by_key), **`total_cmp` for float sorting** (PartialOrd vs Ord, NaN safety, `sort_by`/`max_by` patterns), collecting into Vec/String/HashMap/HashSet/Result, ranges as iterators, std::iter constructors (repeat_n, once, from_fn, successors), implementing Iterator for custom types (Countdown), IntoIterator for custom collections (Playlist), `is_sorted_by_key` (stable 1.82)
- Philosophy: iterators eliminate the trade-off between readable high-level code and fast execution; lazy evaluation enables compiler to fuse pipeline into single loop; zero-cost abstraction applied to data processing
- All 28 code examples verified to compile and produce documented output (Rust 1.93.1, edition 2024)
- No Rust 2024-specific changes to core iterator trait; `IntoIterator for Box<[T]>` is edition-gated but not demonstrated (too niche for intro); `gen` keyword reserved in 2024 for future gen blocks (nightly-only); `is_sorted`/`is_sorted_by_key` stable since 1.82; `repeat_n` stable since 1.82; `f64::total_cmp` stable since 1.62 — taught as the production-grade float sorting pattern (replaces `partial_cmp().unwrap()` anti-pattern)
- Builds on 4.2: closing paragraph bridges from generics to iterators; `impl Iterator` return type pattern from 4.2 revisited
- Builds on 4.1: `Iterator` is the key trait; `IntoIterator` and `FromIterator` are standard library traits
- Builds on 3.3: `Option` and `Result` used in `next()`, `find()`, `collect::<Result<Vec<_>,_>>()`; `filter_map` with `.ok()`
- Builds on 2.3/2.4: three iteration modes mirror ownership model (borrow, mutable borrow, owned)
- Introduced `HashMap` minimally for collect examples — used without deep explanation (covered in Part 5)
- Introduced `HashSet` minimally for collect examples — same
- Deliberately omitted: `Iterator::array_chunks` (nightly-only), `Iterator::map_windows` (nightly-only), `gen` blocks (nightly-only), `IntoIterator for Box<[T]>` 2024 behavior change (too niche), `try_fold`/`ControlFlow` (advanced), `Extend` trait (Part 5), `ExactSizeIterator`/`DoubleEndedIterator` (advanced traits better for Part 7), `iter::chain` free function (1.91, not needed when method form exists)
- **Review items:**
  - ~~The `&&n` pattern in `filter` examples may confuse beginners~~ — RESOLVED: added dedicated "Why the double ampersand" C-head subsection in Filter section with step-by-step trace of `&&i32` origin; contrasts `filter`/`find` (`&Self::Item`) with `map`/`any`/`all`/`position` (`Self::Item`); lazy evaluation example changed to range-based to avoid unexplained `&&` before explanation; consumers section adds brief callback note
  - ~~The capstone uses `partial_cmp(&b).unwrap()` for f64 comparison — could note that f64 is `PartialOrd` not `Ord`~~ — RESOLVED: replaced with `total_cmp` (stable since Rust 1.62); added "Sorting floating-point numbers" C-head subsection after min/max; teaches `total_cmp` as the production-grade pattern, warns against `partial_cmp().unwrap()`
  - ~~The `HashMap` output ordering is non-deterministic; capstone sorts keys for deterministic output — verify this doesn't add confusion~~ — RESOLVED: added "(key order may vary)" annotation on the collecting-into-different-types HashMap output; capstone already sorts keys for deterministic display; consistent with 5.2/5.3/6.1 convention
  - ~~Lazy evaluation warning snippet was simplified~~ — RESOLVED: updated warning to include source line, caret underline, and `help: use let _ = ...` suggestion matching Rust 1.93.1 format; consistent with 7.1 must_use warning pattern
  - The `collect::<Result<Vec<_>,_>>` pattern is powerful but dense — verify the explanation is sufficient for readers who haven't seen advanced generics
  - `repeat_n` (1.82) used instead of `repeat().take()` — modern idiom but less commonly seen in older tutorials
  - The `IntoIterator` custom impl delegates to `Vec::into_iter` — simple approach; more complex custom IntoIter structs deferred
  - Consider whether the `inspect` stderr example output is confusing (interleaved output from lazy evaluation)

### 5.1 Error Handling in Practice — ITERATED
- Covers: `Error` trait (Debug+Display, `source()` for error chains), manual error chain walking, thiserror 2.x (`#[error("...")]` for Display, `#[from]` for From+source, `#[source]` for source-only, `#[error(transparent)]` for delegation), anyhow 1.x (`anyhow::Result<T>`, `.context()`/`.with_context()`, `bail!`/`ensure!`/`anyhow!` macros, `.chain()` for walking), `?` operator `From::from()` conversion mechanism, library vs application error strategy (thiserror for libs, anyhow for apps), unwrap spectrum (`?` > `unwrap_or` > `expect` > `unwrap`), capstone Inventory example with typed errors and `Box<dyn Error>`
- Philosophy: error handling is about communicating what went wrong clearly enough to fix it; typed errors for programmatic consumers, context chains for human readers; two-crate pattern respects both audiences
- All 11 code examples verified to compile and produce documented output (Rust 1.93+, edition 2024)
- thiserror 2.0.18 (latest as of Mar 2026): breaking changes from 1.x include raw identifier format string removal, direct dependency requirement, no_std support; `#[from]` implies `#[source]`; `#[error(fmt = path)]` for external formatting logic (not covered — too advanced for intro)
- anyhow 1.0.102 (latest as of Mar 2026): stable 1.x series, no breaking changes; `Context` trait for `.context()`/`.with_context()`
- `core::error::Error` stabilized in Rust 1.81 (Sep 2024) — mentioned conceptually but not demonstrated (no_std is out of scope for this chapter)
- `Error::sources()` iterator still nightly-only as of Rust 1.93.1
- Builds on 3.3: `Result`, `Option`, `?` operator, custom error enums with Display
- Builds on 4.1: `From` trait for error conversion, trait implementation patterns
- Deliberately omitted: `try` blocks (nightly-only), `Error::provide()` (nightly-only), `Error::sources()` iterator (nightly-only), snafu crate (thiserror is the community standard), backtrace capture (nightly `provide()` required), `#[diagnostic::do_not_recommend]` (too advanced), `#[error(fmt = ...)]` (thiserror 2.x feature, too advanced)
- **Review items:**
  - ~~The "Choosing Variant Shapes" example had `Io(#[from] std::io::Error)` with misleading `#[error("JSON error")]` label and two variants wrapping `std::io::Error`~~ — RESOLVED: replaced `Io` variant with `Parse(#[from] std::num::ParseIntError)` to use distinct error types; added `.into()` demonstration showing `#[from]` auto-conversion; clearer distinction between `#[source]` (context-carrying) and `#[from]` (simple wrapping)
  - ~~The `#[error(transparent)]` example uses `Box<dyn Error + Send + Sync>` without explaining `Send + Sync`~~ — RESOLVED: added inline note explaining `Send + Sync` as thread-safety bounds with forward reference to Part 6; treats `Box<dyn std::error::Error + Send + Sync>` as standard "any error, anywhere" type
  - ~~Heading style: crate names capitalized in headings (Thiserror, Anyhow)~~ — RESOLVED: lowercased all crate names in headings per style guide ("Technical terms that are conventionally lowercase stay lowercase")
  - ~~Sentence-initial crate names capitalized~~ — RESOLVED: restructured sentences to avoid starting with bare crate name ("The thiserror crate is..." instead of "Thiserror is...")
  - The capstone uses `Box<dyn std::error::Error>` instead of `anyhow::Result` to avoid requiring anyhow dependency — noted in prose that anyhow has the same effect; acceptable
  - The "How the Question Mark Converts Errors" section shows `rust,ignore` pseudo-code — acceptable for non-compilable expansion examples
  - Error message convention (lowercase, no trailing punctuation) is stated but not heavily enforced in all examples — consistent enough for teaching purposes
  - The `HOME` env var in expect example is platform-specific (macOS/Linux) — same caveat as 3.3 and other chapters

### 5.2 Collections, Strings, and Smart Pointers — ITERATED
- Covers: Vec (creation with vec!/Vec::new/with_capacity/collect, access with []/get/last, modify with push/pop/insert/remove/retain, slices &[T], three iteration modes), HashMap (new/from/collect, get/indexing/contains_key, entry API with or_insert/or_insert_with), HashSet (insert/contains, intersection/union/difference), String vs &str (owned vs borrowed, deref coercion, when to use each, creation/conversion/concatenation/format!, common operations, UTF-8 guarantees), Box (recursive types Expr tree, trait objects Vec<Box<dyn Shape>>), Rc (reference counting, Rc::clone convention, shared ownership in graph-like structures, limitations: not thread-safe, immutable), Arc (thread-safe shared ownership, thread::spawn example), choosing the right pointer (decision table), capstone Library/Document tag system with Vec/HashMap/HashSet/Rc/String/Display
- Philosophy: ownership extends into data structures; collections own their elements; smart pointers extend the ownership model when simple ownership doesn't fit
- All 24 code examples verified to compile and produce documented output (Rust 1.93+, edition 2024)
- **Added `get_disjoint_mut` C-head** under Modifying Vectors: safe simultaneous mutable access to multiple elements by index (stabilized Rust 1.86); philosophy-first explanation of why borrow checker prevents naive `&mut v[i]` + `&mut v[j]`, `split_at_mut` as prior workaround, `get_disjoint_mut` as modern solution
- **Added `extract_if` C-head** under Modifying Vectors: conditional removal that returns extracted elements as iterator (Vec stabilized Rust 1.87, HashMap/HashSet stabilized 1.88); philosophy-first explanation of retain's limitation (discards removed elements), range parameter for Vec, lazy iterator semantics, HashMap example for cross-collection demonstration
- **Added safe string truncation C-head** under Strings Are UTF-8: `floor_char_boundary`/`ceil_char_boundary` (Rust 1.91); philosophy-first explanation of byte-budget truncation problem, café ☕ example showing byte 7 inside emoji, rounds down to 6 / up to 9; production-grade safe truncation pattern
- No Rust 2024-specific changes to core collection/string/smart pointer types; `IntoIterator for Box<[T]>` is 2024 edition-gated but not demonstrated (too niche); `HashMap::from([...])` stable since 1.56 but modern idiomatic pattern
- Builds on 5.1: bridge from error handling to data structures
- Builds on 4.3: iteration modes (iter/iter_mut/into_iter), collect patterns
- Builds on 4.2: trait objects (dyn Trait), Box<dyn Trait>
- Builds on 2.3/2.4: ownership, borrowing, slices (&[T], &str)
- Introduced `thread::spawn` minimally in Arc example — just enough to demonstrate thread-safe sharing; full concurrency in Part 6
- Deliberately omitted: BTreeMap/BTreeSet (mentioned as alternative), VecDeque/LinkedList (too niche), Cow<str> (advanced), RefCell/Cell (interior mutability pattern, too advanced for intro), Weak<T> (Rc cycles, advanced), LazyCell/LazyLock (better for Part 6/7), slice patterns, Extend trait, drain/retain_mut, Vec::from_raw_parts, HashMap::get_disjoint_mut (available but Vec example is sufficient to teach the concept), HashSet::extract_if (HashMap example sufficient to teach the concept for hash collections)
- **Review items:**
  - HashMap/HashSet output order is non-deterministic; documented with "(key order may vary)" and sorted outputs where needed
  - ~~The `&&str` type in `indexed: HashMap<usize, &&str>` may confuse beginners~~ — RESOLVED: changed `words.iter().enumerate().collect()` to `words.into_iter().enumerate().collect()` on an array literal; type is now `HashMap<usize, &str>` (no double reference); `into_iter()` on arrays yields owned elements directly
  - The capstone uses `Rc` for shared document references in a tag index — verify this feels motivated rather than contrived
  - The `+` operator on strings (moves left, borrows right) asymmetry is mentioned — verify explanation is clear enough
  - ~~UTF-8 byte slicing panic behavior is warned about but no does_not_compile example is shown~~ — RESOLVED: added `floor_char_boundary`/`ceil_char_boundary` C-head subsection (Rust 1.91) showing safe truncation; deliberate choice to show the safe solution rather than the panic
  - `RefCell` is mentioned as "advanced pattern" but not demonstrated — verify this forward reference feels natural
  - Consider whether `BTreeMap` deserves more than a one-sentence mention
  - The `has_tag` method was removed from capstone to avoid unused warning — verify the HashSet::contains mention in the recap is sufficient

### 5.3 Modules and Project Structure — ITERATED
- Covers: `mod`/`use`/`pub`, visibility spectrum (private default, `pub(crate)`, `pub(super)`, `pub`), struct field visibility with invariant protection, re-exports (`pub use`), grouped imports (`use std::io::{self, Write}`), `as` renaming, file layout (named-file convention: `network.rs` + `network/` directory), library vs binary crates (`lib.rs`/`main.rs`), lib+bin pattern, multiple binaries (`src/bin/`), Cargo.toml in depth (package metadata, edition/rust-version, dependencies/dev-dependencies/build-dependencies, `[lints]` section with priority, resolver v3 MSRV-aware), workspaces (members, `workspace.dependencies` with `workspace = true`, `workspace.lints`, 2024 `default-features` hard error), evaluating third-party crates (docs.rs, crates.io, lib.rs, ecosystem defaults table), capstone KeyValueStore example with modules/visibility/re-exports
- Philosophy: modules define boundaries, not just organize files; every `pub` is a promise; private by default forces deliberate API design; visibility enforced by compiler, not convention
- All 8 compilable code examples verified zero-warning (Rust 1.93+, edition 2024); 5 `rust,ignore` multi-file examples (cannot compile in single-file context)
- No Rust 2024-specific changes to core module/path/visibility system; edition-relevant: resolver v3 default, `default-features` rejection in workspace inheritance, `gen` reserved keyword (not demonstrated but relevant context)
- Builds on 5.2: bridge from "data structures" to "how to organize code"
- Builds on 3.1: struct methods, impl blocks
- Builds on 4.3: iterator patterns in capstone (collect, map, sort)
- Introduced `use std::io::{self, Write}` — `self` import pattern explained
- Introduced `writeln!` macro briefly — used without deep explanation (I/O traits)
- `[lints]` section: stable since Rust 1.74, not 2024-specific but modern and relevant
- `workspace.dependencies` and `workspace.lints`: stable since 1.64 and 1.74 respectively
- Deliberately omitted: `pub(in path)` (rarely used, mentioned in visibility table only conceptually), `extern crate` (obsolete since 2018 edition), `#[path]` attribute for custom module paths (rare), conditional compilation (`#[cfg]`, better for advanced chapter), `build.rs` build scripts (too advanced), `[features]` in Cargo.toml (better for library authoring guide), `Cargo.lock` detailed mechanics, `cargo publish` workflow
- Ecosystem defaults table verified current (March 2026): serde, thiserror, anyhow, reqwest, axum, clap, tokio, tracing all remain the standard choices
- **Review items:**
  - ~~The `is_even` dead_code warning in example 1~~ — RESOLVED: added `describe` pub fn that calls `is_even` within the module, demonstrating private-used-internally pattern, zero warnings
  - ~~The `email` field unused warning in the User struct example~~ — RESOLVED: `main` now prints `user.email`, reinforcing that `pub(crate)` fields are accessible within the crate, zero warnings
  - ~~The FmtResult/IoResult renaming example generates unused import warnings~~ — RESOLVED: added `let _fmt: FmtResult = Ok(())` and `let _io: IoResult<()> = Ok(())` to use the renamed types, zero warnings
  - ~~Anti-stacking violations at Package Metadata and Dependencies headings~~ — RESOLVED: added lead-in sentences before code blocks per O'Reilly style
  - ~~`default_settings()` non-idiomatic constructor name~~ — RESOLVED: renamed to `new()` per Rust convention (established in 3.1)
  - The HashSet output order in example 4 is non-deterministic — noted with "(tag order may vary)" in chapter text
  - The multi-file examples use `rust,ignore` since they cannot be verified in single-file context — file layout descriptions substitute for compilation proof
  - Consider whether `pub(super)` deserves a code example or if the visibility table is sufficient — DEFERRED: the table is sufficient for a pocket book
  - The `mod.rs` vs named-file convention is explained — old convention mentioned briefly for codebase literacy
  - The capstone sorts HashMap keys for deterministic output — same pattern as 5.2

### 5.4 Testing as a First-Class Citizen — ITERATED
- Covers: `#[test]` and `#[cfg(test)]`, assert family (`assert!`/`assert_eq!`/`assert_ne!` with custom messages, `PartialEq + Debug` requirement), `#[should_panic(expected = "...")]` with substring matching, `Result`-returning tests (`?` operator, `Box<dyn std::error::Error>`), `#[ignore = "reason"]`, integration tests (_tests/_ directory structure, separate crates, `use` imports, shared helpers in subdirectories), binary crate testing limitations (lib+bin pattern), doc tests (`///` comments as tests, hidden `#` lines, annotations: default/`no_run`/`compile_fail`/`should_panic`/`ignore`/`text`), combined doctests (Rust 2024 edition, `standalone_crate` annotation), `cargo test` workflows (name filtering, `--show-output`, `--test-threads=1`, `--ignored`, `--include-ignored`, `--doc`, `--lib`, `--test`, `--no-fail-fast`, `-p`), capstone stack-based Calculator example with unit tests, Result tests, should_panic tests, ignore tests, and doc tests
- Philosophy: testing is built into the language, not bolted on; if something matters it should be easy; tests live with the code they test
- All 12 compilable code examples verified (Rust 1.93+, edition 2024); multi-file integration test examples use `rust,ignore`
- No Rust 2024-specific changes to core test primitives (`#[test]`, `assert!`, etc.); combined doctests are the main 2024 testing improvement; cross-compiled doctests stable in 1.89 but not demonstrated (out of scope)
- Builds on 5.3: bridge from "organize code with modules" to "verify correctness with tests"; integration tests reference lib+bin pattern
- Builds on 3.3/5.1: `Result` and `?` operator in test functions; `Box<dyn Error>` for multiple error types
- Builds on 4.1: `PartialEq + Debug` requirement for `assert_eq!`/`assert_ne!` connects to derive macros
- Introduced `#[cfg(test)]` conditional compilation — explained as "only compile when testing"
- Introduced `use super::*` — explained as importing from parent module
- Deliberately omitted: custom test frameworks (nightly-only), `cargo nextest` (third-party tooling, not built-in), `pretty_assertions` crate (third-party), `#[bench]` (nightly-only), `proptest`/`quickcheck` (third-party), `assert_matches!` macro (nightly), JSON test output (unstable), `debug_assert!` variants (not testing-specific), test fixtures/setup patterns beyond helpers (too advanced)
- **Review items:**
  - ~~The `fibonacci(40)` ignored test is slow (~1s on modern hardware) but deterministic — verify this is acceptable as a "slow test" example~~ — ACCEPTED: acceptable as a pedagogical "slow test" example; `fibonacci(40)` takes ~1s with naive recursion, which is clearly slow enough to justify `#[ignore]`
  - ~~The `factorial(21)` should_panic doc test relies on debug-mode overflow check — in release mode this would wrap silently; acceptable since doc tests run in debug mode~~ — RESOLVED: added explicit `assert!(n <= 20, "factorial overflow: {n}! exceeds u64 range")` bounds check so the panic is deliberate and consistent regardless of debug/release mode; teaches the correct pattern for `should_panic`
  - ~~The capstone uses builder-style `self`-consuming methods — verify this pattern is approachable before Part 7 (Patterns the Pros Use) covers the builder pattern formally~~ — ACCEPTED: the chaining pattern (`push(x).push(y).add()`) is self-explanatory and doesn't require knowledge of the formal builder pattern; Part 7 adds the name and design principles
  - ~~Integration test file examples use `rust,ignore` since they require multi-file project structure — file layout descriptions substitute for compilation proof~~ — ACCEPTED: `rust,ignore` is the right annotation; file layouts and prose descriptions are sufficient
  - ~~The `Box<dyn std::error::Error>` pattern in Result-returning tests was introduced in 5.1 — verify the callback is sufficient~~ — ACCEPTED: the pattern is shown inline with a brief explanation; full context is in 5.1
  - ~~Consider whether `#[cfg(test)]` conditional compilation deserves more explanation (currently brief)~~ — ACCEPTED: the current explanation ("only compile this module when running tests; test code adds zero bytes to your release binary") is sufficient for a pocket book; deeper `cfg` mechanics are out of scope
  - ~~No mention of test organization best practices (naming conventions, test module structure) — kept simple for intro chapter~~ — ACCEPTED: the chapter teaches the standard `mod tests` pattern by example; formal naming conventions would be over-prescriptive for beginners
  - **Fixed `new_without_default` clippy warning** on Calculator: added `#[derive(Default)]` to `Calculator` struct
  - **Updated all test output** to match Rust 1.93.1 format: `#[ignore]` reason strings now shown inline (`... ignored, reason`); `test result:` lines now include `; finished in X.XXs` suffix
  - **Updated `#[ignore]` prose** to note that reason strings appear directly in test output (not just when listing tests)

### 6.1 Concurrency Without Data Races — ITERATED
- Covers: data race philosophy (ownership prevents races at compile time), `thread::spawn` (JoinHandle, join, move closures, `'static` requirement), `thread::scope` (scoped threads, non-`'static` borrowing, automatic joining), `Send` and `Sync` traits (auto traits, marker traits, `Rc` non-Send example, `Cell`/`RefCell` non-Sync), `Arc<T>` (atomic reference counting, `Arc::clone` convention), `Mutex<T>` (MutexGuard RAII, poisoning, lock scope best practices), **`RwLock<T>` (many-readers-or-one-writer runtime enforcement, read/write guards, Mutex vs RwLock decision guidance)**, `Arc<Mutex<T>>` pattern, channels (`mpsc::channel`, Sender/Receiver, iterator protocol, multiple producers, `drop(tx)` pattern), async taste (`async`/`await`, Future trait, runtime requirement, tokio, `tokio::spawn`, `#[tokio::main]`), async closures (Rust 2024: `async || {}`, `AsyncFn`/`AsyncFnMut`/`AsyncFnOnce` traits), capstone worker pool example (threads + channels + Arc<Mutex<T>>)
- Philosophy: concurrency safe by default; ownership/borrowing rules ARE the data race prevention rules; same system prevents use-after-free and data races
- All 10 compilable code examples verified zero-warning (Rust 1.93.1, edition 2024); 2 does_not_compile examples verified (E0373 borrow in thread, E0277 Rc not Send); 5 `rust,ignore` examples (spawn signature, async/tokio)
- Rust 2024 features: async closures (`async || {}`) stabilized in Rust 1.85.0, `AsyncFn`/`AsyncFnMut`/`AsyncFnOnce` in prelude for all editions; `std::env::set_var`/`remove_var` now unsafe (concurrency safety); `Future`/`IntoFuture` in prelude
- Builds on 5.4: bridge from "testing" to "concurrent programming"; closing paragraph connects to Part 7 (idiomatic patterns)
- Builds on 5.2: `Arc<T>` revisited (introduced in 5.2 for thread-safe shared ownership), `Rc<T>` contrasted
- Builds on 2.3/2.4: ownership and borrowing rules directly prevent data races; move semantics with `move` keyword
- Builds on 2.2: closures, `move` keyword, `Fn`/`FnMut`/`FnOnce` hierarchy mirrored by `AsyncFn` traits
- Async section uses `rust,ignore` for tokio examples (require external dependency)
- **Heading style fix**: `#### The AsyncFn traits` → `#### The async closure traits` (removed code element from heading per O'Reilly style)
- **Review items:**
  - ~~Thread output ordering is non-deterministic — documented with "(order may vary)" notes~~ — VERIFIED: all 10 compilable examples produce correct output; non-deterministic thread order documented with "(order may vary)" or "(thread order may vary)" notes; deterministic results section (sorted) always matches exactly
  - ~~The `thread::scope` example is brief — could demonstrate mutable borrowing across threads~~ — RESOLVED (prior iteration)
  - ~~Mutex poisoning explained briefly~~ — ACCEPTED: brief explanation sufficient for pocket book; poisoning is a rare edge case
  - ~~The async section is deliberately shallow ("a taste")~~ — ACCEPTED: provides enough to recognize and understand async code; links to Tokio tutorial and Async Book for depth
  - ~~`AsyncFn` trait bound syntax shown as `async Fn()`~~ — RESOLVED (prior iteration)
  - ~~No mention of `RwLock`~~ — RESOLVED (prior iteration)
  - ~~No mention of `Atomic*` types~~ — ACCEPTED: mentioned implicitly through Arc's atomic refcount; explicit atomics better for Part 7
  - The capstone wraps `Receiver` in `Arc<Mutex<Receiver>>` — this is a known anti-pattern (better to use crossbeam-channel MPMC), but acceptable for teaching since only std library is used
  - `sync_channel` (bounded channel) deliberately omitted — simpler to teach unbounded first
  - `thread::Builder` (named threads, stack size) deliberately omitted — too niche for pocket book intro

### 7.1 Patterns the Pros Use — ITERATED
- Covers: builder pattern (consuming builders, method chaining, `builder()` convention, fallible `build()` with `Result`, when to use), newtype pattern (zero-cost type safety, `UserId`/`OrderId` example, behavior on newtypes, orphan rule workaround with `PrettyVec`), type-state pattern (`PhantomData<State>`, zero-sized state markers, compile-time state machine enforcement, `Document<Draft>`/`Document<Reviewed>`/`Document<Published>` lifecycle, **reject→revise→approve path**), combinators (`map`/`and_then`/`filter`/`unwrap_or`/`unwrap_or_else`/`or`/`or_else`, combinator quick reference table, pipeline composition vs nested `match`), extension traits (`StrExt` for `str`, blanket implementations with `DisplayExt`, `FooExt` naming convention, ecosystem examples), capstone document processing system combining all five patterns
- Philosophy: patterns make design intent explicit in the type system; the compiler enforces invariants so you spend less time testing impossible states; these are built from structs, traits, generics, and ownership — no new features needed
- All 15 code examples verified to compile zero-warning and produce documented output (Rust 1.93.1, edition 2024); 2 `rust,ignore` examples (match comparison snippets, non-compilable)
- No Rust 2024-specific features used in patterns themselves; patterns are edition-agnostic but taught with 2024 idioms throughout
- Builds on 6.1: bridge from "safe concurrent programs" to "idiomatic patterns"; closing bridges to 7.2 (anti-patterns)
- Builds on 4.1: traits, `Display` impl, derive macros, `From`/`Into`
- Builds on 4.2: generics, `PhantomData`, type parameters
- Builds on 3.3: `Option`/`Result` combinators, newtype for type safety
- Builds on 3.1: struct definition, `impl` blocks, method receivers
- Introduced `PhantomData<T>` for type-state — explained as "tells the compiler this struct is parameterized by T without adding runtime data"
- Deliberately omitted: `bon`/`typed-builder`/`derive_builder` crates (too opinionated for intro; mentioned in ecosystem context only), `Deref`/`DerefMut` on newtypes (advanced, can lead to anti-patterns), sealed traits (advanced extension trait technique), `IntoFuture` async builder pattern (covered in 6.1 async taste), `@` bindings in match (too advanced)
- **Review items:**
  - ~~The builder section does not mention `#[must_use]` annotation on builder types — consider adding as a best practice note~~ — RESOLVED: added "Catching forgotten builds" C-head subsection with `#[must_use]` on `EmailBuilder`, verified warning output; also added `#[must_use]` to `ServerBuilder` (builder convention example) and capstone `DocumentBuilder`; fixed capstone word count output (was 25/9, corrected to 22/8)
  - The `PrettyVec` newtype example wraps `Vec<String>` — accessing inner `.0` field is slightly awkward; consider whether `Deref` should be mentioned (currently deliberately omitted)
  - The type-state section uses `PhantomData` before Part 7 — it was not previously introduced; verify the inline explanation is sufficient
  - ~~The combinator quick reference table covers `Option` only — `Result` equivalents mentioned in prose but not tabled~~ — RESOLVED: added dedicated `Result` combinator table (map/map_err/and_then/unwrap_or/unwrap_or_else/or/or_else/ok), `parse_port` code example demonstrating Result combinator chain (map_err + and_then), symmetry explanation (map vs map_err, unwrap_or_else receives error), verified output
  - The extension trait section does not demonstrate the sealed trait pattern — deliberate omission for simplicity; could add in review pass
  - The capstone uses `word_count()` via extension trait on both `str` and `String` separately — could use a blanket impl instead; current approach is simpler for beginners
  - Consider whether the `impl Into<String>` pattern in builder setters needs more explanation (first introduced in 4.1 with `From`/`Into`)
  - ~~Fix dead_code warnings across 4 examples~~ — RESOLVED: removed unused `#[derive(Debug)]` from `DatabaseConfig` (now matches fields directly), accessed `Email` fields with individual `println!` instead of `Debug` format, added `max_connections(250)` call and field to println in `Server::builder` example, demonstrated `reject()` path in type-state Document (reject→revise→approve flow)
  - ~~Update `#[must_use]` warning output to Rust 1.93.1~~ — RESOLVED: updated line number 36→44, added `= note: #[warn(unused_must_use)]` and `help: use let _ = ...` suggestion lines

### 7.2 What Not to Do — ITERATED
- Covers: cloning to silence borrow checker (performance + correctness costs, narrowing borrow scope, index-based mutation, `iter_mut`, borrowed types in signatures `&str`/`&[T]`, when cloning is correct), unwrap in production code (library vs application, Result propagation with `?`, unwrap spectrum table: `?` > `unwrap_or` > `expect` > `unwrap`), Java-in-Rust syntax (getter/setter boilerplate with `get_` prefix anti-pattern, Rust API Guidelines naming, pub fields vs invariant-enforcing accessors, overusing `dyn Trait` vs `impl Trait`/generics, Deref inheritance anti-pattern, composition with explicit delegation), fighting the type system (stringly-typed code vs enums, boolean blindness vs named enums, making invalid states representable with struct booleans+Options vs enum modeling), reaching for unsafe (split_at_mut safe alternative, checklist before unsafe, Rust 2024 `unsafe_op_in_unsafe_fn` warn-by-default, explicit `unsafe {}` blocks inside `unsafe fn`), overusing Rc/Arc (overhead explanation, move/borrow as default, smart pointer decision table), preferring indices over iterators (bounds check elimination, common translations table, when indices are appropriate), capstone Score/Grade report combining all lessons
- Philosophy: anti-patterns come from fighting the compiler instead of listening to it; the borrow checker is a code reviewer, not an obstacle; the type system is a proof system; unsafe is a scalpel, not a hammer
- All 25 compilable code examples verified (Rust 1.93.1, edition 2024); no does_not_compile or rust,ignore examples; all outputs verified
- Rust 2024 features: `unsafe_op_in_unsafe_fn` lint warn-by-default (explicit `unsafe {}` blocks in `unsafe fn`)
- Builds on 7.1: bridge from "patterns to use" to "patterns to avoid"; closing bridges to 7.3 (where to go from here)
- Builds on 3.3: `Option`/`Result`, `?` operator, making illegal states unrepresentable
- Builds on 4.1: traits, `Display` impl, derive macros
- Builds on 4.2: generics vs `dyn Trait`, static vs dynamic dispatch
- Builds on 4.3: iterators vs indexed loops
- Builds on 2.3/2.4: ownership, borrowing, borrow checker, NLL
- Builds on 5.1: error handling practices, unwrap spectrum
- `#[allow(dead_code)]` used in 5 examples to suppress warnings on unused variants/functions in teaching snippets
- Deliberately omitted: `#[deny(warnings)]` anti-pattern (too niche for intro), `Deref` code example (described in prose, not demonstrated to avoid teaching the anti-pattern), `RefCell`/interior mutability anti-patterns (too advanced), async-specific anti-patterns (blocking in async, covered in 7.3), `mem::take`/`mem::replace` patterns (too advanced for this chapter)
- **Review items:**
  - The `expect` example uses `HOME` env var — platform-specific (macOS/Linux), same caveat as 3.3 and 5.1
  - The `Deref` inheritance section describes the anti-pattern in prose but does not show the wrong code — deliberate to avoid teaching readers how to misuse Deref; consider whether a brief does_not_compile example would be more instructive
  - The `unsafe` section's `process_raw` example is contrived — raw pointer iteration when slice already works; acceptable as it demonstrates the 2024 edition change
  - The smart pointers section is brief — could expand with `Rc` cycle example using `Weak`, but that's covered in 5.2
  - ~~The capstone uses `partial_cmp(&b).unwrap()` for f64~~ — RESOLVED: replaced with `a.0.total_cmp(&b.0)` using newtype inner field; consistent with 4.3 `total_cmp` teaching
  - Consider whether the "when cloning is correct" section needs a code example
  - No mention of `Cow<str>` as an alternative to cloning — too advanced for this chapter
  - **B-head capitalization fix**: all 17 B-heads changed from sentence case to title case per O'Reilly style guide
  - **A-head capitalization fix**: "Over" → "over" in "Preferring Indices over Iterators" (preposition ≤4 letters)
  - **Anti-stacking fix**: added lead-in sentence before code block under "Return Result and Let the Caller Decide"

### 7.3 Where to Go from Here — ITERATED
- Covers: async in depth (tokio runtime, JoinSet structured concurrency, async fn in traits (1.75), async closures (2024), when to use async), unsafe Rust (5 capabilities, 2024 safety improvements: unsafe_op_in_unsafe_fn warn-by-default, unsafe extern blocks with safe annotations, static mut references hard error, newly unsafe env::set_var/remove_var), macros (declarative macro_rules! with `map!` example, procedural derive/attribute/function-like, syn/quote/proc-macro2 ecosystem), ecosystem map (web: axum/actix-web/reqwest/hyper/tonic/tower, CLI: clap/ratatui/colored, serialization: serde/serde_json/toml, databases: sqlx/diesel/sea-orm, observability: tracing/log, embedded: embedded-hal 1.0/embassy/esp-hal 1.0, WebAssembly: wasm-bindgen/wasm-pack/leptos/dioxus), recommended reading (official: Book/RBE/Reference/Cargo Book/Edition Guide/Rustonomicon; community: Design Patterns/Effective Rust/API Guidelines/Performance Book; interactive: Rustlings/Exercism; staying current: This Week in Rust/Rust Blog/Users Forum), four concrete next-steps paths (web services, CLI tools, embedded, systems programming)
- Philosophy: compass not destination; fundamentals don't change; ownership/borrowing/traits/type system are the foundation of every Rust program
- 1 compilable code example verified (macro_rules! `map!` macro, Rust 1.93+, edition 2024); 5 `rust,ignore` examples (tokio runtime, JoinSet, async trait, unsafe 2024 features)
- Builds on 7.2: closing bridge "In the next chapter, we will look forward"
- Builds on 6.1: async taste expanded into depth; tokio, JoinSet, async closures
- Builds on 5.1: thiserror/anyhow referenced in ecosystem context
- Builds on all prior chapters: references specific concepts taught earlier
- Ecosystem versions verified via web research (March 2026): tokio 1.50.0, axum 0.8.x, reqwest 0.13.2, clap 4.5.x, serde 1.0.228, sqlx 0.8.6, diesel 2.3.x, sea-orm 2.0, embedded-hal 1.0, esp-hal 1.0, tracing 0.1.x, tower 0.5.3, leptos 0.8.x, dioxus 0.7.x
- async-std noted as discontinued (March 2025); not recommended in the chapter
- **Review items:**
  - ~~The JoinSet example uses `to_string()` to satisfy `'static` bound — verify this is clear enough as a pattern~~ — ACCEPTED: `to_string()` is the standard idiom for converting `&str` to owned `String` for `'static` task spawning; well-established pattern in tokio documentation
  - ~~The async fn in traits section notes `dyn Trait` limitation — verify `async_trait` crate is still the standard workaround~~ — VERIFIED (March 2026): native `dyn Trait` with async methods is NOT yet stabilized; `async_trait` crate (0.1.88+) remains the standard workaround; `trait_variant` solves a different problem (Send-bounded variants for static dispatch); `dynosaur` is experimental
  - ~~The unsafe 2024 section covers 4 changes; `unsafe_attr` (unsafe attributes like `#[no_mangle]`) was omitted for brevity~~ — ACCEPTED: the four covered changes (unsafe_op_in_unsafe_fn, unsafe extern, static mut, newly unsafe fns) are the most impactful; `unsafe_attr` is less commonly encountered and can be discovered via the Edition Guide link
  - ~~The `map!` macro example is the only compilable example — all others are `rust,ignore` since they require external dependencies (tokio, etc.)~~ — ACCEPTED: verified `map!` macro compiles with expected output `3 colors defined` (Rust 1.93+, edition 2024); `rust,ignore` for tokio examples is the correct approach
  - ~~Ecosystem tables may become dated — consider adding a "verified as of March 2026" note in review pass~~ — RESOLVED: added "Versions and recommendations were verified as of early 2026; check crates.io and lib.rs for the latest" note at the start of the ecosystem section
  - ~~No mention of `rayon` beyond a one-line reference in "when to use async"~~ — ACCEPTED: rayon is mentioned in the right context (CPU-bound alternative to async); a dedicated entry would duplicate the concurrency chapter
  - ~~The "Your Next Steps" section suggests three paths — consider whether a fourth (embedded) should be added~~ — RESOLVED: added embedded path with Embedded Rust Book link, `rustup target add`, embedded-hal traits, and embassy reference
  - ~~No capstone example~~ — ACCEPTED: deliberate choice for a closing chapter that points outward rather than teaching new concepts
  - **Heading style fix**: all 15 B-heads changed from sentence case to title case per O'Reilly style guide
  - **Crate name styling fix**: removed monospace from crate names used in prose context (embedded-hal, wasm-bindgen, anyhow, mio) per style guide rule "Do not use monospace for crate names in prose"

### Part 7 — ALL CHAPTERS COMPLETE (7.1, 7.2, 7.3)

## Rust 2024 Features Tracker

- `use<>` precise capturing syntax — stabilized Rust 1.82.0 (bare fns), Rust 1.88.0 (trait return position) — covered implicitly via 2024 default behavior in 4.2
- Async closures (`async || {}`) — stabilized Rust 1.85.0; `AsyncFn`/`AsyncFnMut`/`AsyncFnOnce` traits in prelude; `async Fn()` bound modifier syntax is nightly-only (`async_trait_bounds`); covered in 6.1 (taste with AsyncFn traits table and retry example) and 7.3 (Where to Go from Here)
- unsafe_op_in_unsafe_fn — covered in 7.2 (anti-patterns) and 7.3 (2024 safety improvements)
- unsafe extern blocks — covered in 7.3
- static mut references disallowed — covered in 7.3
- Newly unsafe functions (env::set_var, etc.) — covered in 6.1 and 7.3

## Book Status: ALL CHAPTERS DRAFTED (Parts 1-7)

## General Notes

- All code must target `edition = "2024"` (Rust 1.85+)
- Follow O'Reilly style guide in docs/book_style.md strictly
- Philosophy first, then syntax — every chapter opens with WHY
- Show behavior first, name it second
- No "we'll cover this later" — if it appears, explain enough to use NOW
- Reserved keyword `gen` in 2024 — warn readers if relevant
- Let chains stabilized in Rust 1.88.0 (June 2025), edition-gated to 2024
- Range types gained `Copy` in Rust 2024 edition (via `IntoIterator` instead of `Iterator`) — note when relevant
